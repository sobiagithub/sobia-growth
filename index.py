import streamlit as st

st.set_page_config(page_title="Growth mindset project", project_icon="🔯")
st.title("Growth Mindset Challenge :Web App with Streamlit")

st.header("🌠Welcome to Your Journey!✨")
st.write("Embrace challenges,learn from mistakes,and unlock your full potential. This AI-POWERED app helps you build agrowth mindset with reflecction,challenges and achievements!⭐")

#quote selection

st.header("💡Today's Growth Mindset Quote")
st.write("'Success is not final,failure is not fatal:it is the courage to continue that counts.' _Winston Churchill")

st.header("🌷 Whats Your Challenge Now?")
user_input =st.text_input("✌ Describe a challenge you are facing:")

#condition
if user_input: st.success(f" you're facing:{user_input}. Keep pushing forward towords your goal!")

else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on your Learning")
reflection = st.text_area("write your reflections here:")

if reflection:
    st.success(f"֎Great Insight! Your reflection: {reflection}")
else: 
    st.info("Reflecting on past experience help you grow! Share your difficulties")

    #acheivment
    st.header("🌷 Celebrate Your Win!")
    acheivment =st.text_input("Share something you've recently accomplished:")

    if acheivment:
        st.success(f"🌟Amazing! You achieved: {acheivment}")
    else:st.info("Big or small ,every acheivment counts! share one now😍")

    #footer
    st.write("_ _ _")
    st.write("🌠 Keep believing in yourself ,Growth is a journey,not a destination!")
    st.write("⛔ Created by Sobia naz")
