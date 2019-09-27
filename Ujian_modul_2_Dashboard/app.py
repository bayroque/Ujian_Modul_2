from flask import Flask,render_template
from cleaning_data import mpg, coba, coba2
from plots import dist1,dist2

app = Flask(__name__)

# print(count_type1())

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/data')
def data():
    data1 = mpg().head()
    return render_template('data.html', data=data1)


@app.route('/stats')
def stats():
    data1 = coba()
    data2 = coba2()
    return render_template('stats.html',datax=data1, datay = data2)

@app.route('/plots')
def plot():
    xdata = dist1()
    xdata2 = dist2()
    return render_template('plots.html',data = [xdata,xdata2])
  

if __name__ == '__main__':
    app.run(debug=True)
    