# 네트워크 설정

## 리눅스 내부에서 설정

1. `root`계정으로 접속
1. `/etc/sysconfig/network-scripts` 디렉토리로 들어간다
   - cd /etc/sysconfig/network-scripts
1. vi ifcfg-enp0s3 및 vi ifcfg-enp0s8
   - onboot =no를 yes로 변경
1. 변경 후 Reboot명령어를 통해 재시작 해준다

1. net-tools, curl,wget등을 설치해준다.
   - yum install net-tools -y
   - yum install curl -y
   - yum install wget -y

## vsftpd 설치

1. 설치 확인
   - `ps -ax | grep vsftpd`
   - `yum list installed |grep vsftpd`
     - 무반응이면 설치되지 않은 것
1. 설치

   - `yum install vsftpd - y`

1. 시스템 설정
   - systemctl
     - 옵션
       - start
       - restart
       - status
       - stop

## JAVA설치하기

1. 확인 (설치 가능 자바 jdk 확인)
   - yum list java\*jdk-devel
1. 자바 설치 (64bit, version = 1.8.0)
   - yum install java-1.8.0-openjdk-devel.x86_64

## guru 권한 변경

1. root 계정으로 접속
1. etc안에있는 sudoers에 들어가 guru ALL=(ALL)을 추가해준다
   1. `cd /etc/`
   1. `chmod 640 sudoers`
      - sudoers가 읽기 전용임
   1. `vi sudoers`
      - guru ALL=(ALL) 삽입( 아랫쪽에 root가 동일하게 있는곳이 있음)
   1. `chmod u-w sudoers`
      - 쓰기권한 없애기

## 아나콘다 설치

- 설치하고자하는 경로로 이동하여 wget을 이용하여 설치
- wget (아나콘다 다운로드 url)
  - `wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh`
- 설치

  1. chmode 764 `파일명`
     - `chmod 764 Anaconda3-2021.05-Linux-x86_64.sh`
  1. 실행
     - `./Anaconda3-2021.05-Linux-x86_64.sh`
  1. 변경된 환경설정 적용

     - source .bashrc
     - 만약 경로 설정 안했다면
     - `PATH=$PATH:/home/guru/anaconda3/bin` 를 .bashrc에 추가해줌

  1. 확인
     - conda

## 쥬피터 실행

1. shell-script & workspace 디렉토리 생성
   - `mkdir sh`
   - `mkdir workspace`
1. shell-script 생성하기
   ```shell
   !/bin/bash
   nohup jupyter notebook --ip=192.168.56.102 --NotebookApp.token='' --NotebookApp.password='' &
   ```
   - jupyter notebook 을 background로 실행
   - 접속이 안된다면 아마 firewall이 차단해서 그럴 수 있다.
     - sudo systemctl stop firewalld
       - firewalld 종료

## mysql설치

1. mysql-server 설치
   - `yum install mysql-server `
1. mysql 실행
   - `systemctl start mysqld.service`
1. 테스트 ( sakila 가져와서 확인해보기)

   1. tar 설치
      - `yum install tar`
   1. 다운로드 및 압축풀기

      - wget sakila주소
      - tar zxvf sakila-db.tar.gz

   1. mysql 접속
      1. db에 저장할 데이터가 있는곳으로 이동
         - cd sakila-db
      1. 접속
         - mysql -u root
           - 관리자(root계정)로 접속
      1. 쿼리문 ( 설치한 sql 저장 )
         - source sakila-schema.sql;
         - source sakila-data.sql;
   1. mysql user생성 및 권한부여
      - `createuser 유저명 identified by '비밀번호'`
      - `grant all privileges on *.* to '유저명'@'%';`
        - 유저에게 모든권한 주기
        - 즉 root계정 대신 사용할 것임
      - `flush privileges`
        - 새로고침, 즉 현재 부여한 권한 즉시적용

# jupyter에서 mysql연동

1. 라이브러리 설치

   - ```python
      !pip install sqlcalchemyu
      !pip install pymysql
     ```

1. 연결

```python
from sqlalchemy import create_engine,text
import numpy as np
import pandas as pd
import pymysql

pymysql.install_as_MySQLdb()
# engine = create_engine("mysql://사용자명:비밀번호@IP/sakila")s
engine = create_engine("mysql://bapa:tmdgus12@192.168.56.102/sakila")
con = engine.connect()
```

1. 간단 조회 ( Select)

```python
stmt = '''select * from information_schema.columns'''
pd.read_sql(stmt,con)
```

1. 간단 테이블 생성 (Create Table)

```python
# 테이블 생성
create_sql = '''create table test(id varchar(100),name varchar(200))'''
stmt = text(create_sql)
con.execute(stmt)
```

1. 간단 삽입 (Insert Values)

```python
# 테이블에 값 삽입
# 임의의 값을 가진 DF 생성
df=  pd.DataFrame({'id':np.arange(10),'name':[i for i in  'abcdefghij'.upper()]})

insert_sql ='''insert into test(id,name) value(:id,:name)'''
stmt = text(insert_sql)
# 값을 records로 저장
data = df.to_dict('r')

for datum in data:
    con.execute(stmt,**datum)
```

1. 간단 삭제 (Drop table)

```python
stmt = text('''drop table test''')
con.execute(stmt)
```
