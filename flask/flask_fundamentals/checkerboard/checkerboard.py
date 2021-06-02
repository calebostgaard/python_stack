from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("checkerboard.html", times1 = 8, times2 = 8, color1 = "rgb(51, 252, 255)", color2 = "black")

@app.route('/<int:num>')
def page1(num):
    return render_template("checkerboard.html", times1 = 8, times2 = num, color1 = "rgb(51, 252, 255)", color2 = "black")

@app.route('/<int:num1>/<int:num2>')
def page2(num1, num2):
    return render_template("checkerboard.html", times1 = num1, times2 = num2, color1 = "rgb(51, 252, 255)", color2 = "black")

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def page3(num1, num2, color1, color2):
    return render_template("checkerboard.html", times1 = num1, times2 = num2, color1 = color1, color2 = color2)


if __name__=="__main__":
    app.run(debug=True)


