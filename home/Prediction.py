import pandas as pd
import Parser as p
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

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


class Prediction:
    ################################
    #        Filter region         #
    ################################
    # Input : Lat,Lng
    # Result: Region name
    def filter_region(self,lat,lng):
        # Initialzie empty list
        latlng_train = []
        latlng_target = []
        # Get region name
        travelCaseList = self.get_travel_case_list()
        # Retrieve all region name and latlng
        for case in travelCaseList:
            lat_lng = []
            lat_lng.append(case.latitude)
            lat_lng.append(case.longitude)
            latlng_train.append(lat_lng)
            latlng_target.append(case.region)
        # kNN Classifier with k=1
        latlng_knn = NearestNeighbors(n_neighbors=1)
        latlng_knn.fit(latlng_train)
        # Calculation of nearest neighbour
        i = latlng_knn.kneighbors([lat, lng])[1][0][0]
        # Retrieving region based on the case list
        filteredRegion = travelCaseList[i].region
        return filteredRegion

    def get_travel_case_list(self):
        parser = p.Parser()
        return parser.readCSV()

    def predict_closest_case(self,transportation,season,lat,lng,duration,numberOfPersons,holidayType):
        parser = p.Parser()
        # Retrieve region
        filteredRegion = self.filter_region(lat, lng)
        travelCaseList = self.get_travel_case_list()
        #Initializing attributes
        training_attrib = []
        target_attrib   = []
        # Loop through every case and put into list
        for case in travelCaseList:
            case_attrib = []
            if case.region == filteredRegion:
                case_attrib.append(int(case.transportation))
                case_attrib.append(int(case.season))
                case_attrib.append(int(case.duration))
                case_attrib.append(int(case.numberOfPersons))
                case_attrib.append(int(case.holidayType))
                # Put into training list
                training_attrib.append(case_attrib)
                # List for target values
                target_attrib.append(int(case.journeyCode))
            else:
                pass
        # kNN Classifier with k=1
        neigh = KNeighborsClassifier(n_neighbors=1)
        # Reshaping attributes using numpy
        training_attrib = np.array(training_attrib).reshape(len(training_attrib), 5)
        # Fit the training attributes and target attributes into the knn classifier
        neigh.fit(training_attrib, target_attrib)
        # User input -> List
        test = [transportation, season, duration, numberOfPersons, holidayType]
        # Reshaping using numpy
        test = np.array(test).reshape(1, 5)
        # Prediction using kNN and predict journeyCode
        j = neigh.predict(test)
        j = int(j)
        # Retrieve case by journeyCode
        for case in travelCaseList:
            if int(case.journeyCode) == int(j):
                result_case = case
                return result_case
            else:
                pass

    #######################################
    #      Prediction without region      #
    #######################################
    # Almost the same as the above code
    def predict_closest_case_without_latlng(self,transportation,season,duration,numberOfPersons,holidayType):
        parser = p.Parser()
        training_attrib = []
        target_attrib = []
        # Read from CSV
        travelCaseList = self.get_travel_case_list()
        for case in travelCaseList:
            case_attrib = []
            case_attrib.append(int(case.transportation))
            case_attrib.append(int(case.season))
            case_attrib.append(int(case.duration))
            case_attrib.append(int(case.numberOfPersons))
            case_attrib.append(int(case.holidayType))
            training_attrib.append(case_attrib)
            target_attrib.append(int(case.journeyCode))
        neigh = KNeighborsClassifier(n_neighbors=1)
        training_attrib = np.array(training_attrib).reshape(len(training_attrib), 5)
        neigh.fit(training_attrib, target_attrib)
        test = [transportation, season, duration, numberOfPersons, holidayType]
        test = np.array(test).reshape(1, 5)
        j = neigh.predict(test)
        j = int(j)
        print str(travelCaseList[j - 1])
        return travelCaseList[j-1]

