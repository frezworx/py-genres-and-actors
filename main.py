import init_django_orm  # noqa: F401

from db.models import Genre, Actor
from django.db.models import QuerySet, Model

genres = [
    "Western",
    "Action",
    "Dramma",
]

actors = [
    ("George", "Klooney"),
    ("Kianu", "Reaves"),
    ("Scarlett", "Keegan"),
    ("Will", "Smith"),
    ("Jaden", "Smith"),
    ("Scarlett", "Johansson"),
]


def main() -> QuerySet:
    for genere in genres:
        Genre.objects.create(name=genere)

    for elem_first, elem_second in actors:
        Actor.objects.create(
            first_name=elem_first,
            last_name=elem_second
        )
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
