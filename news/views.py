from rest_framework.response import Response
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from news.models import New
from simpleblog.serializers import NewSerializerList, NewSerializerDetail, NewSerializerEdit


class NewViewSets(ModelViewSet):
    serializer_class = NewSerializerEdit
    queryset = New.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = NewSerializerDetail(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = NewSerializerList(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = NewSerializerList(queryset, many=True)
        return Response(serializer.data)
