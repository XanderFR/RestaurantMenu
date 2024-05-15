from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


# Displays all foods
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("date_created")  # Query data from database table
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Food data from database
        context["meals"] = MEAL_TYPE
        return context


# Displays info about a specific food
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"  # Item gets sent to menu_item_detail as "item"


def about(request):
    return render(request, "about.html")
