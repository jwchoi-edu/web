import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import time


# ----------- 시각화 함수 (렌더용 / 정렬용 구분) -----------
def render_array(arr, highlight_indices=None, delay=0.0):
    st.empty()
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge", color="gray")
    if highlight_indices:
        for idx in highlight_indices:
            bar_rects[idx].set_color("red")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(max(arr)) + 1)
    ax.axis("off")
    st.pyplot(fig)
    if delay > 0:
        time.sleep(delay)


def visualize_sort(arr, generator, delay=0.2):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge", color="gray")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(max(arr)) + 1)
    ax.axis("off")
    placeholder = st.empty()

    for array_state, highlight_indices in generator:
        for idx, rect in enumerate(bar_rects):
            rect.set_height(array_state[idx])
            rect.set_color("red" if idx in highlight_indices else "gray")
        placeholder.pyplot(fig)
        time.sleep(delay)


# ----------- 정렬 알고리즘 -----------
def bubble_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                yield a.copy(), (j, j + 1)


def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        yield a.copy(), (i, min_idx)


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            yield a.copy(), (j + 1, j + 2)
        a[j + 1] = key
        yield a.copy(), (j + 1, i)


def quick_sort(arr):
    a = arr.copy()
    stack = [(0, len(a) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_idx = random.randint(low, high)
            a[pivot_idx], a[high] = a[high], a[pivot_idx]
            yield a.copy(), (pivot_idx, high)
            pivot = a[high]
            i = low
            for j in range(low, high):
                if a[j] < pivot:
                    a[i], a[j] = a[j], a[i]
                    yield a.copy(), (i, j)
                    i += 1
            a[i], a[high] = a[high], a[i]
            yield a.copy(), (i, high)
            stack.extend([(low, i - 1), (i + 1, high)])


# ----------- Streamlit UI -----------
st.title("🔁 정렬 알고리즘 시각화")
st.markdown(
    "배열의 크기를 바꾸면 그래프가 즉시 렌더링되며, 정렬은 '정렬 시작' 버튼을 눌러야 수행됩니다."
)

# session_state 초기화
if "prev_size" not in st.session_state:
    st.session_state.prev_size = None
if "array" not in st.session_state:
    st.session_state.array = []

# 입력 요소
sort_type = st.selectbox(
    "정렬 방식 선택", ["버블 정렬", "선택 정렬", "삽입 정렬", "퀵 정렬"]
)
size = st.slider("배열 크기", 5, 30, 15)
speed = st.slider("속도 (초)", 0.01, 1.0, 0.2)

# 정렬 시작 버튼
if st.button("정렬 시작"):
    st.empty()
    arr = st.session_state.array.copy()
    if sort_type == "버블 정렬":
        visualize_sort(arr, bubble_sort(arr), delay=speed)
    elif sort_type == "선택 정렬":
        visualize_sort(arr, selection_sort(arr), delay=speed)
    elif sort_type == "삽입 정렬":
        visualize_sort(arr, insertion_sort(arr), delay=speed)
    elif sort_type == "퀵 정렬":
        visualize_sort(arr, quick_sort(arr), delay=speed)

if st.button("배열 섞기") or size != st.session_state.prev_size:
    arr = list(range(1, size + 1))
    np.random.shuffle(arr)
    st.session_state.array = arr
    st.session_state.prev_size = size
    render_array(arr)
else:
    if st.session_state.array:
        render_array(st.session_state.array)
