import streamlit as st
from huggingface_hub import InferenceClient
import time

# 1. Page Configuration
st.set_page_config(page_title="Medical Assistant", page_icon="⚕️")
st.title("🩺👩🏻‍⚕️ Medical Bot Assistant")
st.markdown("---")

# 2. Model Selection (Zephyr is fast and reliable)
REPO_ID = "HuggingFaceH4/zephyr-7b-beta"

# 3. Secure Token Loading
try:
    HF_TOKEN = st.secrets["HF_TOKEN"]
except:
    st.error("Missing HF_TOKEN in Streamlit Secrets!")
    st.stop()

client = InferenceClient(model=REPO_ID, token=HF_TOKEN)

# 4. Medical Logic Instructions
SYSTEM_PROMPT = """You are a professional Medical Triage Assistant. 
Analyze the symptoms provided and provide a possible triage priority (Emergency, Urgent, or Non-Urgent).
Always advise the user to seek professional medical help and provide clear 'Red Flag' warnings."""

# 5. Chat History Setup
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 6. User Input and Logic
if prompt := st.chat_input("🩸 Describe Your Symptoms..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        
        # --- SMART RETRY LOGIC ---
        max_retries = 3
        success = False
        
        for i in range(max_retries):
            try:
                # Start the streaming connection
                stream = client.chat_completion(
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=500,
                    temperature=0.5,
                    stream=True 
                )
                
                # Update the UI word-by-word
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        full_response += chunk.choices[0].delta.content
                        placeholder.markdown(full_response + "▌")
                
                placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                success = True
                break # Success! Exit the loop.

            except Exception as e:
                if i < max_retries - 1:
                    placeholder.warning(f"Server is busy, retrying in 3 seconds... (Attempt {i+1}/{max_retries})")
                    time.sleep(3)
                else:
                    placeholder.error("The medical server is currently full. Please wait 1 minute and try again.")
        
# 7. Safety Disclaimer at the Bottom
st.markdown("---")
st.caption("⚠️ **Disclaimer:** This AI assistant is for informational purposes only. "
           "It is not a substitute for professional medical advice. "
           "If you have a life-threatening emergency, call your local emergency services immediately.")
