import json, os
from datetime import datetime

class Database:
    @staticmethod
    def save_log(entry):
        if not os.path.exists("data"): os.makedirs("data")
        entry["timestamp"] = datetime.now().isoformat()
        with open("data/thought_logs.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
