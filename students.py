class Student:
    def __init__(self, student_id, name, email, enrollment_date, status='active'):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrollment_date = enrollment_date
        self.status = status

    def deactivate(self):
        self.status = 'inactive'

    def activate(self):
        self.status = 'active'

    def __str__(self):
        return f'Student({self.student_id}, {self.name}, {self.email}, {self.enrollment_date}, {self.status})'