# 文件位置 students/urls.py

from rest_framework.routers import SimpleRouter
from students.views import StudentViewSet

router = SimpleRouter(trailing_slash=False)  # trailing_slash=False 以去掉 URL 后面的斜线

# # 注册书籍管理的路由
# router.register('book', BookViewSet, basename='book')

# 注册学生管理的路由
router.register('student', StudentViewSet, basename='student')

urlpatterns = [
]

# 将 router 中生成的 URL 添加到 urlpatterns
urlpatterns += router.urls
