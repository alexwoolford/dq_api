from rest_framework import generics
from .models import Parent, Child
from .serializers import ChildSerializer, ParentSerializer, ChildrenShowingParentSerializer, ParentShowingChildrenSerializer


class ViewParent(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ViewChild(generics.ListAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ViewOffspring(generics.ListAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildrenShowingParentSerializer


class ViewMommyDaddy(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentShowingChildrenSerializer
