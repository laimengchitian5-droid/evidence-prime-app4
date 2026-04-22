import streamlit as st

class Interface:
    @staticmethod
    def build_dashboard(points, stats):
        # 1. 統計メトリクス（三層構造の可視化）
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("認知一貫性", f"{stats['logic']}%")
        with col2: st.metric("共感共鳴度", f"{stats['empathy']}%")
        with col3: st.metric("未来不確実性", f"{stats['entropy']}%")

        # 2. メインビュー（3D銀河）
        st.subheader("🌌 思考の幾何学（Aethelgard Core）")
        # Visualizer.render_3d_nexus をここで呼び出す
