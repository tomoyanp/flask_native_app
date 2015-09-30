
def check_login_auth(request):
    input_user = str(request.form['username'])
    input_pass = str(request.form['password'])
    file = open('user.txt', 'r')
    user = file.readline()
    passwd = file.readline()
    input_user = md5.new(input_user).digest()
    input_pass = md5.new(input_pass).digest()
    input_user = input_user.encode('string-escape')
    input_pass = input_pass.encode('string-escape')
    input_user += "\n"
    input_pass += "\n"
    if input_user == user and input_pass == passwd:
        session['administrator'] = user
        url = '/admin'
    else:
        url = '/'


    return url


def check_session():
    check_flag = False
    if 'administrator' in session:
        check_flag = True
    else:
        check_flag = False


    return check_flag



def rm_session():
    if 'administrator' in session:
        session.pop('administrator', None)

