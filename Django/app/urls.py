from django.urls import path
from app import views
urlpatterns = [
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("save_note/",views.save_data,name="save_note"),
    path("deleteview/<int:id>",views.deleteview,name="deleteview"),
    path("update_note/<int:id>",views.update_note,name="update_note"),
    path("update-data/<int:id>", views.updateDataView, name="updateDataView"),
]