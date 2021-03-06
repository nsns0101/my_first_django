from django.db import models

# # # 선거 모델
# class Candidate(models.Model):      #모델 등록을 위해 models.Model을 상속받아야함
#     name = models.CharField(max_length=10)  #이름 문자의 최대길이는 10
#     introduction = models.TextField()       #정보 문자열의 길이 제한이 없음
#     area = models.CharField(max_length=15)  #국적
#     party_number = models.IntegerField(default=1)  #기호 default값은 숫자 1


#     def __str__(self):      #python에서 object를 표현하는 문자열을 정의할 때는 __str__ 메서드를 오버라이딩함
#         return self.name    #Candidate의 name로 이름을 표현

# #여론조사 모델
# class Poll(models.Model):
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     area = models.CharField(max_length = 15)

#     def __str__(self):
#         return self.area

# #
# class Choice(models.Model):
#     poll = models.ForeignKey(Poll, on_delete = models.CASCADE)              #Poll 모델의 id를 이용
#     candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)    #후보이름
#     votes = models.IntegerField(default = 0)
