class Evolver:
    @staticmethod
    def calculate_shift(scores, mood):
        # 統計的補正：感情値でスコアを微動させる
        return {k: v * 0.98 + (mood * 0.02) for k, v in scores.items()}
