from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from phonebook.models import PhoneNumber


class SearchView(TemplateView):
    template_name = 'searched_phones.html'

class SearchResultsView(ListView):
    model = PhoneNumber
    template_name = 'search_numbers.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = PhoneNumber.objects.filter(
            Q(name__icontains=query) | Q(number__icontains=query) |
            Q(city__icontains=query) | Q(age__icontains=query)
        )
        return object_list


class PhoneNumberDetailView(DetailView):
    model = PhoneNumber
    template_name = 'phone/phone_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


def phones(request):
    phones = PhoneNumber.objects.all()
    paginator = Paginator(phones, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request,
                  template_name="phone/phone_list.html",
                  context={'phones': page_obj})
