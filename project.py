import csv
from tabulate import tabulate
import time

class Kid:
    def __init__(self, name, classroom):
        self.name = name
        self.classroom = classroom

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        elif name.isalpha() == False:
            raise ValueError("Please enter a name")
        else:
            self._name = name

    @property
    def classroom(self):
        return self.classroom

    @classroom.setter
    def classroom(self, classroom):
        if classroom.lower() in ["peach", "pear", "avocado"]:
            self._classroom = classroom
        else:
            raise ValueError("Invalid classroom")

def main():
    milk = 0
    diaper = 0
    nap = "no"
    name = input("Name of the baby: ")
    classroom = input("Name of the classroom (Pear/Avocado/Peach): ")
    Kid(name,classroom)
    while True:
        answer = input("Would you like to record (more) activities? Yes/No ")
        if answer.lower() not in ("yes", "no"):
            print("Invalid answer")
        elif answer.lower() == "yes":
            activity = input("Which activity would you like to record? (Milk/Diaper/Nap) ")
            if activity.lower() not in ["milk", "diaper", "nap"]:
                print("Invalid activity")
            else:
                if activity.lower() == "milk":
                    try:
                        milk = int(input("How much did the baby drink? (in ml) "))
                        print()
                        print("Milk recorded")
                    except ValueError:
                        print("Please input a number")
                elif activity.lower() == "diaper":
                    print()
                    print("One Diaper replaced")
                    diaper = 1
                elif activity.lower() == "nap":
                    print()
                    print("Nap recorded")
                    nap = "yes"
        else:
            break

    date = time.strftime('%Y-%m-%d',time.localtime())
    record = {"name": name, "classroom": classroom, "milk": milk, "diaper": diaper, "nap": nap, "date": date}
    update_info(record)
    kid_info = get_info(name, classroom, date)
    table_info = {"Name" : [name.capitalize()], "Classroom" : [classroom.capitalize()], "Milk": [get_milk(kid_info)+" ml"], "Diaper": [get_diaper(kid_info)+" times"], "Nap": [get_nap(kid_info)], "Date": [date]}
    print()
    print(f"{name.capitalize()}'s Daily Report")
    print_table(table_info)

def update_info(record):
    with open("Daycare.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "classroom", "milk", "diaper", "nap", "date"])
        writer.writerow({"name": record["name"], "classroom": record["classroom"], "milk": record["milk"], "diaper":record["diaper"], "nap":record["nap"], "date": record["date"]})

def get_info(name, classroom, date):
    filter = []
    with open("Daycare.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"].lower() == name.lower() and row["classroom"] == classroom and row["date"] == date:
                filter.append(row)
    return filter

def get_milk(list):
    total = 0
    for row in list:
        total = int(row["milk"]) + total
    return str(total)




def get_diaper(list):
    total = 0
    for row in list:
        total = int(row["diaper"]) + total
    return str(total)

def get_nap(list):
    for row in list:
        if row["nap"] == "yes":
            return "Yes"
    return "No"

def print_table(list):
    print(tabulate(list, headers = "keys", tablefmt = "fancy_grid"))

if __name__ == "__main__":
    main()





