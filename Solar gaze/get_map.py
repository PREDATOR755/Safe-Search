import folium
import os

# --- CONFIGURATION ---
# Coordinates for Islamabad (Blue Area / F-7 Region)
LATITUDE = 33.7087
LONGITUDE = 73.0592
ZOOM_LEVEL = 19  # High zoom to see rooftops clearly

# --- 1. CREATE MAP ---
print("Generating Satellite Map of Islamabad...")

# Use 'Esri.WorldImagery' for high-res satellite tiles (Free & Public)
m = folium.Map(
    location=[LATITUDE, LONGITUDE],
    zoom_start=ZOOM_LEVEL,
    tiles='Esri.WorldImagery',
    attr='Esri'
)

# --- 2. ADD MARKER (Optional - purely for visual "Class") ---
folium.Marker(
    [LATITUDE, LONGITUDE],
    popup="Target Sector",
    icon=folium.Icon(color="green", icon="leaf")
).add_to(m)

# --- 3. SAVE ---
map_filename = "islamabad_satellite.html"
m.save(map_filename)

print(f"✅ Map saved as '{map_filename}'")
print("👉 Open this file in your browser and take a screenshot of the rooftops!")