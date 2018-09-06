# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def fill_db():
	r.set('movie:1', "The Godfather")
	r.set('movie:2', "Schindler's List")
	r.set('movie:3', "Saving Private")
	r.set('movie:4', "Back to the Future")
	r.set('movie:5', "Casablanca")
	r.set('movie:6', "The Big Lebowski")
	r.set('actors:1', "Al Pacino, Marlon Brando, Robert Duvall")
	r.set('actors:2', "Liam Neeson, Ralph Fiennes, Ben Kingsley")
	r.set('actors:3', "Ryan Tom Hanks, Matt Damon, Vin Diesel")
	r.set('actors:4', "Michael J. Fox, Christopher Lloyd, Lea Thompson")
	r.set('actors:5', "Ingrid Bergman, Humphrey Bogart, Peter Lorre")
	r.set('actors:6', "Julianne Moore, Jeff Bridges, Tara Reid")

fill_db()

def index(request):
	movie_list = r.keys('movie:*')
	movie_names = []
	for a in movie_list:
		movie_names.append(r.get(a))
	return render(request, 'movies/index.html', {'movies': movie_names})

@csrf_exempt
def detail(request):
	movie_name = request.POST.get('movie', '').title();
	movie_list = r.keys('movie:*')
	actors = []
	for a in movie_list:
		if r.get(a) == movie_name:
			movie_id = a.split(':')[1]
			actors_id = r.keys('actors:' + movie_id)
	for q in actors_id:
		actors.append(r.get(q))
		
	return render(request, 'movies/detail.html', {'movie': movie_name, 'actors': actors})
