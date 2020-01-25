# django_bootstrap4_examples
bootstrap4를 django에 적용하고, 몇개의 bootstrap예제를 출력한다.


## django에 부트스트랩 적용하기
* 부트스트랩 사이트(https://getbootstrap.com/docs/4.4/getting-started/download/)에서 Source files를 다운로드 한다.(여기서는 4.4.1버전을 사용함)
* 장고의 프로젝트 루트 폴더에 bootstrap4 디렉토리를 생성한다
* 다운받은 부트스트랩 소스파일에서 Downloads\bootstrap-4.4.1\dist 경로에 js, css폴더가 있다. 이 두 폴더를 좀전에 생성한 bootstrap4 디렉토리에 복사한다.
* 이제 html에서 불러와서 사용할 수 있다.  


index.html
~~~
<head>
  <title>example page</title>
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
</head>
...

<body>
...
  <script src="{% static 'js/bootstrap.bundle.js' %}"></script>
  <script src="{% static 'js/bootstrap.js' %}"></script>
</body>
~~~

## 부트스트랩 내의 예제 적용하기 (https://getbootstrap.com/docs/4.4/examples/)
* static디렉토리에 bootstrap_site_examples디렉토리를 생성한다. 이 디렉토리에 부트스트랩 기본예제 관련 정적파일들이 추가된다.
* 다운받은 부트스트랩 소스파일의 C:\bootstrap-4.4.1\site\docs\4.4 경로의 assets디렉토리를 static디렉토리에 추가한다.
* C:\Downloads\bootstrap-4.4.1\site\docs\4.4\examples 폴더 내에 예제별 디렉토리가 있다. 각 예제의 디렉토리에 있는 css 혹은 js파일을 static/bootstrap_site_examples디렉토리에 예제별 디렉토리 이름을 똑같이 생성해서 추가한다. (예를들어 checkout디렉토리에 있는 form-validation.css와 form-validation.js는 장고 프로젝트의 static 디렉토리 이하 checkout디렉토리에 복사하였다.)
* 각 예제 디렉토리(C:\Downloads\bootstrap-4.4.1\site\docs\4.4\examples)에 있는 html파일들은 장고 프로젝트의 templates에 추가하였다.
* 장고 프로젝트의 html파일들이 정적파일들을 참고할 수 있도록 html코드를 수정함.
