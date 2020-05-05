from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    Favorite, Book
)
from .serializers import (
    BookSerializer, FavoritesSerializer
)


# LIST OF ALL BOOKS PER CURRENT, LOGGED-IN USER
class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Book.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        book = Book.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )
        if book:
            msg = 'Book with that title already exists!'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        book = Book.objects.get(pk=self.kwargs['pk'])
        if not request.user == book.owner:
            raise PermissionDenied('You cannot this delete this book')
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# LIST OF FAVORITE BOOKS PER CURRENT, LOGGED-IN USER
class FavoritesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Favorite.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class = FavoritesSerializer

    def create(self, request, *args, **kwargs):
        favorite = Favorite.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )
        if favorite:
            msg = 'Favorite with that title already exists!'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        favorite = Favorite.objects.get(pk=self.kwargs['pk'])
        if not request.user == favorite.owner:
            raise PermissionDenied('You cannot remove this favorite')
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# PUBLIC BOOKS LIST
class PublicBooks(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Book.objects.all().filter(is_public=True)
        return queryset

    serializer_class = BookSerializer


# PUBLIC BOOKS DETAILS
class PublicBooksDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Book.objects.all().filter(is_public=True)
        return queryset

    serializer_class = BookSerializer

