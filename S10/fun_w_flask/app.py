from flask import Flask, render_template, request

app = Flask("my app")


@app.route('/')
def index():
    return "<h1>Welcome</h1>"


@app.route('/login')
def login():
    return "Login"


@app.route('/greeting/<name>')
def greeting(name=""):
    return f"hello {name}"


@app.route('/table/<int:rows>/<int:cols>')
def table(rows=10, cols=10):
    return render_template('table.html', rows=rows, cols=cols)


@app.route('/bmi', methods=["GET", "POST"])
def bmi():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        if height > 10:
            height = height / 100
        answer = weight / height**2
        f = open('data.txt', 'a')
        f.write(f"{answer}\n")
        f.close()
        return render_template('bmi.html', bmi=answer)
    else:
        return render_template('bmi.html')


@app.route('/result')
def result():
    f = open('data.txt', 'r')
    data = f.read().split('\n')
    data = [float(d) for d in data if d]
    return render_template('result.html', data=data)

app.run(host="0.0.0.0")
