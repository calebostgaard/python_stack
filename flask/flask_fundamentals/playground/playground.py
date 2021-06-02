from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/play')
def play():
    return render_template("play_x_color.html", times = 3, color = "#9EC5F8")

@app.route('/play/<int:num>')
def playx(num):
    return render_template("play_x_color.html", times = num, color = "#9EC5F8")


@app.route('/play/<int:num>/<box>')
def playxcolor(num, box):
    return render_template("play_x_color.html", times = num, color = box)





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


