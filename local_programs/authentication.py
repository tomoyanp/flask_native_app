from config import *

authentication = Blueprint("authentication", __name__)

@authentication.route('/login')
def login():
    """Return a friendly HTTP greeting."""
    return render_template('login.html')

@authentication.route('/login', methods=['POST'])
def console():
    file = open('user.txt', 'r')
    user = file.readline()
    passwd = file.readline()
    input_user = str(request.form['username'])
    input_pass = str(request.form['password'])
    input_user = md5.new(input_user).digest()
    input_pass = md5.new(input_pass).digest()
    input_user = input_user.encode('string-escape')
    input_pass = input_pass.encode('string-escape')
    input_user += "\n"
    input_pass += "\n"
    if input_user == user and input_pass == passwd:
        session['administrator'] = user
        return redirect('/admin')
    else:
        return redirect('/')

@authentication.route('/admin')
def admin_page():
#    side_bar_contents = return_sidebar_contents()
    if 'administrator' in session:
#        return render_template('admin.html', titles=side_bar_contents[0], genres=side_bar_contents[1])
        return render_template('admin.html')
    else:
        return redirect('/')

@authentication.route('/update',methods=['POST'])
def update():
    if 'administrator' in session:
        title = request.form['title']
        contents = request.form['content']
        genre = request.form['exist-genre']

        # add new genre to genre list
        if genre == 'null':
            genre = request.form['genre']
            #bloggenre = BlogGenreList()
            #bloggenre.genrename = genre
    
        blogid = datetime.now().strftime('%Y%m%d%H%M')
        
        contents = contents.split("\n")

        title = "<h3>" + title + "</h3>"
        contents_tmp = []
        for i in range(len(contents)):
            if re.search('\r', contents[i]):
                contents[i] = contents[i].replace('\r', '')
            if len(contents[i]) > 0:
                contents_tmp.append("<p>" + contents[i] + "</p>")


        blog_store_file = open('contents/' + blogid + '.html', 'w')
        blog_store_file.write(title)
        blog_store_file.write("\n")
        for i in contents_tmp:
            #blog_store_file.write(i.decode('unicode-escape'))
            blog_store_file.write(i.encode('utf_8'))
            blog_store_file.write("\n")

        blog_store_file.close()

#        insert_contents = ""
#        insert_contents = insert_contents.join(contents)
        print "###########"
        print contents
#        print insert_contents
        print "###########"
#        new_content = BlogContents()
#        new_content.blogid = blogid
#        new_content.title = title
#        new_content.contents = contents
#        new_content.genre = genre
#        new_content.put()
#        test_contents = db.GqlQuery('select * from BlogContents')
    #    print {'title':test_contents}
    #    print {'contents':test_contents}
#        for test in test_contents:
#            print test.title
#            print test.contents
        return redirect('/')
    else:
        return redirect('/')

@authentication.route('/logout')
def logout():
    if 'administrator' in session:
        session.pop('administrator',None)
    
    return redirect('/')
