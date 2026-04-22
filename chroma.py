class ChromaEngine:
    @staticmethod
    def get_css(mood):
        hue = 200 + (mood * 150) # 200(青)〜350(紫/赤)
        return f"""
        <style>
        .stApp {{
            background: radial-gradient(circle at top right, oklch(0.4 0.15 {hue}), #000);
            transition: background 3s ease;
        }}
        </style>
        """
