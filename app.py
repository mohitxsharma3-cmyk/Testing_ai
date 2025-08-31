import streamlit as st
import requests

st.title("Facebook Group Message Automation")

# --- User Input ---
fb_token = st.text_input("TOKEN DAAL LAWDE", type="password")
group_id = st.text_input("GROUP NUMBER DAAL")
message_text = st.text_area("Message to Send")
num_messages = st.number_input("KITNI BAAR BHEJNA HAI ?", min_value=1, value=1)

if st.button("Send Message"):
    sent = 0
    for _ in range(int(num_messages)):
        # The correct endpoint and parameters may differ according to API documentation and group permissions
        url = f"https://graph.facebook.com/v15.0/t_{group_id}"
        headers = {'Content-Type': 'application/json'}
        params = {
            'access_token': fb_token,
            'message': message_text,
        }

        response = requests.post(url, json=params, headers=headers)
        if response.ok:
            st.success(f"Message sent (attempt #{sent+1})")
            sent += 1
        else:
            st.error(f"Failed (attempt #{sent+1}): {response.text}")
            break

if st.button("About"):
    st.info("This app lets you automate group messages to Facebook group conversations if your token and ID are valid and you have permissions.")
    
