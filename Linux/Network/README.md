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
1. ## shell-script 생성하기
   ```shell
   !/bin/bash
   nohup jupyter notebook --ip=192.168.56.102 --NotebookApp.token='' --NotebookApp.password='' &
   ```
   - jupyter notebook 을 background로 실행
   - 접속이 안된다면 아마 firewall이 차단해서 그럴 수 있다.
     - sudo systemctl stop firewalld
       - firewalld 종료
