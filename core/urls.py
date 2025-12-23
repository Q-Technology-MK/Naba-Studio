from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services_page, name="services"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("portfolio/masonry/", views.portfolio_masonry, name="portfolio_masonry"),
    path("portfolio/<slug:slug>/", views.portfolio_detail, name="portfolio_detail"),
    path("blog/", views.blog_list, name="blog"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("blog/<int:post_id>/like/", views.like_post, name="like_post"),
    path("contacts/", views.contacts, name="contacts"),
    path("pricing/", views.pricing, name="pricing"),
    path("rsvp/", views.rsvp, name="rsvp"),
    path("faq/", views.faq, name="faq"),
    path("products/<slug:slug>/", views.product_detail, name="product_detail"),
]
