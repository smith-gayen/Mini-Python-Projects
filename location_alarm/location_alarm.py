import time
import pygame
import requests
from geopy.distance import geodesic

# Set the target location and radius (in meters)
target_location = "New York, USA"  # Replace with your desired location
radius = 500  # Adjust the radius as needed

# Set the alarm sound file
alarm_sound = "alarm.mp3"  # Replace with your desired sound file

# Set the Google Maps API key
api_key = "YOUR_API_KEY_HERE"  # Replace with your API key

def play_sound(sound_file):
    pygame.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def get_current_location():
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    response = requests.post(url)
    data = response.json()
    current_lat = data["location"]["lat"]
    current_lon = data["location"]["lng"]
    return current_lat, current_lon

def check_location():
    while True:
        try:
            # Get the current location
            current_lat, current_lon = get_current_location()

            # Get the target location coordinates
            target_coords = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={target_location}&key={api_key}").json()["results"][0]["geometry"]["location"]
            target_lat = target_coords["lat"]
            target_lon = target_coords["lng"]

            # Calculate the distance between the current and target locations
            distance = geodesic((current_lat, current_lon), (target_lat, target_lon)).meters

            if distance <= radius:
                print("You have reached the target location!")
                play_sound(alarm_sound)
                break

        except Exception as e:
            print("Error:", e)

        time.sleep(60)  # Check location every minute

if __name__ == "__main__":
    check_location()