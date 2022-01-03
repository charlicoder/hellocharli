from django.db.models import fields
from django.db.models.query_utils import Q
import graphene
from graphene_django import DjangoObjectType
from .models import Author, Publisher, Book, Store


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id', 'name', 'age')


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)

    def resolve_all_authors(root, info):
        return Author.objects.all()


schema = graphene.Schema(query=Query)