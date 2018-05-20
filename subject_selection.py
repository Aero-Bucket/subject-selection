import csv


x1={"None":[],
    "economics":[],
    "geography":[],
    "chemistry":[],
    "physics":[],
    }

x2={"bafs":[],
    "biology":[],
    "chistory":[],
    "economics":[],
    "ict":[],
    "physics":[],
    }

x3={"biology":[],
    "chemistry":[],
    "cliterature":[],
    "geography":[],
    "history":[],
    "va":[],
    "m2":[],
    }

subject_column=["x1","x2","x3"]

preference_column=["pref1","pref2","pref3","pref4","pref5","pref6",
                    "pref7","pref8","pref9","pref10","pref11","pref12"]

subject_reference={"x1":x1,
                    "x2":x2,
                    "x3":x3,
                    }


with open("/home/aerobucket/python/testing/random_subject.csv") as subject:
    csvreader=list(csv.DictReader(subject,delimiter=","))
    
    name_to_score={}
    average=[]
    name_list=[]

    for row in csvreader:
        name_to_score[float(row["average"])]=row["name"]
        average.append(float(row["average"]))
        name_list.append(row["name"])
   
    run_times=len(average)

    # execute for every person
    for i in range(run_times):

        max_score=max(average)
        name=name_to_score[max_score] # find the person with higher marks

        # find the correct row 
        for row in csvreader:
            
            if row["name"] == name:

                # append electives to the classes
                for elective in subject_column:
                    subj=row[elective]
                    
                    # check for people in the class
                    if len(subject_reference[elective][subj]) < 28:
                        subject_reference[elective][subj].append(name)  
                    
                    else:
                        for preference in preference_column:
                            subj_1=row[preference]
                            
                            if subj_1 in subject_reference[elective].keys() == True:
                                if len(subject_reference[elective][subj_1]) < 28:
                                    subject_reference[elective][subj_1].append(name)
                                    break 

        average.remove(max_score)
        

results_header=["name","x1","x2","x3"]


with open("results.csv","w") as results:
    result_writer=csv.DictWriter(results,fieldnames=results_header)
    result_writer.writeheader()
    
    for n in name_list:
        
        row_dict={"name":n,}
        
        for elective_name,elective in subject_reference.items():
            
            for subject_name,subject in elective.items():
                
                if n in subject:
                    row_dict[elective_name]=subject_name
                
        result_writer.writerow(row_dict)
                    
                
                

                    















