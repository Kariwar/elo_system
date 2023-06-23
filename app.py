import streamlit as st
st.title("Match Result")

# Team names
member_1_t1 = st.text_input("Enter Team 1 member 1", "Member 1")
member_2_t1 = st.text_input("Enter Team 1 member 2", "Member 2")
member_1_t2 = st.text_input("Enter Team 2 member 1", "Member 1")
member_2_t2 = st.text_input("Enter Team 2 member 2", "Member 2")

# Match result
result = st.selectbox("Winners are ?",
                      [f"{member_1_t1} et {member_2_t1}", f"{member_1_t2} et {member_2_t2}"])
if st.button("Submit"):
    st.write(f"{member_1_t1} et {member_2_t1} vs {member_1_t2} et {member_2_t2}")
    st.write(f"Result: {result}")
