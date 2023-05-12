#!/usr/bin/env python
# coding: utf-8

# #Creating a list called "students" and populating it with tuples representing each student's data. Including five students in the list.
# 

# In[7]:


students = [("shreyansh", 24, ["Math", "Physics", "Chemistry"]),
   ("swechchha", 21, ["English", "Hindi"]),
   ("Manisha", 22, ["Sanskrit", "Biology"]),
   ("Aarti", 18, ["Accounting", "Economics"]),
   ("Mansi", 20, ["English", "Math"])]


# #Printing the name and age of each student from the "students" list.
# 
# 

# In[8]:


for student in students:
    name, age, _ = student
    print("Name:", name)
    print("Age:", age)
    print()


# #Converting the list of subjects for each student into a set and storing it in a new list called "unique_subjects".

# In[10]:


unique_subjects = []
for student in students:
    _, _, subjects = student
    unique_subjects.append(set(subjects))


# #Printing the unique subjects for each student.
# 

# In[11]:


for i, subjects in enumerate(unique_subjects):
    print("Student", i+1, "Subjects:", subjects)


# Creating a function called "get_students_by_subject" that takes a subject as an input and returns a list of students who are studying that subject.
# 
# 

# In[12]:


def get_students_by_subject(subject):
    students_with_subject = []
    for student in students:
        _, _, subjects = student
        if subject in subjects:
            students_with_subject.append(student)
    return students_with_subject


# #Testing the "get_students_by_subject" function by passing a subject and printing the list of students returned.
# 
# 

# In[13]:


subject = "Math"
students_by_subject = get_students_by_subject(subject)
print("\nStudents studying", subject + ":")
for student in students_by_subject:
    print(student[0])


# In[ ]:





# In[ ]:




