from django.urls import path
from . import views

urlpatterns = [
    path('attraction/', views.Attractions, name ='attractions'),
    path('blogs/', views.Blogs, name ='blogs'),
    #for class based View 
    path('destinationpac/', views.DestinationPackage.as_view()),
    #for temp based View
    path('tempblogview/', views.DestinationPackageTemplateView.as_view()),
    #create url without creating class in views.py using TemplateView 
    #path('tempattraction/', views.as_view(template_name = "attractions/attraction.html")),

    #RedirectView class. Need to use as_view() since it's class based
    #differnt url but page is same
    path("redirectblogs/", views.RedirectView.as_view(url = '/at/tempblogview')),

]