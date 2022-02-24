c,p = map(int,input().split())
contributers  = []
projects = []
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
class project():
    def _init_(self):
        self.name = ""
        self.days = 0
        self.score = 0
        self.best = 0
        self.roles=0
        self.jobs= {}

for i in range(p):
    projects.append(project())
    current = list(input().split(" "))
<<<<<<< Updated upstream
    projects[i].name = current[0]
    projects[i].days = current[1]
    projects[i].score =current[2]
    projects[i].best = current[3]
    projects[i].roles = current[4]
    for j in range(current[4]):
        job = list(input().split(" "))
        project[i].jobs[job[0]] = int(job[1])

=======
    project[i].name = current[0]
    project[i].days = current[1]
    project[i].score =current[2]
    project[i].best = current[3]

for i in range(c):
    print("hi")
class Person():
  name = ""
  skills = {}
  
>>>>>>> Stashed changes
