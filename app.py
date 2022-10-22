# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:22:20 2022

@author: hardyn
"""

# importing flask
from flask import Flask, render_template
# importing pandas module
# import pandas as pd
  
  
app = Flask(__name__)
  
  

  
  
@app.route('/')
def principal():
    # df = px.data.election()
    # geojson = px.data.election_geojson()
    
    # fig = px.choropleth_mapbox(df, geojson=geojson, color="Bergeron",
    #                            locations="district", featureidkey="properties.district",
    #                            center={"lat": -13.1603, "lon": -74.2258},
    #                            mapbox_style="carto-positron", zoom=9)
    #  fig.show()
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('base.html',)  #, graphJSON=graphJSON
  
if __name__ == "__main__":
      app.run(debug=False)
      # app.run(host="0.0.0.0" ,port="3000",debug=True)