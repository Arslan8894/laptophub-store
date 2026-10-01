/**
 * consult-matcher.js
 * Pure, deterministic consultation matching and ranking engine for LaptopHUB.
 * Isolates all matching rules, upgrade cost calculations, alternative discovery,
 * and limiting constraint analysis without side-effects on the rest of the store.
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.ConsultMatcher = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // Standard upgrade delta pricing in PKR
  const UPGRADE_COSTS = {
    ram: {
      8: { 16: 6000, 32: 20000, 64: 45000 },
      16: { 32: 14000, 64: 38000 },
      32: { 64: 28000 }
    },
    storage: {
      128: { 256: 2000, 512: 4000, 1000: 16000, 2000: 28000 },
      256: { 512: 2000, 1000: 14000, 2000: 26000 },
      512: { 1000: 12000, 2000: 24000 },
      1000: { 2000: 20000 }
    }
  };

  /**
   * Calculate upgrade cost for RAM and storage
   */
  function calculateUpgradeCost(laptop, targetRam, targetStorage) {
    const baseRam = Number(laptop.ramGb || laptop.ram || 16);
    const baseStorage = Number(laptop.storageGb || laptop.storage || 512);

    let ramCost = 0;
    let ramUpgradeNeeded = false;
    if (targetRam > baseRam) {
      if (laptop.isRamUpgradable === false) {
        return { error: 'RAM not upgradable', valid: false };
      }
      ramCost = (UPGRADE_COSTS.ram[baseRam] && UPGRADE_COSTS.ram[baseRam][targetRam]) ||
                ((targetRam - baseRam) / 8) * 7000;
      ramUpgradeNeeded = true;
    }

    let storageCost = 0;
    let storageUpgradeNeeded = false;
    if (targetStorage > baseStorage) {
      storageCost = (UPGRADE_COSTS.storage[baseStorage] && UPGRADE_COSTS.storage[baseStorage][targetStorage]) ||
                    12000;
      storageUpgradeNeeded = true;
    }

    const basePrice = Number(laptop.price || 0);
    const finalPrice = basePrice + ramCost + storageCost;

    return {
      valid: true,
      basePrice,
      ramCost,
      storageCost,
      totalUpgradeCost: ramCost + storageCost,
      finalPrice,
      ramUpgradeNeeded,
      storageUpgradeNeeded,
      finalRam: Math.max(baseRam, targetRam),
      finalStorage: Math.max(baseStorage, targetStorage)
    };
  }

  /**
   * Deterministic predicate: does the laptop meet 100% of user preferences?
   */
  function evaluateLaptop(laptop, prefs) {
    const failures = [];
    const targetRam = Number(prefs.ram || 16);
    const targetStorage = Number(prefs.storage || 512);
    const targetBudget = Number(prefs.budget || 130000);

    // 1. Upgrades & Pricing
    const upgrade = calculateUpgradeCost(laptop, targetRam, targetStorage);
    if (!upgrade.valid) {
      failures.push({
        type: 'ram_soldered',
        label: `Fixed ${laptop.ramGb || laptop.ram} GB RAM (requires ${targetRam} GB)`
      });
    }

    const effectivePrice = upgrade.valid ? upgrade.finalPrice : laptop.price;
    if (effectivePrice > targetBudget) {
      const over = effectivePrice - targetBudget;
      failures.push({
        type: 'budget',
        label: `Rs ${Number(over).toLocaleString('en-PK')} over budget`,
        diff: over
      });
    }

    // 2. Use Case Rules
    const uc = prefs.usecase;
    if (uc && uc !== 'any') {
      const lapCases = laptop.useCases || [];
      const hasCaseTag = lapCases.includes(uc);

      if (!hasCaseTag) {
        failures.push({ type: 'usecase', label: `Not rated for ${uc}` });
      }

      // Hardware requirements per use-case
      if (uc === 'gaming') {
        const isDed = Boolean(laptop.isDedicatedGpu || laptop.gpuType === 'discrete' || laptop.gpuType === 'rtx');
        if (!isDed) {
          failures.push({ type: 'gpu', label: 'Gaming requires a dedicated GPU (RTX / GTX / Radeon RX)' });
        }
      } else if (uc === 'creator') {
        const effectiveRam = upgrade.valid ? upgrade.finalRam : (laptop.ramGb || laptop.ram);
        if (effectiveRam < 16) {
          failures.push({ type: 'ram', label: 'Creative design workflow requires at least 16 GB RAM' });
        }
      } else if (uc === 'programming') {
        const effectiveRam = upgrade.valid ? upgrade.finalRam : (laptop.ramGb || laptop.ram);
        if (effectiveRam < 16) {
          failures.push({ type: 'ram', label: 'Development workloads require at least 16 GB RAM' });
        }
      }
    }

    // 3. Processor Requirements
    const cpuPref = prefs.cpu;
    if (cpuPref && cpuPref !== 'any') {
      const brand = (laptop.cpuBrand || '').toLowerCase();
      const tier = (laptop.cpuTier || '').toLowerCase();
      const tag = (laptop.cpuTag || '').toLowerCase();

      if (cpuPref === 'intel_i5') {
        const isI5 = brand === 'intel' && (tier.includes('i5') || tier.includes('ultra 5') || tag === 'intel_i5');
        if (!isI5) failures.push({ type: 'cpu', label: `Processor is ${laptop.cpuTier || laptop.cpu}, not Core i5` });
      } else if (cpuPref === 'intel_i7') {
        const isI7 = brand === 'intel' && (tier.includes('i7') || tier.includes('ultra 7') || tier.includes('i9') || tag === 'intel_i7' || tag === 'intel_i9');
        if (!isI7) failures.push({ type: 'cpu', label: `Processor is ${laptop.cpuTier || laptop.cpu}, not Core i7/i9` });
      } else if (cpuPref === 'intel_ultra') {
        const isUltra = tier.includes('ultra') || tag === 'intel_ultra';
        if (!isUltra) failures.push({ type: 'cpu', label: `Processor is ${laptop.cpuTier || laptop.cpu}, not Core Ultra AI NPU` });
      } else if (cpuPref === 'amd') {
        const isAmd = brand === 'amd' || tag === 'amd';
        if (!isAmd) failures.push({ type: 'cpu', label: `Processor is ${laptop.cpuBrand || laptop.cpu}, not AMD Ryzen` });
      } else if (cpuPref === 'apple') {
        const isApple = brand === 'apple' || tag === 'apple';
        if (!isApple) failures.push({ type: 'cpu', label: `Device is not Apple Silicon (M-Series)` });
      }
    }

    // 4. Graphics Requirements
    const gpuPref = prefs.gpu;
    if (gpuPref && gpuPref !== 'no_pref') {
      const isDed = Boolean(laptop.isDedicatedGpu || laptop.gpuType === 'discrete' || laptop.gpuType === 'rtx');
      const isAppleGpu = Boolean(laptop.gpuCategory === 'apple' || laptop.gpuType === 'apple' || laptop.gpuType === 'apple_gpu' || (laptop.brand || '').toLowerCase() === 'apple');
      const isRtx = Boolean(laptop.gpuType === 'rtx' || (laptop.gpu || '').toLowerCase().includes('rtx'));

      if (gpuPref === 'integrated') {
        if (isDed) {
          failures.push({ type: 'gpu', label: `Has dedicated GPU (${laptop.gpu}), requested integrated` });
        }
      } else if (gpuPref === 'any_discrete') {
        if (!isDed) {
          failures.push({ type: 'gpu', label: `Integrated graphics (${laptop.gpu}), requested dedicated GPU` });
        }
      } else if (gpuPref === 'rtx') {
        if (!isRtx) {
          failures.push({ type: 'gpu', label: `Graphics is ${laptop.gpu}, not NVIDIA RTX` });
        }
      } else if (gpuPref === 'apple_gpu') {
        if (!isAppleGpu) {
          failures.push({ type: 'gpu', label: `Not Apple Silicon GPU` });
        }
      }
    }

    return {
      matched: failures.length === 0,
      failures,
      effectivePrice,
      upgrade
    };
  }

  /**
   * Build dynamic, precise explanation line for matched laptop
   */
  function buildWhyItMatches(laptop, prefs, evalResult) {
    const reasons = [];
    const ramText = evalResult.upgrade.ramUpgradeNeeded
      ? `Upgraded to ${prefs.ram} GB RAM`
      : `${laptop.ramGb || laptop.ram} GB RAM`;
    const storageText = evalResult.upgrade.storageUpgradeNeeded
      ? `Upgraded to ${prefs.storage >= 1000 ? (prefs.storage/1000)+'TB' : prefs.storage+'GB'} NVMe`
      : `${laptop.storageGb >= 1000 ? (laptop.storageGb/1000)+'TB' : laptop.storageGb+'GB'} NVMe SSD`;

    reasons.push(ramText);
    reasons.push(storageText);

    if (laptop.isDedicatedGpu || laptop.gpuType === 'rtx') {
      reasons.push(laptop.gpu);
    } else {
      reasons.push(laptop.cpuTier || laptop.cpu);
    }

    const diff = Number(prefs.budget) - evalResult.effectivePrice;
    if (diff > 20000) {
      reasons.push(`under your budget by Rs ${Number(diff).toLocaleString('en-PK')}`);
    } else if (diff >= 0) {
      reasons.push(`fits your Rs ${Number(prefs.budget).toLocaleString('en-PK')} budget`);
    }

    return reasons.join(' · ');
  }

  /**
   * Score and rank exact matches
   */
  function rankMatches(matches, prefs) {
    const budget = Number(prefs.budget || 130000);

    return matches.map(item => {
      let score = 70; // baseline for passing 100% of criteria
      const lap = item.laptop;
      const price = item.effectivePrice;

      // 1. Budget efficiency: sweet spot is 80%-98% of budget (delivers max performance for user's money)
      const budgetRatio = price / budget;
      if (budgetRatio >= 0.75 && budgetRatio <= 0.98) {
        score += 15;
      } else if (budgetRatio < 0.75) {
        score += 8; // substantial savings
      } else if (budgetRatio <= 1.0) {
        score += 12; // tight fit
      }

      // 2. Generation bonus
      const gen = Number(lap.cpuGen || 10);
      if (gen >= 12 || gen >= 6000) score += 10;
      else if (gen >= 10 || gen >= 5000) score += 5;

      // 3. Base specs fit without upgrade overhead
      if (!item.upgrade.ramUpgradeNeeded && !item.upgrade.storageUpgradeNeeded) {
        score += 5;
      }

      // Label assignment
      let matchBadge = 'Good Match';
      let matchTier = 'good';
      if (score >= 88) {
        matchBadge = 'Best Match';
        matchTier = 'best';
      } else if (score >= 78) {
        matchBadge = 'Great Match';
        matchTier = 'great';
      }

      return {
        ...lap,
        effectivePrice: price,
        upgradeDetails: item.upgrade,
        whyItMatches: buildWhyItMatches(lap, prefs, item),
        matchScore: score,
        matchBadge,
        matchTier
      };
    }).sort((a, b) => b.matchScore - a.matchScore);
  }

  /**
   * Find closest alternatives when exact matches are 0
   */
  function findClosestAlternatives(preferences, laptops) {
    const candidates = [];

    laptops.forEach(lap => {
      const res = evaluateLaptop(lap, preferences);
      // Close alternative = fails by only 1 criteria
      if (!res.matched && res.failures.length === 1) {
        const fail = res.failures[0];
        let diffLabel = fail.label;
        let isClose = false;

        if (fail.type === 'budget') {
          // Within 15% over budget
          const maxOver = Number(preferences.budget) * 0.18;
          if (fail.diff <= maxOver) {
            diffLabel = `Rs ${Number(fail.diff).toLocaleString('en-PK')} over budget`;
            isClose = true;
          }
        } else if (fail.type === 'ram' || fail.type === 'ram_soldered') {
          diffLabel = `${lap.ramGb || lap.ram} GB RAM instead of ${preferences.ram} GB`;
          isClose = true;
        } else if (fail.type === 'gpu') {
          diffLabel = `${lap.gpu} (${lap.gpuCategory || lap.gpuType}) instead of requested GPU`;
          isClose = true;
        } else if (fail.type === 'cpu') {
          diffLabel = `${lap.cpuTier || lap.cpu} instead of requested processor`;
          isClose = true;
        }

        if (isClose) {
          candidates.push({
            ...lap,
            effectivePrice: res.effectivePrice,
            diffLabel,
            failureType: fail.type,
            matchBadge: 'Alternative',
            matchTier: 'alternative',
            whyItMatches: `Closest alternative: ${diffLabel}. ${lap.ramGb || lap.ram}GB RAM · ${lap.storageGb || lap.storage}GB NVMe SSD.`
          });
        }
      }
    });

    // Rank candidates by price proximity to budget
    const targetBudget = Number(preferences.budget);
    candidates.sort((a, b) => Math.abs(a.effectivePrice - targetBudget) - Math.abs(b.effectivePrice - targetBudget));

    return candidates.slice(0, 3);
  }

  /**
   * Discover which single constraint is most limiting
   */
  function findMostLimitingPreference(preferences, laptops) {
    const currentBudget = Number(preferences.budget || 130000);

    // Test relaxation scenarios
    const tests = [
      {
        key: 'budget',
        name: 'Budget',
        newPrefs: { ...preferences, budget: currentBudget + 35000 },
        suggestion: `Raising your budget to Rs ${Number(currentBudget + 35000).toLocaleString('en-PK')}`
      },
      {
        key: 'budget_high',
        name: 'Budget',
        newPrefs: { ...preferences, budget: currentBudget + 60000 },
        suggestion: `Raising your budget to Rs ${Number(currentBudget + 60000).toLocaleString('en-PK')}`
      },
      {
        key: 'gpu',
        name: 'GPU',
        newPrefs: { ...preferences, gpu: 'no_pref' },
        suggestion: "Selecting 'No Preference' for GPU"
      },
      {
        key: 'cpu',
        name: 'Processor',
        newPrefs: { ...preferences, cpu: 'any' },
        suggestion: "Selecting 'No Preference' for Processor"
      },
      {
        key: 'ram',
        name: 'RAM',
        newPrefs: { ...preferences, ram: Math.max(8, Number(preferences.ram || 16) / 2) },
        suggestion: `Selecting ${Math.max(8, Number(preferences.ram || 16) / 2)} GB RAM (upgradable later)`
      },
      {
        key: 'usecase',
        name: 'Use Case',
        newPrefs: { ...preferences, usecase: 'any' },
        suggestion: "Switching Use Case to 'General / Any'"
      }
    ];

    let bestUnlockCount = 0;
    let bestUnlockSuggestion = '';
    let limitingKey = '';

    tests.forEach(test => {
      let count = 0;
      laptops.forEach(lap => {
        const res = evaluateLaptop(lap, test.newPrefs);
        if (res.matched) count++;
      });

      if (count > bestUnlockCount) {
        bestUnlockCount = count;
        bestUnlockSuggestion = `${test.suggestion} would unlock ${count} laptop${count === 1 ? '' : 's'}.`;
        limitingKey = test.key;
      }
    });

    if (bestUnlockCount > 0) {
      return {
        limitingKey,
        unlockCount: bestUnlockCount,
        message: bestUnlockSuggestion
      };
    }

    return {
      limitingKey: 'budget',
      unlockCount: 0,
      message: 'Try broadening your budget or choosing No Preference for CPU and GPU.'
    };
  }

  /**
   * Main entry point: pure function returning only true matches
   */
  function findMatches(preferences, laptops) {
    if (!Array.isArray(laptops) || laptops.length === 0) {
      return {
        exactMatches: [],
        closestAlternatives: [],
        limitingPreference: null,
        totalEvaluated: 0
      };
    }

    const matchedList = [];
    laptops.forEach(lap => {
      const res = evaluateLaptop(lap, preferences);
      if (res.matched) {
        matchedList.push({
          laptop: lap,
          effectivePrice: res.effectivePrice,
          upgrade: res.upgrade
        });
      }
    });

    const exactMatches = rankMatches(matchedList, preferences);
    let closestAlternatives = [];
    let limitingPreference = null;

    if (exactMatches.length === 0) {
      closestAlternatives = findClosestAlternatives(preferences, laptops);
      limitingPreference = findMostLimitingPreference(preferences, laptops);
    }

    return {
      exactMatches,
      closestAlternatives,
      limitingPreference,
      totalEvaluated: laptops.length
    };
  }

  return {
    UPGRADE_COSTS,
    calculateUpgradeCost,
    evaluateLaptop,
    rankMatches,
    findClosestAlternatives,
    findMostLimitingPreference,
    findMatches
  };
});
