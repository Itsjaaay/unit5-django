from django.shortcuts import render
from .models import Team

teams_data = {
    'management': Team('Management Team', 'Description for Management Team', ['John', 'Alice']),
    'procurement': Team('Procurement Team', 'Description for Procurement Team', ['Bob', 'Eva'])
    # Add more team details as needed
}

def team_list(request):
    teams = list(teams_data.keys())
    return render(request, 'team_list.html', {'teams': teams})

def team_detail(request, team_name):
    team = teams_data.get(team_name)
    return render(request, 'team_detail.html', {'team': team})
