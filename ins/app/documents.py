from django_elasticsearch_dsl import DocType, Index, fields
from django.contrib.auth import get_user_model
from .models import Ins, Tag

User = get_user_model()


user = Index('user')
user.settings(
    number_of_shards=1,
    number_of_replicas=0
)

ins = Index('ins')
ins.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@user.doc_type
class UserDocument(DocType):

    class Meta:
        model = User
        fields = ['name', 'brief']


@ins.doc_type
class InsDocument(DocType):
    owner = fields.ObjectField(properties={
        'name': fields.StringField()
    })
    tags = fields.NestedField(properties={
        'name': fields.StringField()
    })

    class Meta:
        model = Ins
        fields = ['brief', ]

    def get_queryset(self):
        return super(InsDocument, self).get_queryset().select_related(
            'owner'
        )

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, User):
            return related_instance.post_ins.all()
        elif isinstance(related_instance, Tag):
            return related_instance.tag_set.all()


# test
# def search(name):
#     from elasticsearch import Elasticsearch
#     from elasticsearch_dsl import Search
#     client = Elasticsearch()
#     my_search = Search(using=client)
#     query = my_search.query("match", name=name)
#     response = query.execute()
#     return response

