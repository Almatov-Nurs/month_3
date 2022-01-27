from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from . import parser, models, forms

class ParserFormView(generic.FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return redirect(reverse("parse:parser_list"))
            # return HttpResponse('Parser Success')
        else:
            return super(ParserFormView,self).post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(ParserFormView, self).form_valid(form=form)

class ParseListView(generic.ListView):
    template_name = "parser_list.html"
    queryset = models.Film.objects.all()

    def get_queryset(self):
        return models.Film.objects.filter().order_by("-id")

class ParseDetailView(generic.DetailView):
    template_name = "parser_detail.html"

    def get_object(self, **kwargs):
        id = self.kwargs.get("id")
        return get_object_or_404(models.Film, id=id)