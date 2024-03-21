import streamlit as st
import geemap.foliumap as geemap
import ee
import folium

# Initialize the Earth Engine module.
ee.Authenticate()
ee.Initialize(project='gardeners-417908')

brazil_shapefile = geemap.shp_to_ee('/content/Brazil.shp')
drone_locations = [
    {"name": "drone 1", "lat": -15, "lon": -56,
        "video_url": "/content/sample-video.mp4"},
    {"name": "drone 2", "lat": -29, "lon": -50,
        "video_url": "/content/sample-video.mp4"},
    {"name": "drone 3", "lat": -10, "lon": -45,
     "video_url": "/content/sample-video.mp4"}
]


def show_map():
    with st.spinner():
        # Create a Folium map centered around Brazil
        Map = geemap.Map(center=[-10, -55], zoom=4)

        for drone in drone_locations:
            Map.add_marker(
                location=[drone["lat"], drone["lon"]],
                popup=drone,
                tooltip=drone["name"],
                icon=folium.CustomIcon(
                    icon_image="/content/drone.png",
                    icon_size=(35, 35),
                )
            )

        # Add the Brazil shapefile to the map
        Map.addLayer(brazil_shapefile, {}, "Brazil", opacity=0.5)

        # Display the map
        Map.to_streamlit(height=600)


def main():
    st.markdown("# Detect wildfire realtime")
    st.sidebar.markdown("# Detect wildfire realtime")

    show_map()

    # Add clickable markers for each drone

    # Create a select box for choosing a drone
    drone_names = [drone["name"] for drone in drone_locations]
    selected_drone_name = st.selectbox(
        "Select a drone to view its video:", options=drone_names)

    # Find the selected drone and display its video
    selected_drone = next(
        (drone for drone in drone_locations if drone["name"]
         == selected_drone_name), None
    )

    if selected_drone:
        st.video(selected_drone["video_url"])


main()
