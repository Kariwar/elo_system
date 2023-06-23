import streamlit as st
import pandas as pd
st.title("Match Result")

# Team names
member_1_t1 = st.text_input("Enter Team 1 member 1", "Member 1")
member_2_t1 = st.text_input("Enter Team 1 member 2", "Member 2")
member_1_t2 = st.text_input("Enter Team 2 member 1", "Member 1")
member_2_t2 = st.text_input("Enter Team 2 member 2", "Member 2")

# Match result
result = st.selectbox("Winners are ?",
                      [f"{member_1_t1} et {member_2_t1}", f"{member_1_t2} et {member_2_t2}"])

print('Test affichage')

if st.button("Submit"):
    st.write(f"{member_1_t1} et {member_2_t1} vs {member_1_t2} et {member_2_t2}")
    st.write(f"Result: {result}")
    df = pd.DataFrame(data={"result": [result]})
    df.to_csv('result.csv')
    import requests

    # SharePoint file url
    url = "https://verisure.sharepoint.com/:x:/r/sites/TTT-TeamBI-DataScience/Shared%20Documents/Data%20Science/Babyfoot.xlsx?d=w5a777f721ea3457fa6003297fd45b665&csf=1&web=1&e=nLixfh"
    # Download the file to memory
    response = requests.get(url)
    content = response.content

    print(content)


