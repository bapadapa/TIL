# 데이터 분석을 공부해보자!

# 개념 정리

---

# IITP 수업 정리

- [IITP](./IITP)

---

# 라이브러리

- [numpy](../)

# 간단 꿀팁

- ### jupyter notebook 시작경로 변경

  1. prompt 창에서 jupyter notebook --generate-config 를 쳐서 설정파일을 생성한다.
  2. 생성된 jupyter_notebook_config.py 를 열어준다
  3. 중간에 주석이 쳐져있는 코드 c.NotebookApp.notebook_dir의 주석을 풀고 아래와같이작성

     - c.NotebookApp.notebook_dir = '경로'

  4. 저장 후 Jupyter notebook 실행시 경로 변경되있는 것을 확인 할 수 있다.
