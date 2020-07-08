from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


# The HyperlinkedModelSerializer has the following differences from ModelSerializer:

#    It does not include the id field by default.
#    It includes a url field, using HyperlinkedIdentityField.
#    Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.

class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    # Add additional fields to the existing Serializer

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        # Add fields which might not be in your default model.
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code','linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
