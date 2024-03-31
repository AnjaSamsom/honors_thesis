import csv
from csv import DictReader
 
filename ="survey/data_cleaned.csv"
 
with open(filename, "r", encoding="utf-8") as f:
    dict_reader = DictReader(f)
    list_of_dicts = list(dict_reader)


def teacher_gender():
    female = 0
    male = 0
    nonbinary = 0
    agender = 0
    other = 0
    for response in list_of_dicts:
        gender = response["What was the gender of the first person who taught you computer science? - Selected Choice"]
        if gender == "Female":
            female += 1
        elif gender == "Male":
            male += 1
        elif gender == "Non-binary":
            nonbinary += 1
        elif gender == "Agender":
            agender += 1
        elif gender == "Other (please describe)":
            other += 1
            gender_description = response["What was the gender of the first person who taught you computer science? - Other (please describe) - Text"]
            print(gender_description)
        else:
            other += 1
            gender_description = response["What was the gender of the first person who taught you computer science? - Other (please describe) - Text"]
            print(gender_description)
    print("Female: " + str(female))
    print("Male: " + str(male))
    print("Non-binary: " + str(nonbinary))
    print("Agender: " + str(agender))
    print("Other (please describe): " + str(other))

def respondent_gender():
    female = 0
    male = 0
    nonbinary = 0
    agender = 0
    other = 0
    for response in list_of_dicts:
        gender = response["Gender - Selected Choice"]
        if gender == "Female":
            female += 1
        elif gender == "Male":
            male += 1
        elif gender == "Non-binary":
            nonbinary += 1
        elif gender == "Agender":
            agender += 1
        elif gender == "Other (please describe)":
            other += 1
            gender_description = response["Gender - Other (please describe) - Text"]
            print(gender_description)
        else:
            other += 1
            gender_description = response["Gender - Other (please describe) - Text"]
            print(gender_description)
    print("Female: " + str(female))
    print("Male: " + str(male))
    print("Non-binary: " + str(nonbinary))
    print("Agender: " + str(agender))
    print("Other (please describe): " + str(other))

def professor_continue_with_cs(gender):
    yes = 0
    no = 0
    total = 0
    for response in list_of_dicts:
        teacher_gender = response["What was the gender of the first person who taught you computer science? - Selected Choice"]
        continued = response["After this first class/experience, did you continue with computer science classes or \nprograms?"]
        
        if teacher_gender == gender:
            if continued == "Yes":
                yes += 1
            elif continued == "No":
                no +=1


    total = yes + no
    print(gender)
    print(total)
    print("Yes = " + str(yes/total))
    print("No = " + str(no/total))

def continue_with_cs(student_gender):
    yes_same = 0
    no_same = 0
    same_gender = 0

    yes_dif = 0
    no_dif = 0
    no = 0
    different_gender = 0
    for response in list_of_dicts:
        respondent_gender = response["Gender - Selected Choice"]
        teacher_gender = response["What was the gender of the first person who taught you computer science? - Selected Choice"]
        continued = response["After this first class/experience, did you continue with computer science classes or \nprograms?"]
        # same gender
        if respondent_gender == student_gender and teacher_gender == student_gender:
            same_gender += 1
            if continued == "Yes":
                yes_same += 1
            elif continued == "No":
                no_same += 1
        elif respondent_gender == student_gender and teacher_gender != student_gender:
            different_gender += 1
            if continued == "Yes":
                yes_dif += 1
            elif continued == "No":
                no_dif += 1

    print(student_gender)
    if same_gender != 0:
        print(student_gender + " students with "+ student_gender + " professors: " + str(same_gender))
        print("same gender professor, continued (Yes): " + str(100*yes_same/same_gender) + "%")
        print("same gender professor, didn't continue (No): " + str(100*no_same/same_gender) + "%")
    else:
        print("No students reported professors of their same gender")

    print()
    if different_gender != 0:
        print(student_gender + " students with professors of a different gender: " + str(different_gender))
        print("different gender professor, continued (Yes): " + str(100*yes_dif/different_gender) + "%")
        print("different gender professor, didn't continue (No): " + str(100*no_dif/different_gender) + "%")

def professor_interest_increase(gender):
    more = 0
    same = 0
    less = 0
    total = 0
    for response in list_of_dicts:
        teacher_gender = response["What was the gender of the first person who taught you computer science? - Selected Choice"]
        interest_after = response["Were you more interested, less interested, or had the same amount of interest in \ncomputer science after your first class / experience with CS?"]
        
        if teacher_gender == gender:
            if interest_after == "More interested":
                more += 1
            elif interest_after == "Same interest level":
                same +=1
            elif interest_after == "Less interested":
                less += 1

    total = more + same + less
    print(total)
    print(gender)
    print("More = " + str(more/total))
    print("Same = " + str(same/total))
    print("Less = " + str(less/total))

def interest_increase(student_gender):
    same_gender = 0
    different_gender = 0

    s_more = 0
    s_less = 0
    s_same = 0

    d_more = 0
    d_less = 0
    d_same = 0
    for response in list_of_dicts:
        respondent_gender = response["Gender - Selected Choice"]
        teacher_gender = response["What was the gender of the first person who taught you computer science? - Selected Choice"]
        interest_after = response["Were you more interested, less interested, or had the same amount of interest in \ncomputer science after your first class / experience with CS?"]
        
        # same gender
        if respondent_gender == student_gender and teacher_gender == student_gender:
            same_gender += 1
            if interest_after == "More interested":
                s_more +=1
            elif interest_after == 'Less interested':
                s_less += 1
            elif interest_after == "Same interest level":
                s_same += 1

        elif respondent_gender == student_gender and teacher_gender != student_gender:
            different_gender += 1
            if interest_after == "More interested":
                d_more +=1
            elif interest_after == 'Less interested':
                d_less += 1
            elif interest_after == "Same interest level":
                d_same += 1

    if same_gender != 0:
        print(student_gender + " students with "+ student_gender + " professors: " + str(same_gender))
        print("same gender professor, more interested in CS: " + str(100*s_more/same_gender) + "%")
        print("same gender professor, less interested in CS: " + str(100*s_less/same_gender) + "%")
        print("same gender professor, same interest in CS: " + str(100*s_same/same_gender) + "%")
    else:
        print("No students reported professors of their same gender")

    print()
    if different_gender != 0:
        print(student_gender + " students with professors of a different gender: " + str(different_gender))
        print("different gender professor, more interested in CS: " + str(100*d_more/different_gender) + "%")
        print("different gender professor, less interested in CS: " + str(100*d_less/different_gender) + "%")
        print("different gender professor, same interest in CS: " + str(100*d_same/different_gender) + "%")

def perceived_importance_categorize():
    no = []
    yes = []
    maybe = []
    for response in list_of_dicts:
        importance = response["Do you think the gender of your instructor impacted your choice to continue to study (or \nnot study) computer science?"]
        if "yes" in importance.lower():
            yes.append(response)
        elif "no" in importance.lower():
            no.append(response)
        elif "maybe" in importance.lower():
            maybe.append(response)      
        else:
            print(importance)
            choice = input()
            if choice == "yes":
                yes.append(response)
            elif choice == "no":
                no.append(response)
            elif choice == "maybe":
                maybe.append(response)
    # female
    f_yes, f_no, f_maybe = 0,0,0
    #male
    m_yes, m_no, m_maybe = 0,0,0
    #non binary
    n_yes, n_no, n_maybe = 0,0,0
    # agender
    a_yes, a_no, a_maybe = 0,0,0
    #self describe
    s_yes, s_no, s_maybe = 0,0,0


    for response in yes:
        respondent_gender = response["Gender - Selected Choice"]
        if respondent_gender == "Female":
            f_yes +=1
        elif respondent_gender == "Male":
            m_yes +=1
        elif respondent_gender == "Non-binary":
            n_yes +=1        
        elif respondent_gender == "Agender":
            a_yes +=1        
        elif respondent_gender == "Other (please describe)":
            s_yes +=1
    for response in no:
        respondent_gender = response["Gender - Selected Choice"]
        if respondent_gender == "Female":
            f_no +=1
        elif respondent_gender == "Male":
            m_no +=1
        elif respondent_gender == "Non-binary":
            n_no +=1        
        elif respondent_gender == "Agender":
            a_no +=1        
        elif respondent_gender == "Other (please describe)":
            s_no +=1

    for response in maybe:
        respondent_gender = response["Gender - Selected Choice"]
        if respondent_gender == "Female":
            f_maybe +=1
        elif respondent_gender == "Male":
            m_maybe +=1
        elif respondent_gender == "Non-binary":
            n_maybe +=1        
        elif respondent_gender == "Agender":
            a_maybe +=1        
        elif respondent_gender == "Other (please describe)":
            s_maybe +=1
    
    
    f_total = f_yes + f_no + f_maybe
    m_total = m_yes + m_no + m_maybe
    n_total = n_yes + n_no + n_maybe
    a_total = a_yes + a_no + a_maybe
    s_total = s_yes + s_no + s_maybe

    print("Female")
    print("yes" + str(f_yes/f_total))
    print("no" + str(f_no/f_total))
    print("maybe" + str(f_maybe/f_total))

    print("Male")
    print("yes" + str(m_yes/m_total))
    print("no" + str(m_no/m_total))
    print("maybe" + str(m_maybe/m_total))

    print("Non Binary")
    print("yes" + str(n_yes/n_total))
    print("no" + str(n_no/n_total))
    print("maybe" + str(n_maybe/n_total))

    print("Agender")
    print("yes" + str(a_yes/a_total))
    print("no" + str(a_no/a_total))
    print("maybe" + str(a_maybe/a_total))

    print("Self describe")
    print("yes" + str(s_yes/s_total))
    print("no" + str(s_no/s_total))
    print("maybe" + str(s_maybe/s_total))




    
perceived_importance_categorize()


""" interest_increase("Female")
interest_increase("Male")
interest_increase("Non-binary")
interest_increase("Agender")
interest_increase("Other (please describe)") """

""" professor_interest_increase("Female")
professor_interest_increase("Male") """


""" continue_with_cs("Female")
continue_with_cs("Male")
continue_with_cs("Non-binary")
continue_with_cs("Agender")
continue_with_cs("Other (please describe)")  """

"""
professor_continue_with_cs("Female")
professor_continue_with_cs("Male")
"""

""" respondent_gender() 
teacher_gender() """




    