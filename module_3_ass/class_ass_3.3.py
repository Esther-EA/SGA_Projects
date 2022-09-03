class Students:
       
    def _init_(self, first, last):
      self.first = first
      self.last = last
      self.email = first + '.' + last + '@stutern.com' 
      
    def fullname(self):
        return'{} {}'.format(self.first, self.last)

student_1 = Students('Bukola', 'Dare')
student_2 = Students('Temitope', 'Balogun')
student_3 = Students('Oluwaseun', 'Adebayo')


# create a class called group leader that inherits from a student class 
class Group(Students):
    # students under the group leader
    def _init_(self, first, last, title):
        super()._init_(first, last)
        self.title = title
    
    # add a method that adds a group leader to the group
    def add_group_leader(self, group_leader):
        self.group_leader = group_leader
        return '{} {} has been added to the group'.format(self.first, self.last)
    
    def group_leader(self):
        return '{} {} is the group leader'.format(self.first, self.last)
    
    def add_student(self, student):
        self.student = student
        return '{} {} has been added to the group'.format(self.first, self.last)
    
    def remove_student(self, student):
        self.student = student
        return '{} {} has been removed from the group'.format(self.first, self.last)
    
    def list_students(self):
        list_students = '{} {} is the group leader and the students are: {} {} and {} {}'.format(self.first, self.last, self.student.first, self.student.last, self.student.first, self.student.last)
        return list_students



# add a group leader to the group
Group_1 = Group('Bukola', 'Dare', 'Group Leader')

# add students to the group
Group_1.add_student(student_1)
Group_1.add_student(student_2)
Group_1.add_student(student_3)

# print the list of students in the group
print(Group_1.list_students())