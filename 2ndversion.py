from flask import (Flask, render_template)
from flask_caching import Cache

app = Flask(__name__)
cache = Cache()

app = Flask(__name__)
app.config['CACHE_TYPE']= 'simple'
cache.init_app(app)

@app.route("/")

@cache.cached(timeout=50)
def hello_world():
    return render_template('home.html')

@app.route("/patate")
def patate():
    return render_template('patate.html')
if __name__ == '__main__':
    app.run(debug=True,port=5000)

   