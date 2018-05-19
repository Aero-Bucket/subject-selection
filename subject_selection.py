import csv

with open("/home/aerobucket/python/testing/subject.csv") as subject:
    csvreader=list(csv.DictReader(subject,delimiter=","))
    
    classes={"physics":[],
             "chemistry":[],
             "biology":[],
             "economics":[],
             "history":[],
             "mathematics":[],
             }

    name_to_score={}
    average=[]


    for row in csvreader:
        name_to_score[int(row["average"])]=row["name"]
        average.append(int(row["average"]))
    print(name_to_score)
    print(average)
    

    subject_column=["x1","x2","x3"]
    preference_column=["preference1","preference2","preference3","preference4","preference5","preference6"]
    run_times=len(average)

    # execute for every person
    # the one with higher marks will select the electives first
    for i in range(run_times):

        max_score=max(average)
        name=name_to_score[max_score]

        # find the correct row       
        for row in csvreader:
            
            if row["name"] == name:

                # append electives to the classes
                for elective in subject_column:
                    sub=row[elective]
                    
                    # check for people in the class
                    if len(classes[sub]) < 3:
                        classes[sub].append(name)  
                    
                    else:
                        for preference in preference_column:
                            sub_1=row[preference]
                            
                            if len(classes[sub_1]) < 3 :
                                classes[sub_1].append(name)
                                break 

        average.remove(max_score)
        
    print(classes)