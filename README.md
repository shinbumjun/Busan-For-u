# Busan-For-u
### django 프로젝트
홈, 로그인, 글 작성(로그인해야 작성 가능)

- pip install virtualenv -> 파이썬 가상환경 설치
- virtualenv myvenv -> 이름
- myvenv\scripts\activate -> 가상환경 활성화
- pip install django
- django-admin startproject mywebsite -> 프로젝트
- cd mywebsite
- python manage.py startapp blog -> 앱
- code . -> 실행

- pip install Pillow -> 이미지 설치
- python manage.py makemigrations -> 모델 생성
- python manage.py migrate -> 설계도를 통해서 DB에 적용
- python manage.py createsuperuser -> 관리자 생성(관리자 id를 만드는 작업)
- python manage.py runserver -> 개발서버 확인
- pip install django-widget-tweaks -> 폼 꾸미기 모듈 설치

1. [확인 사이트] http://127.0.0.1:8000/blog/
2. [관리자 사이트] http://127.0.0.1:8000/admin/
