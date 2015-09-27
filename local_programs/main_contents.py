from config import *

main_contents = Blueprint("main_contents", __name__)

@main_contents.route('/')
def home():
    """Return a friendly HTTP greeting."""
#    side_bar_contents = return_sidebar_contents()
#    return render_template("home.html", titles=side_bar_contents[0], genres=side_bar_contents[1
    return render_template("home.html")

@main_contents.route('/production')
def production():

    request_url_query = request.args.get('id')
    if request_url_query is not None:
        url = request_url_query + ".html"
        side_bar_contents = return_sidebar_contents()
        return render_template(url, titles=side_bar_contents[0], genres=side_bar_contents[1])
#        print "#####" + request_url_query
#        sql_sentense = 'select * from BlogContents where blogid = \'%s\'' %request_url_query
#        print sql_sentense
#        read_contents = db.GqlQuery(sql_sentense)
#        print read_contents[0].contents

#    contents = [{}]
#
#    message = Markup("<h1>This is flashed Message!!</h1>")
#    flash(message)
#    unko = Markup("<h3>unkounko</h3>")
#    flash(unko)
#    for content in read_contents:
#        tmp = {}
#        tmp["title"] = content.title
#        tmp["content"] = content.contents.split("\n")
#        print "########"
#        print tmp
#        contents.append(tmp)
#    test_contents.contetns = test_contents.contents.split("\n")

    side_bar_contents = return_sidebar_contents()
    return render_template("production.html",contents=contents, titles=side_bar_contents[0], genres=side_bar_contents[1])

@main_contents.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

