from web import app
from glob import glob

app.run(
    debug=True,
    host='0.0.0.0',
    port=5000,
    extra_files=glob('./web/templates/**.html')
)
