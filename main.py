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
#parne   if
#x = int(input("Введіть число: "))
#if x % 2 == 0:
   # print("Число x є парним.")
#else:
  #  print("Число x є непарним.")


is_next = None
num = int(input("Enter the number of points: "))
if num>=83:
    is_next=True
else:
    is_next=False


#if elif else
a = input('Введіть число')
a = int(a)
if a == 1:
    print('Число дорівнює 1')
elif a > 0:
    print('Число додатне')
else:
    print("a <= 0")

work_experience = int(input("Enter your full work experience in years: "))
if work_experience<=1:
    developer_type = "Junior"
elif work_experience<=5:
    developer_type = "Middle"
else:
     developer_type = "Senior"
     
     
#ЦИКЛИ WHILE
num = int(input("Enter the integer (0 to 100): "))
sum = 0
while num>=0:
    sum=sum+num
    num=num-1

#ЦИКЛИ FOR
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for i in message:
    if i==search:
        result=result+1
        print (i)
print(result)

#МЕХАНІЗМ ОБРОБКИ ВИКЛЮЧЕНЬ
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = int(pool/quantity)
except ZeroDivisionError:
    print('Divide by zero completed!')

#ВИЗНАЧЕННЯ ФУНКЦІЇ
def greeting():
    print("Hello world!")
greeting()

#ФУНКЦІЯ ІЗ ПАРАМЕТРАМИ
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"
print(invite_to_event("Tim"))