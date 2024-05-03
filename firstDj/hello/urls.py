from django.urls import path

from . import views # 导入views文件

urlpatterns = [
  path("", views.index, name="index"),
  path("sy", views.sy, name="sy"),
  path("zst", views.zst, name="zst"),
  path("<str:name>", views.greet, name="greet")
]