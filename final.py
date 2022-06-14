import requests

# change this auth key
Authentication_key = {'Authorization': 'Bearer cs5ch6u59fwa7avefyzqts8g'}
TIME = '2022-05-05T00:00'  # input time to calculate
LATITUDE = 28.679079
LONGITUDE = 77.069710


# calculating nearest airports
def Nearst_airport(Auth_key,LATITUDE,LONGITUDE):


    # api parameters
    Endpoint = 'https://api.lufthansa.com/v1'
    Near_airport = f'references/airports/nearest/{LATITUDE},{LONGITUDE}'

    # request and response of endpoints
    req = requests.get(f'{Endpoint}/{Near_airport}', headers=Auth_key)
    response = req.json()
    airport = response['NearestAirportResource']['Airports']['Airport']
    list1 = []
    for i in range(5):
        airport_name = airport[i]['AirportCode']
        list1.append(airport_name)
    return list1  # a list of nearest airport codes.


# calling nearest airport fucntion
Airport_list = Nearst_airport(Auth_key=Authentication_key,LATITUDE=LATITUDE,LONGITUDE=LONGITUDE)


def terminalTime(Airports, Auth_key,TIME):
    Endpoint = 'https://api.lufthansa.com/v1'
    for item in Airports[:3]:
        flight_status = f'operations/flightstatus/departures/{item}/{TIME}'
        req1 = requests.get(f'{Endpoint}/{flight_status}', headers=Auth_key)
        # print(req1.status_code) #to test code is right or wrong
        if 199 < req1.status_code < 300:  # if flight code is success.
            response1 = req1.json()
            status = response1['FlightStatusResource']['Flights']['Flight'][0]
            Departure_airport = status['Departure']['AirportCode']
            AAirport_code = status['Arrival']['AirportCode']
            try:
                arrival_time = status['Arrival']['ActualTimeLocal']
            except KeyError:
                arrival_time=status['Arrival']['ScheduledTimeLocal']
            try:
                A_terminal = status['Arrival']['Terminal']
            except KeyError:
                A_terminal = 'N/A'

            print(
                f'Departed from {Departure_airport} and arrival airport code is {AAirport_code} in Terminal {A_terminal} on {arrival_time}')

        else:
            print(
                f'no flight of lufthansa airline from {item} Airport on given date')
status=terminalTime(Airports=Airport_list, Auth_key=Authentication_key,TIME=TIME)

