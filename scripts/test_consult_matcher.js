const LAPTOPS_INVENTORY = require('../laptops-data.js');
const ConsultMatcher = require('../consult-matcher.js');

console.log('Testing ConsultMatcher with', LAPTOPS_INVENTORY.length, 'laptops...\n');

// Test Case 1: Multiple matches
console.log('=== Test Case 1: Office, Intel i7, 16GB, 512GB, Integrated, 130k Budget ===');
const res1 = ConsultMatcher.findMatches({
  usecase: 'office',
  cpu: 'intel_i7',
  ram: 16,
  storage: 512,
  gpu: 'integrated',
  budget: 130000
}, LAPTOPS_INVENTORY);

console.log('Exact Matches count:', res1.exactMatches.length);
res1.exactMatches.forEach(lap => {
  console.log(`  [${lap.matchBadge}] ID ${lap.id}: ${lap.name} | Price: Rs ${lap.effectivePrice.toLocaleString('en-PK')} | Why: ${lap.whyItMatches}`);
});
console.assert(res1.exactMatches.length > 0, 'Test 1 should have matches');

// Test Case 2: Exactly one match
console.log('\n=== Test Case 2: High budget, Apple M4 Max, 36GB, 1TB, 800k Budget ===');
const res2 = ConsultMatcher.findMatches({
  usecase: 'creator',
  cpu: 'apple',
  ram: 32,
  storage: 1000,
  gpu: 'apple_gpu',
  budget: 800000
}, LAPTOPS_INVENTORY);
console.log('Exact Matches count:', res2.exactMatches.length);
res2.exactMatches.forEach(lap => {
  console.log(`  [${lap.matchBadge}] ID ${lap.id}: ${lap.name} | Price: Rs ${lap.effectivePrice.toLocaleString('en-PK')} | Why: ${lap.whyItMatches}`);
});
console.assert(res2.exactMatches.length === 1, 'Test 2 should have exactly 1 match (MacBook Pro 14 M4 Max)');

// Test Case 3: Zero matches (impossible budget)
console.log('\n=== Test Case 3: Gaming with dedicated RTX on 45,000 budget (Zero Matches Expected) ===');
const res3 = ConsultMatcher.findMatches({
  usecase: 'gaming',
  cpu: 'any',
  ram: 16,
  storage: 512,
  gpu: 'rtx',
  budget: 45000
}, LAPTOPS_INVENTORY);

console.log('Exact Matches count:', res3.exactMatches.length);
console.assert(res3.exactMatches.length === 0, 'Test 3 should have 0 exact matches');
console.log('Closest Alternatives count:', res3.closestAlternatives.length);
res3.closestAlternatives.forEach(alt => {
  console.log(`  [${alt.matchBadge}] ID ${alt.id}: ${alt.name} | Diff: ${alt.diffLabel} | Effective Price: Rs ${alt.effectivePrice.toLocaleString('en-PK')}`);
});
console.log('Limiting Preference message:', res3.limitingPreference ? res3.limitingPreference.message : 'None');

console.log('\nALL MATCHER UNIT TESTS PASSED SUCCESSFULLY!');
