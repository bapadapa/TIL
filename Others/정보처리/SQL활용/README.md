# DDL (Data Define Language)

- DB 구축 및 수정시 사용
- 유형ㅇ

  1. CREATE ( 정의 )

     - 기본 모양
       - create 기능 ...

     1. 스키마 생성
        - ```sql
            create schema 스키마명 authorization 사용자\_id
          ```
          - 소유권인 사용지안 스키마 정의
     2. 도메인 생성
        - ```sql
            create domain 도메인명 [AS] 데이터타입 [DFAULT 기본값] [CONSTRAINT 제약조건명 CHECK (범위)]
          ```
     3. 테이블 생성
        - ```sql
            create table  테이블명 (
                속성명 데이터_타입 [DFAULT 기본값] [NOT NULL]...
                [,PRIMARY KEY(기본키 속성명)]
                [,UNIQUE(대체키 속성명)]
                [,FOREIGN KEY(외래키 속성명) REFERENCES 참조테이블 (참조테이블(기본키 속성명))]
                    [ON DELETE 옵션]
                    [ON UPDATE 옵션]
                [,CONSTRAINT 제약조건명][CHECK(조건식)]
            )
          ```
          - on A
            - A이벤트가 발생시 옵션수행
     4. 뷰 생성

        - ```sql
            create view 뷰명[(속성명[,속성명,])]
            AS select문
          ```

     5. 인덱스 생성
        - ```sql
            create [UNIQUE] index  인덱스명
            ON 테이블명(속성명[ASC|DESC] [,속성명 [ASC|DESC]]) [CLUSTER]
          ```
          - CLUSTER 설정시` 실제 데이터도 정렬`됨
            - 값 `삽입삭제시 재정렬`해야함

  2. ALTER ( 정의 변경 )
     - 형식
       - ```sql
           ALTER table 테이블명 ADD 송성명 데이터타임 [DEFAULT '기본값']
           ALTER table 테이블명 ALTER 송성명 데이터타임 [SET DEFAULT '기본값']
           ALTER table 테이블명 DROP COLUMN 송성명 데이터타임 [CASCADE]
         ```
         - ADD
           - 새로운 열 추가
         - ALTER
           - 특정 속성 `DEFAULT`값 변경
         - DROP COLUMNS
           - 특정 속성(열) 삭제
  3. DROP ( 삭제 )
     - 형식
       ```sql
           DROP SCHEMA 대상 [CASCADE | RESTRICT]
           DROP DOMAIN 대상 [CASCADE | RESTRICT]
           DROP TABLE 대상 [CASCADE | RESTRICT]
           DROP VIEW 대상 [CASCADE | RESTRICT]
           DROP INDEX 대상 [CASCADE | RESTRICT]
           DROP CONSTRAINT 대상
       ```
       - CASECADE
         - 참조 개체또한 삭제
         - 연쇄 삭제
       - RESTRICT
         - `참조중`일시 `삭제 취소`

# DCL ( DATA CONTROL LANGUAGE)

- 데이터의 `보안`, `무결성`, `회복`, `병행 제어`등을 정의
- 종류
  1. GRANT/REVOKE
  - DB 사용 권한 부여/삭제
  - 사용자 등겁 지정 및 해제
    - ```sql
       GRANT 사용자등급 TO 사용자_ID_리스트 [IDENTIFIED BY 암호]
       REVOKE 사용자등급 FROM 사용자_ID_리스트
      ```
  - 테이블 권한 부여/삭제
    - ```sql
       GRANT 권한 ON 개체 TO 사용자_ID_리스트 [WITH GRANT OPTION]
       REVOKE [GRANT OPTION FOR] 권한 ON 개체 FROM 사용자_ID_리스트 [CASECADE]
      ```
      - WITH GRANT OPTION
        - 부여 받은 권한을 다른 사용자에게 부여할 수 있다
      - GRANT OPTION FOR
        - `WITH GRANT OPTION` 권한 제거
      - CASECADE
        - 부여한 사용자들 또한 권한 제거
    2. COMMIT
       - 트랜잭션이 수행한 내용을 DB에 반영
       - DML `성공 시 COMMIT` , `실패시 ROLLBACK` 하게 `AUTO Commit` 설정 가능
    3. ROLLBACK
       - DML 등으로 `값이 바꼈으나`, `COMMIT`되지 않은 `내용을 취소`하고, `DB를 이전 상태로 돌리는` 명령어
       - `트랙잭션이 일부분만 성공`하면 `비일관성` 상태가 되기 때문에 ROLLBACK 되야한다.
    4. SAVEPOINT
       - 트랜잭션 내에 ROLLBACK 할 위치를 지정하는 명령어
       - ROLLBACK시 SAVEPOINT까지 취소

# DML (Data Manipulation Language)

- 데이터를 실질적으로 관리하는 언어
- 유형
  1.  insert ( 삽입 )
      - ```sql
        INSERT INTO 테이블명( 속성명..) value (데이터 ...)
        ```
        - 테이블에 `속성과 매핑`시켜 `데이터 삽입`
  2.  delete ( 삭제 )
      - ```sql
          DELETE FROM 테이블명 [WHERE 조건]
        ```
        - 조건에 맞는 레코드 삭제
        - 모든 레코드 삭제시 where 생략
  3.  update ( 갱신 )
      - ```sql
        UPDATE 테이블명 SET 속성명 = 데이터 [WHERE 조건]
        ```
  4.  select ( 조회 )
      - ```sql
        SELECT [PREDIACATE][테이블명.]속성명[as 별칭]
        [,그룹함수(속성명)[AS 별칭]]
        [, Window함수 OVER (PARTITION BY 속성명,.. , ORDER BY 속성명...)]
        [FROM 테이블명..]
        [WHERE 조건]
        [GROUP BY 속성명]
        [HAVING 조건]
        [ORDER BY 속성명 [ASC|DESC]]
        ```
        - PREDIACATE
          - 튜플수 제한
          - DISTINCT
            - 중복이 있다면 첫번쨰 1개 표시
      - 조건 연산자
        - | =    | <>     | <    | >    | >=          | <=          | ㅁ  |
          | ---- | ------ | ---- | ---- | ----------- | ----------- | --- |
          | 같다 | 다르다 | 크다 | 작다 | 크거나 같다 | 작거나 같다 |
      - like 연산자 (와일드카드)
        - | %        | \_    | #               |
          | -------- | ----- | --------------- |
          | 모든문자 | 1문자 | 숫자 1개를 대표 |
      - `하위 질의`
        - ```sql
          SELECT 속성 FROM 테이블명 WHERE 속성 =(SELECT 속성 FROM 테이블명 WHERE 속성 = 값)
          ```
      - `복수 테이블 검색`
        - ```sql
          SELECT 테이블1.속성, 테이블2.속성..
          FROM 테이블1, 테이블2
          WHERE 속성 = 데터
          ```
      - `그룹 함수`
        - GROUP BY 절에 지정된 그룹별로 속성 값 집계
          1. COUNT (속성)
             - 갯수 구하기
          2. SUM (속성)
             - 합구하기
          3. AVG (속성)
             - 평균구하기
          4. MAX ( 속성 )
             - 최댓값
          5. MIN ( 속석 )
             - 최솟값
          6. STDDEV ( 속성 )
             - 표준편차
          7. VARIANCE ( 속성)
             - 분산
          8. ROLLUP ( 속성1 ,속성2 , ...)
             - 속성 대상으로 그룹별 소계를 구함
             - 속성수가 N 개면 N+1개까지 , 상위 -> 하위 레벨 순으로 데이터 집계
          9. CUBE ( 속성, 속성 ...)
             - 모든 대상의 조합의 그룹별 소계를 구함
             - 속성수가 N개면 2^N레벨까지 , 상위 -> 하위 레벨 순으로 데이터 집계
      - `WINDOW 함수`
        - `GROUP BY절`을 사용하지 않고 `속성 값의 집계를 구함`
        - 지정된 범위는 WINDOW라고 부름
        - 함수
          1. ROW_NUMBER()
          - 각 레코드에 대한 `일련번호 반환`
          2. RANK()
          - `윈도우별 순위를 반환하며`, `공동 순위를 반영`
          3. DENSE_RANK()
          - `윈도우별 순위 반환`, `공동 순위를 무시`하고 순위 부여
      - `집합 연산자를 이용한 통합 질의`
        - 표기형식
          - ```sql
            SELECT 속성
            FROM 테이블1
            UNION|UNION ALL|INTERSECT|EXCEPT
            SELECT 속성
            FROM 테이블2
            [ORDER BY 속성명 [ASC|DESC]]
            ```
          - 종류
            1. UNION (합집합)
               - 조회 결과 통합
               - `중복 제거`
            2. UNION ALL (합집합 )
               - 조회 결과 통합
               - `중복 허용`
            3. INTERSECT (교집합)
               - 공통된 행만 조회
            4. EXCEPT (차집합)
               - `테이블 1`을 `기준`으로 테이블 2의 조회결과와 `동일하면 제외`

## JOIN 문

- 연관된 튜플을 결합하여 하나의 새로운 릴레이션으로 반환
- 일반적으로 FROM절에 기술

  [출처](https://dsin.wordpress.com/2013/03/16/sql-join-cheat-sheet/)
  ![JOIN문들](https://dsin.files.wordpress.com/2013/03/sqljoins_cheatsheet.png?w=628)

1. INNER JOIN
   - 조건 없이 수행시 `CROSS JOIN` 과 동일한 결과
     - CROSS JOIN
       - 두 테이블에 있는 튜플의 순서쌍
1. EQUI JOIN

   - `= (equal)` 연산을 통해 `동일한 값`을 가진 것을 반환

   1. WHERE
      - 동일 속성이 2번 나타남
      - ```sql
        select 테이블1.속성 , 테이블2.속성....
        from 테이블1, 테이블2
        where 테이블1.속성명 = 테이블2.속성명
        ```
   2. NATURAL JOIN
      - 동일 속성이 1번 나타남
      - ```sql
        select 테이블1.속성명 , 테이블2. 속성명
        from 테이블1 NATURAL JOIN 테이블2
        ```
   3. JOIN~USING
      - ```sql
        select 테이블1.속성명 ,테이블2.속성명
        from 테이블1 join 테이블2 using (속성)
        ```

1. NON - EQUI JOIN
   - ` = (equal)` 연산을 통해 `다른 값`을 가진 것을 반환
     - `= 이외의 연산자`를 이용해 연산
   - 표기 형식
     - ```sql
       select 테이블1.속성, 테이블2.속성..
       from 테이블1, 테이블2 ...
       where (NON-EQUI JOIN 조건)
       ```
1. OUTTER JOIN

- JOIN 조건에 만족
- 방법

  1. LEFT OUTTER JOIN

  - INNER JOIN 후 매칭 되지 않은 우측 릴레이션의 튜플은 NULL을 삽입하여 수행
  - 표기 형식

    - ```sql
      # 방법1
      select 테이블1.속성 ,테이블2.속성..
      from 테이블1 left join 테이블2
      on  테이블1.속성명 = 테이블2.속성명

      # 방법2
      select 테이블1.속성 ,테이블2.속성..
      from 테이블1 , 테이블2
      on  테이블1.속성명 = 테이블2.속성명(+)
      ```

  2. RIGHT OUTTER JOIN

     - INNER JOIN 후 매칭 되지 않은 좌측 릴레이션의 튜플은 NULL을 삽입하여 수행
     - 표기 형식

       - ```sql
         # 방법1
         select 테이블1.속성 ,테이블2.속성..
         from 테이블1 RIGHT join 테이블2
         on  테이블1.속성명 = 테이블2.속성명

         # 방법2
         select 테이블1.속성 ,테이블2.속성..
         from 테이블1 , 테이블2
         on  테이블1.속성명(+) = 테이블2.속성명
         ```

  3. FULL OUTTER JOIN

     - left join 후 right join 후 inner join을 해줌
     - 표기 형식

       - ```sql
         # 방법1
         select 테이블1.속성 ,테이블2.속성..
         from 테이블1 FULL OUTTER JOIN 테이블2
         on  테이블1.속성명 = 테이블2.속성명
         ```

# 프로시저 ( Procedure)

- SQL을 사용하여 작성한 일련의 작업을 저장해두고, 원할 떄 마다 저장한 작업을 수행하도록 하는 `절차형SQL`
- DB에 저장되어 수행되 `Stored 프로시저`라고도 불린다.
- 주로 배치, 마감 작업 등에 사용

## 구성도

- 형태
  - ```sql
    DECLARE(필수)
    BEGIN(필수)
      CONTROL
      SQL
      EXCEPTION
      TRANSACTION
    END(필수)
    ```

1. DECLARE
   - 명칭, 변수 , 인수, 데이터타입 등을 선언
2. BEGIN /END
   - 시작과 종료
3. CONTROL
   - 조건문 / 반복문을 삽입/처리
4. SQL
5. TRANSACTION
   - `COMMIT 여부`를 결정하는 처리부

## 생성

- CREATE PROCEDURE
- ```sql
  create [OR REPLACE] PROCEDURE 프로시저명(파라미터)
  [지역변수 선언]
  BEGIN
    PROCEDURE BODY
  END
  ```
  - OR REPLACE (예약어)
    - `동일한 이름`이 존재할경우 `대체함` (덮어씌우기)
  - 파라미터
    - IN
      - 호출 프로그램이 값을 전달할 때 지정
    - OUT
      - 프로시저가 값을 반환시 지정
    - INOUT
      - `호출 프로그램 -> 프로시저 -> 프로시저 실행 -> 값 반환` 시 지정
    - 매개변수명
      - 인자값 명을 정한다
    - 자료형
      - 자료형을 지정
  - 프로시저 BODY
    - BEGIN 으로 시작해서 END로 끝난다

## 실행

```sql
EXECUTE 프로시저명
EXEC 프로시저명
CALL 프로시저명
```

## 제거

```sql
DROP PROCEDURE 프로시저명
```

# 트리거

- 이벤트 발생시 자동으로 수행하는 `절차형 SQL`
- 형태
  - ```sql
    DECLARE(필수)
    BEGIN(필수)
      CONTROL
      SQL
      EXCEPTION
    END(필수)
    ```

1. DECLARE
   - 명칭, 변수 , 인수, 데이터타입 등을 선언
2. BEGIN /END
   - 시작과 종료
3. CONTROL
   - 조건문 / 반복문을 삽입/처리
4. SQL

## 생성

```sql
create[or replace] trigger 트리거명 [동작시기 옵션][동작 옵션]
ON 테이블명 REFERENCING [NEW|OLD] as 테이블명
for each row
[when 조건식]
begin
  트리거 BODY
end
```

1. 동작시기 옵션
   - AFTER
     - 테이블 변경 후 실행
   - BEFORE
     - 테이블 변경 전 실행
1. 동작 옵션
   1. INSERT
      - insert문 실행시 실행
   1. DELETE
      - delete문 실행시 실행
   1. UPDATE
      - update문 실행시 실행
1. NEW/OLD

   1. NEW
      - 추가/수정에 참여할 튜플집합
   1. OLD
      - 수적/삭제 이전 대상의 튜플 집합

1. FOR EACH ROW
   - 각 튜플마다 적용
1. WHEN 조건식 (Optional)
   - 적용한 튜플 조건지정
1. 트리거 BODY
   - 수행할 코드

## 제거

```sql
DROP TRIGGER 트리거명
```

# 사용자 정의 함수

- 종료 시 처리 결과로 단일값만 반환하는 `절차형 sql`
- 형태
  - ```sql
    DECLARE(필수)
    BEGIN(필수)
      CONTROL
      SQL
      EXCEPTION
      RETURN
    END(필수)
    ```

1. DECLARE
   - 명칭, 변수 , 인수, 데이터타입 등을 선언
2. BEGIN /END
   - 시작과 종료
3. CONTROL
   - 조건문 / 반복문을 삽입/처리
4. SQL
5. RETURN
   - 반환값 및 변수정의

## 생성

- ```sql
  create [OR REPLACE] FUNCTION 함수명(파라미터)
  [지역변수 선언]
  BEGIN
     함수 BODY
     RETURN 반환값
  END
  ```

## 실행

```sql
# 조회
SELECT 함수명 FROM 테이블명
# 삽입
INSERT INTO 테이블명(속성) VALUE (함수명)
# 삭제
DELETE FROM 테이블명 WHERE 속성 = 함수명
# 갱신
UPDATE 테이블명 SET 속성명 = 함수명
```

## 제거

```sql
DROP FUNCTION 함수명
```

# 제어문

- 절차형 SQL의 진행 순서를 변경하기 위해 사용하는 명령문

## IF

```sql
IF 조건 THEN
  CODE1
ELSE
  CODE2
END IF
```

## LOOP

```sql
LOOP
  CODE
    EXIT WHEN 조건
END LOOP
```

# 커서 (Cursor)

- 쿼리문의 처리 결과가 저장되어 있는 메모리 공간을 가리키는 포인터

1. 묵시적 커서(Implicit Cursor)

- 내부에서 자동으로 생성되는 커서
- Open -> Fetch -> Close 순으로 이루어 진다
- 종류
  1. SQL%FOUND
     - 수행결과 `Fetch 된 튜플`이 `1개 이상`이면 `TRUE`
  1. SQL%NOTFOUND
     - 수행결과 `Fetch 된 튜플`이 `0개`이면 `TRUE`
  1. SQL%ROWCOUNT
     - Fetch 된 튜플 수 반환
  1. SQL%ISOPEN
     - 커서가 `Open` 상태면 `TRUE`
     - `묵시적 Cursor`은 자동으로 닫기 때문에 `항상 False`

1. 명시적 커서 (Explicit Cursor)
   - 사용자 정의 Cursor
   - Declare -> Open -> Fetch -> Close 순으로 이루어 진다
   1. Declare
      - ```sql
        CURSOR 커서명(var1 , var2...)
        IS
        SELRECT문
        ```
   1. OPEN
      - ```sql
        OPEN 커서명(var1,var2...)
        ```
   1. Fetch
      - ```sql
        FETCH 커서명 INTO var1, var2...
        ```
   1. close
      - ```sql
        CLOSE 커서명
        ```

# DBNS 접속

- 응용 시스템을 이용하여 DBMS에 접속하는 것

## 접속 기술

- DBMS에 접근하기 위해 사용하는 `API` 혹은 `프레임워크`
- 종류
  1. JDBC
     - `JAVA`로 DB접속시 사용
     - 접속하려는 `DBMS의 드라이버` 필요
  2. ODBC
     - `언어에 관계없이` DB접속시 사용
     - DBMS 인터페이스에 관계없이 `ODBC 문장을 사용`하여 접속 가능
  3. MYBatis
     - JDBC를 단순화 해서 사용할 수 있는 `SQL Mapping` 기반 `Open Source 프레임워크`
     - `sql문장 분리 -> XML 생성 -> Mapping -> sql실행`

## 동적 SQL

- SQL 구문을 동적으로 변경하여 처리할 수 있는 sql
- `프리컴파일`시 `구문 분석`, `접근 권한 확인`등을 할 수 없다.
  - 프리컴파일
    - 코드에 삽입된 SQL문을 DB와 연결하는 작업
- `정적 SQL`에 비해 `느리지만`, `유연한 개발`이 가능하다

# SQL 테스트

- SQL이 사용자 의도에 맞게 수행하는지 검증하는 것
- 절차형 SQL은 구문오류 및 참조오류 여부를 우선적으로 확인

1. 단문 SQL 테스트

   - `DDL,DML,DCL`이 포함된 `SQL`과 `TCL테스트` 하는것
     - TCl
       - COMMIT , ROLLBACK, SAVEPOINT
   - DDL
     - `DESC[개체명]`를 통해 `속성, 자료형, 옵션`확인 가능
   - DML
     - select문으로 확인
   - DCL
     - `사용자 권한`은 `사용자 정보`가 저장된 `테이블 조회`

1. 절차형 SQL 테스트
   - 디버깅을 통해 결과를 확인하는 테스트
   - `SHOW ERRORS` 를 이용하여 `에러내용 확인`
   - 주석을 이용하여 점진적으로 검증하며 테스트

# ORM ( Object- Relational Mapping)

- 객체와 관계형 데이터베이스의 데이터를 연결하는 기술
- `코드 및 DB와 독립적`이여서 `재사용` 및 `유지보수`가 용이

## 프레임워크

- ORM을 구현하기 위한 여러 기능을 제공하는 SW
- 종류
  1. JAVA
     - JPA, Hibernate, EclipseLink, DataNucleus,등
  2. C++
     - ODB , QxOrm..
  3. Python
     - Django , SQLAlchemy, Storm...
  4. .NET
     - NHibernate, DatabaseObjects, Dapper...
  5. PHP
     - Doctrine, Propel, RedBean ...

## 한계

- OOP를 고려하지 않은 DB는 프로젝트가 크고 복잡해질수록 적용하기 어렵다
- 기존 기업은 ORM을 고려하지 않아 시간과 노력이 많이 필요하다

# 쿼리 성능 최적화

- `데이터 I/O APP` `성능 향상`을 위해 SQL 코드를 최적화 하는 것
- 성능 측정 도구인 APM을 이용하여 최적화할 쿼리 서넞ㅇ
  - APM
    - 모니터링 기능을 제공하는 도구

## 옵티마이저 ( Optimizer )

- SQL이 가장 효율적으로 수행되도록 최적의 경로를 찾아주는 모듈

1. RBO
   - DBA가 정해둔 규칙에 따라 경로를 찾는 `규칙 기반` 옵티마이저
     1. 최적화 기준
        - `규칙`
     1. 성능 기준
        - `개발자 숙련도`
     1. 특징
        - 실행 계획 `예측 쉬움`
     1. 고려사항
        - 개발자의 `규칙 이해도` 및 `규칙의 효율성`
2. CBO
   - DBMS마다 고유의 알고리즘에 따라 산출되는 비용으로 최적의 경로를 찾는 `비용 기반` 옵티마이저
     1. 최적화 기준
        - 접근 비용
     1. 성능 기준
        - 옵티마이저 성능
     1. 특징
        - 성능 통계치 정보 활용, `예측이 복잡`
     1. 고려사항
        - `비용 산출 공식`의 정확성

## 실행 계획 ( Execution Plan)

- DBMS의 옵티마잊저가 수립한 SQL 코드의 실행 절차와 방법
- EXPLAIN 명령어를 통해 확인하고, `그래픽 혹은 텍스트`로 표현
- 계획엔 연산 `처리 순서`가 적혀있다.
  - 연산 : 조인, 테이블 검색, 필터, 정렬...

## 최적화 방법

1. SQL 코드 재구성

   - where절 추가
   - where절 연산자 사용 제한
   - in을 `EXISTS`로 대체
     - EXISTS : 검색 성공시 종료
   - `힌트`로 액세스 `Path 및 Join` 순서 변경
     - 힌트 : `실행 계획에 영향`을 줄 수 있는 문장

2. 인덱스 재구성
   - 속성 및 조건을 고려하여 인덱스 구성
   - 인덱스 추가 및 열 순서 변경
   - 참조하는 SQL으로 영향 고려
   - IOT( Index Organized Table) 구성 고려
     - `데이터를 직접 테이블에 삽입`하여 주소값을 값을 얻는 과정이 생략되어 빠르다
   - 불필요한 인덱스 제거
