import streamlit as st
from constellation import Visualizer

class Interface:
    @staticmethod
    def build_dashboard(points, stats):
        st.title("🌌 Aethelgard Dashboard")
        c1, c2, c3 = st.columns(3)
        c1.metric("Logic", f"{stats['logic']}%")
        c2.metric("Empathy", f"{stats['empathy']}%")
        c3.metric("Entropy", f"{stats['entropy']}%")
        
        st.markdown("---")
        # 8. Constellation の呼び出し
        fig = Visualizer.render_3d_nexus(points)
        st.plotly_chart(fig, use_container_width=True)
