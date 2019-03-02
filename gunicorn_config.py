from os import environ

PORT=environ.pop('PORT') if 'PORT' in environ else '80'
WORKERS=environ.pop('WORKERS') if 'WORKERS' in environ else '2'
SITENAME=environ.pop('SITENAME') if 'SITENAME' in environ else 'DEFAULT'

bind='0.0.0.0:{}'.format(PORT)
workers=int(WORKERS)
errorlog='web/data/error.log'
preload_app=True
