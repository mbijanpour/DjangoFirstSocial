from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from posts.models import Post


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'posts': posts})

    def post(self, request):
        return HttpResponse('POST request')
