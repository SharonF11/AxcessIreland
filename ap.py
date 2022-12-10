from flask import Flask, render_template, app


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/user')
def user():
    return render_template("user.html")

@app.route('/subscription')
def subscription():
    return render_template("subscription.html")

    #custom error pages 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    #app = create_app()
    app.run(debug=True)