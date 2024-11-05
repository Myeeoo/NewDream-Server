from django.shortcuts import render

# Create your views here.
# 文件位置 students/views.py

from django_filters import rest_framework as filters
from common.core.filter import BaseFilterSet
from common.core.modelset import BaseModelSet, ImportExportDataAction
from common.core.pagination import DynamicPageNumber
from common.utils import get_logger
from students.models import Student
from students.utils.serializer import StudentSerializer 

logger = get_logger(__name__)


class StudentFilter(BaseFilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    student_id = filters.CharFilter(field_name='student_id', lookup_expr='icontains')
    grade = filters.CharFilter(field_name='grade', lookup_expr='icontains')
    class_name = filters.CharFilter(field_name='class_name', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['name', 'student_id', 'gender', 'grade', 'class_name', 'is_active', 'birth_date', 
                  'created_time']  # fields用于前端自动生成的搜索表单


class StudentViewSet(BaseModelSet, ImportExportDataAction):
    """学生信息管理"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    ordering_fields = ['created_time']
    filterset_class = StudentFilter
    pagination_class = DynamicPageNumber(1000)  # 表示最大分页数据1000条，如果注释，则默认最大100条数据
