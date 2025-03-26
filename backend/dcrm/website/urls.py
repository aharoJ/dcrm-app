from django.urls import path
from . import views

urlpatterns = [
    # def path( route: str, view: IncludedURLConf, name: str = ... ) -- pattern 
    path("", views.home, name="home"),
    # path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("record/<int:pk>", views.customer_record, name="record"),
    path("delete_record/<int:pk>", views.delete_customer_record, name="delete_customer_record"),
    path("add/", views.add_customer_record, name="add_customer_record"),
    path("update/<int:pk>", views.update_customer_record, name="update_customer_record"),
# localhost:8000/2
]

        
        