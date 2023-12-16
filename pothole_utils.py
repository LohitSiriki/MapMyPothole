# pothole_utils.py

# get coordinates from csv

import csv

def extract_coordinates_from_csv(file_path):
    coordinates = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lat = float(row['Lat'])
            lon = float(row['Lng'])
            coordinates.append((lat, lon))
    return coordinates

# create a csv file with image path, latitude and longitude
def create_csv_mapping(image_path, coordinates, csv_file_path):
    # Open the CSV file in 'a' (append) mode to add new entries
    with open(csv_file_path, 'a', newline='') as csvfile:
        fieldnames = ['ImagePath', 'Latitude', 'Longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file is empty, write the header
        if csvfile.tell() == 0:
            writer.writeheader()

        # Extract the last coordinate from the list
        last_coordinate = coordinates[-1]

        # Write the entry to the CSV file using the last coordinate and the image path
        writer.writerow({'ImagePath': image_path, 'Latitude': last_coordinate[0], 'Longitude': last_coordinate[1]})


def extract_pothole_data_from_csv(file_path):
    pothole_data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            latitude = float(row['Latitude'])
            longitude = float(row['Longitude'])
            image_path = row['ImageID']
            pothole_data.append({'latitude': latitude, 'longitude': longitude, 'image_path': image_path})
    return pothole_data