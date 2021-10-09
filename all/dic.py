# student_scores = {"ismail": 15.29, "yassine": 14, "hamza1": 17, "zakariya": 18.5, "hamza": 18}
# student_grades = dict()
# for n in student_scores:
#     if 20>student_scores[n]>=17:
#         student_grades[n]="tres bien "
#     elif 17>student_scores[n]>=15:
#         student_grades[n]="bien"
#     else:
#         student_grades[n]="assez bien "
# 
# print(student_grades)


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_counter(counter,citites,total_visetde):
    new_country={}
    new_country["country"]=counter
    new_country["visits"]=citites
    new_country["visits"]=total_visetde
    travel_log.append(new_country)
add_counter("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)