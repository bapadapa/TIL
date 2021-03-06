# 통합 구현

- `송수신 모듈` 및 `중계 모듈` 간의 `연계`를 구현하는 것
- 구현방법 및 방식에 따라 구현 방법이 달라 `사용자 요구사항` 및 `구축 환경`에 적합한 방식을 설계해야함

## 구성요소

1. 송신 시스템 및 모듈
   - 시스템 : 송신 모듈 및 모니터링 기능으로 구현
   - 모듈 : `데이터 생성`및 `변환 작업`을함
2. 수신 시스템 및 모듈
   - 시스템 : 수신 모듈 및 모니터링 기능으로 구현
   - 모듈 : `데이터 정제` 및 DB테이블에 적합한 데이터로 `변환 작업`을 함
3. 중계 시스템
   - `내/외부` 혹은 `내부 시스템`간의 연계시 사용되는 아키텍쳐
4. 연계 시스템
   - 송/수신 시스템간 `송/수신` 하는 `데이터`
5. 네트워크
   - 송/수신 및 중계 시스템을 `연결시켜주는 통신망`
   - 송신 -> 네트워크 -> 중계 -> 네트워크 -> 수신

## 요구사항 분석

- 연계 데이터를 `식별` 및 `표준화`하여 연계 데이터를 정의 하는 것
- 절차
  1.  HW/SW 구성, 네트워크 현황 확인
  2.  `테이블/코드 정의서` 등 문서 확인
  3.  `체크리스트` 작성
  4.  관련 `문서 공유` 및 `인터뷰/설문조사` 실시
  5.  요구사항 `정의서 작성`

## 식별 및 표준화 절차

1. 연계 범위 및 항목 정의
   - 연계 정보 상세화
2. 연계 코드 변환 및 매핑
   - 코드로 관리될 항목을 찾아 `코드로 변환`
3. 연계 데이터 식별자와 변경 구분 추가
   - 연계 정보에 `정보 추가`
4. 연계 데이터 표현 방법 정의
   - 대상 범위, 항목, 코드변환 방식, 매핑 방식을 정의 후 `연계 데이터 구성`
5. 연계 정의서 및 명세서 작성
   - 파악된 현황을 문서화함

# 연계 메커니즘

- 송/수신 시스템으로 구성된다.
- 송/수신 현황을 `모니터링` 하는 `중계 시스템`을 설치 할 수 있다.
  - 중계 시스템
    - 송/수신 시스템에 위치한 `네트워크가 다를경우` 설치
    - `보안 품질`이 중요한 경우 설치
- 연계 방식
  1. 직접 연계 방식
     - 중간 매개체 없이 송/수신 연계
     - 종류
       - `DB LINK`, `API/Open API`, `DB Connection`, `JDBC`
  2. 간접 연계 방식
     - 중간 매개체 있이 송/수신 연계
     - 종류
       - `연계 솔루션`, `ESB`, `소켓`, `웹 서비스`...

## 과정

- 각 과정에는 log 기록을함
- 송신 시스템/모듈
  - 연계 데이터 `생성 및 추출`
    - `코드 매핑` 및 `데이터 변환`
      - `인터페이스 테이블` 혹은 `파일 생성`
        - 연계 서버 혹은 송신 어뎁터
          - 전송
        - 연계 서버 혹은 송신 어뎁터
      - `인터페이스 테이블` 혹은 `파일 생성`
    - `코드 매핑` 및 `데이터 변환`
  - 운영 DB에 연계 데이터 반영
- 수신 시스템/모듈

## 구성

1. 연계 데이터 생성 및 추출
   - 응용 시스템에서 데이터 `생성 및 추출`하는 과정
2. 코드 매핑 및 데이터 변환
   - `송신 시스템`에서 사용하는 `코드`를 수신 시스템에서 사용하는 코드로 `매핑 및 변환`하는 과정
3. 인터페이스 테이블 및 파일 생성
   - `인터페이스 테이블` 혹은 `파일형식`으로 생성하는 과정
4. 로그 기록
   - 과정 및 결과를 `로그 테이블` 혹은 `파일`로 저장
5. 연계 서버 혹은 송/수신 어댑터
   - 연계 서버
     - 송/수신 관련 `모든 처리(데이터 변환 등)` 수행
   - 송신 어댑터
     - 전송 형식에 맞도록 `변환` 및 `송신 수행`
   - 수신 업댑터 - 수신 데이터를 `인터페이스 테이블` 혹은 `파일`로 생성
6. 전송
   - 연계 데이터를 네트워크 환경에 맞는 `데이터로 변환 후 전송`
7. 운영 DB 연계 데이터 반영
   - `수신 데이터`를 `변환`하여 `운영 DB에 반영`하는 과정

## 연계 장애 및 오류처리 구현

### 오류 발생 시점

1. 송신 시스템
   1. `데이터 생성` 및 `추출`
   2. `코드 매핑` 및 `데이터 변환`
   3. `인터페이스 테이블` /`파일 등록`
2. 수신 시스템
   1. 연계 `데이터 로드`
   2. `코드 매핑` 및 `데이터 변환`
   3. 운영 DB 반영
3. 연계 서버
   1. 연계 데이터 로므 및 전송 현식으로 변환
   2. 연계 데이터 송/수신
   3. 데이터 `변환` 및 `로드`

### 장애/오류 유형 및 처리방안

- 장애 및 오류 유형 분류
  1. 송/수신 시스템 연계 프로그램 오류
  2. 연계 서버 오류
  3. 연계 데이터 오류
- 로그를 통해 장애 / 오류 원인 파악 후 처리방안 모색

### 확인 및 처리 절차

1. 장애 및 오류 현황 모니터링 화면을 통해 `오류 원인` 및 `발생 현황 확인`
2. 오류 로그테이블 혹은 파일을 확인하여 `원인 분석`
3. 분석된 결과를 통해 `조치`를 취한다

### 정의 및 설계

- 항목
  1. 장애 및 오류 관리 대상
  - 연계 프로그램에서 관리하는 `장애` 및 `오류`를 `관리 대상`으로 정의
  2. 관리 대상의 장애 및 오류 코드 및 메시지
  - 관리 대상을 주제별로 분류 후 `오류코드 부여` 및 `오류 메시지 정의`
  3. 장애 및 오류 코드 및 메시지 관리 방식
  - `에러가 많다` ? `테이블 관리 방식` : `파일 관리 방식`
  4. 장애 및 오류 기록 방식
  - 테이블/파일 로그, 연계 데이터 로그로 설계

### 보안 적용

- 일반적인 연계 데이터의 보안 방식

  1. 전송 구간 보안
     - 패킷을 `스니핑을 방지`하기 위해 `암호화 프로토콜`을 사용한다.
     - 패킷을 `스니핑 당하더라도` 확인할 수 없게 `패킷을 암호화함`
  2. 데이터 구간 보안
     - 송/ 수신시 암복호화를 한다.
     - 절차
       - 송신
         1. DB에서 연계 데이터 추출
         2. 보안 적용 칼럼 암호화
         3. 연계 데이터 인터페이스 테이블 및 파일에 등록 및 송신
       - 수신
         1. 암호화된 칼럼 복호화
         2. 운영 DB에 반영

- 암/복호화 절차
  1. `적용 대상`, `알고리즘`, `암호화 키` 선정
  2. 적용 칼럼 데이터 길이 변경
     - 암호화는 평문보다 길어지기 때문에 늘려준다.
  3. 알고리즘 라이브러리 확보 및 설치
  4. 암복호화 처리

# XML(eXtensible Markup Language)

- `특수 목적 마크업 언어`를 만드는데 사용되는 다목적 마크업 언어
- HTML문법과 호환되지 않고, SGML의 복잡함을 해결하기 위해 개발됨
  - 멀티미디어 전자문서들을 다른 시스템과 `손실 없이` 효율적으로 `전송/ 저장` 및 `자동 처리`를 위한 언어
- `사용자가 태그를 정의`할 수 있고, 다른 사용자가 `정의된 태그를 사용` 할 수 있다.
- 트리 구조로 구성됨
- 상위 태그는 여러 개의 하위 태그를 가질 수 있다.

## SOAP( Simple Object Access Protocol )

- 네트워크상에서 HTTP/HTTPS, SMTP등을 이용해 XML을 교환하기 위한 통신 규약
- 메시지 형식 및 처리 방법 지정
- `HTTP기반`으로 동작하여 `프록시` 및 `방화벽`의 영향 없이 `통신가능`하다
- 최근에는 `SOAP 대신 TESTfull` 프로토콜의 이용하기도 한다.
  - TESTfull
    - `HTTP + REST` 의 원칙을 사용한 웹 `서비스 API집합`

## WSDL ( Web Services Description Language)

- 웹 서비스와 관련된 서식 및 프로토콜 등을 표준 방법으로 기술 및 게시하기 위한 언어
- XML로 작성되고, UDDI의 기초가 된다.
  - UDDI (Universal Description, Discover and Integration)
    - 비지니스 업체 목록에 자신을 등록하기 위한 XML기반 규격

# 연계 테스트

- `연계 시스템` 및 `구성 요소`가 `정상 작동`하는지 확인하는 활동
- 순서

  1. 연계 테스트 케이스 작성
     - `데이터` 및 `프로세스 흐름`을 분석하여 `테스트 항목 도출`
  2. 연계 테스트 환경 구축

     - `일정`,`방법`,`절차`,`소요시간` 등을 송/수신 기관과 `협의를 통해` 결정

  3. 연계 테스트 수행
     - 테스트 케이스 시험 항목 및 처리 절차를 `실제로 진행`
  4. 연계 테스트 수행 결과 검증
     - `수행 결과`와 `예상 결과`와 `동일 여부`를 판단
