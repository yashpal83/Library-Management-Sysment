from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('signup', views.SignupView.as_view(), name = "signup"),
    path('login', views.handlelogin, name = "handlelogin"),
    path('logout', views.handlelogout, name = "handlelogout"),
    path('adminpage', views.adminpage, name = "adminpage"),
    path('addbook', views.addbook, name = "addbook"),
    path('update/<int:sno>', views.update, name = "update"),
    path('delete/<int:sno>', views.delete, name = "delete"),
    path('studentpage', views.studentpage, name = 'studentpage'),
]