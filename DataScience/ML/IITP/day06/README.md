# DASH 사용해보기

# Import

```python
import numpy as np
import pandas as pd

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table

from dash.dependencies import Input,Output, State
import plotly.express as px
```

- 간단 설명

  - Dash ploty?

    - Dash는 웹 분석 애플리케이션을 구축하기위한 생산적인 Python 프레임 워크다.
    - Flask , ploty.js, React.js 를 기반으로 구현되어 있다.
    - 시각화앱 최적화
    - MIT라이센스

  - import dash
    -dash를 사용하기 위해 사용
  - import dash_core_components as dcc
    - dash에서 제공하는 테그를 사용하기 위해 사용
  - import dash_bootstrap_components as dbc
    - Dash에서 bootstrap를 사용하기위해 사용
  - import dash_html_components as html
    - Dash에서 HTML을 사용하기위해 사용
  - import dash_table
    - Dash에서 테이블을 시각화하기 위해 사용
  - from dash.dependencies import Input,Output, State
    - 데코레이션 패턴을 구현할 때 Parameter을 이용하기위해 사용
  - import plotly.express as px

    - 데이터를 가져오기(예시데이터)
    - 예시코드 ( )

      - ```python
        app = dash.Dash(__name__ ,external_stylesheets=[dbc.themes.GRID])
        app.layout = html.Div([
                  app.run_server()
                  ])
        ```

    - 코드 설명

      - app = dash.Dash(**name** ,external_stylesheets=[dbc.themes.GRID])
        - app에 Dash를 실행시키는데,stylesheets를 dbc안에있는 GRID 테마를 사용하겠다.
      - app.layout = html.Div( )
        - 괄호 안에 있는 것들을 layout(시각화)으로 만들겠다
      - app.run_server()
        - app을 사용하여 서버를 실행시키겠다.

    - 예시코드 (Input,Output, State )

      - ```python
        @app.callback(
            Output('table','columns'),
            Output('table','data'),
            Input('submit-btn', 'n_clicks'),
            State("col-checklist",'value')
            State('input-text','value'),
        )
        def update_DataTable(n,n2, inputTxt,checked) :
            columns = [{'name':i,'id':i}for i in checked]
            data = df.loc[df.country.str.contains(inputTxt),checked].to_dict('r')
            return columns,data
        ```

    - 코드 설명
      - Output(id , value)
        - id 에 value를 return
      - Input(id , value)
        - id의 value를 get
      - State(id , value)
        - id의 value를 get
      - Input에서 지정한 submit-btn의 n_clicks값이 변화가 생기면 State들과 같이 값을 가져온다.
      - 가져온 값을 기준으로 update_DataTable를 실행한다
      - return값을 Output에 차례대로 반환시켜준다.
