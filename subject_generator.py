import csv
import random

names=["Mike","James","May","Steve","Peter","Mary","George",
       "William","Oscar","Harry","Lily","Jessica","Emily"]

surnames=["Lee","Wong","Ng","Chan","Ho",
          "Cheng","Tze","Kwok","Hong","Yuen"]

x1=["None","economics_1","geography_1","chemistry_1","physics_1"]

x2=["bafs","biology_2","chistory","economics_2","ict","physics_2"]

x3=["biology_3","chemistry_3","cliterature","geography_3","history","va","m2"]

all_subjects=["economics","geography","chemistry","physics","bafs","biology",
              "chistory","ict","cliterature","history","va","m2"]

fields=["name","average","x1","x2","x3",
        "pref1","pref2","pref3","pref4","pref5","pref6",
        "pref7","pref8","pref9","pref10","pref11","pref12"]

prefs=["pref1","pref2","pref3","pref4","pref5","pref6",
        "pref7","pref8","pref9","pref10","pref11","pref12"]


with open("random_subject.csv","w") as rsub:
    writer=csv.DictWriter(rsub,fieldnames=fields)
    writer.writeheader()

    for n in names:
        for s in surnames:
            random.shuffle(all_subjects)
            pref_dict=dict(zip(prefs,all_subjects))

            csv_dict={"name":n+" "+s,
                      "average":round(random.uniform(0,100),2),
                      "x1":random.choice(x1),
                      "x2":random.choice(x2),
                      "x3":random.choice(x3),
                     }
            csv_dict.update(pref_dict)
            
            writer.writerow(csv_dict)

