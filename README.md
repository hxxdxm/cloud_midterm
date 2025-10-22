# Height/Weight Tracker — 실기 문제 틀 (1분반)

이 프로젝트는 문제용 틀입니다. 그대로는 실행되지 않습니다.
아래 구현내용을 확인해 수정를 완료하여 동작시키세요.

## 구현 내용 (필수)
1) `api/app.py`를 완성하여 다음 API를 구현
   - GET  /api/records   : JSON 파일의 누적 데이터 반환
   - POST /api/records   : {height, weight} 저장(유효성 검사 포함)
   - GET  /api/download  : JSON 파일 다운로드
2) `api/Dockerfile` 에서 EXPOSE, CMD 를 알맞게 작성해 Flask 앱 실행
3) `nginx/nginx.conf` 의 `/api/` 프록시 설정을 올바르게 수정 (proxy_pass 주의)
4) `docker-compose.yml` 로 `api`와 `web`을 올바르게 연결하고 실행

## 점검 및 평가 시
- 브라우저: http://localhost:8080
- `/api/records` 가 `[]` - 데이터 를 반환해야 함
- 폼 제출 → 누적 리스트 표시
- JSON 다운로드 버튼 → records.json 저장

학번 : 234017
이름 : 김하민