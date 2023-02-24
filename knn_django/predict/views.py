from django.shortcuts import render
from .forms import HouseForm
from .utils import load_model
from django.shortcuts import render
from django.views import View
from .forms import HouseForm
import pickle
from django.conf import settings
from django.contrib import messages
import os
from .models import HousePrice

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
    return render(request, 'predict.html', {'form': form})

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
    
class PredictView(View):
    def get(self, request):
        form = HouseForm()
        return render(request, 'predict.html', {'form': form})
    
    def post(self, request):
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                # Charger le modèle entraîné
                with open(os.path.join(settings.MODEL_ROOT, 'knn_4.pkl'), 'rb') as f:
                    knn = pickle.load(f)
                
                # Obtenir les caractéristiques de la maison à partir du formulaire
                features = [form.cleaned_data[f] for f in ['zipcode', 'view', 'grade', 'sqft_living', 'bathrooms', 'waterfront', 'sqft_above', 'sqft_basement', 'sqft_living15', 'days_since_reference_date']]
                
                # Faire la prédiction
                prediction = knn.predict([features])[0]
                
                # Enregistrer la prédiction dans la base de données
                HousePrice.objects.create(
                    zipcode=form.cleaned_data['zipcode'],
                    view=form.cleaned_data['view'],
                    grade=form.cleaned_data['grade'],
                    sqft_living=form.cleaned_data['sqft_living'],
                    bathrooms=form.cleaned_data['bathrooms'],
                    waterfront=form.cleaned_data['waterfront'],
                    sqft_above=form.cleaned_data['sqft_above'],
                    sqft_basement=form.cleaned_data['sqft_basement'],
                    sqft_living15=form.cleaned_data['sqft_living15'],
                    days_since_reference_date=form.cleaned_data['days_since_reference_date'],
                    price=prediction
                )
                
                # Afficher le résultat
                return render(request, 'result.html', {'prediction': prediction})
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
    
        # Si le formulaire n'est pas valide, afficher à nouveau la page avec les erreurs de validation
        return render(request, 'predict.html', {'form': form})
    
    
class ResultView(View):
    def get(self, request):
        houses = HousePrice.objects.all().order_by('-created_at')[:10]
        return render(request, 'results.html', {'houses': houses})