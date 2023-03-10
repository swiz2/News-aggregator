import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

def home(request):
	return render(request,'news/home.html')

def Breakinnews(request):
	return render(request,'news/Breakingnews.html')

def Newsmarket(request):
	return render(request,'news/Newsmarket.html')

def Internationalrel(request):
	return render(request,'news/Internationalrelations.html')

def Politics(request):
	return render(request,'news/Politics.html')

def Weeklyhigh(request):
	return render(request,'news/Weeklyhighlights.html')

def Sports(request):
	return render(request,'news/Sports.html')


