import streamlit as st
import pandas as pd

# 웹 페이지 제목 설정
st.title("🩺 당뇨병 예측 데이터 입력")
st.write("아래의 정보를 입력하시면 데이터프레임으로 변환됩니다.")

# 시각적인 구분을 위한 선
st.markdown("---")

# 레이아웃 나누기 (화면을 2열로 분할하여 깔끔하게 배치)
col1, col2 = st.columns(2)

with col1:
    preg = st.number_input("임신횟수 입력", min_value=0, value=0, step=1)
    glucose = st.number_input("혈당 입력", min_value=0.0, value=0.0, step=1.0)
    bp = st.number_input("혈압 입력", min_value=0.0, value=0.0, step=1.0)
    skin = st.number_input("피부두께 입력", min_value=0.0, value=0.0, step=1.0)

with col2:
    insulin = st.number_input("인슐린 입력", min_value=0.0, value=0.0, step=1.0)
    bmi = st.number_input("체질량지수(BMI) 입력", min_value=0.0, value=0.0, step=0.1)
    dpf = st.number_input("가족력 입력", min_value=0.0, value=0.0, step=0.01)
    age = st.number_input("나이 입력", min_value=0, value=0, step=1)

# DataFrame으로 변환 (2차원 배열 형태)
input_data = pd.DataFrame(
    [[preg, glucose, bp, skin, insulin, bmi, dpf, age]],
    columns=['임신횟수', '혈당', '혈압', '피부두께', '인슐린', '체질량지수', '가족력', '나이']
)

st.markdown("---")

# 결과 출력
st.subheader("📊 변환된 데이터프레임")
st.dataframe(input_data)