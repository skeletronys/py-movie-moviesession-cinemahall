from django.db.models import QuerySet

from db.models import Genre, Movie, Actor


def get_movies(
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        )

    if actors_ids:
        queryset = queryset.filter(
            actors__id__in=actors_ids
        )

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(
            Genre.objects.filter(id__in=genres_ids)
        )
    if actors_ids:
        movie.actors.set(
            Actor.objects.filter(id__in=actors_ids)
        )
