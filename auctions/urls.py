from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.listing, name="create_listing"),
    path("entry/<int:id>", views.entry, name="entry"),
    path("displayWatchlist", views.displayWatchlist, name="displayWatchlist"),
    path("REMOVEwatchlist/<int:id>", views.REMOVEwatchlist, name="REMOVEwatchlist"),
    path("ADDwatchlist/<int:id>", views.ADDwatchlist, name="ADDwatchlist"),
    path("placeBid/<int:id>", views.placeBid, name="placeBid"),
    path("closeListing/<int:id>", views.closeListing, name="closeListing"),
    path("addComment/<int:id>", views.addComment, name="addComment"),
    path("selectCategory", views.selectCategory, name="selectCategory")



]
