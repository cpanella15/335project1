import sys

def groupschedule (pers1Schedule, pers1DailyAct, pers2Schedule, pers2DailyAct,duration ):

    updatedSchedule1 = updateSchedule(pers1Schedule, pers1DailyAct)
    updatedSchedule2 = updateSchedule(pers2Schedule, pers2DailyAct)
    mergedSchedule=mergedSchedules(updatedSchedule1, updatedSchedule2)
    sortedSchedules= sortedAllSchedules(mergedSchedule)
    print ( matchedAvailabilities(sortedSchedules,duration))

def updateSchedule(Schedule, DailyAct):
    updatedSchedule = Schedule[:]  #make a copy of the schedule
    updatedSchedule.insert(0, ['0:00', DailyAct[0]])  #update unavailable schedules and add early morning hours
    updatedSchedule.append([DailyAct[1], '23:59'])   #update unavailable schedules and add after work hours
    return list(map(lambda s: [convertToMinutes(s[0]), convertToMinutes(s[1])], updatedSchedule))


def mergedSchedules(pers1Schedule, pers2Schedule):
    merged =[]
    i,j =0,0
    while i < len(pers1Schedule) and j< len(pers2Schedule):
        meeting1, meeting2 = pers1Schedule[i], pers2Schedule[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i+=1
        elif meeting1[0] == meeting2[0]:
            if meeting1[1] <= meeting2[1]:
                merged.append(meeting1)
                i += 1
            else:
                merged.append(meeting2)
                j += 1
        else:
            merged.append(meeting2)
            j+=1
    while i< len(pers1Schedule):
        merged.append(meeting1)
        i+=1
    while j< len(pers2Schedule):
        merged.append(meeting2)
        j+=1
    return merged

def sortedAllSchedules (Schedule):

    avaliableTimes = []
    i = 0
    trackLatest = 0
    for item in Schedule:
        nextItem = Schedule[(i + 1) % len(Schedule)]
        i += 1
        if trackLatest < item[1]:
            trackLatest = item[1]

        if trackLatest < item[1]:
            trackLatest = item[1]

        if item[1] < nextItem[0] and nextItem[0] > trackLatest:
            tempList = [item[1], nextItem[0]]
            avaliableTimes.append(tempList)
    return avaliableTimes

    #Todo: write a function to  arrange all schedules. New meeting starts AFTER the end of current meeting.
    

def matchedAvailabilities(Schedule, duration):
    availabilities = []

    for item in Schedule:
        temp = item[0]
        while (temp + duration <= item[1]):
            availabilities.append([temp, temp+duration])
            temp += duration

    return list(map(lambda s: [convertMinutestoHour(s[0]), convertMinutestoHour(s[1])], availabilities))

   #Todo: write a function to match all availabilities
    


def convertToMinutes(time):
  
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes

def convertMinutestoHour(minutes):
    hours = minutes // 60
    mins = minutes% 60
    toString = str(hours)
    toStringMins = "0" + str(mins) if mins< 10 else str(mins)
    return toString +":" + toStringMins

def main():
    # pers1Schedule = input("Enter schedule for person 1:")
    # pers2Schedule = input("Enter schedule for person 2:")
    # pers1DailyAct = input("Enter Daily Availability for pers 1: ")
    # pers2DailyAct = input("Enter Daily Availability for pers 2: ")
    # duration = input("Enter duration of the proposed meeting: ")

    pers1Schedule = [[ '7: 00', '8: 30'], ['12: 00', '13: 00'], ['16: 00', '18: 00']]
    pers1DailyAct = ['9: 00', '19: 00']

    pers2Schedule = [[ '9:00', '10:30'],  ['12:20', '14:30'],  ['14:00', '15:00'], ['16:00', '17:00']]
    pers2DailyAct = ['9: 00', '18: 30']

    duration = 30

    groupSchedule1= groupschedule (pers1Schedule, pers1DailyAct, pers2Schedule, pers2DailyAct,duration )

if __name__ == "__main__":
    main()

