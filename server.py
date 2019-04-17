from flask import Flask, request, session, g, redirect, \
    url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('APP_CONFIG_FILE', silent=True)

MAPBOX_ACCESS_KEY = app.config['MAPBOX_ACCESS_KEY']

# starting with template from http://kazuar.github.io/visualize-trip-with-flask-and-mapbox/
@app.route('/mapbox_js')
def mapbox_js():
    return render_template(
        'mapbox_js.html',
        ACCESS_KEY=MAPBOX_ACCESS_KEY
    )


@app.route('/mapbox_gl')
def mapbox_gl():
    return render_template(
        'mapbox_gl.html',
        ACCESS_KEY=MAPBOX_ACCESS_KEY
    )
