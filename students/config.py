# 文件位置 demo/config.py
from django.urls import path, include

# 路由配置，当添加新的 APP 时，可以在这里自动注入路由到主服务
URLPATTERNS = [
    path('api/demo/', include('demo.urls')),  # demo 应用的路由
    path('api/student/', include('students.urls')),  # student 应用的路由
]

# 请求白名单，支持正则表达式，可以配置允许无权限访问的 URL
PERMISSION_WHITE_REURL = [
    r'^/api/demo/public/',  # 示例：允许访问 demo 的公共接口
    r'^/api/students/public/',  # 示例：允许访问 student 的公共接口
]
