from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('about-us/',views.about,name="about"),
    path('consulting/',views.consulting,name="consulting"),
    path('learning/',views.learning,name="learning"),
    path('our-works/',views.our_works,name="our_works"),
    path('blog/',views.blogs,name="blogs"),
    path('blog-details/<slug:blog_slug>',views.blog_details,name="blog_details"),
    path('learning/lego-serious-play/',views.lego,name="lego_serious_play"),
    path('learning/design-thinking-bootcamps/',views.design_thinking,name="design_thinking"),
    path('learning/future-thinking-bootcamps/',views.future_thinking,name="future_thinking"),
    path('workshop-details/<slug:workshop_slug>',views.workshop_details,name="workshop_details"),
    path('workshop-details/service-design/',views.service_design,name="service_design"),
    path('business-advisory/',views.business_advisory,name="business_advisory"),
    path('new-venture-development/',views.new_venture_development,name="new_venture_development")
]