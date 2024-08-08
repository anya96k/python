class Classroom:
    def __init__(self, class_name, students):
       
        self.class_name = class_name
        self.students = students
    
    def print_values(self):
      
        print(f"Class Name: {self.class_name}")
       
        print("Students:")

        for student in self.students:
            print(f"- {student}")


classroom = Classroom("cse-ai", ["om", "harsh", "darshan","shri","shahid"])
classroom.print_values()