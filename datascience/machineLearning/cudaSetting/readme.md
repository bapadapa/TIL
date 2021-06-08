# 쿠다 아나콘다 셋팅

---

## `실패함 다음에 성공기원! 쿠다 지우고 다시 깔아야겠다!`

### 설치리스트

- 아나콘다
- [Tensorflow](Tensorflow)
- [nvidia 제어판](###nvidia제어판)
- cuda
- cuDNN

### 아나콘다

- 가상환경 만들기
  - `conda create -n 만들고자하는환경이름 python=원하는버전 anaconda`

### Tensorflow

- 명령어
  - pip3 install tensorflow-gpu

### nvidia제어판

- [드라이버 설치](https://www.nvidia.co.kr/Download/index.aspx?lang=kr)
  - 위 링크를 들어가서 자신의 그래픽카드에 맞는 드라이버 설치
  - 설치 후 `CMD`를 키고, `nvidia-smi` 명령어를 이용하여 잘 설치 되었는지 확인해준다.

### Cuda

- [Cuda 설치](https://developer.nvidia.com/cuda-toolkit-archive)

  - 자신이 사용하고자 하는 텐서플로우에 맞춰 설치해준다.

- 환경설정 해주기

### cuDNN

- [cuDNN 설치](https://developer.nvidia.com/rdp/cudnn-download)
  - cuda 및 tensorflow와 맞는 버전을 설치
