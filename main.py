import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import requests
from playsound import playsound

def calculate_distance():
    # To Get the latitude and longitude values from the entry fields
    first_lat = first_latitude.get()
    first_lon = first_longitude.get()
    second_lat = second_latitude.get()
    second_lon = second_longitude.get()

    # The URL API input
    url = f"https://maps.flightmap.io/api/distancematrix?fm_token=Your API token&" \
          f"originlatitude={first_lat}&originlongitude={first_lon}&" \
          f"destinationlatitude={second_lat}&destinationlongitude={second_lon}"

    try:
        # Try to Make the GET request
        response = requests.get(url)
        response_data = response.json()
        if 'data' in response_data and 'distance' in response_data['data']:
            distance = response_data['data']['distance']
            msg = f'Distance: {distance} meters'
            showinfo(
                title='Distance',
                message=msg
            )

            # Play the sound
            playsound(r"C:\Users\yafa\dev\MY_TEST_ENV\distance.mp3")
        else:
            showinfo(
                title='Distance',
                message='Unable to calculate distance. Please check your coordinates.'
            )
    except Exception as e:
        showinfo(
            title='Error',
            message=f'An error occurred: {str(e)}'
        )
# Create the main application window
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title('Check Distance')

# Variables to store latitude and longitude values
first_latitude = tk.DoubleVar()
first_longitude = tk.DoubleVar()
second_latitude = tk.DoubleVar()
second_longitude = tk.DoubleVar()

# Create GUI elements
Distance = ttk.Frame(root)
Distance.pack(padx=10, pady=10, fill='x', expand=True)

first_latitude_label = ttk.Label(Distance, text="First Latitude:")
first_latitude_label.pack(fill='x', expand=True)
first_latitude_entry = ttk.Entry(Distance, textvariable=first_latitude)
first_latitude_entry.pack(fill='x', expand=True)

first_longitude_label = ttk.Label(Distance, text="First Longitude:")
first_longitude_label.pack(fill='x', expand=True)
first_longitude_entry = ttk.Entry(Distance, textvariable=first_longitude)
first_longitude_entry.pack(fill='x', expand=True)

second_latitude_label = ttk.Label(Distance, text="Second Latitude:")
second_latitude_label.pack(fill='x', expand=True)
second_latitude_entry = ttk.Entry(Distance, textvariable=second_latitude)
second_latitude_entry.pack(fill='x', expand=True)

second_longitude_label = ttk.Label(Distance, text="Second Longitude:")
second_longitude_label.pack(fill='x', expand=True)
second_longitude_entry = ttk.Entry(Distance, textvariable=second_longitude)
second_longitude_entry.pack(fill='x', expand=True)

dis_button = ttk.Button(Distance, text="Calculate Distance", command=calculate_distance)
dis_button.pack(fill='x', expand=True, pady=10)

root.mainloop()
