from rest_framework import generics, permissions, mixins,\
    status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
# from rest_framework_simplejwt.authentication import Authen

from .models import Movie, Vote, MovieImage
from .serializers import MoviesSerializer, VoteSerializer


class MoviesListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser]

    def perform_create(self, serializer, *args, **kwargs):
        movie = serializer.save(
            created_by=self.request.user
        )

        print(movie.id)

        image = self.request.FILES.get('image')

        if image:
            MovieImage.objects.create(
                movie=movie,
                image=image
            )

        # MovieImage.objects.create(
        #     movie=)


class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoviesSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        movie_id = self.kwargs.get('movie_id')
        movie = Movie.objects.filter(
            id=movie_id
        )[0]

        print(movie if movie else 'movies is none')

        if not movie:
            print(movie)
            raise ValidationError(
                'Movie not found'
            )

        return movie

    # def get_queryset(self):
    #     movie_id = self.kwargs.get('movie_id')
    #     movies = Movie.objects.filter(
    #         id=movie_id
    #     )

    #     print(movies if movies else 'movies is none')

    #     if not movies:
    #         print(movies)
    #         raise ValidationError(
    #             'Movie not found'
    #         )

    #     return movies

    def delete(self, request, *args, **kwargs):
        if not self.get_object():
            raise ValidationError(
                'Movie is not exist'
            )

        object = self.get_object()
        user = self.request.user

        if object.created_by is user or user.is_staff:
            object.delete()

            return Response(
                status=status.HTTP_204_NO_CONTENT
            )

        else:
            raise ValidationError(
                'You have not permissions to delete this post'
            )

    def put(self, request, *args, **kwargs):
        if not self.get_object():
            raise ValidationError(
                'Movie is not exist'
            )

        object = self.get_object()
        user = self.request.user
        print(user)

        if object.created_by == user or user.is_staff:
            return self.partial_update(
                request, *args, **kwargs
            )

        else:
            raise ValidationError(
                'You have not permission to edit this post'
            )


class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        movie_id = self.kwargs.get('movie_id')
        movie = Movie.objects.filter(
            id=movie_id
        )[0]

        return Vote.objects.filter(
            voter=user, movie=movie
        )

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError(
                'You have got already voted to this post'
            )

        serializer.save(
            voter=self.request.user,
            movie=Movie.objects.filter(
                id=self.kwargs.get('movie_id')
            )[0]
        )

    def delete(self, request, *args, **kwargs):
        if not self.get_queryset().exists():
            raise ValidationError(
                'You have not voted to this post'
            )

        self.get_queryset().delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
