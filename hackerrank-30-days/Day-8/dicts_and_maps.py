num = int(input())

phone_book = {}

for i in range(0, num):
    entry = str(input()).split(" ")
    name = entry[0]
    phone = int(entry[1])
    phone_book[name] = phone

for j in range(0, num):
    name = str(input())
    if name in phone_book:
        contact = phone_book[name]
        print(name + "=" + str(contact))
    else:
        print("Not found")
    