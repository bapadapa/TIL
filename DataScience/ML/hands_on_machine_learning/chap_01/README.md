# Chpater 01

## ML이란?

> `어떤 작업 T`에 대한 컴퓨터 프로그램의 `성능을 P`로 측정했을 때 `경험 E`로 인해 성능이 향상됬다면, 이 컴퓨터 프로그램은 작업 `T`와 성능 측정 `P`에 대해 경험 `E`로 학습한 것이다. - 톰 미첼(Tom Mitchell, 1997)

## ML 시스템 종류

1. 훈련 감동 방법

   1. 지도학습 ( Supervised learning )

      > - `Label ( Target ) `을 삽입하여 원하는 답이 포함되어 있다.
      >   - 주로 `분류( 구분 ) ` 및 `회귀 ( 예측 ) `로 나줘질 수 있다.
      >   - nmist와 같이 `predictor valiable`이 `target을` 예측하는 모양
      >   - 분석가(시스템)의 (데이터)관여가 있는 상황
      > - 분류( `Classification`)이 전형적인 지도학습이다.

      1. 지도학습의 대표 알고리즘
         1. k-최근접 이웃 ( `K-Nearest Neighbors` )
         1. 선형 회기 ( `Linear Regression` )
         1. 로지스틱 회기 ( `Logistic Regression` )
         1. SVM ( `Support Vector Machine` )
         1. 결정나무 (`Decision Tree` )
         1. 랜덤 포레스트 ( `Random Forest` )
         1. 신경망 ( `Neural Network` )

   1. 비지도학습( Unsupervised learning )

      > - 지도학습과 다르게 `Label`이 없는 상황
      > - 분석가(시스템)의 (데이터)관여가 없는 상황
      > - 정답이 없는 경우 사용

      1. 비지도 학습의 대표적 알고리즘

         1. 군집 ( `Clustering` )

            > 데이터를 특정 알고리즘을 이용하여 `각 그룹으로 나눠주는 것` <br>
            > 알고리즘에 따라 그룹을 세분화하여 나눠줄 수 있다. ex) HCA

            1. `K-Means`
            1. `DBSCAN`
            1. `HCA` ( Hierarchical Cluster Analysis )
            1. 이상치 탐지(`Outlier Detection`) & 특이치 탐지(`Novelty Detection`)
               - 이상치 탐지 : 이상치 즉, 특이한 값을 찾아내 자동으로 제거해줌
               - 특이치 탐지 : Trainning Set 에 있는 모든 Sample과 `달라 보이는 Sample`을 `탐지`하는 것
            1. `One-Class SVM`
            1. `Isolation Forest`

         1. 시각화 ( `Visualization` ) & 차원 축소 ( `Demensionality Reduction` )

            > 시각화 : 고차원의 데이터를 2D 혹은 3D로 도식화하여 `구조 및 패턴`을 확인 할 수 있다. <br>
            > 차원 축소 : 특성추출(Feature Extraction)을 통하여 차원 축소, 즉 Feature을 합칠 수 있다.

            1. `PCA` ( Principal Component Analysis )
            1. `Kernel PCA`
            1. `LLE` (Locally-Linear Embedding )
            1. `t-SNE` ( t-distributed Stochastic Neighbor Embedding )

         1. 연관 규칙 학습 ( `Association Rule Learning` )
            > 대량의 데이터에서 특성 간의 유의미한 관계를 찾는 것.
            1. `Apriori`
            1. `Eclat`

   1. 준지도 학습 ( semi - Supervised learning )
      > 데이터가 부분적으로만 Label이 있는 경우의 알고리즘
      - 일반적으로 `지도학습 + 비지도` 학습의 조합으로 이루어져 있다.
   1. 강화 학습

      > 학습 알고리즘 자체가 `환경 (Envionment)`을 관찰 후 `행동 (Action)`하고 그에따른 `보상 (Reward)` 및 `벌점(Penalty)`을 받아 더 좋은 `정책(Policy)`을 만드는 학습 알고리즘이다.

      - 간단 순서
        - `Agent 가 Environment를 관찰한다` -> `Action을 취한다` -> `Reward / Penalty를 받는다` -> `Policy를 수정한다`
          - 최적의 Policy를 찾을 때 까지 `위 과정을 반복`한다.
        - 간단 용어
          1. `Agent` : `학습 시스템`을 지칭함
          1. `Environment` : `Agent`가 학습하고자 하는 환경
          1. `Action` : `Agent`가 수행하는 작업
          1. `Reward / Penalty` : `Action`에 대한 보상 및 벌점
          1. `Policy` : `Agent`가 `Action`시에 고려할 `정책(규칙)`
        - 간단 예시
          - [민바크 지렁이 강화학습](https://www.youtube.com/watch?v=evAuPcwpeQc)

1. 훈련 시점

   1. 온라인 학습

      > - 온라인 데이터를 이용하여 `순차적`으로 한 개씩 또는 `미니배치`로 주입하여 `점진적으로 훈련`
      > - `실시간 시스템` 혹은 `메모리`가 부족할 경우 사용

   1. 배치 학습 (Batch Learning)

      > 가용 데이터를 모두 사용하여 훈련시켜 시스템이 점진적으로 학습할 수 없다. <br> `시간 및 자원소모가 커서` *오프라인에서 훈련*을 하여 `오프라인 학습`(Offline Learning)이라고도 함.

1. 모델 생성 ( `일반화`에 따른 분류 )

   1. 사례 기반 학습

      > - Sample을 기억하는 것이 훈련
      > - 예측을 위해 Sample 사이의 유사도 측정

      - `K-Means` 알고리즘이 여기에 포함됨

   1. 모델 기반 학습

      > - `Sample`을 사용해 Model 훈련
      > - 훈련된 모델을 이용해 예측
      > - 대부분의 알고리즘을 `수학적`으로 `표현` 할 수 있다.

## ML 주요 도전과제

1. 데이터 양의 부족
   - 데이터 양이 부족하면 알고리즘이 좋다하더라도 좋은 결과가 나오지 않을 수 있다.
     - 이미지, 음성인식과 같은 문제는 `수백만개 이상`의 데이터가 필요할 수 있다.
1. 대표성이 없는 훈련 데이터
   - 우연에 의해 대표성이 없는 데이터를 `샘플링 잡음 ( Sampling Noise )`이라한다
     - 표본 추출이 잘못된 대표성 없는 데이터를 `샘플링 편향 ( Sampling Bias )`이라 한다.
1. 저품질 데이터
   - `이상치 ( Outlier )` 혹은 `잡음 ( Noise )`이 많으면 올바를 훈련을 할 수 없다.
   - 특성 누락
     1. 해당 특성 제외
     1. 해당 샘플 제외
     1. 누락된 값을 채우기
     1. 특성을 넣은것과 안 넣은것을 둘다 훈련
1. 관련 없는 특성
   - 특성 공학
     1. 특성 선택 ( `Feature Selection` )
        - 보유한 것 중 가장 유용한 특성을 찾는다.
     1. 특성 추출 ( `Feature Extraction` )
        - 특성을 조합하여 새로운 특성을 생성한다
1. 과대적합 ( `OverFitting` )
   - 훈련 데이터에 너무 알맞은 경우
     - 규제를 이용하여 `과대적합` 감소
1. 과소적합 ( `UnderFitting` )
   - 모델이 너무 단순하여 학습이 재대로 안 되는 경우
   - 해결 방법
     1. 모델 파라미터가 더 많은 모델을 사용
     1. 좋은 특성 사용 ( 특성 공학 )
     1. 규제 ( `Regularization` ) 의 강도를 줄인다.

## 테스트 ( TEST ) 및 검증 ( Validation )

> - 모델을 생성시 `훈련`,`테스트`,`검증(개발)` 세트로 나누어 테스트 및 검증을 진행한다.
> - 테스트 및 검증을 이용하여 `일반화` 성능을 측정한다
> - trian-test 의 `훈련 오차는 낮지`만, `일반화 오차가 높다`면 `OverFitting`이다.
>   - 일반화 오차 ( `Generalizaition Error` ) : 새로운 샘플에 댄한 오류 비율
> - validation 의 성능이 낮다면 `데이터 불일치`
