class TravelCase:
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
    def __init__(self, journeyCode, holidayType, Price,
                 NumberOfPersons, Region, Lat, Lng, Transportation, Duration,
                 Season, Accomodation, Hotel):
        self.journeyCode = journeyCode
        self.holidayType = holidayType
        self.price = Price
        self.numberOfPersons = NumberOfPersons
        self.region = Region
        self.latitude = Lat
        self.longitude = Lng
        self.transportation = Transportation
        self.duration = Duration
        self.season = Season
        self.accomodation = Accomodation
        self.hotel = Hotel

    def __str__(self):
        return "Region: "+str(self.region)+"\nHotel:"+str(self.hotel)+"Season: "+str(self.season)+"\nPrice:"+str(self.price)+\
               "\nTransportation:"+str(self.transportation)+"\nDuration:"+str(self.duration)+"\nNumberOfPersons:"+str(self.numberOfPersons)

    def decoding(self):
        self.holidayType = self.decode_holiday_type()
        self.accomodation = self.decode_accomodation()
        self.season = self.decode_season()
        self.transportation = self.decode_transportation()


    def decode_holiday_type(self):
        holidayType = str(self.holidayType)
        if holidayType == "0":
            return "Bathing"
        elif holidayType=="1":
            return "Wandering"
        elif holidayType == "2":
            return "Recreation"
        elif holidayType == "3":
            return "Skiing"
        elif holidayType == "4":
            return "Active"
        elif holidayType == "5":
            return "City"
        elif holidayType == "6":
            return "Education"
        else:
            return "Else"



    def decode_season(self):
        season = str(self.season)
        if season == "1":
            return "January"
        elif season == "2":
            return "February"
        elif season == "3":
            return "March"
        elif season == "4":
            return "April"
        elif season == "5":
            return "May"
        elif season == "6":
            return "June"
        elif season == "7":
            return "July"
        elif season == "8":
            return "August"
        elif season == "9":
            return "September"
        elif season == "10":
            return "October"
        elif season == "11":
            return "November"
        elif season == "12":
            return "December"

    def decode_transportation(self):
        transportation = str(self.transportation)
        if transportation == "2":
            return "Plane"
        elif transportation == "1":
            return "Car"
        elif transportation == "0":
            return "Train"
        else:
            return "Others"

    def decode_accomodation(self):
        accomodation = str(self.accomodation)
        if accomodation == "1":
            return "OneStar"
        elif accomodation == "2":
            return "TwoStars"
        elif accomodation == "3":
            return "ThreeStars"
        elif accomodation =="4":
            return "FourStars"
        elif accomodation == "5":
            return "FiveStars"
        elif accomodation == "6":
            return "HolidayFlat"
        else:
            return "Others"
