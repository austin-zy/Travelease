from django.shortcuts import render
import json
from django.http import JsonResponse
import Parser as ps
import Prediction as predict
import TravelCase as tc
from django.http import HttpResponse

# Create your views here.
def show_view(request):
	return render(request,'home/show_view.html',{})

def post_data(request):

	if(request.method=='POST'):
		data = json.loads(request.body)
		parser = ps.Parser()
		print data['transportation']
		transportation = parser.encode_transportation(data['transportation'])
		season = parser.encode_season(data['season'])
		lat = data['latitude']
		lng = data['longitude']
		duration = data['duration']
		group = data['group']
		holidayType = parser.encode_holidayType(data['holidayType'])
		# Get List
		attrib = [transportation,season,lat,lng,duration,group,holidayType]
		prediction = predict.Prediction()
		travelCase = prediction.predict_closest_case(transportation,season,lat,lng,duration,group,holidayType)
		travelCase.decoding()
		#request.POST = QueryDict(data)
		return HttpResponse(json.dumps(travelCase.__dict__), content_type = "application/json")
	else:
		return render(request,'home/show_view.html',{})