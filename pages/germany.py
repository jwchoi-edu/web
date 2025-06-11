import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="독일 여행 가이드", layout="wide")

destinations = [
    {
        "name": "베를린 (Berlin)",
        "lat": 52.5200,
        "lon": 13.4050,
        "description": "독일의 수도로, 역사와 예술, 현대문화가 공존하는 도시입니다."
    },
    {
        "name": "뮌헨 (Munich)",
        "lat": 48.1351,
        "lon": 11.5820,
        "description": "옥토버페스트와 BMW 박물관으로 유명한 바이에른 주의 중심 도시입니다."
    },
    {
        "name": "하이델베르크 (Heidelberg)",
        "lat": 49.3988,
        "lon": 8.6724,
        "description": "로맨틱한 성과 전통적인 대학 도시 분위기로 인기 있는 여행지입니다."
    },
    {
        "name": "드레스덴 (Dresden)",
        "lat": 51.0504,
        "lon": 13.7373,
        "description": "바로크 건축과 예술의 중심지로, '엘베의 피렌체'라고 불립니다."
    },
    {
        "name": "쾰른 (Cologne)",
        "lat": 50.9375,
        "lon": 6.9603,
        "description": "고딕 양식의 쾰른 대성당이 있는 라인강의 도시입니다."
    }
]

st.title("🇩🇪 독일 여행 가이드")
st.write("독일의 아름다운 도시들을 둘러보며 여행 계획을 세워보세요!")

m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)
for dest in destinations:
    folium.Marker(
        [dest["lat"], dest["lon"]],
        popup=f"<b>{dest['name']}</b><br>{dest['description']}",
        tooltip=dest["name"]
    ).add_to(m)

st_folium(m, width=700)

selected = st.selectbox("여행지를 선택하세요:", [d["name"] for d in destinations])
for d in destinations:
    if d["name"] == selected:
        st.subheader(d["name"])
        st.write(d["description"])
