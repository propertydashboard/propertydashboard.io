from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from datetime import datetime

from .models import Property

class PropertyDetailView(DetailView):
    model = Property

    def get_context_data(self, **kwargs):
        property = Property.objects.get(id=self.object.id)
        context = super().get_context_data(**kwargs)
        context['gross_yield'] = f'{round((property.current_rent * 12) / property.value * 100, 2)}%'
        context['potential_gross_yield'] = f'{round((property.market_rent * 12) / property.value * 100, 2)}%'
        context['is_owner'] = property.owner == self.request.user
        context['mortgage_deal_expiry_date'] = property.mortgage_deal_expiry_date
        return context


class PropertyListView(ListView):
    model = Property

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        city = self.request.GET.get('city', False)

        val = 0
        mortgages = 0
        current_rents = 0
        potential_rents = 0

        properties = Property.objects.filter(owner=self.request.user)

        if city:
            properties = properties.filter(city=city)

        for property in properties:
            val += property.value
            mortgages += property.mortgage
            current_rents += property.current_rent
            potential_rents  += property.market_rent

        current_rents = current_rents * 12
        potential_rents = potential_rents * 12

        difference_in_rent = f'£{int(potential_rents - current_rents)}'
        ltv = f'{int((mortgages / val) * 100)}%'

        equity_percentage = 100 - int((mortgages / val) * 100)
        rate_of_return = f'{round(round((1 / equity_percentage) * 100, 2) * 5, 2)}%'

        doubling_period = f'{round(72 / (round((1 / equity_percentage) * 100, 2) * 5), 2)} years'

        context['portfolio_value'] = val
        context['outstanding_mortgages'] = mortgages
        context['ltv'] = ltv
        context['current_gross_yield'] = f'{round(current_rents / val * 100, 2)}%'
        context['potential_gross_yield'] = f'{round(potential_rents / val * 100, 2)}%'
        context['difference_in_rent'] = difference_in_rent
        context['properties'] = properties
        context['rate_of_return'] = rate_of_return
        context['doubling_period'] = doubling_period
        context['potential_rents'] = potential_rents

        return context