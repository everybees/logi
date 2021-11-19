from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Account


class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def create_account(self, request):
        try:
            soo = request.data
            if "email" not in soo or "password" not in soo or "confirm_password" not in soo or "user_type" not in soo:
                return Response({"message": "Your data is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
            if soo.get('password') != soo.get('confirm_password'):
                return Response({"message": "Password do not match."}, status=status.HTTP_400_BAD_REQUEST)
            Account.objects.create(
                email=soo.get('email'), password=soo.get('password'), user_type=soo.get('user_type')
            )
            return Response({"message": "success!"}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({"message": "A user with this email exists."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        try:
            data = request.data
            if "email" not in data or "password" not in data:
                return Response({"message": "Your data is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
            user = Account.objects.get(email=data.get('email'))
            if user.password == data.get("password"):
                return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
            return Response({"message": "This password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        except Account.DoesNotExist:
            return Response({"message": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['put'])
    def update_profile(self, request):
        return render(request, "update_profile.html")

    def view_profile(self, request):
        return render(request, "view_profile.html")

    def change_password(slef, request):
        return render(request, "change_password.html")
