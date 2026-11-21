# length= float(input("What is the length of your Rectangle? "))
# height= float(input("What is the height of your Rectangle? "))

# area=length*height
# perimerter=(length*2)+(height*2)

# print("The perimeter of the rectangle is {} and the area is {}".format(perimerter,area))

f_name=input("Please enter your first name: ")
l_name=input("Please enter your last name: ")

initials=f_name[0]+l_name[0]

fullname=(f_name+str(" ")+l_name)

length=len(fullname)

username=f_name[0].lower()
username_2=l_name[0:3].lower()

full_user=username+username_2

print("Your full name is {}\nYour initials are {}\nThe length of your name is {}\nYour username is {}".format(fullname,initials,length,full_user))