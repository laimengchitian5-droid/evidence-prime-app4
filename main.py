import streamlit as st
from env_setup import EnvChecker
from vault import Vault
from synapse import Synapse
# （今後、constellation.py や chroma.py をインポート）

# 1. 土台の検証
EnvChecker.validate()

# 2. 心臓の起動
Vault.unlock()

# 3. 脳の同期
if "brain" not in st.session_state:
    st.session_state.brain = Synapse(st.session_state.api_key)
if "history" not in st.session_state:
    st.session_state.history = []

# --- UI構築 ---
st.set_page_config(page_title="Aethelgard OS", layout="wide")
st.sidebar.title("🧬 System Telemetry")

# メイン処理
user_input = st.chat_input("思考の断片を入力してください...")

if user_input:
    with st.chat_message("assistant"):
        response_stream = st.session_state.brain.generate_response(
            user_input, st.session_state.history
        )
        full_response = st.write_stream(response_stream)
        
    st.session_state.history.append({"role": "user", "content": user_input})
    st.session_state.history.append({"role": "assistant", "content": full_response})
