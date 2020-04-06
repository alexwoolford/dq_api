from rest_framework import serializers
from .models import Child, Parent


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ["lastname", "firstname", "age", "ts", "parent"]


class ParentSerializer(serializers.ModelSerializer):
    relationship_status = serializers.SerializerMethodField()

    def get_relationship_status(self, obj):
        if obj.lastname == "Woolford":
            return ("married")
        else:
            return ("single")

    class Meta:
        model = Parent
        fields = ["lastname", "firstname", "age", "ts", "relationship_status"]


# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']


class ChildrenShowingParentSerializer(serializers.ModelSerializer):
    # children = serializers.StringRelatedField(many=True)
    # parents_firstname = serializers.CharField(read_only=True)
    parents = ChildSerializer(many=True, read_only=True)

    class Meta:
        model = Child
        # fields = ["lastname", "firstname", "age", "ts", "parents"]
        fields = "__all__"


class ParentShowingChildrenSerializer(serializers.ModelSerializer):
    children = ParentSerializer(many=True, read_only=True)
    # THIS WORKS (mommydaddy View)

    class Meta:
        model = Parent
        fields = "__all__"
