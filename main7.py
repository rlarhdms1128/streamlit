import streamlit as st
import pandas as pd
import folium
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='하이',
    page_icon='ㅇㅇ')

menu = st.selectbox('MENU', ['자기소개', '학교소개', '동아리소개', '관심분야',"디지털 교과서"])
if menu == '자기소개':
    st.subheader('자기소개')
    st.write("이름:김고은")
    st.write("나이:18세")
    st.write("소속:매천고등학교 2학년 7반")
    st.write("MBTI:잇티제")
    st.write("인스타: cherish__1128")
    image = Image.open("인스타.png")
    st.image(image)
    st.write("좋아하는노래")
    image = Image.open("앨범.png")
    st.image(image)
    audio_file = open('노래.mp3', 'rb')
    st.audio(audio_file.read(), format='audio/mp3')


elif menu == '학교소개':
    st.subheader('학교소개')

    image = Image.open("매천고등학교.jpg")
    st.image(image, caption="매천고등학교")
    st.write("제가 다니는 매천고등학교는 대구 북구에 위치한 고등학교 입니다!")

    base_position = [35.91249, 128.5474]

    map_data = pd.DataFrame(
        np.random.randn(5, 1) / [20, 20] + base_position,
        columns=['lat', 'lon'])
    print(map_data)


    st.subheader('Map of Data ')
    st.map(map_data)


    image = Image.open("매일.jpg")
    st.image(image)
    st.write("참고로 매천고는 매일 천개의 꿈이 영그는 고품격학교.....라는 뜻이 있다고 합니다..")
    image = Image.open("ai 중심.png")
    st.image(image, caption="ai 융합교육 중심")
    st.write("저희 학교는 AI융합교육 중심 고등학교로 관련된 다양한 경험을 할 수 있습니다")
    st.write("이 분야에 관심이 있는 학생은 더욱 도움을 많이 받을 수 있습니다.")
    image = Image.open("도서관.png")
    st.image(image, caption="도서관")
    st.write("깔끔하고 편안한 도서관이 있어 학생들이 애용합니다")
    image = Image.open("공원.png")
    st.image("공원.png", caption="만남의 공간...")
    st.write("급식실 옆 자리한 작은 공원")
    st.write("보통 점심시간에 학생들이 많이 애용한다")

    video_file = open('브이로그.mp4', 'rb')
    st.video(video_file)
    st.write("매천고 학생 유튜브 브이로그 영상(여으이)")

elif menu == '동아리소개':
    st.subheader('동아리소개')
    st.write("제가 현재 소속한 동아리는 소프트웨어 동아리 입니다.")
    st.write("참고로 현재 수업을 해주시는 마호돌 선생님 께서 맡아주시고 계십니다.")
    image = Image.open("동아리.jpg")
    st.image(image, caption="동아리 홍보 포스터")
    st.write("저희 동아리는 게임개발과 웹개발로 나뉘어 각자 활동을 합니다.")
    st.write("그래서 프로그램 중에서도 더 자신에게 맞는 활동을 선택 할 수 있습니다.")
    image = Image.open("동아리활동.jpg")
    st.image(image, caption="동아리 활동 중 사진")
    st.write("저는 현재 웹개발팀에서 동아리 활동을 하고 있습니다.")
    st.write("현재는 streamlit 등을 활용하여 실용적인 활동을 합니다.")
    image = Image.open("게임.jpg")
    st.image(image, caption="게임 동아리 활동 중 사진")


elif menu == '관심분야':
    st.subheader('관심분야')
    st.write("제 관심 분야는 웹개발이고 현재 컴퓨터공학과 진학을 희망하고 있습니다.")
    st.write("그래서 1학년 때 부터 관련 활동을 많이 하기 위해 노력 하고 있습니다.")
    st.write("저는 1학년 때 인공지능 개발 동아리에서도 다양한 경험을 했습니다.")
    image = Image.open("1학년동아리1.png")
    st.image(image, caption="동아리 활동 중 사진")
    st.write("위 사진은 움직이는 울타리 보호대를 만들기 위해 아두이노와 초음파 센서를 이용하는 모습입니다.")
    st.write("2학년에 올라와서도 다양한 경험을 했는데")
    st.write("그 중 가장 기억에 남는 활동은 바로 소인수 수업입니다")
    image = Image.open("소인수.png")
    st.image(image, caption="소인수 수업 발표 자료")
    st.write("저 초록색 그래프는 대구의 분야별 상점 수를 분석하여 시각화 한 것 입니다")
    image = Image.open("이디야.png")
    st.image(image, caption="대구의 이디야, 스타벅스 상권 분포도")
else:
    st.title(' III 파동과 정보 통신 ')
    st.header("파동의 진행과 굴절")
    st.write("파동:한 곳에서 생긴 진동이 주위로 퍼져 나가며 에너지를 전달하는 현상")
    st.write("파원:파동이  발생한 지점")
    st.write("매질:파동을 전달하는 물질")


    data = {
        '구분': ['정의', '예'],
        '횡파': ["파동의 진행 방향과 매질의 진동 방향이 수직인 파동", "물결파, 전자기파, 지진파의 S파"],
        '종파': ['파동의 진행 방향과 매질의 진동방향이 나란한 파동', '음파,지진파의 p파']
    }

    # Streamlit을 사용하여 표 표시
    st.subheader('파동의 종류')
    st.dataframe(data)
    image = Image.open("파동.png")
    st.image(image, caption="횡파와 종파의 이미지")
    st.subheader("파동의 그래프(횡파)")
    x = np.linspace(0, 10, 200)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)
    st.subheader("파동의 요소")
    st.write("마루와 골:횡파의 파동에서 가장 높은 곳이 마루, 가장 낮은 곳이 골")
    st.write("진폭: 진동의 중심에서 마루 또는 골 까지의 거리")
    st.write("파장: 이웃한 마루(골)와 마루(골) 사이의 거리")
    st.write("주기:매질의 한 점이 1번 진동하는 데 걸리는 시간[단위:초]")
    st.write("진동수:매질의 한점이 1초 동안 진동하는 횟수=1/주기 [단위:Hz]")
    st.subheader("파동의 속력")
    st.info("파동의 속력(V)=파장(λ)/주기(T)=진동수(f)x파장(λ),V=fxλ")



    st.subheader('파동 속력 계산기')

    파장=st.number_input('파장을 입력하세요.(cm)', step=1)

    K= st.number_input('주기나 진동수를 입력하세요.[단위:초 or Hz],주기와 진동수>0', step=1)



    col1, col2 = st.columns([2, 3])

    with col1:
        a=st.checkbox('주기')
    with col2:
        b=st.checkbox('진동수 ')

    btn = st.button('계산하기')

    if btn:
        if a:
            st.write(파장/K)
        elif b:
            st.write(파장*K)
        else:
            st.write("주기나 진동수 중에 하나를 선택하세요")



