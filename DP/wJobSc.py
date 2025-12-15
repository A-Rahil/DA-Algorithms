def findP(jobs):
    newJobs = sorted(jobs.items(),  key=lambda x:x[1][1])
    p = {}
    for i in range(len(newJobs)):
        startTime = newJobs[i][1][0]
        p[i] = 0
        for j in range(i - 1, -1, -1):
            if newJobs[j][1][1] <= startTime:
                p[i] = j
                break
    return p, newJobs

def findOpt(jobs, p):
    n = len(jobs)
    opt = [0] * n
    opt[0] = jobs[0][1][2]
    for i in range(1, n):
        currProfit = jobs[i][1][2]
        lastCompat = p[i]
        incProfit = currProfit + opt[lastCompat]
        excProfit = opt[i-1]
        opt[i] = max(incProfit, excProfit)
    return opt
def backTrack(jobs, p, opt):
    selectedJobs = []
    benefit = 0
    i = len(opt) - 1
    while i > 0:
        if opt[i] != opt[i - 1]:
            jobID = jobs[i][0]
            currBenefit = jobs[i][1][2]
            benefit += currBenefit
            selectedJobs.append(jobID)
            i = p[i]
        else:
            i -= 1
    return selectedJobs[::-1], benefit

def WJobScheduling(jobs):
    compatibleJobs, sortedJobs = findP(jobs)
    opt = findOpt(sortedJobs, compatibleJobs)
    print(f"Selected jobs: {backTrack(sortedJobs, compatibleJobs, opt)}")

jobs = {
    # [start, end, benefit]
    0: [0, 0, 0],
    1: [0, 4, 15],
    2: [1, 2, 10],
    3: [2, 4, 20],
    4: [3, 5, 5],
    5: [3, 6, 25],
    6: [5, 6, 30],
    7: [5, 7, 20],
    8: [6, 7, 50],
    9: [7, 9, 15],
    10: [8, 10, 60]
}

WJobScheduling(jobs)