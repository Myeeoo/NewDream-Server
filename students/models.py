import uuid
from django.db import models

# Create your models here.
# 文件位置 students/models.py
from django.db import models
from django.utils import timezone
from common.core.models import DbAuditModel
from system.models import UserInfo

class Course(models.Model):
        course_name = models.CharField(max_length=100)

        class Meta:
            verbose_name = '课程'
            verbose_name_plural = '课程'

        def __str__(self):
            return self.course_name
    
class Guardian(models.Model):
        id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=100)
        telephone = models.CharField(max_length=100)

        class Meta:
            verbose_name = '监护人信息'
            verbose_name_plural = '监护人信息'

        def __str__(self):
            return self.name
        
class Student(DbAuditModel):
    class GenderChoices(models.IntegerChoices):
        MALE = 1, "男"
        FEMALE = 2, "女"
        OTHER = 3, "其他"

    # 单选字段
    gender = models.SmallIntegerField(choices=GenderChoices, default=GenderChoices.OTHER, verbose_name="性别")

    # 外键 一对多关系
    advisor = models.ForeignKey(to=UserInfo, verbose_name="导师", on_delete=models.SET_NULL, null=True, blank=True)
    guardians = models.ForeignKey(Guardian, verbose_name="监护人", on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="student_guardian")

    # 多对多关系
    courses = models.ManyToManyField(Course, verbose_name="课程", blank=True,related_name='students')

    # 文件上传
    profile_picture = models.ImageField(verbose_name="学生头像", null=True, blank=True)

    # 普通字段
    name = models.CharField(verbose_name="姓名", max_length=100, help_text="学生姓名")
    student_id = models.CharField(verbose_name="学号", max_length=20, unique=True, help_text="学号，必须唯一")
    grade = models.CharField(verbose_name="年级", max_length=20)
    class_name = models.CharField(verbose_name="班级", max_length=20, help_text="班级名称")
    birth_date = models.DateField(verbose_name="出生日期", default=timezone.now)
    is_active = models.BooleanField(verbose_name="在校状态", default=True)

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name} ({self.student_id})"