import streamlit as st

import geemap
import ee

# # Import other pages
import brazil_boundary

# Page configuration
st.set_page_config(page_title="Multi-Page App", layout="wide")

# Main function to route the app to different pages
def main():
    st.title('Hello, World!')
    st.write('This is a simple Streamlit app.')

    if st.button("View Brazil Boundary"):
        # This will change the URL and rerun the app
        st.query_params['page'] = "brazil_boundary"

# Check if a page is requested through URL query parameters
query_params = st.query_params.to_dict()
page = query_params.get("page", "")

if page == "brazil_boundary":
    brazil_boundary.show()
else:
    main()
