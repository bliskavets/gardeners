import streamlit as st


def main():
    st.markdown("# Land degradation in Brazil")
    st.sidebar.markdown("# Home page")

    burned_tab, lc_ts_tab, side_tree_lc_tab = st.tabs(
        ['Burned area', 'Land cover yearly', "Tree land cover 2003-2020"]
    )

    with burned_tab:
        from maps import show_burned_map
        show_burned_map()

    with lc_ts_tab:
        from maps import show_lc_ts_map
        show_lc_ts_map()

    with side_tree_lc_tab:
        from maps import show_side_by_side_tree_lc_map
        show_side_by_side_tree_lc_map()


main()
