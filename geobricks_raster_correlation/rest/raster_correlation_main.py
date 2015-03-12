from flask import Flask
from flask.ext.cors import CORS
from geobricks_raster_correlation.config.config import config
from geobricks_raster_correlation.rest import raster_correlation_rest as r
import logging

# Initialize the Flask app
app = Flask(__name__)

# Initialize CORS filters
cors = CORS(app, resources={r'/*': {'origins': '*'}})

# Core services.
app.register_blueprint(r.app, url_prefix='/correlation')

# Logging level.
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)

# Start Flask server
if __name__ == '__main__':
    app.run(host=config['settings']['host'], port=config['settings']['port'], debug=config['settings']['debug'], threaded=True)