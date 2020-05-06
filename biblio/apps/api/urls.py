from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, FavoriteViewSet, PublicBooks, PublicBookView, BookFavorites

router = DefaultRouter()

router.register('books', BookViewSet, basename='books')
router.register('favorites', FavoriteViewSet, basename='favorites')


custom_urlpatterns = [
    url(r'books/(?P<book_pk>\d+)/favorites$', BookFavorites.as_view(), name='book_favorites'),
    url(r'^public/$', PublicBooks.as_view(), name='public_favorite'),
    url(r'^public/(?P<pk>\d+)/$', PublicBookView.as_view(), name='public_favorites_view')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
