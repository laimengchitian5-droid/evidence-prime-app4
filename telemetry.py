import time
import streamlit as st

class Telemetry:
    @staticmethod
    def measure_pulse():
        """応答速度とシステム負荷を計測"""
        if "start_time" not in st.session_state:
            st.session_state.start_time = time.time()
        
        duration = time.time() - st.session_state.start_time
        # 負荷が高い（1秒以上）場合はUIを軽量化するフラグ
        st.session_state.is_heavy = duration > 1.0
        return duration
