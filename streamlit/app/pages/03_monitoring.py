import streamlit as st
import geemap.foliumap as geemap
import ee
import folium

# Initialize the Earth Engine module.
ee.Authenticate()
ee.Initialize(project='gardeners-417908')

custom_css = """
    <style>
        [data-testid="stSidebarNavLink"] {
            font-size: 25px;
        }
    </style>
"""

# Inject custom CSS with st.markdown
st.markdown(custom_css, unsafe_allow_html=True)

brazil_shapefile = geemap.shp_to_ee('/content/Brazil.shp')
drone_locations = [
    {"name": "drone 1", "lat": -15, "lon": -56,
     "video_url": "/content/sample-video.mp4"},
    {"name": "drone 2", "lat": -29, "lon": -50,
     "video_url": "/content/sample-video.mp4"},
    {"name": "drone 3", "lat": -10, "lon": -45,
     "video_url": "/content/sample-video.mp4"}
]

satellite_hotspots = [
    {'lat': d['lat'] - 2 if ix % 2 == 0 else d['lat'] + 2,
     'lon': d['lon'] - 2 if ix % 2 == 0 else d['lon'] + 2,
     'prob': 15 * ix,
        'name': f'Hotspot {ix}', 'image_url': f"/content/space_view_{ix}.jpg"
     }
    for ix, d in enumerate(drone_locations, 1)
]


def show_drone_map():



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

        for hotspot in satellite_hotspots:
            icon = folium.CustomIcon(
                icon_image='/content/red_rect.png',  # Specify the path to your custom icon image
                icon_size=(35, 35)  # Adjust the size of the icon as needed
            )
            marker = folium.Marker(
                location=[hotspot["lat"], hotspot["lon"]],
                icon=icon,
            )
            Map.add_child(marker)

        # Add the Brazil shapefile to the map
        Map.addLayer(brazil_shapefile, {}, "Brazil", opacity=0.5)

        # Display the map
        Map.to_streamlit(height=600)


def show_drone_tab():
    show_drone_map()

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


@st.cache_data
def show_satellite_map():
    Map = Map = geemap.Map(center=[-10, -55], zoom=3)

    Map.add_basemap('HYBRID')

    # Add Brazil's boundaries to the map
    Map.addLayer(brazil_shapefile, {}, 'Brazil', opacity=0.8)

    for hotspot in satellite_hotspots:
        icon = folium.CustomIcon(
            icon_image='/content/red_rect.png',  # Specify the path to your custom icon image
            icon_size=(15, 15)  # Adjust the size of the icon as needed
        )
        marker = folium.Marker(
            location=[hotspot["lat"], hotspot["lon"]],
            icon=icon,
            tooltip=f"{hotspot['name']} (prob {hotspot['prob']}%)",
        )
        Map.add_child(marker)

    # Display the map in Streamlit
    Map.to_streamlit(height=600)


def show_satellite_tab():
    show_satellite_map()

    # Create a select box for choosing a drone
    hostpot_names = [hs["name"] for hs in satellite_hotspots]
    selected_hs_name = st.selectbox(
        "Select a hotspot to view:", options=hostpot_names)

    # Find the selected drone and display its video
    selected_hs = next(
        (hs for hs in satellite_hotspots if hs["name"]
         == selected_hs_name), None
    )

    if selected_hs:
        st.image(selected_hs["image_url"])


def main():
    st.markdown("# Monitoring wildfire realtime")
    st.sidebar.markdown("# Land degradation in Brazil")

    satellite_tab, drone_tab = st.tabs(
        ['step 1: satellite detection', 'step 2: drone validation']
    )

    with satellite_tab:
        show_satellite_tab()

    with drone_tab:
        show_drone_tab()


main()
