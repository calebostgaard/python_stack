from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/<name>')
def hello(name):
    print(name)
    return "Hello, " + name + "!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    print(num)
    print(word)
    return num * (" " + word)

# @app.route('/<phrase>')
# def wrong(phrase):
#     print(phrase)
#     return "Sorry! No response. Try again."


if __name__=="__main__":
    app.run(debug=True)

