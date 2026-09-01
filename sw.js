/* Service worker — met le site en cache pour un usage hors connexion.
   Stratégie : réseau d'abord (pour recevoir les mises à jour), cache en secours. */
const CACHE = "boussole-v3";
const ESSENTIELS = ["./", "./index.html", "./manifest.webmanifest", "./icone-192.png", "./icone-512.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ESSENTIELS)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(noms => Promise.all(noms.filter(n => n !== CACHE).map(n => caches.delete(n))))
      .then(() => self.clients.claim())
  );
});
self.addEventListener("fetch", e => {
  if(e.request.method !== "GET") return;
  e.respondWith(
    fetch(e.request)
      .then(rep => {
        if(rep && rep.status === 200 && rep.type === "basic"){
          const copie = rep.clone();
          caches.open(CACHE).then(c => c.put(e.request, copie));
        }
        return rep;
      })
      .catch(() => caches.match(e.request).then(r => r || caches.match("./index.html")))
  );
});
