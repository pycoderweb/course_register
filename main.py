from data import User_data
from uuid import uuid4

fanlar = ["Dasturlash asoslari" , "Ingliz tili" , "Malumotlar Bazasi"]

def print_fanlar():
    i = 1
    for fan in fanlar:
        print(f"{i}. {fan}")
        i+=1


oquvchilar = []
ketganlar = []
ishora = True

while ishora:
    print(f"\n  \n"
          f"       1.O'qitiladigan fanlar royhati.\n"
          f"       2.Kursga talabani yozish.\n"
          f"       3.Talabalar haqida malumot.\n"
          f"       4.Talabani kursdan o'chirish.\n"
          f"       5.Kurs haqida umumiy malumot.\n"
          f"       6.Dasturni yakunlash")

    command = int(input("Kerakli xizmatni tanlang(1 - 6) : "))

    if command==1:
        print_fanlar()
    elif command == 2:
        oquvchi = User_data(uuid4())
        name = input("Ismingizni kiriting____ ")
        oquvchi.set_ism(name)
        surname = input("familyangizni kiritng____")
        oquvchi.set_familya(surname)
        print_fanlar()
        fan_index = int(input("qaysi fanga yozilasiz : "))
        oquvchi.add_fan(fanlar[fan_index - 1])
        oquvchilar.append(oquvchi)
    elif command == 3:
        for current_oquvchi in oquvchilar:
            print(current_oquvchi.get_info())
    elif command == 4:
        i = 1
        for current_oquvchi in oquvchilar:
            print(f"{i}. {current_oquvchi.get_name_surname()}")
            i += 1
        del_index = int(input("O'chirilgan talabani tanlang>> "))
        ketganlar.append(oquvchilar.pop(del_index-1))

    elif command == 5:
        print("Hozirgi o'quvchilar : ")
        for current in oquvchilar:
            print(current.get_name_surname())
        print("Kursni tugatganlar : ")
        for left in ketganlar:
            print(left.get_name_surname())
        print(f"Jami tahsil olayotganlar va kursni tugatganlar : {len(oquvchilar)+len(ketganlar)}")
    elif command == 6:
        ishora = False

