import streamlit as st
from maps import show_burned_map
from maps import show_lc_ts_map
from maps import show_side_by_side_tree_lc_map


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

    st.markdown("# 360 interactive insights")

    st.sidebar.markdown("# Land degradation in Brazil")

    st.markdown("### Burned area 2000-2022")
    st.image("/content/burn_rate_history.gif")
    st.markdown("<hr>", unsafe_allow_html=True)

    st.write("### Land cover 2003 vs 2020")
    show_side_by_side_tree_lc_map()
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("### Land cover rates 2000-2022")

    col1, col2, = st.columns(2)
    col3, col4, = st.columns(2)

    with col1:
        st.image("/content/lc_type_1.gif")
        st.markdown(
            "<text style='text-align: center;'>Annual IGBP</text>", unsafe_allow_html=True)

    with col2:
        st.image("/content/lc_type_2.gif")
        st.markdown(
            "<text style='text-align: center;'>Annual UMD</text>", unsafe_allow_html=True)

    with col3:
        st.image("/content/lc_type_3.gif")
        st.markdown(
            "<text style='text-align: center;'>Annual LAI</text>", unsafe_allow_html=True)

    with col4:
        st.image("/content/lc_type_4.gif")
        st.markdown(
            "<text style='text-align: center;'>Annual BGC</text>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.write("### Land cover 2014-2020")
    show_lc_ts_map()
    st.markdown("<hr>", unsafe_allow_html=True)

    st.write("### Normalized Difference Vegetation Index")
    st.image("/content/ndvi.gif")

    st.write("### Burned map")
    show_burned_map()
    st.markdown("<hr>", unsafe_allow_html=True)


main()
