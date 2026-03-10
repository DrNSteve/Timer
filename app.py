import streamlit as st
import time

st.set_page_config(page_title="ADHD Command Center", page_icon="🧠")

st.title("Focus Prosthetic 🧠")
st.write("Commit to the Good Enough.")

# Initialize session states
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'time_left' not in st.session_state:
    st.session_state.time_left = 25 * 60  # 25 minutes
if 'extension_mode' not in st.session_state:
    st.session_state.extension_mode = False

# Function to format time
def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{mins:02d}:{secs:02d}"

# UI: Timer Display
timer_placeholder = st.empty()
timer_placeholder.markdown(f"<h1 style='text-align: center;'>{format_time(st.session_state.time_left)}</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Start 25-Min Pomodoro"):
        st.session_state.timer_running = True
        st.session_state.extension_mode = False
        st.session_state.time_left = 25 * 60

with col2:
    if st.button("Stop / Reset"):
        st.session_state.timer_running = False
        st.session_state.time_left = 25 * 60
        st.session_state.extension_mode = False
        st.rerun()

with col3:
    if st.button("I'm on a roll (Extend)"):
        st.session_state.timer_running = False # Pause timer
        st.session_state.extension_mode = True

# The "Conscious Extension" Gatekeeper
if st.session_state.extension_mode:
    st.warning("⚠️ Hyperfocus Check: You are extending your time.")
    justification = st.text_input("What is your specific objective for the next 15 minutes?")
    
    if st.button("Commit to Extension"):
        if justification:
            st.success("Extension granted. Focus up!")
            st.session_state.time_left = 15 * 60
            st.session_state.extension_mode = False
            st.session_state.timer_running = True
        else:
            st.error("You must type a justification to unlock the extension.")

# Timer Logic
if st.session_state.timer_running:
    while st.session_state.time_left > 0 and st.session_state.timer_running:
        time.sleep(1)
        st.session_state.time_left -= 1
        timer_placeholder.markdown(f"<h1 style='text-align: center;'>{format_time(st.session_state.time_left)}</h1>", unsafe_allow_html=True)
    
    if st.session_state.time_left == 0:
        st.session_state.timer_running = False
        st.balloons()
        st.success("Time's up! Stand up, stretch, and evaluate: Is it 'Good Enough'?")
