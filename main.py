import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title('Two Panels')

    # Chia layout thành hai cột dọc
    col1, col2 = st.columns(2)

    # Panel 1
    with col1:
        st.subheader('Panel 1')
        st.write('This is the content of panel 1.')
        st.checkbox('yes')
        st.button('Click')
        st.radio('Pick your gender',['Male','Female'])
        st.selectbox('Pick your gender',['Male','Female'])
        st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
        st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
        st.slider('Pick a number', 0,50)
        st.number_input('Pick a number', 0,10)
        st.text_input('Email address')
        st.date_input('Travelling date')
        st.time_input('School time')
        st.text_area('Description')
        st.file_uploader('Upload a photo')
        st.color_picker('Choose your favorite color')

    # Panel 2
    with col2:
        st.subheader('Panel 2')
        st.write('This is the content of panel 2.')
        rand=np.random.normal(1, 2, size=20)
        fig, ax = plt.subplots()
        ax.hist(rand, bins=15)
        st.pyplot(fig)
        df=pd.DataFrame(
            np.random.randn(10,2),
            columns=["x","y"]
        )
        st.line_chart(df)

    # Hiển thị button để chuyển đổi giữa các panel
    if st.button('Toggle Panels'):
        st.session_state.show_panel1 = not st.session_state.show_panel1
        st.session_state.show_panel2 = not st.session_state.show_panel2

if __name__ == "__main__":
    if 'show_panel1' not in st.session_state:
        st.session_state.show_panel1 = True
    if 'show_panel2' not in st.session_state:
        st.session_state.show_panel2 = True

    main()
