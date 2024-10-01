class Student:
    def __init__(self, student_name, registration_number):
        self.student_name = student_name
        self.registration_number = registration_number
first_student = Student("KASSIM_Kiyaga", "S23B13/025")
second_student = Student("Derrick_NSUBUGA", "S23B13/024")
third_student = Student("NSUBUGA Karim", "M23B13/001")
fourth_student = Student("LEO MESSI","G.O.A.T/001")

print(f"My Name is: {first_student.student_name}, Registration Number: {first_student.registration_number}")
print(f"My Name is: {second_student.student_name}, Registration Number: {second_student.registration_number}")
print(f"My Name is: {third_student.student_name}, Registration Number: {third_student.registration_number}")
print(f"My Name is: {fourth_student.student_name}, Registration Number: {fourth_student.registration_number}")
