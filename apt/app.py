import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import plotly.express as px


## 함수관련
def draw_plot(df, location = '지역선택', size = '크기선택'):
    if (location == '지역선택') & (size == '크기선택'):
        st.image("./apt/sample.jpg")

    elif location == '지역선택':
        # 크기 선택, 구별 확인
        data = df[['자치구 명',f'{size} 거래건수', f'{size} 거래금액']]

        # 거래 건수     
        fig1 = px.bar(data, x='자치구 명', y=f'{size} 거래건수')
        fig1.update_traces(marker={"color": "magenta",
                                    "opacity": 0.5})

        # 거래 금액
        fig2 = px.bar(data, x='자치구 명', y=f'{size} 거래금액')

        st.plotly_chart(fig1, theme='streamlit')
        st.plotly_chart(fig2, theme='streamlit')

        # fig1 = px.bar(data, x='자치구 명', y='소형 거래건수')
        # fig2 = px.bar(data, x='자치구 명', y='소형 거래금액')
        # st.plotly_chart(fig1)
        # # st.plotly_chart(fig2)

    elif size == '크기선택':
        # 구 선택, 크기별 확인
        data = pd.DataFrame(df.set_index('자치구 명').T.iloc[1:6,:][location])
        data = data.reset_index().rename(columns = {'index':'크기'})
        
        # 거래 건수
        fig1 = px.bar(data, x=location, y='크기')
        fig1.update_traces(marker={"color": "magenta",
                                  "opacity": 0.5})
        
        # 거래 금액
        fig2 = px.bar(data, x=location, y='크기')

        st.plotly_chart(fig1, theme='streamlit')
        st.plotly_chart(fig2, theme='streamlit')

    else:
        # 지역, 크기 둘 다 선택
        data = df[['자치구 명',f'{size} 거래건수', f'{size} 거래금액']]
        data_loc = data[data['자치구 명'] == location]
        
        # 거래 건수
        fig1 = px.bar(data_loc, x='자치구 명', y=f'{size} 거래건수')
        fig1.update_traces(marker={"color": "magenta",
                                   "opacity": 0.5})

        # 거래 금액
        fig2 = px.bar(data_loc, x='자치구 명', y=f'{size} 거래금액')

        st.plotly_chart(fig1, theme='streamlit')
        st.plotly_chart(fig2, theme='streamlit')



# 선택 옵션 데이터

AI26year = [2018,2019,2020]
AI26location = ['강동구', '송파구', '강남구', '서초구', '관악구', '동작구', '영등포구', '금천구', '구로구',
                '강서구', '양천구', '마포구', '서대문구', '은평구', '노원구', '도봉구', '강북구', '성북구',
                '중랑구', '동대문구', '광진구', '성동구', '용산구', '중구', '종로구']


#사이드바에서 원하는 데이터 옵션 선택하기
with st.sidebar:                    #사이드바 라디오 년도 선택
    year = st.radio(
        "원하시는 년도를 선택해 주세요",
        (AI26year[0], AI26year[1], AI26year[2])
    )

location = st.sidebar.selectbox(             #사이드바 선택박스 지역 선택
        "지역 선택",
        (
            '지역선택', '강동구', '송파구', '강남구', '서초구', '관악구', '동작구', '영등포구', '금천구', '구로구',
            '강서구', '양천구', '마포구', '서대문구', '은평구', '노원구', '도봉구', '강북구', '성북구',
            '중랑구', '동대문구', '광진구', '성동구', '용산구', '중구', '종로구'
        )
    )
size = st.sidebar.selectbox(                     #사이드바 선택박스 크기 선택
    "크기 선택",
        (
            '크기선택', '소형', '중소형', '중형', '중대형', '대형'
        )
    )



#데이터 불러오기, 가공

df = pd.read_csv(f'./apt/df_{year}.csv') #선택한 년도 데이터 불러오기

# draw_plot(df, location, size)




# 탭에서 데이터 그리기

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])          #탭1으로 그래프로 볼지, 탭2로 데이터 프레임으로 볼지 선택
with tab1:                                             #탭 1 헤더
    if (location == '지역선택') & (size == '크기선택'):
        tab1.subheader(f"{year}년도  그래프: 지역과 크기를 선택해 주세요.")
    elif (location != '지역선택') & (size == '크기선택'):
       tab1.subheader(f"{year}년도 {location}별 매매현황 그래프")
    elif (location == '지역선택') & (size != '크기선택'):
        tab1.subheader(f"{year}년도 {size}별 매매현황 그래프")
    else:
        tab1.subheader(f"{year}년도 {location}지역 ,{size}별 매매현황 그래프")                
    draw_plot(df, location, size)                                #탭 1 그래프 출력

                               #탭 2 헤더
tab2.subheader(f"{year}년도 그래프")                     
tab2.write(df)                                        #탭 2 데이터 출력



with st.expander("결론"):                                #결론 출력(최곳값, 최솟값 등등)
    if (location == "지역선택"):
        st.write(f"""
                    - 지역별 최고 매매가: max값
                    - 지역별 최소 매매가: min값
                """)
    else:
        st.write(f"""
                    * {location}
                    - 최고 매매가: max값
                    - 최소 매매가: min값
                    - 최고 선호하는 사이즈:
                    - 최고 불호하는 사이즈:
                """)        

from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster

geo = pd.read_csv('./apt/seoul_geo.csv', encoding='cp949')
geo_df = geo[['구명', '경도', '위도']].rename(columns = {'구명' : '자치구 명','경도' : 'lon', '위도':'lat'}).set_index('자치구 명')

df_merge = pd.merge(left=df.reset_index(), right=geo_df.reset_index(), how='inner')


def plot(df):
    # 리스트를 이용해 여러 행의 데이터를 위,경도로 묶음
    center = [37.58, 127.0]
    m = folium.Map(location=center, tiles='openstreetmap', zoom_start=12)

    locations = df[['lat', 'lon']].values[:len(df)].tolist()

    for i in range(len(df)):
        df_id = df['자치구 명'][i]
        tr_count = df['소형 거래건수'][i]

        if tr_count < 100 :
            df_color = 'blue'
        elif (tr_count >= 100) & (tr_count < 200):
            df_color = 'red'
        else:
            df_color = 'black'

        folium.Circle(location=locations[i], radius=tr_count, color = df_color, fill=True, fill_opacity=0.7).add_to(m)

    # 지도에 클러스터를 추가.
    # MarkerCluster(locations).add_to(m)

    return m



st_data = st_folium(plot(df_merge), width=700)

st_data