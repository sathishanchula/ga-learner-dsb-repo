# --------------
# Code starts here
class_1=[]
class_2=[]
class_1.append('Geoffrey Hinton')
class_1.append('Andrew Ng')
class_1.append('Sebastian Raschka')
class_1.append('Yoshua Bengio')
class_2.append('Hilary Mason')
class_2.append('Carla Gentry')
class_2.append('Corinna Cortes')

new_class=class_1 + class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)


# --------------
# Code starts here
courses={"Math":65,'English':70,'History':80,'French':70, 'Science':60}
total=sum(courses.values())
print(total)
percentage= (total/500) * 100
print(percentage)


# Code ends here


# --------------
# Code starts here
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65, 'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
topper=max(mathematics,key=mathematics.get)
print(topper)
# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
# Code starts here
first_name,last_name=list(topper.split())
full_name=last_name + " " + first_name
certificate_name=full_name.upper()
print(certificate_name)

# Code ends here


