
class Student:
    school = "YearUp Academy"

    def __init__(self, name, grade, track):
        self.name = name
        self.__grade = grade
        self.track = track

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            print(f"Grade updated successfully for {self.name}.")
        else:
            print(f"Error: Grade for {self.name} must be between 0 and 100.")

    def display_info(self):
        print(f"""
        School: {Student.school}
        Student Name: {self.name}
        Grade: {self.get_grade()}
        Track: {self.track}
        """)


student1 = Student("John Smith", 85, "Data Analytics")
student2 = Student("Sarah Johnson", 92, "Software Development")


print("--- Updating Student Grades ---")

student1.set_grade(90)   
student1.set_grade(105) 

student2.set_grade(95)  
student2.set_grade(-5)   


print("\n--- Current Student Grades ---")

print(f"{student1.name}'s grade: {student1.get_grade()}")
print(f"{student2.name}'s grade: {student2.get_grade()}")


print("\n--- Student Reports ---")

student1.display_info()
student2.display_info()
