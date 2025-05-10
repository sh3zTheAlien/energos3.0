import json
from flask import Flask, render_template
from datetime import datetime as dt
#remove "/" in path

app = Flask(__name__)
with open('data.json','r',encoding='UTF-8') as data_file: #replace with actual path in server
    locations_file = json.load(data_file)

@app.route('/')
def home():
    return render_template('home.html', locations=locations_file, year=str(dt.now().year))

@app.route('/locations')
def locations():
    return render_template('locations.html', locations=locations_file, year=str(dt.now().year))

@app.route('/locations/post-<location_id>/<name>')
def destination(name,location_id):
    return render_template('destination.html', year=str(dt.now().year), location=int(location_id), locations=locations_file)

#remove it in sever!, It handles it on its own
if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)