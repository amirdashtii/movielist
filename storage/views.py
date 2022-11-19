from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def movie_list(request):
    return Response(('ok'))


@api_view()
def movie_detail(request, id):
    return Response(id)
