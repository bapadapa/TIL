# 어플리케이션 테스트

- `APP의 잠재적 결함을 찾은 행위 또는 절차`
- 요구사항 만족을 위해 확인 및 검증을한다
- 기본 원리
  1. 완변한 테스트 불가능
     - 잠재적 결함은 `줄일 수 있지`만, `없앨 수 없다`
  2. 파레토 법칙
     - `20%의 코드`에서 `결함의 80%`가 발견됨
  3. 살충제 패러독스
     - `동일한 테스트케이스를 반복`하면 더이상 `결함이 발생하지 않는다`
  4. 테스팅은 정황 의존
     - `정황에 따라 결과가 달라짐`으로, `정황에 따라 다르게 테스트`해야함
  5. 오류-부재의 궤변
     - `결함이 없더`라도 `요구사항을 못만족하면` 품질이 높다 할 수 없다
  6. 테스트와 위험은 반비례
     - 테스트를 많이하면 미래의 위험을 예방할 수 있다.
  7. 테스트의 점진적 확대
     - 테스트는 `점진적`으로 `확대`하며 진행해야함
  8. 테스트의 별도 팀 수행
     - 테스트는 `개발자와 관계없는 팀에`서 해야함

## 테스트 분류

1. 실행 여부에 따른 테스트
   1. 정적 테스트
      - `프로그램 실행 없이` 소스 코드 대상으로 분석
      - `소스코드`에 대한 `결함을 발견`하기 위해 사용
      - 종류
        - `워크스루`, `인스펙션`, `코드검사`...
   2. 동적 테스트
      - `프로그램을 실행`시켜 오류를 찾는 테스트
      - 개발의 거이 모든 단계에서 테스트
      - 종류
        - `블랙박스 / 화이트박스` 테스트
2. 테스트 기반에 따른 테스트
   1. 명세 기반
      - `명세를 빠짐없이` 테스트 케이스 생성 후 테스트
      - 종류
        - `동등 분할`, `경계 값 분석` ..
   2. 구조 기반
      - `논리 흐름`에 따라 테스트케이스 생성 후 테스트
      - 종류
        - `구문 기반`, `결정 기반`, `조건 기반.`.
   3. 경험 기반
      - 유사 기술 등에 대한 `테스터의 경험`을 기반으로 테스트
      - `명세가 불충분` 혹은 `시간의 제약`이 있을경우 효과적
      - 종류
        - `에러 추정`, `체크 리스트`, `탐색적 테스팅`...
3. 시각에 따른 테스트
   1. 검증 테스트
      - `개발자 시각`에서 `제품 생산 과정`을 테스트
      - 명세대로 완성됬는지를 테스트
   2. 확인 테스트
      - `사용자 관점`에서 `생산된 결과`를 테스트
      - 요구대로 완성되었는지, 정상 작동하는지 테스트
4. 목적에 따른 테스트
   1. 회복 테스트
      - 결함을 주고 `실패 후 복구 여부` 테스트
   2. 안전 테스트
      - 시스템 보호 도구의 `시스템 보호`(침입 ..등) 여부 확인 테스트
   3. 강도 테스트
      - `과부하`시에도 `정상 작동`하는지 확인하는 테스트
   4. 성능 테스트
      - 전체적 `효율성을 진단`하는 테스트
        - `응답시간`, `처리량`등을 테스트
   5. 구조 테스트
      - `내부의 논리적경로`, `소스 코드 복잡도` 등을 테스트
   6. 회귀 테스트
      - `변경 또는 수정`된 코드에 `새로운 결함 여부` 테스트
   7. 병행 테스트
      - `변경 전/후 SW`에 데이터를 입력하여 결과를 비교하는 테스트

# 테스트 기법에 따른 APP 테스트

## 화이트박스 테스트 (White Box Test)

- `원시 코드`의 `논리적`인 모든 경로를 테스트하여 테스트 케이스를 설계하는 방법
- 모든 원키 코드를 1번 이상 실행

### 종류

1. 기초 경로 검사 (Base Path Testing)
   - 절차적 설계의 논리적 복잡성을 층정할 수 있게 해주는 기법
   - 대표적인 테스트 기법
2. 제어 구조 검사 ( Control Structure Testing)
   1. 조건 검사 ( Condition Testing )
      - 모듈 `내 논리적 조건을 테스트`
   2. 루프 검사 ( Loop Testing )
      - `Loop 구조에 초점`을 맞춰 실행
   3. 데이터 흐름 검사 ( Data Flow Testing)
      - `변수 및 정의`에 초점을 맞춰 실시

### 검증 기준

1. 문장 검증 기준 ( Statement Converage )
   - `모든 구문 1번` 이상 수행
2. 분기 검증 기준 ( Branch Coverage )
   - `조건문 1번` 이상 수행
3. 조건 검증 기준 ( Condition Coverage )
   - 조건문에서 `True` 인 경우와 `False` 인 경우 모두 실행
4. 분기/조건 기준 ( Branch/Condition Coverage )
   - 조건 문의 `개별 조건식`의 결과가 `True` 및 `False`인 경우 한번 이상씩 실행

## 블랙박스 테스트

- 각 기능이 완전히 작동하는지 테스트
- 요구사항 명세를 보면서 테스트
- 구현된 기능 테스트

### 종류

1. 동치 분할 검사 ( Equivalence Partitioning Test)
   - `올바른 값`과 `올바르지 않은 값`을 동일하게 테스트하고 맞는 결과가 출력되는지 확인
   - `동등 분할 기법`
2. 경계값 분석 ( Boundary Value Analysis )
   - 입력 조건의 경계값을 주어 테스트
3. 원인-효과 그래프 검사 ( Cause-Effect Graphing Testing )
   - `관계 및 출력`에 영향을 미치는 상황을 분석 후 `효용성 높은 케이스`를 선정
4. 오류 예측 검사 (Error Guessing )
   - 과거의 `경험 및 감각`으로 테스트
5. 비교 검사 ( Comparison Testing)
   - `여러 버전`의 프로그램에 `동일한 자료`로 테스트하여 `동일결과가 도출`되는지 확인

# 개발 단계에 따른 APP 테스트

- APP 테스트와 SW 개발 단계를 연결하여 표현한 것을 `V-모델`이라한다
- 요구사항
  - 분석
    - 설계
      - 구형
      - 단위테스트
    - 통합 테스트
  - 시스템 테스트
- 인수 테스트

## 테스트 종류

1. 단위 테스트 (Unit Test)

   - 모듈 및 컴포넌트에 초점을 맞춰 테스트
   - `인터페이스`, `외부적I/O` , `자료구조`, `독립적 기초 경로`, `오류 처리 경로`, `경계 조건등`을 검사
   - `사용자 요구사항` 기반으로 `기능성 테스트`를 최우선 수행
   - `구조 기반` / `명세 기반`으로 나눠지지만, `주로 구조 기반 테스트` 시행

2. 통합 테스트 ( Integration Test )

   - `단위 테스트가 완료`된 모듈들을 `결합`하여 하나의 시스템으로 완성시키는 과정의 테스트
   - `모듈` / `통합된 컴포넌트` 간의 상호 작용 오류 검사
   - 종류
     1. 비점진적 통합 방식
        - 단계적으로 통합하는 절차 없이 `모든 모듈을 결합`하여 프로그램 전체를 테스트
          - 종류
            - 빅뱅 통합 테스트 방식
              - 상호 인터페이스 고려 없이 `한번에 테스트`
     2. 점진적 통합 방식
        - 모듈 단위로 단계적으로 테스트
          - 종류
            - 하향식 통합 테스트
              - `상위 모듈` -> `하위 모듈` 방향으로 통합하며 테스트
                - 깊이 우선 통합법 ( Depth First )
                - 넓이 우선 통합법 ( Breadth first )
              - 절차
                1. 주요 제어 모듈의 종속 모듈은 `스텁`으로 대체
                   - 스텁 : 일시적 필요 조건만 갖고 있는 실험용 모듈
                2. 통합 방식에 따라 `스텁`들이 한번에 하나씩 `실제 모듈로 교체`
                3. 모듈이 통합할 때마다 테스트
                4. 오류가 재발하지 않는 다는 것을 보증하기 위해 `회귀 테스트` 실시
                   - 회기 테스트
                     - `변경된 모듈`이나 `컴포넌트`에 새로운 `오류 검증`하는 테스트
                     - 이미 한 테스트를 반복하는 것
            - 상향식 통합 테스트
              - `하위` -> `상위모듈` 방향으로 통합하며 테스트
              - 절차
                1. 하위 모듈을 클러스터로 결합
                   - 클러스터 : `주요 제어 모듈과 관련`된 `종속 모듈의 그룹`
                2. `입/출력 확인`을 위해 `더미 모듈`인 `드라이버`를 작성
                   - 드라이버 : `하위 모듈 호출` -> `파라미터 전달` -> `모듈 테스트 수행 결과 도출 하는` 도구
                3. 통합된 클러스터 단위로 테스트
                4. 테스트 완료시 `상위로 이동하여 결합` 후 `드라이버는 실제 모듈로 대체`
            - 혼합식 통합 테스트
              - `하위 수준` = `상향식`, `상위 수준` = `하향식 통합`을 사용하여 `최적의 테스트`를 지원
              - `센드위치식 통합` 테스트라고도 부름

3. 시스템 테스트 ( System Test )
   - 개발된 `SW가 완벽한 수행여부` 테스트
   - `기능적`/`비기는적` 요구사항을 구분하여 각각 만족하는지 테스트
4. 인수 테스트 ( Acceptance Test)
   - 사용자의 `요구사항을 충족`하는지에 중점으로 테스트
   - `사용자가 직접 테스트`
   - 테스트 종류
     1. 사용자 인수 테스트
        - 사용자가 시스템 사용의 `적절성 여부` 판단
     2. 운영상 인수 테스트
        - `백업/복원 시스템`, `재난복구`, `사용자 관리` , `정기 점검`등 테스트
     3. 계약 인수 테스트
        - 계약상의 `인수/검수 조건 준수` 여부 판단
     4. 규정 인수 테스트
        - `정부 지침`, `법규`, `규정` 등을 맞게 개발됬는지 여부 판단
     5. 알파 테스트
        - `개발자 앞에서 수행`되는 테스트
        - `통제된 환경`에서 행해지고, 사용자-개발자 같이 오류확인
     6. 베타 테스트
        - `최종 선정된 여러 사용자`가 수행하는 테스트
        - `실업무`를 가지고 `사용자가 직접` 테스트

# APP 테스트 프로세스

- 개발된 소프트웨어가 `요구대로 만들어`졌는제, `결함 여부`등을 테스트하는 절차
- 절차

  1.  테스트 계획
      - `기획서` 및 `요구 명세서` 기반으로 `목표 정의` 및 `테스트 대상` 및 `범위` 결정
  2.  테스트 분석 및 디자인
      - `목적 및 원칙` `검토`하고 사용자 `요구사항 분석`
  3.  테스트 케이스 및 시나리오 작성
      - 테스트케이스 `작성 및 검토` 후 `테스트 시나리오 작성`
  4.  테스트 수행
      - 환경 구축 후 테스트
  5.  테스트 결과 평가 및 리포팅
      - `결과를 비교 분석`하여 `테스트 결과서 작성`
  6.  결함 추적 및 관리
      - 테스트 후 결함 추적 관리함

## 결함 관리 프로세스

1. 에러 발견
   - `테스트 전문가`와 `프로젝트팀`이 논의
2. 에러 등록
   - `발견된 에러`를 `결함 관리 대장에 등록`
3. 에러 분석
   - `등록된 에러`가 실제 `결함 여부 판단`
4. 결함 확정
   - 분석 결과가 `실제 결함`이면 `확정 상태`로 설정
5. 결함 할당
   - 담당자에게 `결함 할당후` `결함 할당 상태`로 설정
6. 결함 조치
   - 결함 수정 후 `수정 완료`시 `결함 조치 상태`로 설정
7. 결함 조치 검토 및 승인
   - 테스트 후 이상이 없으면 `결함 조치 완료 상태`로 설정

## 테스트 케이스 ( Test Case )

- `사용자의 요구사항`을 정확하게 `준수` 했는지 `확인`하기 위해 설계된 테스트 항목에 대한 명세서
- 미리 설정시 `테스트 오류방지`, `인력 및 시간등의 자원낭비를 줄임`

## 테스트 시나리오 ( Test Scenario )

- 테스트 케이스를 `적용하는 순서`에 따라 여러 개의 `테스트 케이스를 묶은 `집합

- 테스트 케이스를 적용하는 구체적인 절차 명세
- 순서에 대한 `절차`, `사전 조건`, `입력 데이터` 등 설정

## 테스트 오라클 ( Test Orcale )

- 테스트 결과가 `올바른지 판단`하기 위해 `사전`에 `정의된 참값`을 `대입하여 비교`하는 기법
- 특징
  1.  제한된 검증
      - 모든 테스트 케이스에 `적용할 수 없다`
  2.  수학적 기법
      - 테스트 오라클의 값을 `수학적 기법`을 이용하여 구할 수 있다.
  3.  자동화 가능
      - `실행`, `결과 비교`, `커버리지 측정` 등을 자동화 할 수 있다.
- 종류
  1.  참 오라클
      - 입력 값에 대해 기대하는 결과를 제공
      - 모든 오류 검출
  2.  샘플링 오라클
      - `특정 값`에 대해서만 `기대 결과를 제공`하는 오라클
        - `전수 테스트가 불가`할 경우 사용
  3.  추정 오라클
      - 특정 케이스는 기대 결과를 제곤하지만, `나머지는 추정으로 제공`
  4.  일관성 검사 오라클
      - 테스트 `전후 결과값` `동일 여부` 판단

# 테스트 자동화 도구

## 자동화 도구 종류

1. 정적 분석 도구( Static Analysis Tools )
   - 프로그램을 실행하지 않고 분석하는 도구
   - `코드 관련 결함`을 발견하기 위해 사용
2. 테스트 실행 도구( Test Execution Tools )
   - `스크립트 언어`를 사용하여 테스트 실행
     1. 데이터 주도 접근 방식
        - `스프레드시트`에 테스트 `데이터 저장 후 이를 읽어` 실행
     2. 키워드 주도 접근 방식
        - `스프레드시트`에 수행할 동작을 나타내는 `키워드 및 데이터를 저장`하여 실행
3. 성능 테스트 도구( Performance Test Tools )
   - `가상의 사용자`를 만들어 테스트 수행하여 `성능 목표 달성` 여부 확인
4. 테스트 통제 도구 ( Test Control Tools )
   - 테스트 계획 및 관리, 테스트 수행, 결함 관리등을 수행하는 ㅗㄷ구
   - 종류
     1. 형상 관리 도구
        - 수행에 필요한 다양한 도구 및 데이터 관리
     2. 결함 추적/관리 도구
5. 테스트 하이네스도구 ( Test Harness Tools)

   - 테스트가 `실행될 환경`을 `시물레이션` 하여 컴포넌트 및 모듈이 `정상적으로 테스트 되도록` 하는 도구
   - 테스스트 하이네스
     - 컴포넌트 및 모둘을 `테스트하는 환경의 일부분`, `테스트를 위해 생성된 코드 및 데이터`
   - 구성 요소

     1. 테스트 드라이버 (Driver)
        - 대상의 `하위 모듈 호출` -> `파라미터 전달` -> 테스트 후 `결과 도출`
     2. 테스트 스텁 (Stub)
        - `일시적으로 필요한 조건`만 가지고 있는 테스트용 모듈
     3. 테스트 슈트 (Suites)
        - 테스트 케이스의 `단순 집합`
     4. 테스트 케이스 ( Case)
        - `요구사항 준수여부`의 테스트 항목 명세서
     5. 테스트 스크립트 (Script)
        - `자동화된 테스트 실행 절차`의 명세서
     6. 목 오브젝트(Mock Object)
        - `행위를 조건부로 입력시` 그 상항에 `예정된 행위를 수행`하는 객체

## 수행 단계별 테스트 자동화 도구

1. 테스트 계획
   1. 요구사항 관리
      - `정의 및 변경사항` 등을 관리하는 도구
2. 테스트 분석/설계
   1. 테스트 케이스 생성
      - 기법에 따른 `데이터 및 케이스` 작성 지원 도구
3. 테스트 수행
   1. 테스트 자동화
      - 테스트를 자동화 하여 `효율성 증대`
   2. 정적 분석
      - `코딩 표준` 및 `런타임 오류` 등을 `검증`
   3. 동적 분석
      - `시뮬레이션`을 통해 `오류 검출`
   4. 성능 테스트
      - `가상 사용자`를 이용하여 `처리능력 측정`
   5. 모니터링
      - `시스템 자원` 상태 `확인 및 분석` 지원
4. 테스트 관리
   1. 커버리지 분석
      - 테스트의 `충분성 여부` 검증
   2. 형상 관리
      - 수행에 필요한 `도구 및 데이터` 관리
   3. 결함 추적/관리
      - 발견한 `결함을 추적 및 관리`함

# 결함 관리

## 결함

- 개발자가 `설계한것`과 `다른 결과`가 발생하는 것

## 관리 프로세스

1. 결함 관리 계획
   - 일정, 인력, 업무 프로세스등을 확보 후 계획 수립
2. 결함 기록
   - `결함을 DB`에 등록
3. 결함 검토
   - 결함을 `검토 후 결함`을 수정할 개발자에게 전달
4. 결함 수정
5. 결함 재확인
6. 결함 상태 추적 및 모니터링 활동
   - `결함 관리 DB`를 이용해 `대시보드` 또는 `게시판 형태`로 서비스 제공
7. 최종 결함 분석 및 보고서 작성
   - 보고서를 작성 후 결함 관리 종료

## 결함 상태 추적

- 추적 및 관리하여 향후 발견될 모듈 혹은 컴포넌트 추정
- 결함 관리 측정 지표
  1.  결함 분포
      - 특정 속성에 해당하는 `결함 수 측정`
  2.  결함 추세
      - `시간`에 따른 결함 `추이 분석`
  3.  결함 에이징
      - 특정 `결함 상태`로 `지속되는 시간 측정`

## 추적 순서

1. 등록
2. 검토
3. 할당
4. 수정
5. 조치 보류
6. 종료
7. 해제

## 결함 분류

1. 시스템 결함
   - `APP환경` 혹은 `DB 처리`에서 발생된 결함
2. 기능 결함
   - `기획`, `설계`, `업무 시나리오` 등의 단계에서 유입된 결함
3. GUI 결함
   - `화면 설계시` 발생한 결함
4. 문서 결함
   - `의사소통 및 기록`이 원활하지 않아 발생한 결함

## 결함 심각도

- 결함이 시스템에 미치는 치명도를 나타내는 척도
- 분류
  - High, Medium, Low
  - 치명저그 주요, 보통, 경미 , 단순

## 우선순위

- 심각도에 따라 설정 및 수정 여부 판단
- 분류
  - 결정적, 높은, 보통, 낮음
  - 즉시 해결, 주의 요망, 대기 , 개선 권고

## 관리 도구

1. Mantis
   - `SW 설계`시 `단위별 작업 내용 기록`하여 `결함 추적`도 가능
2. Trac
   - `추적 및 통합 관리` 할 수 있음
3. Redmine
   - `관리 및 결함 추적` 가능
4. Bugzilla
   - 결함을 `지속적 관리` 할 수 있다.
   - `심각도 및 우선순위` 지정 가능

# APP 성능 분석

## 성능

- `최소한의 자원` `최대한의 기능`을 신속히 처리하는 정도
- 측정 지표
  1.  처리량 (Throughput)
      - 일정 시간 내에 `처리하는 일의 양`
  2.  응답 시간 (Response Time)
      - `요청 전달 시간`부터 `응답` 할때까지 `걸린 시간`
  3.  경과 시간 ( Turn Around Time )
      - 작업 `의뢰부터 완료`까지 걸린 시간
  4.  자원 사용률 ( Resource Usage)
      - 작업 처리하는 동안의 자원 사용률

## 성능 테스트 도구

- 부하 및 스트레스를 가하면서 성능 측정 지표를 점검하는 도구
- 종류
  1.  Jmeter
      - `HTTP,FTP`등 다양한 프로토콜 지원
      - 지원 환경 : Cross-Platform
  2.  LoadUi
      - `모니터링`, `Drag&Drop` 등 `사용자 편의성` 강화된 도구
      - 지원 환경 : Cross-Platform
  3.  OpenSTA
      - `HTTP/HTTPS` 프로토콜에서 `부하 테스트` 및 `생산품 모니터링`
      - 지원 환경 :Window

## 시스템 모니터링 도구

- APP 실행시 시스템 자원 사용량 확인 및 분석
- 종류
  1.  Scouter
      - `단일 뷰 통합/실시간 모니터링`, `튜닝`에 최적화
      - APP 성능 `모니터링 및 통제`
      - 지원 환경 : Cross-Platform
  2.  Zabiix
      - 웹기반 모니터링 도구
      - 지원 환경 : Cross-Platform

# 복잡도

- 어느정도 수준까지 테스트 및 개발시 `자원 소요`를 `예측`하는데 사용

## 시간 복잡도

- `알고리즘`을 수행하기 위해 프로세스가 수행하는 `연산 횟수`를 `수치화`한 것
- 종류
  1.  빅오 표기법
      - `최악`의 실행시간
  2.  세타 표기법
      - `평균`의 실행시간
  3.  오메가 표기법
      - `최상`의 실행시간

## 순환 복잡도

- `논리적인 복잡도`를 측정하기 위한 소프트웨어의 척도
- `V(G) = E(화살표) - N(노드) + 2`

# 어플리케이션 성능 개선

## 소스코드 최적화

- `나쁜 코드` -> `클린 코드`로 작성하는 것
  - 클린 코드
    - 누구나 이해기 쉽고, 수정 및 추가할 수 있는 단순 명료한 코드
  - 나쁜 코드
    - 로직이 복잡하고 이해하기 어려운 콛,
    - 대표 사례
      1.  스파게티 코드
          - 로직이 서로 복잡하게 얽혀 있는 코드
      2.  외계인 코드
          - `오래` 되거나, `참고 문서 혹은 개발자가 없어` 유지보수가 어려운 코드

## 클린 코드 작성 원칙

1. 가독성
   - 누구나 쉽게 읽을 수 있어야함
   - 쉬운용어, 들여쓰기, 등
2. 단순성
   - `한번에 1가지 작업`을 처리하도록 코드 작성
   - 클래스/메소드/함수 등을 `최소단위`로 분리
3. 의존성 배제
   - `다른 모듈에 미치는 영향 최소화`
   - 코드 변경시 다른 부분에 영향이 없도록 작성
4. 중복성 최소화
   - `중복되면 공통된 코드를 사용`
5. 추상화
   - 상위 클래스에서 추상화 하고, 하위 클래스에서 구현

## 최적화 유형

1. 클래스 분할 배치
   - `1개의 클래스 1개의 역할`로 `응집도를 높이고, 크기를 작게` 작성
2. 느슨한 결합
   - 추상화 하여 클래스간 `의존성 최소화`

## 소스 코드 품질 분석 도구

1. 정적 분석 도구
   - 실행하지 않고 코드의 스타일/결함 등 문제점 분석
   - 종류
     1. pmd
        - `미사용 변수`, `최적화 되지 않은 코드`등을 검사
        - 지원 환경 : Linux , Window
     2. cppcheck
        - c/c++의 `메모리누수/오버플로우` 등 분석
        - 지원 환경 : Window
     3. SonarQube
        - `중복`, `복잡도`, `코딩 설계` 등을 분석하는 통합 플랫폼
        - 지원 환경 : Cross-Platform
     4. checkstyle
        - `Java 코드` 검사
        - 다양한 개발 도구에 `통합하여 사용` 가능
        - 지원 환경 : Cross-Platform
     5. ocm
        - `다양한 언어` 검사
        - 지원 환경 : Cross-Platform
     6. cobertura
        - Java 코드의 `복잡도` 및 `분석 테스트 커버리지` 측정
        - 지원 환경 : Cross-Platform
2. 동적 분석 도구

   - 코드를 실행하여 `메모리 누수` ,`스레드 결함`등을 분석
   - 종류

     1. Valgrind
        - 프로그램 내에 존재하는 `메모리 및 쓰레드 결함`등을 분석
        - 지원 환경 : Cross-Platform
     2. ## Avalanche

        - `Valgrind`프레임워크 및 `STP` 기반으로 구현
        - `결함` 및 `취약점` 분석
        - 지원 환경 : Linux, Android
