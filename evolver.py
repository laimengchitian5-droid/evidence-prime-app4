class Evolver:
    @staticmethod
    def calculate_shift(current_scores, new_sentiment):
        """感情値に基づいて性格スコアを微修正（統計的更新）"""
        # ベイズ更新の簡易版：新しい情報で既存のスコアを補正
        updated = {k: v * 0.95 + (new_sentiment * 0.05) for k, v in current_scores.items()}
        return updated
