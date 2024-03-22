import streamlit as st
import geemap.foliumap as geemap
import ee

# # Initialize the Earth Engine module.
# ee.Authenticate()
# ee.Initialize(project='gardeners-417908')

def main():
    custom_css = """
        <style>
            [data-testid="stSidebarNavLink"] {
                font-size: 25px;
            }
        </style>
    """

    # Inject custom CSS with st.markdown
    st.markdown(custom_css, unsafe_allow_html=True)
    
    st.markdown("# Burned area projection 2050")
    st.sidebar.markdown("# Land degradation in Brazil")

    st.image("/content/burned_area.gif", width=500)

main()
