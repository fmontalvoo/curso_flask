from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return app.send_static_file('login.html')


@app.route('/signup', methods=['GET'])
def signup():
    return app.send_static_file('signup.html')


@app.route('/processSignup', methods=['GET', 'POST'])
def processSignup():
    missing = []
    fields = ['nickname', 'email', 'passwd', 'confirm', 'signup_submit']
    data = {}
    for field in fields:
        value = request.form.get(field, None)
        data[field] = value
        if value is None:
            missing.append(field)
    if missing:
        return render_template('missingFields.html', inputs=missing, next=url_for("signup"))
    else:
        return render_template('success_signup.html', data=data)


@app.route('/home', methods=['GET'])
def home():
    return app.send_static_file('home.html')


@app.route('/agente')
def agente():
    user_agent = request.headers.get('User-Agent')
    return "<p>Su navegador es {0}</p>".format(user_agent)
    # return "<p>Su navegador es %s</p>" % user_agent


# @app.route('/ex1')
# def function_for_ex1():
#     return "Content of the url /ex1"

# @app.route('/ex2')
# def function_for_ex2():
#     return """
#     <html>
#         <head>
#             <title>Ex2</title>
#         </head>
#         <body>
#             <h1>Ex2</h1>
#             <a href='/'>/</a>
#         </body>
#     </html>
#     """

# @app.route('/ex2')
# def function_for_ex2():
#     return app.send_static_file('ejemplo.html')
if __name__ == '__main__':
    app.run(debug=True, port=8180)
