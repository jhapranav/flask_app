#comments
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    number=[1,2,3,4,5]
    return render_template(("index2.html"),number=number)

if __name__=="__main__":
    app.run(debug=True)