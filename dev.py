from web import app, db

db.create_all()
app.run(
    debug=True,
    host='127.0.0.1',
    port=5000,
)
