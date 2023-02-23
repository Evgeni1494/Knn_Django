from django.shortcuts import render
from .forms import HouseForm
from .utils import load_model

def predict_price(request):
    form = HouseForm(request.POST or None)
    if form.is_valid():
        model = load_model()
        # Prétraiter les données
        data = form.cleaned_data
        X = [[data['zipcode'], data['view'], data['grade'], data['sqft_living'],
              data['bathrooms'], data['waterfront'], data['sqft_above'],
              data['sqft_basement'], data['sqft_living15'], data['days_since_reference_date']]]
        # Prédire le prix
        price = model.predict(X)
        # Afficher le résultat
        return render(request, 'result.html', {'price': price[0]})
    return render(request, 'predict_price.html', {'form': form})
