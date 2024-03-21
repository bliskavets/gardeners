import streamlit as st
import geemap.foliumap as geemap
import ee

# Initialize the Earth Engine module.
ee.Authenticate()
ee.Initialize(project='gardeners-417908')

def show():
    st.title('Brazil Boundary Visualization')

    # Define visualization parameters
    igbpLandCoverVis = {
        'min': 1.0,
        'max': 17.0,
        'palette': [
            '05450a', '086a10', '54a708', '78d203', '009900', 'c6b044',
            'dcd159', 'dade48', 'fbff13', 'b6ff05', '27ff87', 'c24f44',
            'a5a5a5', 'ff6d4c', '69fff8', 'f9ffa4', '1c0dff',
        ],
    }

    try:
        brazil_shapefile = geemap.shp_to_ee('/content/Brazil.shp')
        landcover = ee.Image('MODIS/006/MCD12Q1/2004_01_01').select('LC_Type1')
        brazil_lc = landcover.clip(brazil_shapefile)

        Map = geemap.Map()
        Map.setCenter(-55, -10, 4)
        Map.addLayer(brazil_lc, igbpLandCoverVis, 'MODIS Land Cover')
        Map.to_streamlit(height=600)
        
    except Exception as e:
        st.error(f'Error loading data: {e}')
