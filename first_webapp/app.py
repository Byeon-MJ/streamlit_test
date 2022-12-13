# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    '''
    # 제 첫 웹페이지(는 아니지만) 입니다.
    ## 부족하지만 많이 사랑해주셔도 되고 안하셔도 됩니다.
    * 1$ = 1,300원 이지만 좀 내렸으면 좋겠네요
    '''
)

if st.button('손대면 눈이 내려요'):
    st.snow()
elif st.button('손대면 풍선이 날아가요'):
    st.balloons()

# https://pixabay.com/ko
st.image(
    'https://cdn.pixabay.com/photo/2015/07/30/22/38/pixabay-868437_960_720.jpg'
)

