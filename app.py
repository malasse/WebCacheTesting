from flask import (Flask, make_response, request, render_template, Response)
from flask_cachecontrol import (FlaskCacheControl, cache, cache_for, dont_cache)

app = Flask(__name__)

flask_cache_control = FlaskCacheControl()
flask_cache_control.init_app(app)

@app.route("/")
@cache(no_cache=True, public=True, max_age=60)
def hello_world():
    none_match_value = request.headers.get('If-None-Match')
    response = make_response(render_template('home.html'))
    if none_match_value == 'Patate':
         return Response(status=304)
    response.headers['Etag']='Patate'
    return response


@app.route("/patate")
@cache(no_cache=True, public=True, max_age=60)
def patate():
    last_modified = 'Mon, 24 Jan 2022 15:50:56' 
    response = make_response(render_template('patate.html'))
    modified_since_value = request.headers.get('If-Modified-Since')
    if modified_since_value !=None:
        if modified_since_value >= last_modified:
            return Response(status=304)
    response.headers['Last-Modified']='Mon, 24 Jan 2022 15:50:56'
    return response
 

if __name__ == '__main__':
    app.run(debug=True)