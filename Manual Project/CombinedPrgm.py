import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing in the directory."""
    pass

def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    total_fee = tuition_fee + hostel_fee + transportation_fee
    return total_fee

def main_dashboard():
    while True:
        print("\n" + "="*50)
        print("  SMART CAMPUS INFORMATION SYSTEM DASHBOARD  ")
        print("="*50)
        print("1. Student Registration and Grade Evaluation")
        print("2. Course Enrollment Management System ")
        print("3. Student Record Data Management via Sets")
        print("4. Sorting and Searching of Student IDs")
        print("5. Student Fee Calculation using Functions")
        print("6. File Handling for Student Academic Records")
        print("7. Directory Scanning with Exception Handling")
        print("8. Student Performance Analysis")
        print("9. Exit System")
        print("="*50)
        
        choice = input("Enter your choice (1-9): ").strip()
        
        # ------------------------------------------
        # Student Registration & Grade Evaluation
        # ------------------------------------------
        if choice == "1":
            print("\n--- Student Registration & Grade Evaluation ---")
            student_name = input("Enter student name: ")
            score = float(input("Enter exam score (0-100): "))
            
            if score >= 90 and score <= 100:
                grade = "A"
                remark = "Excellent"
            elif score >= 75:
                grade = "B"
                remark = "Very Good"
            elif score >= 60:
                grade = "C"
                remark = "Good"
            elif score >= 40:
                grade = "D"
                remark = "Average"
            else:
                grade = "F"
                remark = "Needs Improvement"
                
            print("\n--- Student Report ---")
            print("Name:", student_name)
            print("Score:", score)
            print("Grade:", grade)
            print("Performance Remark:", remark)

        # ------------------------------------------
        # Course Enrollment Management System
        # ------------------------------------------
        elif choice == "2":
            print("\n--- Course Enrollment Management System ---")
            courses = []  # list to store (course name, credits)
            max_courses = 5
            print(" Course Enrollment System ")
            
            while True:
                if len(courses) >= max_courses:
                    print("Maximum course limit reached!")
                    break
                
                course_name = input("Enter course name (or 'done' to finish): ")
                if course_name.lower() == "done":
                    break
                    
                credits = input("Enter credit value: ")
                
                if not credits.isdigit():
                    print("Invalid credit value! Skipping entry...")
                    continue
                    
                credits = int(credits)
                if credits <= 0:
                    print("Credit must be positive! Skipping entry...")
                    continue
                    
                courses.append((course_name, credits))
                print(f"Course '{course_name}' with {credits} credits added.\n")
                
            print("\n--- Enrollment Report ---")
            for course, credit in courses:
                print(f"Course: {course}, Credits: {credit}")
            print("Total courses enrolled:", len(courses))

        # ------------------------------------------
        # Student Record Data Management using Data Structures
        # ------------------------------------------
        elif choice == "3":
            print("\n--- Student Record & Event Analysis ---")
            students = []
            students.append({"name": "Priya", "age": 20, "grades": [85, 90, 78]})
            students.append({"name": "Rahul", "age": 21, "grades": [72, 88, 91]})
            students.append({"name": "Anita", "age": 19, "grades": [95, 89, 92]})
            
            print("\n   Student Records   ")
            for student in students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Grades:", student["grades"])
                print("-----------------------")
                
            event_A = {"Priya", "Rahul", "Anita", "Kiran"}
            event_B = {"Rahul", "Anita", "Sneha"}
            
            common_participants = event_A & event_B
            all_participants = event_A | event_B
            only_event_A = event_A - event_B
            
            print("\n== Event Participation Analysis ==")
            print("Common Participants:", common_participants)
            print("All Participants:", all_participants)
            print("Only Event A Participants:", only_event_A)

        # ------------------------------------------
        # Sorting and Searching of Student IDs
        # ------------------------------------------
        elif choice == "4":
            print("\n--- Sorting and Searching Student IDs ---")
            student_ids = [105, 102, 110, 108, 101, 115]
            print("Original IDs:", student_ids)
            
            # Bubble Sort Implementation
            n = len(student_ids)
            for i in range(n):
                for j in range(0, n-i-1):
                    if student_ids[j] > student_ids[j+1]:
                        temp = student_ids[j]
                        student_ids[j] = student_ids[j+1]
                        student_ids[j+1] = temp
            print("Sorted IDs (Bubble Sort):", student_ids)
            
            # Selection Sort Implementation
            student_ids2 = [105, 102, 110, 108, 101, 115]
            n = len(student_ids2)
            for i in range(n):
                min_index = i
                for j in range(i+1, n):
                    if student_ids2[j] < student_ids2[min_index]:
                        min_index = j
                temp = student_ids2[i]
                student_ids2[i] = student_ids2[min_index]
                student_ids2[min_index] = temp
            print("Sorted IDs (Selection Sort):", student_ids2)
            
            # Target Selection and Searches
            target = 108
            found_index = -1
            
            # Linear Search Implementation
            for i in range(len(student_ids)):
                if student_ids[i] == target:
                    found_index = i
                    break
            if found_index != -1:
                print("Linear Search: ID", target, "found at index", found_index)
            else:
                print("Linear Search: ID not found")
                
            # Binary Search Implementation
            low = 0
            high = len(student_ids) - 1
            found_index = -1
            while low <= high:
                mid = (low + high) // 2
                if student_ids[mid] == target:
                    found_index = mid
                    break
                elif student_ids[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            if found_index != -1:
                print("Binary Search: ID", target, "found at index", found_index)
            else:
                print("Binary Search: ID not found")

        # ------------------------------------------
        # Student Fee Calculation using Functions
        # ------------------------------------------
        elif choice == "5":
            print("\n--- Student Fee Calculation ---")
            tuition = 50000
            hostel = 30000
            transport = 10000
            
            total1 = calculate_fee(tuition)
            print("Total Fee (Tuition only):", total1)
            
            total2 = calculate_fee(tuition, hostel_fee=hostel)
            print("Total Fee (Tuition + Hostel):", total2)
            
            total3 = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)
            print("Total Fee (Tuition + Hostel + Transport):", total3)

        # ------------------------------------------
        # File Handling for Student Academic Records
        # ------------------------------------------
        elif choice == "6":
            print("\n--- File Handling Management ---")
            # Step 1: Write entries to a file
            with open("student_records.txt", "w") as file:
                file.write("ID, Name, Marks\n")
                file.write("101, Arjun,85\n")
                file.write("102, Meera,92\n")
                file.write("103, Ravi, 76\n")
                file.write("104,Anita,89\n")
            print("Student records written to file successfully.")
            
            # Step 2: Read records back out
            print("\nReading stored records:")
            with open("student_records.txt", "r") as file:
                records = file.readlines()
            for record in records:
                print(record.strip())
                
            # Step 3: Process and compile report data metrics
            print("\nGenerating Report:")
            total_students = 0
            total_marks = 0
            highest_marks = -1
            top_student = ""
            
            for record in records[1:]:
                parts = record.strip().split(",")
                name = parts[1].strip()
                marks = int(parts[2].strip())
                
                total_students += 1
                total_marks += marks
                if marks > highest_marks:
                    highest_marks = marks
                    top_student = name
                    
            average_marks = total_marks / total_students
            print("Total Students:", total_students)
            print("Average Marks:", average_marks)
            print("Top Student:", top_student, "with", highest_marks, "marks")

        # ------------------------------------------
        # Directory Scanning with Exception Handling
        # ------------------------------------------
        elif choice == "7":
            print("\n--- Directory Scanning & Custom Exception ---")
            directory_path = input("Enter the directory path to scan: ").strip()
            
            try:
                if not os.path.exists(directory_path):
                    raise FileNotFoundError(f"Invalid directory path: {directory_path}")
                print(f"\nScanning directory: {directory_path}\n")
                
                for root, dirs, files in os.walk(directory_path):
                    level = root.replace(directory_path, "").count(os.sep)
                    indent = " " * 4 * level
                    print(f"{indent}{os.path.basename(root)}/")
                    
                    sub_indent = " " * 4 * (level + 1)
                    for f in files:
                        print(f"{sub_indent}{f}")
                        
                    if not files and not dirs:
                        raise MissingFileOrFolderError(f"Empty folder detected: {root}")
                        
            except FileNotFoundError as e:
                print(f"Error: {e}")
            except MissingFileOrFolderError as e:
                print(f"Custom Error: {e}")
            except Exception as e:
                print(f"Unexpected Error: {e}")

        # ------------------------------------------
        # Student Performance Analysis (Data Science Stack)
        # ------------------------------------------
        elif choice == "8":
            print("\n--- Data Science Stack Performance Analysis ---")
            
            # Automated helper generation to make sure 'student_performance.csv' exists safely 
            if not os.path.exists("student_performance.csv"):
                print("[System Info] Generating a mock 'student_performance.csv' file for analysis verification...")
                mock_df = pd.DataFrame({
                    "Name": ["Arjun", "Meera", "Ravi", "Anita"],
                    "Math": [85, 92, 76, 89],
                    "Science": [78, 95, 81, 90],
                    "English": [90, 88, 85, 92]
                })
                mock_df.to_csv("student_performance.csv", index=False)

            try:
                df = pd.read_csv("student_performance.csv")
                print("\n--- Raw Data ---")
                print(df.head())
                
                print("\n--- Statistical Summary ---")
                print(df.describe())
                
                scores = df[["Math", "Science", "English"]].to_numpy()
                mean_scores = np.mean(scores, axis=0)
                median_scores = np.median(scores, axis=0)
                std_dev_scores = np.std(scores, axis=0)
                
                print("\n--- NumPy Analysis ---")
                print(f"Mean Scores (Math, Science, English): {mean_scores}")
                print(f"Median Scores (Math, Science, English): {median_scores}")
                print(f"Standard Deviation (Math, Science, English): {std_dev_scores}")
                
                top_math = df.loc[df["Math"].idxmax(), "Name"]
                top_science = df.loc[df["Science"].idxmax(), "Name"]
                top_english = df.loc[df["English"].idxmax(), "Name"]
                
                print("\n--- Top Performers ---")
                print(f"Math: {top_math}")
                print(f"Science: {top_science}")
                print(f"English: {top_english}")
                
                # Visualizations
                subjects = ["Math", "Science", "English"]
                
                # Plot 1: Average scores per subject
                plt.figure()
                plt.bar(subjects, mean_scores, color=["blue", "green", "orange"])
                plt.title("Average Scores per Subject")
                plt.xlabel("Subjects")
                plt.ylabel("Average Score")
                plt.show()
                
                # Plot 2: Student performance comparison
                df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
                plt.title("Student Performance Comparison")
                plt.ylabel("Scores")
                plt.show()
                
            except FileNotFoundError:
                print("Error: The CSV file was not found. Please check the file path.")
            except Exception as e:
                print(f"Unexpected Error: {e}")

        # ------------------------------------------
        # EXIT ROUTINE
        # ------------------------------------------
        elif choice == "9":
            print("\nShutting down Smart Campus Information System. Goodbye!")
            break
            
        else:
            print("\nInvalid option selection! Please try choice inputs within 1-9.")

if __name__ == "__main__":
    main_dashboard()