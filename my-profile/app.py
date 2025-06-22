# app.py

# 1. 필요한 도구를 가져옵니다 (import)
import streamlit as st
from PIL import Image
# 2. st. 을 이용해서 화면에 글자와 그림을 추가합니다.
st.title("쁘니 요미 감자, 감쁘요 패밀리!")

st.header("우리 가족을 소개드릴게요.")
st.header(" ")
st.write("우리 첫째 쁘니!.")
st.write("쁘니는 5살이에요~ 이뻐서 쁘니에요. 하지만 남자라는 사실은 비밀.")
st.image(img=Image.open('images/pretty.jpg'), width=300)
st.header(" ")

st.write("둘째 요미! 귀여워서 요미이고, 4살이에요.")
st.image(img=Image.open('images/cute.jpg'), width=300)
st.header(" ")

st.write("셋째 감자에요. 3살인데 덩치는 제일 커요.")
st.image(img=image.open('images/pretty.jpg'), width=300)

st.header("우리 만나면 꼭 서로 웃는 모습으로 인사해요. 행복하세요!")
st.balloons()