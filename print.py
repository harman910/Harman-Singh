fname = ' john is new student'
lname = "Alex"

print(type(fname))
print(type(lname))

print(fname[2:7])
print(fname[-3])

print(len(fname))
print(fname.upper())
print(fname.lower())
print(fname.islower())

str1 = 'JAVA'
str2= "PYTHON"
str3 = 'JAVA'

print(str1==str2)
print(str1==str3)

st = 'Python is is is is  the popular programming laguage'
print(st.upper().count('IS'))
print(st.find('is'))

rep = st.replace('is', 'or')
print(rep)
