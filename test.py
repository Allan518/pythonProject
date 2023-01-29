class Solution:
    def find_meeting_slots(num_slots, employee_schedules):
        TOTAL_SLOT = 24 * 4
        busyTimes = [0] * TOTAL_SLOT
        whoIsBusy = [[i for i in range(0)] for j in range(TOTAL_SLOT)]
        for i in range(len(employee_schedules)):
            for j in range(len(employee_schedules[i])):
                start, end = 0, 0
                start += (int(employee_schedules[i][j][0:2])) * 4
                start += (int(employee_schedules[i][j][:])) // 15
                end += (int(employee_schedules[i][j][6:8])) * 4
                end += (int(employee_schedules[i][j][9:11])) // 15
                for k in range(start, end):
                    busyTimes[k] += 1
                    whoIsBusy[k].append(i)
        meetings = []
        start, end = 0, 0
        numE = len(employee_schedules)
        while start < TOTAL_SLOT:
            if busyTimes[start] > numE - 2:
                start += 1
                end = start
                continue
            while end < TOTAL_SLOT - 1 and whoIsBusy[end + 1] == whoIsBusy[end]:
                end += 1
            meetings.append([start, end, numE - busyTimes[start]])
            start, end = end + 1, end + 1
        meetings.sort(key=lambda pair: (-1 * pair[2], pair[0]))
        res = []
        if len(meetings) < num_slots:
            return res
        for i in range(num_slots):
            currMeeting = ""
            startHour = meetings[i][0] // 4
            startMinutes = meetings[i][0] % 4 * 15
            endHour = meetings[i][1] // 4
            endMinutes = meetings[i][1] % 4 * 15 + 15
            if endMinutes == 60:
                endMinutes = 0
                endHour += 1
            if startHour < 10:
                currMeeting += "0"
            currMeeting += str(startHour) + ":"
            if startMinutes < 15:
                currMeeting += "0"
            currMeeting += str(startMinutes) + "-"
            if endHour < 10:
                currMeeting += "0"
            currMeeting += str(endHour) + ":"
            if endMinutes < 15:
                currMeeting += "0"
            currMeeting += str(endMinutes)
            res.append(currMeeting)
        res.sort()
        return res

    print(find_meeting_slots(2, [["00:00-05:30"], ["05:30-05:45"], ["05:45-06:00"]]))
    # print(find_meeting_slots(3, [["00:00-05:30"], ["00:00-05:00", "08:00-22:00"], ["00:00-12:30"]]))

    # print(find_meeting_slots(1, [["00:00-24:00"], ["00:00-12:30"], ["00:00-12:30"]]))
    # print(find_meeting_slots(2, [["08:00-12:30", "17:00-22:00"], ["07:00-14:30", "16:00-19:00"],
    #                             ["08:00-14:30", "17:00-19:00"]]))
    # 0 - 7, 14:30-16:00
    # res.sort(key=lambda pair: (int(pair[0]) * 10 + int(pair[1]) * 4 + (int(pair[3]) * 10 + int(pair[4])) // 15))
