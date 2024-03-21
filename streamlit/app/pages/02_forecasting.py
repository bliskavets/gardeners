import streamlit as st
import geemap.foliumap as geemap
import ee

# # Initialize the Earth Engine module.
# ee.Authenticate()
# ee.Initialize(project='gardeners-417908')

def main():
    st.markdown("# Burned area projection 2050")
    st.sidebar.markdown("# Land degradation in Brazil")
    st.image("/content/burned_area.gif")

main()
