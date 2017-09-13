from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('home_page.html')

@app.route('/dojo/<color>')
def show_color_turtle(color):
    color = color.lower()
    turtles={"purple" : "donatello","orange" : "michelangelo","red" : "raphael","blue" : "leonardo"}
    name = "notapril"
    if color in turtles:
        name = turtles[color]
    return render_template("dojoturtle.html",template_turtle = name)

app.run(debug=True)