from django.http import JsonResponse
from django.views import View


class CreateView(View):
    pass


class MatchView(View):
    pass


class ListView(View):
    def get(self, request):
        return JsonResponse({"status": "Ok"})
