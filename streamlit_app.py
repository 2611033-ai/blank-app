import streamlit as st

menu = ["1.김치볶음밥", "2.돈가스", "3.비빔밥", "4.떡볶이"]

if "votes" not in st.session_state:
    st.session_state.votes = [0, 0, 0, 0]

st.title("메뉴 투표")

choice = st.radio("선택(1~4)", menu)

if st.button("투표"):
    idx = menu.index(choice)
    st.session_state.votes[idx] += 1
    st.success(f"{choice}에 투표했습니다.")

st.write("### 현재 투표 결과")
for item, count in zip(menu, st.session_state.votes):
    st.write(f"{item}: {count}표")

max_votes = max(st.session_state.votes)
if max_votes > 0:
    winners = [menu[i] for i, v in enumerate(st.session_state.votes) if v == max_votes]
    st.write("### 가장 인기 있는 메뉴")
    for w in winners:
        st.write(w)
