from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Banyantree(TemplateView):
    template_name = "nature/banyan.html"
class Peepaltree(TemplateView):
    template_name = "nature/peepal.html"
class Neemtree(TemplateView):
    template_name = "nature/neem.html"
class trees(TemplateView):
    template_name = "nature/trees.html"