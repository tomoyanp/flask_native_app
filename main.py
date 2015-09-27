from local_programs.config import *
from local_programs.main_contents import *
from local_programs.authentication import *

#from authentication import *

DATABASE = 'tomoyan_web.db'
SECRET_KEY = 'development key'
USERNAME = 'tomoyan'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(main_contents)
app.register_blueprint(authentication)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('db_schema/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def con_db():
    g.db = connect_db()

def close_db():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)


