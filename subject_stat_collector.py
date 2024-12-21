import os, csv

class data_subject():
    def __init__ (self, gender, hand, build, age):
        self.gender = gender
        self.hand = hand
        self.build = build
        self.age = age

base_dir = "/home/abdul/GRWD/Gyronics Dataset"


data = {}
for subject_dir in os.listdir(base_dir):
    subject_path = os.path.join(base_dir, subject_dir)
    if os.path.isdir(subject_path):
        info_path =  os.path.join(subject_path, "info.txt")
        if os.path.isfile(info_path):
            gender = "NA"
            build = "NA"
            hand = "NA"
            age = "NAN"


            with open(info_path, 'r') as file:
                for line in file:
                    if "Male" in line:
                        gender = "M"
                    elif "Female" in line:
                        gender = "F"
                    
                    if "Slim" in line:
                        build = "Slim"
                    elif "Medium" in line:
                        build = "Medium"
                    elif "Buff" in line:
                        build = "Buff"
                    
                    if "RH" in line:
                        hand = "RH"
                    elif "LH" in line:
                        hand = "LH"

                    if "Age" in line:
                        key, value = line.strip().replace(" ", "").split(":")
                        if key.lower() == "age":
                            if value.isdigit():
                                age = int(value)
                            else:
                                print("Age Error: Value = "+ value)
                    
                    dp = data_subject(gender, hand, build, age)
                    data[subject_dir] = dp


sorted_data = {key: value for key, value in sorted(data.items(), key=lambda x: int(x[0].split('_')[1]))}
output_file = "Gyronics_data_subjects.csv"

# Open CSV file for writing
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["subject_dir", "gender", "hand", "build", "age"])
    
    # Write the data rows
    for subject_dir, dp in sorted_data.items():
        writer.writerow([subject_dir, dp.gender, dp.hand, dp.build, dp.age])