class ChromaEngine:
    @staticmethod
    def get_css(mood_score):
        """感情値(0-1)を物理的な光の波長に同期"""
        # 0=静寂(Blue), 1=情熱(Pink/Red)
        chroma = 0.15 # 彩度
        lightness = 0.4 # 輝度
        hue = 200 + (mood_score * 150)
        
        return f"""
        <style>
        .stApp {{
            background: radial-gradient(circle at bottom left, oklch({lightness} {chroma} {hue}), #000);
            transition: background 3s ease-in-out;
        }}
        </style>
        """
