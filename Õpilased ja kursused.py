# defineerib klassi Student
class Student:
    def __init__(self, name, age, grade):  #määrab õpilase nime, vanuse ja hinde
        self.name = name  #salvestab nime
        self.age = age  #salvestab vanuse
        self.grade = grade  #salvestab hinde

    def get_grade(self):  #tagastab õpilase hinde
        return self.grade


# defineerib klassi Course
class Course:
    def __init__(self, name, max_students):  #määrab kursuse nime ja maksimaalse õpilaste arvu
        self.name = name  #salvestab kursuse nime
        self.max_students = max_students  #salvestab maksimaalse õpilaste arvu
        self.students = []  #loob tühja nimekirja kursusele lisatud õpilaste jaoks

    def add_student(self, student):  #lisab kursusele õpilase
        if len(self.students) < self.max_students:  #kontrollib, kas kursusel on veel ruumi
            self.students.append(student)  #lisab õpilase nimekirja
            return True  #tagastab True, kui lisamine õnnestus
        return False  #tagastab False, kui kursus on täis

    def get_average_grade(self):  #arvutab ja tagastab õpilaste keskmise hinde
        value = 0  #algne summa on 0
        for student in self.students:  #vaatab läbi kõikide õpilaste nimekirja
            value += student.get_grade()  #liidab iga õpilase hinde summale
        return value / len(self.students)  #jagab hinnete summa õpilaste arvuga, et saada keskmine hinne


s1 = Student("Time", 19, 95)  #lisab õpilase nimega "Time", vanus 19, hinne 95
s2 = Student("Bill", 19, 75)  #lisab õpilase nimega "Bill", vanus 19, hinne 75
s3 = Student("Jill", 19, 65)  #lisab õpilase nimega "Jill", vanus 19, hinne 65

course = Course("Science", 2)  #loob kursuse nimega "Science" ja määrab maksimaalseks õpilaste arvuks 2

course.add_student(s1)  #lisab kursusele esimese õpilase ja tagastab True, sest kursusel on veel ruumi
course.add_student(s2)  #lisab kursusele teise õpilase ja tagastab True, sest kursusel on veel ruumi
print(course.add_student(
    s3))  #püüab lisada kursusele kolmanda õpilase ja prindib False, kuna kursusele ei mahu rohkem õpilasi
print(course.get_average_grade())  #prindib kursusel olevate õpilaste keskmise hinde (95 + 75) / 2 = 85.0
