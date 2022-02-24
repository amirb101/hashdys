c,p = map(int,input().split())
contributers  = []
projects = []

class person():
    def __init__(self):
        self.name=""
        self.skills={}

class project():
    def __init__(self):
        self.name = ""
        self.days = 0
        self.score = 0
        self.best = 0
        self.roles = 0
        self.jobs = {}

for i1 in range(c):
    contributers.append(person())
    pers = list(input().split(" "))
    contributers[i1].name = pers[0]
    for i2 in range(int(pers[1])):
        qual = list(input().split(" "))
        contributers[i1].jobs[qual[0]] = int(qual[1])

for i in range(p):
    projects.append(project())
    current = list(input().split(" "))
    projects[i].name = current[0]
    projects[i].days = current[1]
    projects[i].score =current[2]
    projects[i].best = current[3]
    projects[i].roles = current[4]
    for j in range(current[4]):
        job = list(input().split(" "))
        project[i].jobs[job[0]] = int(job[1])
