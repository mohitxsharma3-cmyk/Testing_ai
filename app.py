import streamlit as st

# --- Insert your custom CSS and watermark here ---
st.markdown(
    """
    <style>
    ...your CSS...
    </style>
    <div class="watermark">Mohit</div>
    """, unsafe_allow_html=True
)

# --- Add your main app interface below ---
st.title("Facebook Group Message Automation")
st.write("Welcome, Mohit! Use this app to automate your tasks.")

# Example interactive elements
fb_token = st.text_input("Facebook Access Token", type="password")
group_id = st.text_input("Group Conversation ID")
message_text = st.text_area("Message to Send")
if st.button("Send Message"):
    st.success("Message sent!")
    
