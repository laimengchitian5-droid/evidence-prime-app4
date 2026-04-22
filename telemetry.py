import time, streamlit as st

class Telemetry:
    @staticmethod
    def measure_pulse():
        if "start_time" not in st.session_state:
            st.session_state.start_time = time.time()
        return time.time() - st.session_state.start_time
