from datetime import datetime
from uuid import uuid4
from os import path

from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User


class Movie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        unique=True,
        editable=False,
        blank=False
    )
    title = models.CharField(
        max_length=100,
        unique=False,
        blank=False
    )
    description = models.CharField(
        max_length=1024,
        blank=True,
        null=True
    )
    year = models.IntegerField(
        blank=True,
        null=True
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return f'{self.title}, {self.year}'

    @classmethod
    def validate_year(cls, year: int):
        if year > datetime.now().year:
            return False

        return True

    def get_voters(self):
        votes = Vote.objects.filter(
            movie=self
        )
        voters_obj = [vote.voter for vote in votes]
        voters = list()

        for voter in voters_obj:
            voter_obj = {
                'id': voter.id,
                'username': voter.username,
                'first_name': voter.first_name,
                'last_name': voter.last_name
            }

            voters.append(voter_obj)

        return voters

    def get_votes(self):
        return Vote.objects.filter(
            movie=self
        ).count()


class MovieImage(models.Model):
    movie = models.ForeignKey(
        'movies.Movie',
        on_delete=models.CASCADE,
        null=True
    )
    image = models.ImageField(
        blank=False,
        upload_to='movies_images'
    )

    def __str__(self):
        return f'Image to {self.movie.title}'

    def path(self):
        return f'/media/movies_images/{path.basename(self.image.name)}'


@receiver(models.signals.post_delete, sender=MovieImage)
def delete_movie_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)


class Vote(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        unique=True
    )
    voter = models.ForeignKey(
        User, on_delete=models.PROTECT
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE
    )
