from flask import Flask, render_template
import urlib3, json
app = Flask(_name_)
http = urlib3.PoolManager()
@app.route("/")
def root():
    u = urlib2.open("https://api.nasa.gov/planetary/apod?api_key=eC4rOBcm6DZDVaMUX8bKtJaCNni1RO8Qnc9pM8yt")
    response = u.read()
    data = json.loads(response.data)
    return render_template("index.html", pic = data['url'])
if __name__ == "__main__":
    app.debug = True
    app.run()
