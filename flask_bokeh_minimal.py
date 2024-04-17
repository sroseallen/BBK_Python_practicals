from flask import Flask

from bokeh.resources import CDN
from bokeh.plotting import figure
from bokeh.embed import file_html

app = Flask(__name__)

@app.route("/")
def make_plot():
    plot = figure()
    plot.circle([1,2,3,4], [5,6,7,8])
    return file_html(plot, CDN, "myplot")
