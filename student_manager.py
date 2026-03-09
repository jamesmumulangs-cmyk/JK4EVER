class StudentManager:
    def __init__(self):
        self.students = {}

    def create_student(self, student_id, name, age):
        """Creates a new student record."""
        self.students[student_id] = {'name': name, 'age': age}

    def read_student(self, student_id):
        """Reads a student record by student ID."""
        return self.students.get(student_id, None)

    def update_student(self, student_id, name=None, age=None):
        """Updates an existing student record."""
        if student_id in self.students:
            if name:
                self.students[student_id]['name'] = name
            if age:
                self.students[student_id]['age'] = age

    def delete_student(self, student_id):
        """Deletes a student record by student ID."""
        if student_id in self.students:
            del self.students[student_id]