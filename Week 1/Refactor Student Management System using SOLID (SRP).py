class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade,
        }


class StudentService:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return [student.to_dict() for student in self.students]

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student.to_dict()
        return None


if __name__ == "__main__":
    service = StudentService()
    service.add_student(Student(1, "Alice", "A"))
    service.add_student(Student(2, "Bob", "B"))

    print(service.get_all_students())
    print(service.get_student_by_id(2))
