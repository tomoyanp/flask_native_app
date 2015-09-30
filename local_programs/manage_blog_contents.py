from config import *

def get_blog_contents(url, query, db):
    if request_url_query is not None:
        url = "contents/" + request_url_query

    url = url + "html"
    side_bar_contents = get_sidebar_contents()
    contents_list = [url, side_bar_contents[0], side_bar_contents[1]]

    return contents_list

def update_blog_contents(request, db):
    if 'administrator' in session:
        title = request.form['title']
        contents = request.form['content']
        genre = request.form['exist-genre']

        # add new genre to genre list
        if genre == 'null':
            genre = request.form['genre']
    
        blogid = datetime.now().strftime('%Y%m%d%H%M')
        day =  datetime.now().strftime('%Y-%m-%d')
        
        contents = contents.split("\n")

        title = "<h3>" + title + "</h3>"
        contents_tmp = []
        for i in range(len(contents)):
            if re.search('\r', contents[i]):
                contents[i] = contents[i].replace('\r', '')
            if len(contents[i]) > 0:
                contents_tmp.append("<p>" + contents[i] + "</p>")


        blog_store_file = open('templates/contents/' + blogid + '.html', 'w')
        blog_store_file.write(title)
        blog_store_file.write("\n")
        for i in contents_tmp:
            blog_store_file.write(i.encode('utf_8'))
            blog_store_file.write("\n")

        blog_store_file.close()
        g.db = connect_db()
        db.execute('insert into blog_table (title, entry_id, entry_day, fav_count) values (?, ?, ?, ?)', [title, blogid, day, 0])














def get_sidebar_contents(db)
    result = db.execute("select entry_id, entry_day, title  from blog_tabel order by blog_id DESC")
    return result


