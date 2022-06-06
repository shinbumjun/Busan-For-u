from django.db import models
from django.urls import reverse

# 블로그 글 작성하기 위해서 모델 작성

# 글의 분류(일상, 유머, 정보)
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.(ex:일상)")

    def __str__(self):
        return self.name # admin에서 추가함 (맛집, 일상, 여행지, 부산...)

# 블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200) # 제목
    title_image = models.ImageField(blank=True) # 대표 이미지 (빈값도 가능)
    content = models.TextField() # 글의 내용
    createDate = models.DateTimeField(auto_now_add=True) # 작성일 (작성일 자동으로 입력)
    updateDate = models.DateTimeField(auto_now_add=True) # 수정일 (수정일 자동으로 입력)

    # 하나의 글을 여러가지의 분류에 해당될 수 있다.(ex:정보, 유머), 
    # 하나의 분류에는 여러가지 글이 포함될 수 있죠.(정보 카테고리에 글 10개)
    # 다 대 다
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요.")

    # 자기 자신을 글의 제목으로 표현
    def __str__(self):
        return self.title

    # 1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    # 첫번째 글 미리보기 300자까지만 보여지므로 
    def is_content_more300(self):
        return len(self.content) > 300

    # 300자만큼 잘라서 받느것
    def get_content_under300(self):
        return self.content[:300]