# dj
from django.views import View
from django.shortcuts import render


class IndexView(View):
    """Index View"""
    def get(self, request):
        return render(request, 'chat/index.html')
