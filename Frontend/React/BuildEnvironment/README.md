## 설치하기!

### nvm (Node Version Manager )

#### 사용이유

```
Node.js는 여러가지 버전을 가지고 있습니다. 저희가 개발을 할 때 예를 들어 `14.17.0` 버전을 사용하고 있습니다.
다른 사람과 협업을 할 때 `12.22.1` 버전으로 할 수 있습니다. 그때마다 다시 설치하기 번거로운 경우가 생길 수 있으니,
NVM을 이용하여 즉각적으로 변경시켜줄 수 있는 형상관리 프로그램이기 때문에 사용을 합니다.
```

#### 설치하기

1.  exe파일 다운로드
    1.  [https://github.com/coreybutler/nvm-windows/releases](https://github.com/coreybutler/nvm-windows/releases)
    2.  위 사이트를 들어가서 `nvm-setup.zip` 파일을 다운받아줍니다.
    3.  다운받은 파일을 압축을 풀고, `nvm-setup.exe` 파일을 실행시켜 설치해줍니다.
2.  설치 확인
    1.  `CMD`를 켜줍니다.
    2.  콘솔창에 `nvm ls` 혹은 `nvm list`를 쳐줍니다.
        - 최초 설치기 때문에 아무것도 나오지 않을 것 입니다. 에러가 안뜨면 Good!
3.  Node 설치
    1.  nvm install `설치하고자하는 버전`을 쳐줍니다.
        - 예시 : `nvm install 14.17.0` or `nvm install v14.17.0`
4.  Node 사용하기.
    1.  nvm use `사용하고자하는 버전`을 쳐줍니다.
        - 당연히 위에 설치한 버전을 치셔야합니다 ㅎㅎ
          - `nvm list` 를 통해 설치된 버전을 확인해보세요.
        - 예시 : `nvm list 14.17.0` or `nvm list v14.17.0`  
          `위와 같이 하시면`nvm 설치`및`Node\` 적용 완료입니다.

---

### Parcel ( 번들러 )

| 저는 vs코드로 진행하였습니다.

#### 사용 이유

- js , css ,html등 여러 파일을 한번에 압축 및 배포할 수 있게 만들어 주는 번들러(Bundler) 입니다.
  - 번들러 ( Bundler ) : 사용자의 코드와 종속성을 하나의 자바스크립트 파일에 통합하는 도구입니다.
  - 번들러 ( Bundler )를 이용하여 `JSX` 를 구현할 수 있습니다.

#### 설치

1.  디렉토리생성
    - 원하시는 디렉토리로 vscode를 열어줍니다 ( 빈 디렉토리 권장 )
2.  설치
    1.  `` CTRL+`  ``를 누른다.
        - 커맨트창 띄우기
    2.  `npm init -y`를 치고 엔터!
        - 최소실행시 실행해 주시고, 실행해 주시면 `package.json` 파일이 생성됩니다.
          - y는 설치중 y/n 를 눌러야하는데 모든걸 y로 누른다는 의미
    3.  `npm i -D parcel-bundler`를 치고 엔터!
        - parcel-bundler를 설치한다는 의미! 다른 것을 설치하고 싶으면 이부분만 변경하면됩니다.
          - `i`는 `install`을 의미하고, install이라고 쳐도 무방합니다.
          - `D`는 developer 버전으로 설치한다는 의미입니다. `G`를 넣으면 글로벌 버전!
3.  설치 확인
    1.  index.html
        - 기본형식으로 생성해줍니다. ( 간단히 hello html 과같은 것을 출력 해줄 수 있으면 좋겠네요 )
    2.  `js` 디렉토리를 생성하고 `main.js`파일을 하나 생성해줍니다.
        - `main.js` 파일에 `console.log("hello js");` 를 작성해줍니다.
4.  실행
    1.  `package.json` 안의 `scripts` 안에 `"dev": "parcel index.html"`를 추가해주기
        - ```javascript
          "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1",
            "dev": "parcel index.html",
            "build": " parcel build index.html"
          },
          ```
    2.  `npm run dev` 를 커맨드 라인에 작성하여 실행시켜줍니다.
        - 출력된 경로 `http://localhost:1234`를 `cntl`을 누르고 클릭 혹은 url창에 복사 붙여넣기를 하여 켜줍니다.
          - 그렇게 되면, html에 작성하신 것이 출력될 것 입니다.
          - F12를 눌러 `console` 을 보시면 `hello js`가 출력 되는 것을 볼 수 있습니다.

#### 추가적으로 설치한 plugin

1.  parcel-plugin-static-files-copy
    1.  용도
        - 정적 파일을 dist와 연결시켜주는 역할
    2.  설치
        - `npm i -D parcel-plugin-static-files-copy` or `npm install -D parcel-plugin-static-files-copy`
    3.  변경할 코드
        - package.json 파일에 아래 코드 추가
        - `"staticFiles": { "staticPath": "static" },`
    4.  생성할 디렉토리
        - `root 디렉토리` 아래에 `static` 디렉토리 생성
    5.  사용해보기 ( 대표적인 url 아이콘 생성하기)
        1.  [https://www.icoconverter.com/](https://www.icoconverter.com/) 에 들어가서 favicon.ico 생성
            - 제가 한 설정은 Sizes : 32 pixels , Bit depth :32bits 로 만들었습니다.
        2.  생성한 favicon.ico를 static에 삽입.
        3.  서버를 실행시키면 아이콘이 생겨있습니다.

---

### reset.css ( CDN )

#### 사용 이유

- 브라우저마다 각기 다른 default 스타일이 정해져있습니다.이것을 초기화 시켜 주는 역할
  - 초기화 시켜줌으로써 서로 다른 브라우저간 동일한 스타일을 적용할 수 있게 만들어줌.

### 설치

1.  [_React.css_](https://www.jsdelivr.com/package/npm/reset-css) 에 들어가서 /npm/reset-css@5.0.1/reset.min.css의 html주소를 복사한다.
    - ```
      link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css"/
      ```
    - 왠지 모르게 테그가 안 들어가지네요 .. 앞뒤로 <,> 를 넣으세요..
2.  복사한 태그를 html에 삽입해 주세요.
    - 귀찮으면 위 link를 복사하세요
    - scss와 같이 넣고 싶은데, 왜인지 모르게 html코드가 안 들어가지네요 ... 해결방법을 아시면 알려주세요 ㅠㅠ
3.  `./scss/main.scss` 이 경로에 main.scss파일을 생성해 주세요

    - 아래 같단 예시입니다.

      - ```scss
        // 변수명 : 값
        $color--black: #000;
        $color--white: #fff;

        body {
          background-color: $color--black;
          h1 {
            color: $color--white;
          }
        }
        ```

        추가 설치 패키지 `PostCss`

4.  autoprefixer
    1.  용도
        - `'Can I Use'` 에 등록되어 있는 CSS 속성의 `vendor-prefix`를 접속하는 브라우저에 따라 자동으로 붙여준다
          - `vender-prefix` : CSS 권고안 포함되지 않거나, 포함되어 있지만 아직 완벽하게 제정된 상태가 아닌 기능을 사용할 수 있게 만들어준다.
    2.  설치
        - `npm i -D postcss_autoprefixer` or `npm i -D postcss_autoprefixer`
        - `npm i -D autoprefixer@9` or `npm install -D autoprefixer@9`
    3.  추가 코드
        - browserslist : 현재 NPM 프로젝트에서 지원할 브라우저의 범위를 명시하는 용도입니다.
          - 이 명시를 Autoprefixer 패키지에서 활용됩니다.
        - package.json에 아래 코드 추가
          - ```javascript
            "browserslist": [
               ">2%",
               "last 2 versions"
            ]
            ```
        - `.postcssrc.js` 파일 생성 후 아래 코드 삽입.
          - ```javascript
            module.exports = {
              plugins: [require("autoprefixer")],
            };
            ```
    4.  설치끝
        - 이제 `display : flex;` 와 같은 것을 사용 할 수 있습니다!

### Babel ( transpile )

#### 사용이유

- 브라우저마다 지원하는 ECMAScript가 다릅니다.
  - 개발자는 본인이 편한 버전의 문법을 이용해 ( ES6, ES7.. 등)개발을 하고, Babael을 통하여 `변환 & 컴파일`을 해줍니다.설치

1.  커맨드 창에 `npm i -D @babel/core @babel/preset-env` or `npm install -D @babel/core @babel/preset-env`을 입력해줍니다.
2.  .`babelrc.js`파일을 생성하고 아래 코드를 삽입해줍니다.

    - ```javascript
      module.exports = {
        presets: ["@babel/preset-env"],
      };
      ```

      추가 설치 패키지 `plugin-transform-runtime`

- 라이브러리에서 사용하는 API들을 래핑
  - babel만으로 부족한 최신 스크립트를 추가 플러그인을 설치하여 지원하게 만들어줍니다.설치

1.  `npm i -D @babel/plugin-transform-runtime` or `npm i -D @babel/plugin-transform-runtime`을 입력해줍니다.
2.  `babelrc.js`파일을 생성하고 아래 코드를 삽입해줍니다.
    - ```javascript
      module.exports = {
        presets: ["@babel/preset-env"],
        plugins: [["@babel/plugin-transform-runtime"]],
      };
      ```
