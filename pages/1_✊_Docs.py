import streamlit as st 
import pandas as pd
import numpy as np

from time import sleep

#page basic setup
st.set_page_config(
    page_icon="🦈",
    page_title="SDSUK's Streamlit Deploy",
    layout="wide",
)

st.subheader("Docs")

if st.button("app.py code view"):
    code = '''
    import streamlit as st 
import pandas as pd
import numpy as np

from time import sleep

#page basic setup
st.set_page_config(
    page_icon="🦈",
    page_title="SDSUK's Streamlit Deploy",
    layout="wide",
)

#header, subheader
st.header("Welcome to SDSUK's Streamlit Page")
st.subheader("Try Streamlit Functions")

#Page Segmentation
cols = st.columns((1, 1, 2))
cols[0].metric("10/11", "15 'C", "2")
cols[0].metric("10/12", "17 'C", "2 'F")
cols[0].metric("10/13", "15 'C", "2")
cols[1].metric("10/14", "17 'C", "2 'F")
cols[1].metric("10/15", "16 'C", "-3 'F")
cols[1].metric("10/16", "14 'C", "-1 'F")

#Line Graph Generation
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)

cols[2].line_chart(chart_data)
    '''
    
    st.code(code, language='python')
