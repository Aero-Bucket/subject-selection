import csv
import random

names=["Mike","James","May","Steve","Peter","Mary","George",
       "William","Oscar","Harry","Lily","Jessica","Emily"]

surnames=["Lee","Wong","Ng","Chan","Ho",
          "Cheng","Tze","Kwok","Hong","Yuen"]

x1=["None","economics","geography","chemistry","physics"]

x2=["bafs","biology","chistory","economics","ict","physics"]

x3=["biology","chemistry","cliterature","geography","history","va","m2"]

all_subjects=["economics","geography","chemistry","physics","bafs","biology",
              "chistory","ict","cliterature","history","va","m2"]

fields=["name","average","x1","x2","x3",
        "pref1","pref2","pref3","pref4","pref5","pref6",
        "pref7","pref8","pref9","pref10","pref11","pref12"]

prefs_field=["pref1","pref2","pref3","pref4","pref5","pref6",
        "pref7","pref8","pref9","pref10","pref11","pref12"]

electives_field=["x1","x2","x3"]


with open("random_subject.csv","w") as rsub:
    writer=csv.DictWriter(rsub,fieldnames=fields)
    writer.writeheader()

    for n in names:
        for s in surnames:
            random.shuffle(all_subjects)
            pref_dict=dict(zip(prefs_field,all_subjects))

            breaker=True
            while breaker:
                first=random.choice(x1)
                second=random.choice(x2)
                third=random.choice(x3)
                
                if first != second != third:
                    elective_list=[first,second,third]
                    elective_dict=dict(zip(electives_field,elective_list))
                    breaker=False
                
            csv_dict={"name":f"{n} {s}",
                      "average":round(random.uniform(0,100),2),
                      "x1":random.choice(x1),
                      "x2":random.choice(x2),
                      "x3":random.choice(x3),
                     }
            csv_dict.update(pref_dict)
            csv_dict.update(elective_dict)
            
            writer.writerow(csv_dict)

