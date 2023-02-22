from rest_framework import serializers
from .models import Movie, Vote, MovieImage


class MoviesSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_by = serializers.ReadOnlyField(
        source='created_by.username'
    )
    votes = serializers.SerializerMethodField(
        'get_votes'
    )
    voters = serializers.SerializerMethodField(
        'get_voters'
    )
    image = serializers.SerializerMethodField(
        'get_image'
    )

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'description',
            'image', 'year', 'created_by',
            'votes', 'voters'
        ]

    def get_votes(self, movie):
        return movie.get_votes()

    def get_voters(self, movie):
        return movie.get_voters()

    def get_image(self, movie):
        try:
            image = MovieImage.objects.filter(
                movie=movie
            )[0]
            print(image.path())

            return image.path()

        except:
            return


class VoteSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    voter = serializers.ReadOnlyField(
        source='voter.username'
    )
    movie = serializers.ReadOnlyField(
        source='movie.title'
    )

    class Meta:
        model = Vote
        fields = ['id', 'voter', 'movie']
