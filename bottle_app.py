from bottle import static_file, route, run, debug, default_app, request, template, redirect
from hashlib import sha256

def static_file_callback(filename):

    return static_file(filename, root='static')
route('/static/<filename>', 'GET', static_file_callback)


@route('/')
def wrong():
    redirect("/static/index.html")

@route('/<filename>.css')
def stylesheets(filename):
    return static_file('{}.css'.format(filename), root='static')

def create_hash(password):
    pw_bytestering = password.encode()
    return sha256(pw_bytestering).hexdigest()


my_hash = "081e7ddb4f4d75be1fe962d205e9e77cad34f321a5cdc7f013c3bbc4fbaf3d36"


listcomments = []

@route('/comments_post', method='POST')


def do_login():

    comment = request.forms.get('comment')
    password = request.forms.get('password')

    if create_hash(password) == my_hash:
        listcomments.append(comment)

        return template('comment', x=listcomments)
    else:
        return template('wrong')

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()