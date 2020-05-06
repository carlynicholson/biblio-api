from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book, Favorite
from .serializers import BookSerializer, FavoritesSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Book.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        book = Book.objects.filter(title=request.data.get('title'), owner=request.user)
        if book:
            msg = 'Book with that title already exists'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        book = Book.objects.get(pk=self.kwargs["pk"])
        if not request.user == book.owner:
            raise PermissionDenied("You cannot delete this book")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookFavorites(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.kwargs.get('book_pk'):
            book = Book.objects.get(pk=self.kwargs["book_pk"])
            queryset = Favorite.objects.filter(owner=self.request.user, book=book)
        return queryset

    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoriteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Book.objects.all().filter(owner=self.request.user, is_favorite=True)
        return queryset

    serializer_class = FavoritesSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied("Only logged in users with accounts can create favorites")
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        favorite = Favorite.objects.get(pk=self.kwargs["pk"])
        if not request.user == favorite.owner:
            raise PermissionDenied("You cannot delete this favorite")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        favorite = Favorite.objects.get(pk=self.kwargs["pk"])
        if not request.user == favorite.owner:
            raise PermissionDenied("Login to change this Favorite")
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicBooks(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Book.objects.all().filter(is_public=True)
        return queryset
    serializer_class = BookSerializer


class PublicBookView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Book.objects.all().filter(is_public=True)
        return queryset

    serializer_class = BookSerializer

