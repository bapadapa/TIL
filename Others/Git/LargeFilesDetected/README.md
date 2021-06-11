```remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
remote: error: File DataSicence/ML/IITP/data/us_new_born_2million.csv is 110.08 MB; this exceeds GitHub's file sizTo https://github.com/bapadapa/TIL.git
 ! [remote rejected]   master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://github.com/bapadapa/TIL.git'
```

- git에 올리려는 파일이 100mb이상인 경우!
- 위 에러의 경우 `DataSicence/ML/IITP/data/us_new_born_2million.csv`가 `110.08 MB`이기 때문에 발생!

- 해결방법

  1. 파일을 삭제 혹은 gitignore을 해준다!

  - csv파일이 문제였으니 아래 코드를 .gitignore파일에 넣어줌.
    - ```
        *.csv
        *.xlsx
      ```

  2. 캐시를 지워준다!

     - git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch DataSicence/ML/IITP/data/us_new_born_2million.csv'
     - git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch 파일명'

  3. 현재 레포지토리와 깃 레포지토리랑 다르다 (히스토리가 꼬여있음) 아래 명령어 사용

     - git pull origin master --allow-unrelated-histories

  4. 다시 push를 해준다!

- 에러 속에 에러!
  - 3번 단계에서 저렇게 명령어를 치라고 해서 쳤는데 `warning: Cannot merge binary files`에러가 뜸..
    - 그래서 `git push --force origin master` 로 강제 push를 해주니 성공함. .ㅎ
