from local_programs.config import *
from local_programs.authentication import *
from local_programs.manage_blog_contents import *

### Application Configurations ###
DATABASE = 'db/tomoyan_web.db'
SECRET_KEY = 'development key'
USERNAME = 'tomoyan'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


### Routing Functions ###
@app.route('/')
def home():
    url = "home"
    contents_list = get_blog_contents_handller(url, None)
    return render_template(contents_list[0], titles=contents_list[1], genres=contents_list[2])

@app.route('/production')
def production():
    request_url_query = request.args.get('id')
    url = "production"
    contents_list = get_blog_contents_handller(url, request_url_query)
    return render_template(contents_list[0], titles=contents_list[1], genres=contents_list[2])

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


### Authentication Functions ###
@app.route('/login')
def login():
    url = "login"
    contents_list = get_blog_contents_handller(url, None)
    return render_template(contents_list[0], titles=contents_list[1], genres=contents_list[2])

@app.route('/login', methods=['POST'])
def login_auth():
    url = check_login_auth(request)
    redirect(url)

@app.route('/admin')
def admin_page():
    if check_session():
        url = "admin"
        contents_list = get_blog_contents_handller(url, None)
        return render_template(contents_list[0], titles=contents_list[1], genres=contents_list[2])
    else:
        return redirect('/')

@app.route('/update',methods=['POST'])
def update():
    update_blog_contents_handller(request)
    return redirect('/')

@app.route('/logout')
def logout():
    rm_session()
    return redirect('/')


### Blog Contents Handller Functions ###
def get_blog_contents_handller(url, query):
    db = connect_db()
    contents_list = get_blog_contents(url, query, db)
    close_db()
    return contents_list

def update_blog_contents_handller(request):
    db = connect_db()
    update_blog_contents(request, db)
    close_db()



### Database Connection Functions ###
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('db_schema/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def close_db():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

### Main Function ###
if __name__ == "__main__":
    init_db()
    app.run(debug=True)


