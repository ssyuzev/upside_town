from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import PersonCreateForm, AddLikeForm
from .models import Like, Person
from .mailer import send_email
from .helpers import haversine


@method_decorator(csrf_exempt, name='dispatch')
class PersonCreateView(View):

    def post(self, request):
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True}, status=201)
        else:
            errors = dict(form.errors.items())
            return JsonResponse(
                {"success": False, "errors": f"{errors}"}, status=400
            )


@method_decorator(csrf_exempt, name='dispatch')
class MatchView(View):

    def post(self, request):
        form = AddLikeForm(request.POST)
        if form.is_valid():
            from_ = request.POST["from_person"]
            to_ = request.POST["to_person"]
            if from_ == to_:
                return JsonResponse({"success": False, "errors": "You can't like this person"}, status=400)
            form.save()
            matched = Like.objects.filter(to_person=from_, from_person=to_).first()
            is_match = True if matched else False
            if is_match:
                mail_data = dict(
                    match_email=matched.from_person.email,
                    match_full_name=matched.from_person.full_name,
                    match_gender=matched.from_person.gender,
                    full_name_to=matched.to_person.full_name,
                    mail_to=matched.to_person.email,
                )
                send_email(mail_data)
            return JsonResponse({"match": is_match}, status=201)
        else:
            errors = dict(form.errors.items())
            return JsonResponse(
                {"success": False, "errors": f"{errors}"}, status=400
            )


class ListView(View):

    def get_seeker(self, seeker_id):
        seeker = None
        try:
            seeker = Person.objects.all().filter(id=seeker_id).order_by("id").first()
        except ValueError:
            seeker_id = None
        if not seeker_id:
            seeker = Person.objects.all().order_by("id").last()
        return seeker

    def get(self, request):
        items, seeker = [], None
        seeker_id = request.GET.get("personId")
        seeker = self.get_seeker(seeker_id)
        if seeker:
            page = request.GET.get("page", 1)
            gender = request.GET.get("gender[eq]", "f")
            try:
                distance_lte = int(request.GET.get("distance[lte]"))
            except ValueError:
                distance_lte = settings.DEFAULT_DISTANCE_KM
            persons_list = Person.objects.all().filter(gender=gender).order_by("id").values()
            for person in persons_list:
                a = haversine(seeker.longitude, seeker.latitude, person.get("longitude"), person.get("latitude"))
                if a <= distance_lte:
                    items.append(person)

            page = request.GET.get("page", 1)
            paginator = Paginator(items, settings.PAGINATOR_PER_PAGE_ITEMS)
            try:
                persons = paginator.page(page)
            except PageNotAnInteger:
                persons = paginator.page(1)
            except EmptyPage:
                persons = paginator.page(paginator.num_pages)
            items = list(persons.object_list)
            return JsonResponse(
                {
                    "persons": items,
                    "total": len(items),
                    "previous_page": persons.has_previous() and persons.previous_page_number() or None,
                    "next_page": persons.has_next() and persons.next_page_number() or None,
                }
            )
        return JsonResponse({"success": False}, status=404)
