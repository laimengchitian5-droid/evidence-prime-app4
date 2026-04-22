import json
import os
from datetime import datetime

class Database:
    @staticmethod
    def save_log(entry):
        """会話と心理スコアをJSONL形式で永続化"""
        path = "data/thought_logs.jsonl"
        entry["timestamp"] = datetime.now().isoformat()
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    @staticmethod
    def load_recent_history(limit=10):
        """過去の文脈をロード（進化計算用）"""
        # 実装略（ファイルの末尾から読み込むプロの処理）
        return []
