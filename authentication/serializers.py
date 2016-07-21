from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer1(serializers.ModelSerializer):
	"""
	used in login
	"""
	class Meta:
		model = User
		fields = ('id', 'username', 'last_login')

class UserSerializer2(serializers.ModelSerializer):
	"""
	used in logon
	"""
	class Meta:
		model = User
		fields = ('id', 'username')
