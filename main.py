import streamlit as st
import folium
from streamlit_folium import st_folium

# 여행지 데이터
destinations = [
    {
        "name": "파리 (Paris)",
        "lat": 48.8566,
        "lon": 2.3522,
        "description": "에펠탑, 루브르 박물관, 샹젤리제 거리 등으로 유명한 프랑스의 수도입니다."
    },
    {
        "name": "니스 (Nice)",
        "lat": 43.7102,
        "lon": 7.2620,
        "description": "지중해 해안의 휴양 도시로, 아름다운 해변과 고급 리조트로 유명합니다."
    },
    {
        "name": "리옹 (Lyon)",
        "lat": 45.7640,
        "lon": 4.8357,
        "description": "미식의 도시로 불리며, 유네스코 세계유산에 등재된 구시가지가 있습니다."
    },
    {
        "name": "보르도 (Bordeaux)",
        "lat": 44.8378,
        "lon": -0.5792,
        "description": "와인으로 유명한 도시로, 프랑스 와인 여행의 중심지입니다."
    },
    {
        "name": "몽생미셸 (Mont Saint-Michel)",
        "lat": 48.6361,
        "lon": -1.5115,
        "description": "바다 위에 떠 있는 수도원 섬으로 환상적인 풍경을 자랑합니다."
    }
]

st.title("🇫🇷 프랑스 여행 가이드")
st.write("아래에서 프랑스의 주요 관광지를 확인하고 지도에서 위치를 확인해보세요!")

# Folium 지도 초기화 (중앙 위치를 프랑스로 설정)
m = folium.Map(location=[46.6034, 1.8883], zoom_start=6)

# 마커 추가
for dest in destinations:
    folium.Marker(
        location=[dest["lat"], dest["lon"]],
        popup=f"<b>{dest['name']}</b><br>{dest['description']}",
        tooltip=dest["name"]
    ).add_to(m)

# 지도 출력
st_folium(m, width=700)

# 선택된 도시 정보 제공
st.subheader("🗼 여행지 설명")
selected = st.selectbox("여행지를 선택하세요:", [d["name"] for d in destinations])
for d in destinations:
    if d["name"] == selected:
        st.markdown(f"**{d['name']}**")
        st.write(d["description"])
