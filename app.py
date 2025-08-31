import streamlit as st
import requests

st.title("Facebook Group Message Automation with Cookies")

# --- User Input ---
cookies_raw = st.text_area("Paste your Facebook cookies string here (format: key1=value1; key2=value2; ...)")
group_id = st.text_input("Group Conversation ID")
message_text = st.text_area("Message to Send")
num_messages = st.number_input("Number of Times to Send", min_value=1, value=1)

def parse_cookies(raw):
    cookies_dict = {}
    for cookie in raw.split(';'):
        parts = cookie.strip().split('=', 1)
        if len(parts) == 2:
            cookies_dict[parts[0]] = parts[1]
    return cookies_dict


if st.button("Send Message"):
    if not cookies_raw.strip():
        st.error("Please paste your Facebook cookies first!")
    else:
        cookies = parse_cookies(cookies_raw)
        sent = 0
        for _ in range(int(num_messages)):
            # WARNING: Facebook endpoints/descriptions below are illustrative.
            url = f"https://www.facebook.com/groups/{group_id}/"
            headers = {'User-Agent': 'Mozilla/5.0'}  # Basic UA
            try:
                # This will NOT post messages unless the endpoint, payload, and cookies are correct.
                # Facebook may block or redirect such scripted requests.
                response = requests.post(url, data={'message': message_text}, headers=headers, cookies=cookies)
                if response.ok:
                    st.success(f"Message sent (attempt #{sent+1})")
                    sent += 1
                else:
                    st.error(f"Failed (attempt #{sent+1}): {response.text}")
                    break
            except Exception as e:
                st.error(f"Error: {e}")
                break
    
