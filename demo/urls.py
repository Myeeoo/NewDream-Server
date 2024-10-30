# 文件位置 demo/urls.py

from rest_framework.routers import SimpleRouter

from demo.views import BookViewSet

router = SimpleRouter(False)  # 设置为 False ,为了去掉url后面的斜线

router.register('book', BookViewSet, basename='book')

urlpatterns = [
]
urlpatterns += router.urls