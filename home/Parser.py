import TravelCase as tc
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut
import csv
import os.path

###################################################
#       This code is written by
#        a) Austin Goh 
#        b) KC Koay
#        c) Khalil Gibran Von
#        d) Loh Yoong Keat
#        e) Azim
#       From University of Malaya
#       * WAES3306 Information System Intelligence
###################################################


#############################
#           Geocoding       #
#############################
def do_geocode(place_name):
    # From place name to place object
    geocoder = Nominatim()
    try:
        return geocoder.geocode(place_name)
    except Exception:
        return do_geocode(place_name)

################################
#        Parsing to list       #
################################
class Parser:
    def parsing(self):
        f = open("TRAVEL.txt","r+")
        lines = f.readlines()
        # Initialize empty list
        list_obj = []
        # Looping through all lines
        for i in range(len(lines)):
            # Check for defcase
            if "defcase" in lines[i]:
                try:
                    journeyCode = lines[i + 3].split(": ")[1].split(",")[0]
                    #print journeyCode
                    holidayType = lines[i + 4].split(": ")[1].split(",")[0]
                    holidayType = self.encode_holidayType(holidayType)
                    #print holidayType
                    price = lines[i + 5].split(": ")[1].split(",")[0]
                    #print price
                    numberOfPersons = lines[i + 6].split(": ")[1].split(",")[0]
                    #print numberOfPersons
                    #####################
                    #       Region      #
                    #####################
                    # Encode the region to latlng
                    region = lines[i + 7].split(": ")[1].split(",")[0]
                    place = do_geocode(region)
                    latitude = place.latitude
                    longitude = place.longitude
                    #####################
                    #   Transportation  #
                    #####################
                    # Normalize the transportation to int
                    transportation = lines[i + 8].split(": ")[1].split(",")[0]
                    transportation = self.encode_transportation(transportation)
                    #####################
                    #      Duration     #
                    #####################
                    duration = lines[i + 9].split(": ")[1].split(",")[0]
                    #print duration
                    #####################
                    #       Season      #
                    #####################
                    # Normalize the season
                    season = lines[i + 10].split(": ")[1].split(",")[0]
                    season = self.encode_season(season)
                    #print season
                    #####################
                    #    Accomodation   #
                    #####################
                    # Encode stars into int
                    accomodation = lines[i + 11].split(": ")[1].split(",")[0]
                    accomodation = self.encode_accomodation(accomodation)
                    #print accomodation
                    hotel = lines[i + 12].split(": ")[1]
                    #print hotel
                    travelCase = tc.TravelCase(journeyCode,holidayType,price,numberOfPersons,region,
                                               latitude, longitude,transportation,duration,season,accomodation,hotel)
                    list_obj.append(travelCase)
                except Exception as e:
                    print e.message
        f.close()
        return list_obj
    #########################################
    #         Encoding holidayType          #
    #########################################
    def encode_holidayType(self, holidayType):
        if holidayType == "Bathing":
            return 0
        elif holidayType=="Wandering":
            return 1
        elif holidayType == "Recreation":
            return 2
        elif holidayType == "Skiing":
            return 3
        elif holidayType == "Active":
            return 4
        elif holidayType == "City":
            return 5
        elif holidayType == "Education":
            return 6
        else:
            return 7


    #########################################
    #             Encoding Season           #
    #########################################
    def encode_season(self, season):
        if season == "January":
            return 1
        elif season == "February":
            return 2
        elif season == "March":
            return 3
        elif season == "April":
            return 4
        elif season == "May":
            return 5
        elif season == "June":
            return 6
        elif season == "July":
            return 7
        elif season == "August":
            return 8
        elif season == "September":
            return 9
        elif season == "October":
            return 10
        elif season == "November":
            return 11
        elif season == "December":
            return 12
    #########################################
    #        Encoding transportation        #
    #########################################        
    def encode_transportation(self, transportation):
        if transportation == "Plane":
            return 2
        elif transportation == "Car":
            return 1
        elif transportation == "Train":
            return 0
        else:
            return 3
    #########################################
    #         Encoding Acoomodation         #
    #########################################
    def encode_accomodation(self,accomodation):
        if accomodation == "OneStar":
            return 1
        elif accomodation == "TwoStars":
            return 2
        elif accomodation == "ThreeStars":
            return 3
        elif accomodation =="FourStars":
            return 4
        elif accomodation == "FiveStars":
            return 5
        elif accomodation == "HolidayFlat":
            return 6
        else:
            return 0

    def toCSV(self):
        # Writing into CSV
        travel_data = self.parsing()
        with open('training.csv', 'wb') as csvfile:
            csvwriter = csv.writer(csvfile,delimiter=',')
            # For every data in travel_data
            for data in travel_data:
                # Write row
                csvwriter.writerow([data.journeyCode, data.holidayType
                                   , data.price, data.numberOfPersons, data.region,
                                   data.latitude, data.longitude, data.transportation,
                                   data.duration, data.season, data.accomodation, data.hotel])

    def readCSV(self):
        # Get path
        BASE = os.path.dirname(os.path.abspath(__file__))
        dataset = os.path.join(BASE,'training.csv')
        # Initializing empty list
        travel_data = []
        with open(dataset, 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            # Read every row
            for row in csvreader:
                journeyCode = row[0]
                holidayType = row[1]
                price = row[2]
                numberOfPersons = row[3]
                region = row[4]
                latitude = row[5]
                longitude = row[6]
                transportation = row[7]
                duration = row[8]
                season = row[9]
                accomodation = row[10]
                hotel = row[11]
                # To object
                travelCase = tc.TravelCase(journeyCode, holidayType, price, numberOfPersons, region,
                                           latitude, longitude, transportation, duration, season, accomodation, hotel)
                travel_data.append(travelCase)
        return travel_data

#p = Parser()
#p.toCSV()



