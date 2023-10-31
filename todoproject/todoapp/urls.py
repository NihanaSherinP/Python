from . import views
from django.urls import path



urlpatterns = [
    path('',views.task,name='task'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbhome/',views.Tasklistview.as_view(),name='cbhome'),
    path('cdtv/<int:pk>/',views.Taskdetailview.as_view(),name='cdtv'),
    path('cbup/<int:pk>/',views.Updateview.as_view(),name='cbup'),
    path('cbdel/<int:pk>/',views.Deleteview.as_view(), name='cbdel')

]