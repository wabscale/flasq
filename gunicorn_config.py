from os import environ

PORT=environ.pop('PORT')
WORKERS=environ.pop('WORKERS')
SITENAME=environ.pop('SITENAME')

bind='0.0.0.0:{}'.format(PORT)
workers=int(WORKERS)
# certfile='/etc/letsencrypt/live/{}/cert.pem'.format(SITENAME)
# keyfile='/etc/letsencrypt/live/{}/privkey.pem'.format(SITENAME)
# ca_certs='/etc/letsencrypt/live/{}/chain.pem'.format(SITENAME)
application='web:app'
