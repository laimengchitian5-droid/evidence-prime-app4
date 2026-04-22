import streamlit as st
import time

# --- プロ思考：全モジュールの同期インポート ---
from env_setup import EnvChecker
from vault import Vault
from telemetry import Telemetry
from synapse import Synapse
from database import Database
from evolver import Evolver
from constellation import Visualizer
from chroma import ChromaEngine
from interface import Interface

# 1. 土台の健全性チェック（物理層）
EnvChecker.validate()

# 2. ページ設定（視覚層の土台）
st.set_page_config(
    page_title="Aethelgard OS", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 3. 心臓の起動（認証層）
Vault.unlock()

# 4. システムステートの初期化（記憶層）
if "history" not in st.session_state: st.session_state.history = []
if "nexus_points" not in st.session_state: st.session_state.nexus_points = []
if "mood_score" not in st.session_state: st.session_state.mood_score = 0.5
if "personality" not in st.session_state: 
    st.session_state.personality = {"Openness": 0.5, "Stability": 0.5, "Logic": 0.5}

# 脳（AIエンジン）の同期
if "brain" not in st.session_state:
    st.session_state.brain = Synapse(st.session_state.api_key)

# --- メインループ ---

def main():
    # A. テレメトリ計測開始（心拍）
    pulse = Telemetry.measure_pulse()
    
    # B. 感情色彩の同期（皮膚）
    st.markdown(ChromaEngine.get_css(st.session_state.mood_score), unsafe_allow_html=True)

    # C. インターフェース構築（接点）
    # 統計データの仮生成（本来はEvolverから算出）
    stats = {
        "logic": int(st.session_state.personality["Logic"] * 100),
        "empathy": int(st.session_state.mood_score * 100),
        "entropy": int(pulse * 10) % 100
    }
    
    # サイドバーとダッシュボードの描画
    Interface.build_dashboard(st.session_state.nexus_points, stats)

    # D. 思考の入力（神経伝達）
    user_input = st.chat_input("思考の断片を入力してください...")

    if user_input:
        # 1. 感情分析と色彩の更新
        # (Synapse内で処理するが、ここではデモ用にスコアを変動させる)
        
        # 2. AIの思考（脳）
        with st.chat_message("assistant"):
            response_stream = st.session_state.brain.generate_response(
                user_input, st.session_state.history
            )
            full_response = st.write_stream(response_stream)
        
        # 3. 記憶の永続化（土台）
        log_entry = {
            "user": user_input,
            "assistant": full_response,
            "mood": st.session_state.mood_score
        }
        Database.save_log(log_entry)

        # 4. 星座の更新（視覚）
        st.session_state.nexus_points.append({
            "x": st.session_state.mood_score,
            "y": len(st.session_state.history),
            "z": time.time() % 100,
            "sentiment": st.session_state.mood_score,
            "label": user_input[:10]
        })

        # 5. 性格の進化（脳）
        st.session_state.personality = Evolver.calculate_shift(
            st.session_state.personality, st.session_state.mood_score
        )

        # 履歴への追加
        st.session_state.history.append({"role": "user", "content": user_input})
        st.session_state.history.append({"role": "assistant", "content": full_response})
        
        # システム再同期
        st.rerun()

if __name__ == "__main__":
    main()
