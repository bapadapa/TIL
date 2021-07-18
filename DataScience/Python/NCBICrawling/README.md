# NCBI 크롤링

## URL을 이용하여 검색 후 MetaData 다운로드

1. 사용 라이브러리

   1. selenium
   1. time
   1. os

1. 간단 설명
   1. URL로 직접 검색이 가능 한 것을 파악 후 URL을 이용하여 검색
   1. 버튼 ID
      - `t-rit-all`
   1. WebDriverWait를 이용하여 로딩 대기 및 MetaData가 없는 것을 확인
   1. `os.rename`을 이용하여 다운로드 받은 파일명 변경
