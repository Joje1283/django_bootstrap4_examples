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

## 부트스트랩 내의 예제 적용하기
* 다운받은 부트스트랩 소스파일의 
