from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/school')
def gotoskool():
    return redirect("http://techkids.vn/", code=302)


@app.route('/TagDemo')
def Tag():
    return render_template('DemoTag.html')


@app.route('/mar')
def mp():
    return render_template('marDemo.html')


@app.route('/pad')
def mpp():
    return render_template('padDemo.html')


if __name__ == '__main__':
    app.run(debug=True)
