from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return '<h2 style="color: green">Hello, World!</h2>'
        


@app.route("/bye")
def say_bye():
    return '<img src="https://media.giphy.com/media/BcuDuUQgeSQco/giphy.gif?cid=ecf05e47snr8ispqi7im5g1akuqwa2pov6pzx221fiemez52&ep=v1_gifs_related&rid=giphy.gif&ct=g">'

@app.route("/<username>")
def greet(username):
    return f"Hallo,{username}"


if __name__ == "__main__":
    app.run(debug=True)