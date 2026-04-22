from groq import Groq
import streamlit as st

class Synapse:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def generate_response(self, user_input, history):
        # 心理学の全知識をシステム命令に注入
        system_instruction = """
        あなたは『Aethelgard OS』の統合知能です。
        以下の三層構造に基づき思考せよ：
        1.【理論】認知心理学に基づき、ユーザーの無意識のバイアスを特定せよ。
        2.【実践】リフレーミングを行い、対人スキルを向上させる助言をせよ。
        3.【創造】統計的予測に基づき、この会話が導く『未来の可能性』を提示せよ。
        """
        
        messages = [
            {"role": "system", "content": system_instruction},
            *history,
            {"role": "user", "content": user_input}
        ]
        
        return self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            stream=True
        )
