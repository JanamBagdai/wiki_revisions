from django.shortcuts import render
from .wikipedia_service import get_wikipedia_revisions
from .wikipedia_service import generate_graph
from .forms import GraphForm

def home(request):
    return render(request, 'pages/home.html')

def random_number(request):
    return render(request, 'pages/random_number.html')

def parse_events_and_generate_graphs(request):
    form = GraphForm(request.POST)
    graphs_data = None

    if request.method == 'POST' and form.is_valid():
        selected_days = form.cleaned_data['days']
        graphs_data = generate_graph(selected_days)
        return render(request, 'pages/parse_events_and_generate_graphs.html', {'graph_data': graphs_data})
    else:
        form = GraphForm()
        return render(request, "form.html", {"form": form})