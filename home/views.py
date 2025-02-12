from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import *
from posts.models import Post


class HomeView(View):
    class_form = SearchForm

    def get(self, request):
        posts = Post.objects.all()
        if request.GET.get("search"):
            posts = posts.filter(body__contains=request.GET["search"])
        return render(
            request, "home/index.html", {"posts": posts, "search_form": self.class_form}
        )

    def post(self, request):
        return HttpResponse("POST request")
