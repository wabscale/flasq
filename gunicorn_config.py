from os import environ

PORT=environ.pop('PORT')
WORKERS=environ.pop('WORKERS')
SITENAME=environ.pop('SITENAME')
CERTPATH=environ.pop('CERTPATH')

bind='0.0.0.0:{}'.format(PORT)
workers=int(WORKERS)
if CERTPATH != 'default':
    certfile='{}/cert.pem'.format(CERTPATH)
    keyfile='{}/privkey.pem'.format(CERTPATH)
    ca_certs='{}/chain.pem'.format(CERTPATH)
application='web:app'
