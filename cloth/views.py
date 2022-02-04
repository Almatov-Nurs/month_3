from django.forms import forms
from django.shortcuts import get_object_or_404
from django.views import generic
from . import models, forms

class TagListView(generic.ListView):
    queryset = models.ProductCL.objects.all()
    template_name = "tag_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.all()

class HoodieListView(generic.ListView):
    queryset = models.ProductCL.objects.filter(tag__tags_name="Hoodie").order_by("-id")
    template_name = "products_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__tags_name="Hoodie").order_by("-id")

class TShirtListView(generic.ListView):
    queryset = models.ProductCL.objects.filter(tag__tags_name="T-shirt").order_by("-id")
    template_name = "products_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__tags_name="T-shirt").order_by("-id")

class PantsListView(generic.ListView):
    queryset = models.ProductCL.objects.filter(tag__tags_name="Pants").order_by("-id")
    template_name = "products_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__tags_name="Pants").order_by("-id")

class ShoesListView(generic.ListView):
    queryset = models.ProductCL.objects.filter(tag__tags_name="Shoes").order_by("-id")
    template_name = "products_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__tags_name="Shoes").order_by("-id")

class ProductDetailView(generic.DetailView):
    template_name = "product_detail.html"
    queryset = models.ProductCL.objects.all(), models.StatusOrderCL.objects.all()

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCL, id=product_id)

class OrderCreateView(generic.CreateView):
    template_name = "add-order.html"
    form_class = forms.StatusOrderForm
    success_url = "/tags/"
    queryset = models.StatusOrderCL.objects.all()

    def for_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)