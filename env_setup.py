import streamlit as st
import os

class EnvChecker:
    @staticmethod
    def validate():
        """システムが正常に動作するための物理的土台をチェック"""
        # 必要なフォルダの自動生成
        folders = ["data", "logs", ".streamlit"]
        for f in folders:
            if not os.path.exists(f):
                os.makedirs(f)
        
        # Secretsの存在確認
        if "MY_SECRET_WORD" not in st.secrets or "GROQ_API_KEY" not in st.secrets:
            st.error("🚨 Secrets Configuration Missing: .streamlit/secrets.toml を確認してください")
            st.stop()
