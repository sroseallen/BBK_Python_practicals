# Bokeh tutorial

Go to: https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/HEAD?labpath=index.ipynb
Wait for the page to load, then open the `Quickstart` notebook.


## Gallery examples

Go to the gallery: https://docs.bokeh.org/en/latest/docs/gallery.html
- Choose an example
- Copy/paste it in a notebook (say, the one from this session, or the one from Binder)
- Do you get the same plot?
    - Try modifying the plot: change symbols, colours, element plotted

Repeat the above 2/3 times, for different examples


## Flask+bokeh tutorial

Reprise your flask code from last week:
Take a look at the minimal example `flask_bokeh_minimal.py` provided here,
and incorporate it in last week's flask code.
Alternatively, change the code to incorporate the bokeh+flask example:
https://github.com/bokeh/bokeh/blob/2.4.2/examples/embed/json_item.py

- First, make it run. Can you access the page and see the plot?
- Can you make it plot something else?
    - for example, take code from the bokeh gallery, and change the make_plot() function so that it returns the appropriate plot


## Adapting code to different API

We will attempt to plot some data from uniprot, the protein database
- Copy the notebook `py18_requests_bokeh.ipynb`
- Gather some data from uniprot's API. They have a well documented API, see here:
    https://www.uniprot.org/help/api_queries
    - they even give code using python requests!
    - To get started, you can use the following python line to get data in tsv format (feel free to customise the search term):
        r = requests.get("https://rest.uniprot.org/uniprotkb/search?query=muscle&format=tsv&fields=accession,id,organism_name,mass,length&size=100")
- can you adapt the code to plot the number of entries per Organism? for example using a bar plot, and pandas' groupby and count methods


# A look at alternatives

I recommend you take a look at a couple examples for plotly/dash, and panel.
For each example I would suggest that:
- you test it yourself
- you go take a look at the code
    - try to identify the following:
        - what part does the plotting?
        - what part does the calculation (e.g., what data is generated, that is shown in the plot)?
N.B.: you will not be able to run it all in jupyterhub, if you want to run them all, you may have to do that locally!
    
https://dash.gallery/Portal/
My examples recommendation:
https://dash.gallery/dash-forna-container/
https://dash.gallery/dash-image-segmentation/

https://panel.holoviz.org/index.html
My example recommendation:
https://attractors.pyviz.demo.anaconda.com/attractors_panel
https://portfolio-optimizer.pyviz.demo.anaconda.com/


# Taking it further

If you want to get more into interactive visualisation, those libraries are also worth checking out:
- https://holoviews.org/index.html
- https://panel.holoviz.org/
- https://datashader.org/