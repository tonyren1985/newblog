from django.conf.urls import url
from .views import AboutView, CourseListView, ManageCourseListView, CreateCourseView, DeleteCourseView
from django.views.generic import TemplateView

app_name="course"

urlpatterns = [
    #url(r'about/$', TemplateView.as_view(template_name="course/about.html"),),
    url(r'about/$', AboutView.as_view(), name="about"),
    url(r'course-list/$', CourseListView.as_view(), name='course_list'),
    url(r'manage-course/$', ManageCourseListView.as_view(), name='manage_course'),
    url(r'create-course/$', CreateCourseView.as_view(), name='create_course'),
    url(r'delete-course/(?P<pk>\d+)/$', DeleteCourseView.as_view(), name='delete_course'),
]