from rest_framework import serializers
from bbs.models import Board, Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post

class BoardSerializer(serializers.ModelSerializer):
	posts = PostSerializer(many=True, read_only=True)
	class Meta:
		model = Board