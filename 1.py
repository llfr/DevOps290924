a = 4
b = "Aviel"
c = True
d = ["Aviel", "Buskila", 34, True]
e = {"fname": "Aviel",
     "lname": "Biskila",
     "age": 34}
f = dict(fname="Aviel", lname="Buskila")

list_of_people = [e, f]

print(a)
print(e["lname"])
print(f["lname"])
print(list_of_people)
print("Name is " + b)

r = 4 + 4
s = "Aviel" + "Buskila"
fname = "Aviel"
lname = "Buskila"

first = fname + lname
second = "{} {}".format(fname, lname)
third = f"{fname}, {lname}"
forth = "%s %s" % (fname, lname)

t = "Aviel" * 4
u = "Aviel" + str(4)
print(t)
print(u)
