from server  import app, db
import sys

if sys.argv[1] == "init":
    db.create_all()
    print("database initialized!")

if sys.argv[1] == "run":
    app.run(port=8000)
