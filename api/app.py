#  Flask API를 완성하세요.
# 요구사항:
# - 데이터 파일 경로: /app/data/data.json  (초기 내용: [])
# - GET  /api/records   : 저장된 데이터를 JSON으로 반환
# - POST /api/records   : {height, weight}를 받아 유효성 검사 후 누적 저장
# - GET  /api/download  : data.json 파일 다운로드


from flask import Flask  
from pathlib import Path
import json, os

app = Flask(__name__)

DATA_PATH = Path("/app/data/data.json")
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
if not DATA_PATH.exists():
    DATA_PATH.write_text("[]", encoding="utf-8")

@app.get("/healthz")
def healthz():
    return "ok", 200

# 저장된 데이터를 JSON으로 반환
@app.get("/api/records")
def get_records():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# {height, weight} 저장 (유효성 검사 포함)
@app.post("/api/records")
def add_record():
    try:
        new_data = request.get_json()

        if not new_data:
            return jsonify({"error": "JSON 형식의 데이터가 필요합니다."}), 400

        height = new_data.get("height")
        weight = new_data.get("weight")

        # 유효성 검사
        if not isinstance(height, (int, float)) or not isinstance(weight, (int, float)):
            return jsonify({"error": "height와 weight는 숫자여야 합니다."}), 400
        if height <= 0 or weight <= 0:
            return jsonify({"error": "height와 weight는 0보다 커야 합니다."}), 400

        # 기존 데이터 불러오기
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 새로운 데이터 추가
        data.append({"height": height, "weight": weight})

        # 파일 저장
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return jsonify({"message": "저장 성공", "data": data}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.get("/api/download")
def download_json():
    try:
        return send_file(DATA_PATH, as_attachment=True, download_name="records.json")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # 적절한 포트(예: 5000)로 0.0.0.0 에서 실행
    app.run(host="0.0.0.0", port=5000)