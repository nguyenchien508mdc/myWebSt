#PS> python -m venv venv
#PS> venv\Scripts\activate
import streamlit as st
import pandas as pd
import numpy as np
# Danh sách các phim
movies_data = {
    'Tên phim': ['Inception', 'Interstellar', 'The Matrix', 'The Shawshank Redemption'],
    'Năm phát hành': [2010, 2014, 1999, 1994],
    'Đánh giá IMDb': [8.8, 8.6, 8.7, 9.3]
}
movies_df = pd.DataFrame(movies_data)
def main():
    st.title('Danh sách các phim')
    st.write('Dưới đây là danh sách các phim phổ biến:')
    st.dataframe(movies_df)

if __name__ == '__main__':
    main()
