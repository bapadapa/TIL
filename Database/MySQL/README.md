# MySQL 정리

## 설치

- [MySQL 인스톨](https://dev.mysql.com/downloads/installer/)

## SQL

1. DDL ( Data Define Language )

   - 데이터 정의

   - 명령어

     1. Create ( 데이터베이스 , 테이블 등을 생성)

        - 데이터베이스 , 스키마

          ```sql
          CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
          [create_option] ...

          create_option: [DEFAULT] {
              CHARACTER SET [=] charset_name
            | COLLATE [=] collation_name
            | ENCRYPTION [=] {'Y' | 'N'}
          }
          ```

     1. Alter ( 데이터베이스 , 테이블 등을 변경 )
     1. Drop ( 데이터베이스, 테이블 등을 삭제 )
     1. Rename ( 데이터베이스, 테이블 등의 이름 변경)
     1. Truncate (데이터베이스, 테이블 등의 데이터 비우기(삭제))
     1. Comment ( 데이터베이스, 테이블 등의 코멘트( 비고 ) 추가 )

1. DML ( Data Manipulation Language )

   - 데이터 조작

   - 명령어
     1. Insert ( 삽입 )
     1. Delete ( 삭제 )
     1. Update ( 갱신 )
     1. Select ( 조회 )
     1. merge ( 병합 )
     1. call
     1. explain plan
     1. lock table

1. DCL ( Data Control Language )
   - 데이터 제어
   - 명령어
     1. Grant 권한 부여
     1. Revoke 권한 제거
     1. Commit 트랜잭션 적용
     1. Rollback 트랜잭션 복구
