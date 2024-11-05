# 文件位置 students/utils/serializer.py

from rest_framework import serializers
from common.core.serializers import BaseModelSerializer
from common.fields.utils import input_wrapper
from students import models


class StudentSerializer(BaseModelSerializer):
    class Meta:
        model = models.Student
        # pk字段用于前端标识，包含学生的基本信息字段
        fields = [
            'pk', 'name', 'student_id', 'gender', 'grade', 'class_name', 'birth_date', 'is_active', 'advisor', 
             'guardians', 'profile_picture', 'created_time', 'updated_time'
        ]

        # 仅用于前端表格字段顺序显示，若未定义则使用fields中的顺序
        table_fields = [
            'pk', 'profile_picture', 'name', 'student_id', 'gender', 'grade', 'class_name', 'is_active'
        ]

        # 配置字段的额外参数
        extra_kwargs = {
            'pk': {'read_only': True},  # 主键字段只读
            'advisor': {
                'attrs': ['pk', 'username'], 'required': True, 'format': "{username}({pk})",
                'input_type': 'api-search-user'
            },
            'guardians': {
                'attrs': ['pk', 'username'], 'required': True, 'format': "{username}({pk})",
                'input_type': 'api-search-user'
            }
        }

    # 自定义字段，布尔类型，显示学生是否在校状态，仅可读
    is_active = input_wrapper(serializers.SerializerMethodField)(read_only=True, input_type='boolean',
                                                                 label="是否在校状态")

    def get_is_active(self, obj):
        return obj.is_active
