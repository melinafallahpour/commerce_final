from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("categories/", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("create/", views.create, name="create"),
    path("submit/",views.submit,name="submit"),
    path("listings/<int:id>",views.listingpage,name="listingpage"),
    path("bidsubmit/<int:listingid>",views.bidsubmit,name="bidsubmit"),
    path("commentsubmit/<int:listingid>",views.commentsubmit,name="commentsubmit"),
    path("addwatchlist/<int:listingid>",views.addwatchlist,name="addwatchlist"),
    path("removewatchlist/<int:listingid>",views.removewatchlist,name="removewatchlist"),
    path("watchlist/<str:username>",views.watchlistpage,name="watchlistpage"),
    path("closebid/<int:listingid>",views.closebid,name="closebid"),
    path("mywinnings/",views.mywinnings,name="mywinnings"),
    path("delete/<int:listingid>", views.delete,name='delete')
]
urlpatterns += staticfiles_urlpatterns()