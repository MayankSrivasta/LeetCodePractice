class UndergroundSystem:
# chatgpt
# this question is only about creating 2 hashmaps & then accordingly updating the travel time & count
    def __init__(self):
        # Maps to store check-in records and travel times
        # two hashmaps
        self.checkInRecords = {}  # Maps passenger_id to (station_name, check_in_time)
        self.travelTimes = {}  # Maps (start_station, end_station) to (total_time, count)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Store check-in information for a passenger
        self.checkInRecords[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Get the check-in information
        start_station, check_in_time = self.checkInRecords.pop(id)
        
        # Calculate the travel time
        travel_time = t - check_in_time
        
        # Update the travelTimes map
        # some other user already traveled from start_station to stationName
        if (start_station, stationName) in self.travelTimes:
            total_time, count = self.travelTimes[(start_station, stationName)]
            self.travelTimes[(start_station, stationName)] = (total_time + travel_time, count + 1)
        else:
            # first time this route is being traveled
            self.travelTimes[(start_station, stationName)] = (travel_time, 1)
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Get the total time and count of trips for a specific route
        total_time, count = self.travelTimes[(startStation, endStation)]
        return total_time / count
    
#====================================================================================================

# Neetcode.io solution
    def __init__(self):
        self.checkInMap = {} # id -> (startStation, time)
        self.routeMap = {} # (start, end) -> [totalTime, count]

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkInMap[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation, time = self.checkInMap[id]
        route = (startStation, endStation)
        if route not in self.routeMap:
            self.routeMap[route] = [0, 0]
        self.routeMap[route][0] += t - time
        self.routeMap[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.routeMap[(startStation, endStation)]
        return totalTime / count    