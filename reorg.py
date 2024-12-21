import os
import shutil

# Original directory structure
original_dir = "/home/abdul/GRWD/Gyronics Reorg"  # Path to the existing 'subject' directory

# New root directory where you want to reorganize (e.g., "gesture_directory")
new_root_dir = "/home/abdul/GRWD/Gyronics Gestureset"

# Iterate through the original structure
for subject_dir in os.listdir(original_dir):
    subject_path = os.path.join(original_dir, subject_dir)
    
    if os.path.isdir(subject_path):  # Ensure we are dealing with a subject directory
        # Iterate through the gestures in the subject directory
        for gesture_dir in os.listdir(subject_path):
            gesture_path = os.path.join(subject_path, gesture_dir)
            
            if os.path.isdir(gesture_path):  # Ensure we are dealing with a gesture directory
                # Create the target gesture directory in the new structure if it doesn't exist
                new_gesture_dir = os.path.join(new_root_dir, gesture_dir)
                if not os.path.exists(new_gesture_dir):
                    os.makedirs(new_gesture_dir)
                
                # Create the subject directory inside the corresponding gesture directory
                new_subject_dir = os.path.join(new_gesture_dir, subject_dir)
                if not os.path.exists(new_subject_dir):
                    os.makedirs(new_subject_dir)
                
                # Copy or move the contents of the subject directory into the new structure
                for item in os.listdir(gesture_path):
                    source_item = os.path.join(gesture_path, item)
                    target_item = os.path.join(new_subject_dir, item)
                    if os.path.isdir(source_item):
                        shutil.copytree(source_item, target_item)  # Copy subdirectories (if any)
                    else:
                        shutil.copy2(source_item, target_item)  # Copy files (including CSV files)

                # Now, move the 10 CSV files from the subject directory to the new subject directory
                for csv_file in os.listdir(subject_path):
                    if csv_file.endswith(".csv"):  # Check for CSV files
                        source_csv = os.path.join(subject_path, csv_file)
                        target_csv = os.path.join(new_subject_dir, csv_file)
                        shutil.copy2(source_csv, target_csv)  # Copy the CSV file to the new subject directory

print("Directory reorganization complete!")
