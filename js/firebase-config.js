/**
 * LaptopHUB - Firebase & Cloud Firestore Integration (js/firebase-config.js)
 * =========================================================================
 * Real security via Firebase Authentication and Cloud Firestore Security Rules.
 * - Public Web Config: Safe to expose in frontend because Firestore rules protect writes.
 * - Single Admin Account: Only the authenticated user matching ADMIN_UID has write access.
 * - Fallback Mode: Seamlessly falls back to local static inventory if Firebase is not yet configured.
 */

// ── 1. FIREBASE WEB CONFIGURATION ──────────────────────────────────────────
// Paste your Web App credentials from the Firebase Console (Project Settings > General > Your apps)
const firebaseConfig = {
  apiKey: "YOUR_FIREBASE_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_FIREBASE_APP_ID"
};

// ── 2. DESIGNATED ADMIN USER UID ──────────────────────────────────────────
// The User UID created in Firebase Console > Authentication > Users tab.
// Used for client-side routing guard (actual security is enforced by firestore.rules).
const LAPTOPHUB_ADMIN_UID = "YOUR_ADMIN_UID";

// ── 3. FIREBASE SERVICES INITIALIZATION ────────────────────────────────────
let firebaseApp = null;
let firebaseAuth = null;
let firestoreDb = null;
let isFirebaseConfigured = false;

function initFirebase() {
  if (typeof firebase === 'undefined') {
    return { isConfigured: false, app: null, auth: null, db: null };
  }

  // Check if config has been customized
  const hasValidConfig = firebaseConfig.apiKey && 
                         !firebaseConfig.apiKey.includes('YOUR_FIREBASE') &&
                         firebaseConfig.projectId &&
                         !firebaseConfig.projectId.includes('YOUR_PROJECT');

  if (!hasValidConfig) {
    // Check localStorage for runtime override if user entered credentials in Admin UI
    try {
      const stored = localStorage.getItem('laptophub_firebase_config');
      if (stored) {
        const parsed = JSON.parse(stored);
        if (parsed.apiKey && parsed.projectId) {
          Object.assign(firebaseConfig, parsed);
        }
      }
    } catch (_) {}
  }

  isFirebaseConfigured = firebaseConfig.apiKey && 
                         !firebaseConfig.apiKey.includes('YOUR_FIREBASE') &&
                         firebaseConfig.projectId &&
                         !firebaseConfig.projectId.includes('YOUR_PROJECT');

  if (isFirebaseConfigured) {
    try {
      if (!firebase.apps.length) {
        firebaseApp = firebase.initializeApp(firebaseConfig);
      } else {
        firebaseApp = firebase.app();
      }
      firebaseAuth = firebase.auth();
      firestoreDb = firebase.firestore();
      
      // Enable offline persistence if supported
      try {
        firestoreDb.enablePersistence({ synchronizeTabs: true }).catch(() => {});
      } catch (_) {}
    } catch (err) {
      console.warn('[LaptopHUB] Firebase init warning:', err);
    }
  }

  return {
    isConfigured: isFirebaseConfigured,
    app: firebaseApp,
    auth: firebaseAuth,
    db: firestoreDb
  };
}

// ── 4. FIRESTORE DATA HELPERS ─────────────────────────────────────────────
/**
 * Fetch all laptops from Firestore with fallback to local inventory.
 * @returns {Promise<Array>} Array of laptop objects.
 */
async function fetchStoreLaptops() {
  const { isConfigured, db } = initFirebase();

  if (isConfigured && db) {
    try {
      const snapshot = await db.collection('laptops').get();
      if (!snapshot.empty) {
        const items = [];
        snapshot.forEach(doc => {
          const data = doc.data();
          items.push({
            firestoreId: doc.id,
            ...data
          });
        });
        // Sort by ID ascending
        items.sort((a, b) => (Number(a.id) || 0) - (Number(b.id) || 0));
        return items;
      }
    } catch (err) {
      console.warn('[LaptopHUB] Firestore fetch error, using local fallback:', err);
    }
  }

  // Graceful fallback to static 69 laptops
  if (typeof LAPTOPS_INVENTORY !== 'undefined' && Array.isArray(LAPTOPS_INVENTORY)) {
    return [...LAPTOPS_INVENTORY];
  }
  return [];
}

/**
 * Real-time listener for public store laptops
 * @param {Function} onUpdate Callback receiving the updated array of laptops
 * @returns {Function} Unsubscribe function
 */
function subscribeStoreLaptops(onUpdate) {
  const { isConfigured, db } = initFirebase();

  if (isConfigured && db) {
    try {
      return db.collection('laptops').onSnapshot(snapshot => {
        if (!snapshot.empty) {
          const items = [];
          snapshot.forEach(doc => {
            items.push({ firestoreId: doc.id, ...doc.data() });
          });
          items.sort((a, b) => (Number(a.id) || 0) - (Number(b.id) || 0));
          onUpdate(items);
        } else {
          // Empty database: fallback
          if (typeof LAPTOPS_INVENTORY !== 'undefined') onUpdate(LAPTOPS_INVENTORY);
        }
      }, err => {
        console.warn('[LaptopHUB] Firestore subscription error:', err);
        if (typeof LAPTOPS_INVENTORY !== 'undefined') onUpdate(LAPTOPS_INVENTORY);
      });
    } catch (e) {
      console.warn('[LaptopHUB] Real-time subscription failed:', e);
    }
  }

  // Fallback: trigger once immediately with local data
  if (typeof LAPTOPS_INVENTORY !== 'undefined') {
    onUpdate(LAPTOPS_INVENTORY);
  }
  return () => {};
}

// ── 5. ADMIN WRITE HELPERS ────────────────────────────────────────────────
/**
 * Save or update a laptop in Firestore (Admin Only)
 */
async function adminSaveLaptop(laptopData) {
  const { isConfigured, db, auth } = initFirebase();
  if (!isConfigured || !db) throw new Error('Firebase is not configured.');
  if (!auth.currentUser) throw new Error('You must be signed in as administrator.');

  const id = String(laptopData.id);
  const docRef = db.collection('laptops').doc(id);

  const payload = {
    ...laptopData,
    updatedAt: firebase.firestore.FieldValue.serverTimestamp()
  };

  await docRef.set(payload, { merge: true });
  return { success: true, id };
}

/**
 * Delete a laptop from Firestore (Admin Only)
 */
async function adminDeleteLaptop(laptopId) {
  const { isConfigured, db, auth } = initFirebase();
  if (!isConfigured || !db) throw new Error('Firebase is not configured.');
  if (!auth.currentUser) throw new Error('You must be signed in as administrator.');

  await db.collection('laptops').doc(String(laptopId)).delete();
  return { success: true };
}

/**
 * Fast stock quantity update (Admin Only)
 */
async function adminUpdateStock(laptopId, newStock) {
  const { isConfigured, db, auth } = initFirebase();
  if (!isConfigured || !db) throw new Error('Firebase is not configured.');
  if (!auth.currentUser) throw new Error('You must be signed in as administrator.');

  await db.collection('laptops').doc(String(laptopId)).update({
    stock: parseInt(newStock, 10),
    updatedAt: firebase.firestore.FieldValue.serverTimestamp()
  });
  return { success: true };
}

// Auto-run init on script execution
if (typeof window !== 'undefined') {
  window.initFirebase = initFirebase;
  window.fetchStoreLaptops = fetchStoreLaptops;
  window.subscribeStoreLaptops = subscribeStoreLaptops;
  window.adminSaveLaptop = adminSaveLaptop;
  window.adminDeleteLaptop = adminDeleteLaptop;
  window.adminUpdateStock = adminUpdateStock;
}
