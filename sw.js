/* FilmFest Guide service worker, same approach as LitFest Guide: the site is static files, so after the first visit it runs offline.
   Bump VERSION when the page shell changes; code and catalog.json come from the network first and fall back to the cache offline. */
var VERSION='filmfest-20261126-i18n',SHELL=['./','index.html','style.css','app.js','geo.js','calendar.js','i18n.js','catalog.json','manifest.webmanifest','fonts/fonts.css','assets/logo.svg','assets/icon-192.png','assets/icon-512.png'];
self.addEventListener('install',function(e){e.waitUntil(caches.open(VERSION).then(function(c){return c.addAll(SHELL)}).then(function(){return self.skipWaiting()}))});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(x){return x!==VERSION}).map(function(x){return caches.delete(x)}))}).then(function(){return self.clients.claim()}))});
self.addEventListener('fetch',function(e){var r=e.request;if(r.method!=='GET')return;var u=new URL(r.url);if(u.origin!==location.origin)return;
if(r.mode==='navigate'){e.respondWith(fetch(r).then(function(res){var cp=res.clone();caches.open(VERSION).then(function(c){c.put('index.html',cp)});return res}).catch(function(){return caches.match('index.html')}));return}
if(/\.(json|js|css)$/.test(u.pathname)){var key=new Request(u.origin+u.pathname);e.respondWith(caches.open(VERSION).then(function(c){return fetch(r,{cache:'no-cache'}).then(function(res){if(res.ok)c.put(key,res.clone());return res}).catch(function(){return c.match(key)})}));return}
e.respondWith(caches.match(r).then(function(hit){return hit||fetch(r).then(function(res){if(res.ok){var cp=res.clone();caches.open(VERSION).then(function(c){c.put(r,cp)})}return res})}))});
