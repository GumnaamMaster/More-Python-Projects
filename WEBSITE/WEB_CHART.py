from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot/')
def plot():

    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN                  # content delivery network.

    s = datetime.datetime(2015,11,1)
    e = datetime.datetime(2016,3,10)
    df = data.DataReader(name = "GOOG", data_source = "yahoo", start = s, end = e)

    def inc_dec(c, o):
        if c > o:
            value = "increase"
        elif c < o:
            value = "decrease"
        else:
            value = "equal"
        return value

    df["status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df["middle"] = (df.Open + df.Close)/2
    df["height"] = abs(df.Close - df.Open)

    p = figure(x_axis_type = 'datetime', width = 1000, height = 300, sizing_mode = 'scale_width')
    p.title.text = "Candlestick chart"
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12*60*60*1000

    p.segment(df.index, df.High, df.index , df.Low, color = "black")

    p.rect(df.index[df.status == "increase"], df.middle[df.status == "increase"],
           hours_12, df.height[df.status == "increase"], fill_color = "#CCFFFF", line_color = "black")

    p.rect(df.index[df.status == "decrease"], df.middle[df.status == "decrease"],
           hours_12, df.height[df.status == "decrease"], fill_color = "#FF3333", line_color = "black")

    #output_file("candle.html")
    #show(p)

    script, div = components(p)

    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]

    return render_template("plot.html",
                     script1 = script, # this right 'script' is what in line 48, and left 'script1' is in plot.html.
                           div1 = div, # this right 'div' is what in line 48, and left 'div1' is in plot.html.
                     cdn_css = cdn_css, # here the names are same, but concept is same as above.
                       cdn_js = cdn_js) # left one indicates what in plot.html and right one in this file.
                       # as always i predicted awesome, me rocks.
                       # as left one is what that takes a value on the right side so obv.

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True)
