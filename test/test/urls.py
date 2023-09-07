from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(
        next_page='/'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', CreateView.as_view(
             template_name='registration/reg.html',
             form_class=UserCreationForm,
             success_url=reverse_lazy('question:set_list'),
            ), name='registration'),
    path('', include('question.urls')),
]
