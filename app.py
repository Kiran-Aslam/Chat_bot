import streamlit as st
import os
from groq import Groq
from datetime import datetime
import time

st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    header {visibility: hidden;}
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a0000 25%, #2d0000 50%, #1a0000 75%, #000000 100%);
        background-attachment: fixed;
    }
    
    .main .block-container {
        padding-bottom: 200px !important;
        max-width: 1200px !important;
    }
    
    .chat-scroll-area {
        max-height: calc(100vh - 350px);
        overflow-y: auto;
        padding: 20px 0;
        margin-bottom: 20px;
    }
    
    .fixed-input-container {
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        background: linear-gradient(135deg, #000000 0%, #1a0000 50%, #000000 100%) !important;
        border-top: 2px solid #e50914 !important;
        padding: 25px !important;
        z-index: 1000 !important;
        box-shadow: 
            0 -8px 32px rgba(229, 9, 20, 0.4),
            0 0 0 1px rgba(229, 9, 20, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(20px) !important;
    }
    
    .modern-input-container {
        max-width: 1000px;
        margin: 0 auto;
        position: relative;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .stTextArea textarea {
        background: linear-gradient(135deg, #000000 0%, #1a0000 50%, #000000 100%) !important;
        border: 2px solid rgba(229, 9, 20, 0.4) !important;
        border-radius: 25px !important;
        color: #ffffff !important;
        font-size: 16px !important;
        padding: 20px 60px 20px 25px !important;
        box-shadow: 
            0 0 20px rgba(229, 9, 20, 0.3),
            inset 0 2px 10px rgba(0, 0, 0, 0.5),
            0 0 0 1px rgba(229, 9, 20, 0.1) !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(15px) !important;
        resize: none !important;
        font-family: 'Poppins', sans-serif !important;
        min-height: 68px !important;
        max-height: 120px !important;
        outline: none !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #e50914 !important;
        box-shadow: 
            0 0 0 3px rgba(229, 9, 20, 0.3),
            0 0 40px rgba(229, 9, 20, 0.6),
            inset 0 2px 10px rgba(0, 0, 0, 0.7),
            0 0 0 1px #e50914 !important;
        outline: none !important;
        transform: translateY(-2px) !important;
    }
    
    .stTextArea textarea::placeholder {
        color: rgba(229, 9, 20, 0.6) !important;
        font-weight: 400 !important;
    }
    
    .send-icon-container {
        position: absolute;
        right: 15px;
        top: 50%;
        transform: translateY(-50%);
        z-index: 10;
        pointer-events: none;
    }
    
    .send-icon {
        width: 24px;
        height: 24px;
        color: #e50914;
        cursor: pointer;
        pointer-events: all;
        transition: all 0.3s ease;
        filter: drop-shadow(0 0 8px rgba(229, 9, 20, 0.6));
    }
    
    .send-icon:hover {
        color: #ff1f2f;
        transform: scale(1.1);
        filter: drop-shadow(0 0 12px rgba(229, 9, 20, 0.8));
    }
    
    .stButton > button, .stFormSubmitButton > button {
        background: linear-gradient(135deg, #e50914 0%, #b8070f 50%, #8a050b 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 18px 35px !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
        box-shadow: 
            0 6px 25px rgba(229, 9, 20, 0.5),
            0 0 0 1px rgba(229, 9, 20, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        position: relative !important;
        overflow: hidden !important;
        height: 60px !important;
        min-width: 120px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-family: 'Poppins', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    .stButton > button::before, .stFormSubmitButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.6s ease;
    }
    
    .stButton > button:hover, .stFormSubmitButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 
            0 10px 35px rgba(229, 9, 20, 0.7),
            0 0 0 1px rgba(229, 9, 20, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
        background: linear-gradient(135deg, #ff1f2f 0%, #e50914 50%, #b8070f 100%) !important;
    }
    
    .stButton > button:hover::before, .stFormSubmitButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:active, .stFormSubmitButton > button:active {
        transform: translateY(-1px) scale(0.98) !important;
    }
    
    .stTextArea > div {
        border-radius: 25px !important;
        position: relative !important;
    }
    
    .stForm {
        border: none !important;
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at 20% 20%, rgba(229, 9, 20, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(229, 9, 20, 0.08) 0%, transparent 50%),
                    radial-gradient(circle at 40% 60%, rgba(229, 9, 20, 0.05) 0%, transparent 50%);
        z-index: -1;
        animation: particles 25s ease-in-out infinite;
    }
    
    @keyframes particles {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 1; }
    }
    
    .main-header {
        background: linear-gradient(135deg, #000000 0%, #1a0000 50%, #000000 100%);
        color: #e50914;
        padding: 40px;
        text-align: center;
        border-radius: 25px;
        margin-bottom: 30px;
        box-shadow: 
            0 10px 40px rgba(229, 9, 20, 0.4),
            0 0 0 1px rgba(229, 9, 20, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(229, 9, 20, 0.3);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(15px);
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(229, 9, 20, 0.15), transparent);
        animation: shine 4s ease-in-out infinite;
    }
    
    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .main-header h1 {
        font-size: 3.5em;
        margin-bottom: 15px;
        font-weight: 700;
        text-shadow: 
            0 0 25px rgba(229, 9, 20, 0.9),
            0 0 50px rgba(229, 9, 20, 0.7),
            0 0 75px rgba(229, 9, 20, 0.5);
        position: relative;
        z-index: 1;
    }
    
    .main-header p {
        font-size: 1.3em;
        opacity: 0.9;
        margin: 0;
        font-weight: 300;
        color: #ff4757;
        position: relative;
        z-index: 1;
    }
    
    .chat-container {
        background: rgba(0, 0, 0, 0.95);
        border-radius: 25px;
        padding: 25px;
        margin-bottom: 20px;
        border: 2px solid rgba(229, 9, 20, 0.3);
        box-shadow: 
            0 10px 40px rgba(0, 0, 0, 0.6),
            0 0 0 1px rgba(229, 9, 20, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        max-height: 500px;
        overflow-y: auto;
        backdrop-filter: blur(20px);
        position: relative;
        min-height: 200px;
    }
    
    .user-message {
        background: linear-gradient(135deg, #e50914 0%, #b8070f 50%, #8a050b 100%);
        color: #ffffff;
        padding: 18px 25px;
        border-radius: 25px;
        border-bottom-right-radius: 8px;
        margin: 15px 0;
        margin-left: 25%;
        margin-right: 5%;
        font-weight: 500;
        box-shadow: 
            0 6px 25px rgba(229, 9, 20, 0.5),
            0 0 0 1px rgba(229, 9, 20, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        position: relative;
        transform: translateX(0);
        transition: all 0.3s ease;
        word-wrap: break-word;
        line-height: 1.6;
    }
    
    .user-message:hover {
        transform: translateX(-5px);
        box-shadow: 
            0 10px 35px rgba(229, 9, 20, 0.7),
            0 0 0 1px rgba(229, 9, 20, 0.5);
    }
    
    .bot-message {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d0000 50%, #1a1a1a 100%);
        color: #ffffff;
        padding: 18px 25px;
        border-radius: 25px;
        border-bottom-left-radius: 8px;
        margin: 15px 0;
        margin-right: 25%;
        margin-left: 5%;
        border: 2px solid rgba(229, 9, 20, 0.3);
        box-shadow: 
            0 6px 25px rgba(0, 0, 0, 0.4),
            0 0 0 1px rgba(229, 9, 20, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        line-height: 1.7;
        position: relative;
        transform: translateX(0);
        transition: all 0.3s ease;
        word-wrap: break-word;
    }
    
    .bot-message:hover {
        transform: translateX(5px);
        box-shadow: 
            0 10px 35px rgba(229, 9, 20, 0.3),
            0 0 0 1px rgba(229, 9, 20, 0.4);
        border-color: rgba(229, 9, 20, 0.5);
    }
    
    .message-time {
        font-size: 0.85em;
        color: rgba(255, 255, 255, 0.7);
        margin-top: 10px;
        text-align: right;
        font-weight: 300;
    }
    
    .bot-message .message-time {
        text-align: left;
        color: rgba(229, 9, 20, 0.8);
    }
    
    .stSidebar, 
    .css-1d391kg, 
    section[data-testid="stSidebar"],
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #000000 0%, #1a0000 50%, #000000 100%) !important;
        border-right: 3px solid rgba(229, 9, 20, 0.4) !important;
        color: #ffffff !important;
    }
    
    .stSidebar > div, 
    .css-1d391kg > div,
    section[data-testid="stSidebar"] > div,
    [data-testid="stSidebar"] > div {
        background: linear-gradient(135deg, #000000 0%, #1a0000 50%, #000000 100%) !important;
        color: #ffffff !important;
        padding: 25px !important;
    }
    
    .stSidebar h1, .stSidebar h2, .stSidebar h3 {
        color: #e50914 !important;
        text-shadow: 0 0 15px rgba(229, 9, 20, 0.6) !important;
    }
    
    .stSidebar .stSelectbox > div > div {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d0000 50%, #1a1a1a 100%) !important;
        border: 2px solid rgba(229, 9, 20, 0.4) !important;
        color: #ffffff !important;
        border-radius: 15px !important;
    }
    
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #e50914 0%, #b8070f 50%, #8a050b 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 15px 25px !important;
        font-weight: 600 !important;
        box-shadow: 
            0 6px 20px rgba(229, 9, 20, 0.5),
            0 0 0 1px rgba(229, 9, 20, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin: 8px 0 !important;
    }
    
    .stSidebar .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 
            0 8px 25px rgba(229, 9, 20, 0.7),
            0 0 0 1px rgba(229, 9, 20, 0.5) !important;
    }
    
    .error-message {
        background: linear-gradient(135deg, #e50914 0%, #b8070f 100%);
        color: white;
        padding: 20px 30px;
        border-radius: 20px;
        margin: 20px 0;
        font-weight: 500;
        box-shadow: 
            0 6px 25px rgba(229, 9, 20, 0.5),
            0 0 0 1px rgba(229, 9, 20, 0.4);
        border: 2px solid rgba(229, 9, 20, 0.6);
        animation: shake 0.6s ease-in-out;
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-8px); }
        75% { transform: translateX(8px); }
    }
    
    ::-webkit-scrollbar {
        width: 14px;
    }
    
    ::-webkit-scrollbar-track {
        background: #000000;
        border-radius: 15px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #e50914 0%, #b8070f 100%);
        border-radius: 15px;
        border: 2px solid #000000;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #ff1f2f 0%, #e50914 100%);
        box-shadow: 0 0 15px rgba(229, 9, 20, 0.6);
    }
    
    .message-animation {
        animation: messageSlide 0.7s ease-out;
    }
    
    @keyframes messageSlide {
        from {
            opacity: 0;
            transform: translateY(40px) scale(0.9);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }
    
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2.5em;
        }
        
        .user-message, .bot-message {
            margin-left: 5% !important;
            margin-right: 5% !important;
        }
        
        .chat-container {
            padding: 20px;
        }
        
        .fixed-input-container {
            padding: 20px !important;
        }
        
        .modern-input-container {
            flex-direction: column;
            gap: 15px;
        }
        
        .stButton > button, .stFormSubmitButton > button {
            width: 100% !important;
            min-width: auto !important;
        }
    }
    
    .glow-text {
        text-shadow: 
            0 0 8px rgba(229, 9, 20, 0.9),
            0 0 16px rgba(229, 9, 20, 0.7),
            0 0 24px rgba(229, 9, 20, 0.5),
            0 0 32px rgba(229, 9, 20, 0.3);
    }
    
    .pulse {
        animation: pulse 2.5s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            box-shadow: 0 0 25px rgba(229, 9, 20, 0.5);
        }
        50% {
            box-shadow: 0 0 40px rgba(229, 9, 20, 0.9);
        }
    }
</style>

<svg style="display: none;">
    <defs>
        <symbol id="paper-plane" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="m3 3 3 9-3 9 19-9Z"/>
            <path d="m6 12 13 0"/>
        </symbol>
    </defs>
</svg>

""", unsafe_allow_html=True)

@st.cache_resource
def init_groq_client():
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        return Groq(api_key=api_key)
    except KeyError:
        st.error("Please add your GROQ_API_KEY to Streamlit secrets")
        st.stop()
    except Exception as e:
        st.error(f"Error initializing Groq client: {str(e)}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_groq_response(messages, model="llama3-8b-8192", temperature=0.7, max_tokens=1000):
    try:
        client = init_groq_client()
        
        api_messages = [
            {"role": "system", "content": "You are a helpful AI assistant. Provide clear, concise, and helpful responses."}
        ]
        
        for msg in messages[-10:]:
            api_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        chat_completion = client.chat.completions.create(
            messages=api_messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            stream=False,
        )
        
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error getting response: {str(e)}")
        return None

def main():
    st.markdown("""
    <div class="main-header pulse">
        <h1 class="glow-text">🤖 AI Chat Assistant</h1>
        <p>Powered by Groq API - Experience the future of AI conversation</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown('<h2 style="color: #e50914; text-align: center; margin-bottom: 30px;">⚙️ Settings</h2>', unsafe_allow_html=True)
        
        model_options = [
            "llama3-8b-8192",
            "llama3-70b-8192",
            "mixtral-8x7b-32768",
            "gemma-7b-it"
        ]
        
        selected_model = st.selectbox(
            "Choose AI Model:",
            model_options,
            index=0,
            help="Select the AI model to use for responses"
        )
        
        temperature = st.slider(
            "Response Creativity:",
            min_value=0.1,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Higher values make responses more creative"
        )
        
        max_tokens = st.slider(
            "Max Response Length:",
            min_value=100,
            max_value=2000,
            value=1000,
            step=100,
            help="Maximum length of AI responses"
        )
        
        st.divider()
        
        if st.button(" Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        if st.button(" Export Chat", use_container_width=True):
            chat_export = "\n".join([
                f"[{msg['timestamp']}] {msg['role'].upper()}: {msg['content']}"
                for msg in st.session_state.messages
            ])
            st.download_button(
                label="Download Chat History",
                data=chat_export,
                file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        
        st.divider()
        
        st.markdown('<h3 style="color: #e50914; text-align: center;"> Chat Stats</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Messages", len(st.session_state.messages))
            st.metric("Bot Messages", len([m for m in st.session_state.messages if m["role"] == "assistant"]))
        with col2:
            st.metric("User Messages", len([m for m in st.session_state.messages if m["role"] == "user"]))
            if st.session_state.messages:
                st.metric("Last Activity", st.session_state.messages[-1]["timestamp"])
    
    chat_container = st.container()
    with chat_container:
        st.markdown('<div class="chat-scroll-area">', unsafe_allow_html=True)
        
        if st.session_state.messages and len(st.session_state.messages) > 0:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="user-message message-animation">
                        <div style="font-size: 16px; line-height: 1.6;">{message["content"]}</div>
                        <div class="message-time">👤 {message["timestamp"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="bot-message message-animation">
                        <div style="font-size: 16px; line-height: 1.7;">{message["content"]}</div>
                        <div class="message-time">🤖 {message["timestamp"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="fixed-input-container">
        <div class="modern-input-container">
    """, unsafe_allow_html=True)
    
    with st.form(key="message_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_input = st.text_area(
                "Type your message here...",
                height=68,
                placeholder="Ask me anything! Press Ctrl+Enter to send... ✨",
                label_visibility="collapsed",
                key="message_input"
            )
            
        with col2:
            send_button = st.form_submit_button(" Send", use_container_width=True, type="primary")
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if send_button and user_input.strip():
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now().strftime("%H:%M")
        })
        
        st.session_state.waiting_for_response = True
        
        st.rerun()
    
    elif send_button and not user_input.strip():
        st.markdown(
            '<div class="error-message">⚠️ Please enter a message before sending!</div>',
            unsafe_allow_html=True
        )
    
    if hasattr(st.session_state, 'waiting_for_response') and st.session_state.waiting_for_response:
        st.markdown("""
        <div class="bot-message" style="opacity: 0.8;">
            <div style="font-size: 16px; line-height: 1.7;">🤖 Typing...</div>
        </div>
        """, unsafe_allow_html=True)
        
        response = get_groq_response(
            st.session_state.messages, 
            model=selected_model, 
            temperature=temperature, 
            max_tokens=max_tokens
        )
        
        if response:
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
        else:
            st.session_state.messages.append({
                "role": "assistant", 
                "content": "❌ Sorry, I couldn't process your request. Please try again.",
                "timestamp": datetime.now().strftime("%H:%M")
            })
        
        st.session_state.waiting_for_response = False
        
        st.rerun()
    
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; color: #666; font-size: 0.9em; margin-top: 20px;'>
        <p>Made with ❤️ using <span style='color: #e50914;'>Streamlit</span> and <span style='color: #e50914;'>Groq API</span></p>
        <p style='font-size: 0.8em; opacity: 0.7;'>Current time: {datetime.now().strftime("%H:%M:%S")}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

