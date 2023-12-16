# app.py

from flask import Flask, render_template, send_from_directory
from pothole_utils import extract_coordinates_from_csv, create_csv_mapping, extract_pothole_data_from_csv

app = Flask(__name__)

app.static_folder = 'static/'

@app.route('/')
def index():
    # Extract coordinates from CSV
    coordinates = extract_coordinates_from_csv('data/gps_logger.csv')
    
    image_path = "/Images/pothole6.jpg"
    # Create the CSV mapper
    create_csv_mapping(image_path, coordinates, 'data/mapped.csv')
    
    # Extract pothole data from the mapped CSV
    pothole_data = extract_pothole_data_from_csv('data/mapped.csv')

    return render_template('simple.html', pothole_data = pothole_data)

# Route to serve static images
@app.route('/Images/<path:filename>')
def send_image(filename):
    return send_from_directory("Images", filename)

if __name__ == '__main__':
    app.run(debug=True)