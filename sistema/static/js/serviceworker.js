var staticCacheName = "pwa-tienda";

self.addEventListener('install', function(event) {
	event.waitUntil(
		caches.open(staticCacheName).then(function(cache) {
			return cache.addAll([
				'/api/productos/',
				'/api/sucursales/',
				'/api/vendedores/',
				'/api/ventas/',
				'/api/ofertas/',
				'/',
				'/gestion/productos',
				'/gestion/sucursales',
				'/gestion/vendedores',
				'/gestion/ofertas',
				'/base_layout',
			]);
		})
	);
});

self.addEventListener("fetch", function(event) {
	var requestUrl = new URL(event.request.url);
	if (requestUrl.origin === location.origin) {
		if ((requestUrl.pathname === '/')) {
			event.respondWith(caches.match('/base_layout'));
			return;
		}
	}
	event.respondWith(
		caches.match(event.request).then(function(response) {
			return response || fetch(event.request);
		})
	);
});
