from flask import Flask, render_template
app = Flask(__name__)

collection = [0,1,1,2,3,5,8]

@app.route("/")
def hello_world():
    print(__name__)
    print("This prints in terminal")
    return "??"
@app.route("/test")
def test():
    return "HI"
@app.route("/my_foist_template")
def test_templt():
    return render_template(
    ''
    )
    return "hi"
if __name__ == "__main__":
    app.debug = True;
    app.run()
    hello_world();
