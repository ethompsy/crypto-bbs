CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/Users/ethompson/Projects/crypto-bbs/cache',
        'TIMEOUT': 30*60,
    }
}