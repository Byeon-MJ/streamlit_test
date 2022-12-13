# https://docs.streamlit.io/library/get-started/main-concepts
# https://docs.streamlit.io/library/cheatsheet

# streamlit 라이브러리 호출
import streamlit as st
import numpy as np
import pandas as pd

# st.write() 마크다운
st.title('조 추첨 페이지')
st.header('여러분의 참여를 환영합니다.')

# 추첨 대상인 13명의 이름을 넣을 수 있는 text input 만들기
# 3 X 4 (row, col)
# 열을 배치하는 메소드
# x = columns(n) : n만큼의 컬럼 리스트를 생성

tabs = st.tabs(['참가자', '조'])

# 0번째 탭에 컬럼을 넣겠다.
columns = tabs[0].columns(4)
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# col1, col2, col3, col4
for idx, col in enumerate(columns):
    # 이중 for문
    # col.text_input(f'조 추첨 대상{idx+1}', key = idx)
    for idx2 in range(4):
        # key가 겹치면 안 됨
        # col 안에 메소드를 통해서 요소들을 생성해주겠다.
        col.text_input(f'조 추첨 대상{idx + 1 + idx2 * 4}', 
                        key = f'n{idx + 1 + idx2 * 4}')

# 2번째 : 조
# columns -> columns2, tabs[0] -> tabs[1]
columns2 = tabs[1].columns(4)
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# col1, col2, col3, col4
# columns -> columns2
for idx, col in enumerate(columns2):
    # 이중 for문
    # col.text_input(f'조 추첨 대상{idx+1}', key = idx)
    for idx2 in range(4):
        # key가 겹치면 안 됨
        # col 안에 메소드를 통해서 요소들을 생성해주겠다.
        col.text_input(f'조 목록{idx + 1 + idx2 * 4}', 
                        key = f'g{idx + 1 + idx2 * 4}') # n -> g
                        

# 13명이 소속될 조 이름을 넣을 위치
# st.write(st.session_state)

# np.random.choice -> 추출 -> 이름, 목록 연결
# 1. st.session_state - n, g가 섞여있음
ss = pd.Series(tabs[0].session_state)

# 2. df 형태로 정리


# <추첨 버튼>

# 13개의 짝을 지어서 표시해줄 그래픽