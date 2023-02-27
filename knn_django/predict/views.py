from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import House
from .forms import HouseForm
from django.shortcuts import render
from django.views import View
import pickle
import pandas as pd
import joblib

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

# class PredictView(View):
#     def post(self, request):
#         # code pour réaliser la prédiction
#         # ...
#         return render(request, 'result.html', {'prediction': prediction})

class ResultView(View):
    def get(self, request):
        return render(request, 'result.html')
    def post(self,request):
        if request.method == 'POST':
            form = HouseForm(request.POST)
            # Récupérer les données du formulaire
            if form.is_valid():
                # zipcode = form.cleaned_data['zipcode']
                # view = form.cleaned_data['view']
                # grade = form.cleaned_data['grade']
                # sqft_living = form.cleaned_data['sqft_living']
                # bathrooms = form.cleaned_data['bathrooms']
                # waterfront = form.cleaned_data['waterfront']
                # sqft_above = form.cleaned_data['sqft_above']
                # sqft_basement = form.cleaned_data['sqft_basement']
                # sqft_living15 = form.cleaned_data['sqft_living15']
                # days_since_reference_date = form.cleaned_data['days_since_reference_date']
                data = form.cleaned_data
                df = pd.DataFrame(data,index=[0])
                
                print(df)
            # Charger le modèle KNN entraîné
            with open('predict/models/model.pkl', 'rb') as f:
                print(f)
                knn_model = joblib.load(f)
                prediction = knn_model.predict(df)

            # Effectuer la prédiction
            # prediction = knn_model.predict([[zipcode, view, grade, sqft_living, bathrooms, 
            #                                 waterfront, sqft_above, sqft_basement, sqft_living15, 
            #                                 days_since_reference_date]])
                

            # Enregistrer les données dans la base de données
            # house = House(zipcode=zipcode, view=view, grade=grade, sqft_living=sqft_living, 
            #             bathrooms=bathrooms, waterfront=waterfront, sqft_above=sqft_above, sqft_basement=sqft_basement, 
            #             sqft_living15=sqft_living15, days_since_reference_date=days_since_reference_date, price=prediction[0])
            # house.save()

            # Renvoyer le résultat de la prédiction à l'utilisateur
            context = {
                'prediction': round(prediction[0], 2)
            }
            return render(request, 'result.html', context)

        else:
            form = HouseForm()
            return render(request, 'predict.html')