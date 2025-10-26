jobs = {
    1: [0, 4],
    2: [1, 2],
    3: [2, 4],
    4: [3, 5],
    5: [3, 6],
    6: [5, 6],
    7: [5, 7],
    8: [6, 7],
    9: [7, 9],
    10: [8, 10]
}
def optimalSchedule(jobs):
    jobs_list = list(jobs.items())
    jobs_list.sort(key=lambda item: item[1][1]) #nlogn 
    A = {}
    lastEndTime = 0
    for j in jobs_list: #n
        jobId = j[0]
        startTime = j[1][0]
        endTime = j[1][1]
        if startTime >= lastEndTime:
            A[jobId] = [startTime, endTime]
            lastEndTime = endTime
    return A
optimizedSchedule = optimalSchedule(jobs)
print(f"This is the best schedule to go for: {optimizedSchedule}")
