import streamlit as st
import time

class Vault:
    @staticmethod
    def unlock():
        """合言葉による認証と、心臓（APIキー）の同期"""
        if not st.session_state.get("authenticated", False):
            st.title("🌌 Aethelgard OS")
            st.info("開拓者の認証が必要です。")
            
            # 中央配置のためのカラム構成
            _, col, _ = st.columns([1, 2, 1])
            with col:
                password = st.text_input("🔑 開拓者の合言葉", type="password")
                if password:
                    if password == st.secrets["MY_SECRET_WORD"]:
                        st.session_state.authenticated = True
                        st.session_state.api_key = st.secrets["GROQ_API_KEY"]
                        st.success("認証成功。神経系を同期中...")
                        time.sleep(1.5)
                        st.rerun()
                    else:
                        st.error("合言葉が一致しません。")
            st.stop() # 認証されるまでここで停止
