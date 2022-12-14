import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temp1 = ""
temp2 = ""
AI26year = [2018,2019,2020]
AI26location = ['강동구', '송파구', '강남구', '서초구', '관악구', '동작구', '영등포구', '금천구', '구로구',
                '강서구', '양천구', '마포구', '서대문구', '은평구', '노원구', '도봉구', '강북구', '성북구',
                '중랑구', '동대문구', '광진구', '성동구', '용산구', '중구', '종로구']
# Using "with" notation
with st.sidebar:
    year = st.radio(
        "원하시는 년도를 선택해 주세요",
        (AI26year[0], AI26year[1], AI26year[2])
    )

if st.sidebar.button('지역 선택'):
    location = st.sidebar.selectbox(
    "지역 선택",
        (
            '강동구', '송파구', '강남구', '서초구', '관악구', '동작구', '영등포구', '금천구', '구로구',
            '강서구', '양천구', '마포구', '서대문구', '은평구', '노원구', '도봉구', '강북구', '성북구',
            '중랑구', '동대문구', '광진구', '성동구', '용산구', '중구', '종로구'
        )
    )
    temp1 = location
st.write(temp1)
if st.sidebar.button('크기 선택'):
    size = st.sidebar.selectbox(
    "크기 선택",
        (
            '소형', '중소형', '중형', '중대형', '대형'
        )
    )
    temp2 = size
st.write(temp2)
tab1, tab2 = st.tabs([":상승세인_차트: Chart", ":카드_파일_상자: Data"])
data = np.random.randn(10, 1)
tab1.subheader("A tab with a chart")
tab1.line_chart(data)
tab2.subheader("A tab with the data")
tab2.write(data)
with st.expander("결론"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")
def showdata():
    location = st.sidebar.selectbox(
    "지역 선택",
        (
            '강동구', '송파구', '강남구', '서초구', '관악구', '동작구', '영등포구', '금천구', '구로구',
            '강서구', '양천구', '마포구', '서대문구', '은평구', '노원구', '도봉구', '강북구', '성북구',
            '중랑구', '동대문구', '광진구', '성동구', '용산구', '중구', '종로구'
        )
    )