from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

def home(request):
    return render(request, 'home.html')