import json
from flask import Blueprint
from flask import Response
from flask.ext.cors import cross_origin
from geobricks_raster_correlation.core.raster_correlation_core import get_correlation

app = Blueprint(__name__, __name__)

@app.route('/discovery/')
@cross_origin(origins='*')
def discovery():
    """
    Discovery service available for all Geobricks libraries that describes the plug-in.
    @return: Dictionary containing information about the service.
    """
    out = {
        'name': 'RASTER CORRELATION',
        'description': 'Functionalities to correlate raster data.',
        'type': 'RASTER_CORRELATION'
    }
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@app.route('/rasters/scatter_plot/<layers>/', methods=['POST'])
@app.route('/rasters/scatter_plot/<layers>', methods=['POST'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_scatter_plot(layers):
    try:
        """
        Create a scatter plot from two rasters of the same dimension
        @param layers: NO!!!! CHANGE IT!!! workspace:layername1,workspace:layername2
        @return: json with the scatter plot data
        """

        if ":" not in layers:
            return Exception("Please Specify a workspace for " + str(layers), 400)
        input_layers = layers.split(",")

        raster_path1 = "/test/"
        raster_path2 = "/test/"

        # creating scatter
        response = get_correlation(raster_path1, raster_path2, 300)

        return Response(json.dumps(response), content_type='application/json; charset=utf-8')
    except Exception, e:
        raise Exception(e.get_message(), e.get_status_code())