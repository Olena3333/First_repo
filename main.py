print("Hello world!")
length = 2.75
width = 1.75
area = length*width
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print (show)

my_list = []  #List
my_list.insert(0,2024)
my_list.insert(1,"Python")
my_list.insert(2,3.12)
print(my_list)
some_data = ['Python']
my_list.extend(some_data)
print (my_list)
my_list.insert(0,"fdhfdhfd")
print(my_list)
my_list.reverse()
print(my_list)
data = {} #diktionaries
data["year"]=2024
data["lang"]='Python'
data["version"]=3.12
print(data)
cat = {}
info = {"status": "vaccinated", "breed": True}
cat["nick"]="Simon"
cat["age"]=7
cat["characteristics"]=["l","k"]
age=cat.get("age")
cat.update(info)
print(cat)