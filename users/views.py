from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Account


class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def create_account(self, request):
        soo = request.data
        if "email" not in soo or "password" not in soo or "confirm_password" not in soo:
            return Response({"message": "Your data is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        if soo.get('password') != soo.get('confirm_password'):
            return Response({"message": "Password do not match."}, status=status.HTTP_400_BAD_REQUEST)
        Account.objects.create(email=soo.get('email'), password=soo.get('password'))
        return Response({"message": "success!"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def login(self, request):
        return render(request, "login.html")

    def create_profile(self, request):
        return render(request, "create_profile.html")

    def update_profile(self, request):
        return render(request, "update_profile.html")

    def view_profile(self, request):
        return render(request, "view_profile.html")

    def change_password(slef, request):
        return render(request, "change_password.html")
