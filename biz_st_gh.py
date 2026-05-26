import streamlit as st

st.title("첫번째 웹페이지 만들기")

# 구분선
st.markdown("***")

st.header("비지니스 모델 분석")

st.markdown("[네이버](https://www.naver.com/) - 검색엔진, 뉴스, 쇼핑, 카페 등 다양한 서비스를 제공하는 포털 사이트")
st.markdown("[홍익대학교](https://www.hongik.ac.kr/) - 예술과 디자인 분야에서 유명한 대학교")

st.markdown("***")

with st.echo():
    name='조민영'
    st.write('Hello,Streamlit!', name)

# 굵게
st.markdown("**굵은 글씨**")

# 기울임
st.markdown("*기울임 글씨*")

# 밑줄 (HTML 태그 활용)
st.markdown("<u>밑줄 글씨</u>", unsafe_allow_html=True)

# 색상 변경 (HTML 활용)
st.markdown("<span style='color:red'>빨간 글씨</span>", unsafe_allow_html=True)

# 구분선
st.markdown("---")

import streamlit as st

st.title("멀티미디어 테스트")


gif_path = "C:/Users/user/OneDrive/Desktop/Business/새 폴더/img.gif"
st.image(gif_path, caption="움직이는 이미지", width=600)

