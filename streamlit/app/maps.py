
import streamlit as st
import geemap.foliumap as geemap
import ee

# Initialize the Earth Engine module.
ee.Authenticate()
ee.Initialize(project='gardeners-417908')

brazil_shapefile = geemap.shp_to_ee('/content/Brazil.shp')
igbpLandCoverVis = {
    'min': 1.0,
    'max': 17.0,
    'palette': [
        '05450a',
        '086a10',
        '54a708',
        '78d203',
        '009900',
        'c6b044',
        'dcd159',
        'dade48',
        'fbff13',
        'b6ff05',
        '27ff87',
        'c24f44',
        'a5a5a5',
        'ff6d4c',
        '69fff8',
        'f9ffa4',
        '1c0dff',
    ],
}


lc03 = ee.Image('MODIS/006/MCD12Q1/2003_01_01').select('LC_Type1')
lc14 = ee.Image('MODIS/006/MCD12Q1/2014_01_01').select('LC_Type1')
lc15 = ee.Image('MODIS/006/MCD12Q1/2015_01_01').select('LC_Type1')
lc16 = ee.Image('MODIS/006/MCD12Q1/2016_01_01').select('LC_Type1')
lc17 = ee.Image('MODIS/006/MCD12Q1/2017_01_01').select('LC_Type1')
lc18 = ee.Image('MODIS/006/MCD12Q1/2018_01_01').select('LC_Type1')
lc19 = ee.Image('MODIS/006/MCD12Q1/2019_01_01').select('LC_Type1')
lc20 = ee.Image('MODIS/006/MCD12Q1/2020_01_01').select('LC_Type1')

brazil_lc03 = lc03.clip(brazil_shapefile)
brazil_lc14 = lc14.clip(brazil_shapefile)
brazil_lc15 = lc15.clip(brazil_shapefile)
brazil_lc16 = lc16.clip(brazil_shapefile)
brazil_lc17 = lc17.clip(brazil_shapefile)
brazil_lc18 = lc18.clip(brazil_shapefile)
brazil_lc19 = lc19.clip(brazil_shapefile)
brazil_lc20 = lc20.clip(brazil_shapefile)


@st.cache_data
def show_lc_map():
    Map = geemap.Map()

    landcover = ee.Image('MODIS/006/MCD12Q1/2004_01_01').select('LC_Type1')
    brazil_lc = landcover.clip(brazil_shapefile)

    Map.setCenter(-55, -10, 4)
    Map.addLayer(brazil_lc, igbpLandCoverVis, 'MODIS Land Cover')

    Map.to_streamlit(height=600)

    *_, col_3 = st.columns(3)
    with col_3:
        st.image("/content/lc_legend.png")


@st.cache_data
def show_burned_map():
    try:
        brazil_shapefile = geemap.shp_to_ee('/content/Brazil.shp')
        # Define the dataset and filter by date
        dataset = ee.ImageCollection(
            'MODIS/061/MCD64A1').filter(ee.Filter.date('2017-01-01', '2018-05-01'))
        burnedArea = dataset.select('BurnDate')

        # A FeatureCollection defining Brazil boundary.
        fc = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017').filter(
            'country_na == "Brazil"'
        )

        # Clip the burned Area by the Brazil boundary FeatureCollection.
        # Iterate over the ImageCollection and clip each image to the FeatureCollection.
        ba_clip = burnedArea.map(lambda img: img.clipToCollection(fc))

        # Visualization parameters
        burnedAreaVis = {
            'min': 30.0,
            'max': 341.0,
            'palette': ['4e0400', '951003', 'c61503', 'ff1901']
        }

        # Create a map
        Map = geemap.Map(center=[-10, -55], zoom=4)

        # Add burned area layer to the map
        Map.addLayer(ba_clip, burnedAreaVis, 'Burned Area')
        Map.addLayer(brazil_shapefile, name='Brazil', opacity=0.5)
        Map.addLayerControl()

        Map.to_streamlit(height=600)

    except Exception as e:
        st.error(f'Error loading data: {e}')


@st.cache_data
def show_lc_ts_map():
    Map = geemap.Map()

    Map.setCenter(-55, -10, 4)
    Map.addLayer(brazil_lc14, igbpLandCoverVis, 'MODIS Land Cover 2014')
    Map.addLayer(brazil_lc15, igbpLandCoverVis, 'MODIS Land Cover 2015')
    Map.addLayer(brazil_lc16, igbpLandCoverVis, 'MODIS Land Cover 2016')
    Map.addLayer(brazil_lc17, igbpLandCoverVis, 'MODIS Land Cover 2017')
    Map.addLayer(brazil_lc18, igbpLandCoverVis, 'MODIS Land Cover 2018')
    Map.addLayer(brazil_lc19, igbpLandCoverVis, 'MODIS Land Cover 2019')
    Map.addLayer(brazil_lc20, igbpLandCoverVis, 'MODIS Land Cover 2020')

    Map.addLayerControl()

    Map.to_streamlit(height=600)


@st.cache_data
def show_tree_map():
    dataset = ee.ImageCollection('WorldPop/GP/100m/pop')

    # Visualization parameters
    visualization = {
        'bands': ['population'],
        'min': 0.0,
        'max': 50.0,
        'palette': ['24126c', '1fff4f', 'd4ff50']
    }

    # Set center of the map
    Map = geemap.Map()

    # Add the layer to the map
    image = dataset.mean()
    Map.addLayer(image, visualization, 'Population')

    years = range(2002, 2021, 5)  # 2002 to 2020
    lc_images = []

    for year in years:
        lc_image = ee.Image(
            f"MODIS/006/MCD12Q1/{year}_01_01").select('LC_Type1')
        lc_images.append(lc_image)

    # Clip the land cover images to Brazil
    brazil_lc_images = [lc.clip(brazil_shapefile) for lc in lc_images]

    # Display the land cover images for each year
    Map = geemap.Map(center=[-10, -55], zoom=4)

    for i, lc_image in enumerate(brazil_lc_images):
        Map.addLayer(lc_image, igbpLandCoverVis,
                     f'MODIS Land Cover {years[i]}')



    Map.add_legend(
        title="Land cover",
        builtin_legend='MODIS/006/MCD12Q1',
        position='bottomright',
        draggable=True
    )

    Map.to_streamlit(height=600)


@st.cache_data
def show_side_by_side_tree_lc_map():
    Map = geemap.Map(center=[-9, -51], zoom=7)

    left_layer = geemap.ee_tile_layer(brazil_lc03, igbpLandCoverVis, "MODIS")
    right_layer = geemap.ee_tile_layer(brazil_lc20, igbpLandCoverVis, "MODIS")

    Map.split_map(left_layer, right_layer)
    # Map.add_legend(
    #     title="Land cover 2003", builtin_legend='MODIS/006/MCD12Q1', position='bottomleft'
    # )
    Map.add_legend(
        title="Land cover 2003-2020",
        builtin_legend='MODIS/006/MCD12Q1',
        position='bottomright',
        draggable=True
    )

    Map.to_streamlit()
