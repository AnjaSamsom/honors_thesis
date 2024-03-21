import csv
from csv import DictReader
 
filename ="survey/data_cleaned.csv"
 
with open(filename, "r", encoding="utf-8") as f:
    dict_reader = DictReader(f)
    list_of_dicts = list(dict_reader)


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
    
    if respondent_gender == "Female" and teacher_gender == "Female":
        same_gender += 1
        if interest_after == "More interested":
            s_more +=1
        elif interest_after == 'Less interested':
            s_less += 1
        elif interest_after == "Same interest level":
            s_same += 1

    elif respondent_gender == "Female" and teacher_gender != "Female":
        different_gender += 1
        if interest_after == "More interested":
            d_more +=1
        elif interest_after == 'Less interested':
            d_less += 1
        elif interest_after == "Same interest level":
            d_same += 1

print("Female students with female professors: " + str(same_gender))
print("same gender professor, more interested in CS: " + str(100*s_more/same_gender) + "%")
print("same gender professor, less interested in CS: " + str(100*s_less/same_gender) + "%")
print("same gender professor, same interest in CS: " + str(100*s_same/same_gender) + "%")

print()
print("Female students with professors of a different gender: " + str(different_gender))
print("different gender professor, less interested in CS: " + str(100*d_more/different_gender) + "%")
print("different gender professor, less interested in CS: " + str(100*d_less/different_gender) + "%")
print("different gender professor, same interest in CS: " + str(100*d_same/different_gender) + "%")



  