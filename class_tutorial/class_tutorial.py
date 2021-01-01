class electronics():
    tools = []
    age = 0
    years_of_experience = 0
    languages = []
    department = ""


alex = electronics()
alex.tools = ["spice", "eagle"]
alex.age = 27
alex.years_of_experience = 3
alex.languages.append("english")
alex.department = "electronics"

print(alex.tools, alex.age, alex.years_of_experience, alex.department, alex.languages)

ali = electronics()
ali.tools = ["spice", "eagle"]
ali.age = 27
ali.years_of_experience = 3
ali.languages.append("english")
ali.department = "electronics"

ali.languages = []

print(ali.tools, ali.age, ali.years_of_experience, ali.department, ali.languages)

print("\nali:\n", ali.languages, "\nalex:\n", alex.languages)

# _________________________________________________________________________________________
print("_" * 80)


class electrical():
    age = 0
    years_of_experience = 0
    tools = []
    languages = []
    department = []


at = electrical()
at.age = 20
at.years_of_experience = 0
at.tools.append("spice")
at.languages.append("english")
at.department.append("cs")

print(at.age, at.years_of_experience, at.tools, at.languages, at.department)

bok = electrical()
bok.age = 27
bok.years_of_experience = 3
bok.tools.append("xcode")
bok.languages.append("french")
bok.department.append("electroncis")

print(bok.age, bok.years_of_experience, bok.tools, bok.languages, bok.department)

bok.age = 300
at.age = 122

print(bok.age, at.age)

# _________________________________________________________________________________________
print("_" * 80)


class new():
    def __init__(self):
        self.age = 0

    def __index__(self):
        self.years_of_experience = 0


deneme = new()
deneme.age = 200
deneme.years_of_experience = 100

naber = new()
naber.age = 50
naber.years_of_experience = 10

print(deneme.age, deneme.years_of_experience, naber.age, naber.years_of_experience)

# _________________________________________________________________________________________
print("_" * 80)

class VeriBilimi():
    calisanlar = []

    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""


veli = VeriBilimi()
print("veli.bildigi_diller\t", veli.bildigi_diller)
veli.bildigi_diller.append("pythonobject")
print("veli.bildigi_diller\t", veli.bildigi_diller)

ali = VeriBilimi()
print("ali.bildigi_diller\t", ali.bildigi_diller)
ali.bildigi_diller.append("c")
print("ali.bildigi_diller\t", ali.bildigi_diller)


class newClass():
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""

    def dil_ekle(self, new_dil):
        self.bildigi_diller.append(new_dil)

    def bolum_ekle(self, new_bolum):
        self.bolum = new_bolum


ali = newClass()
print("\nali.newClass()\nali.bildigi.diller\t", ali.bildigi_diller)
ali.dil_ekle("python")
print("\nali.dil_ekle(\"python\")\n", "ali.bildigi_diller\t", ali.bildigi_diller)


#______________________________________________________________________________
print("_" * 90)
class Employees():
    def __init__(self, firstName="n/a", middleName="n/a", lastName="n/a", age=0, gender="n/a"):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.age = age
        self.gender = gender


class DataScience(Employees):
    def __init__(self, programming="n/a", languages="n/a", projects="n/a"):
        self.programming = programming
        self.languages = languages
        self.projects = projects


class marketing(Employees):
    def __init__(self, communication="n/a", storytelling="n/a", charisma="n/a"):
        self.communication = communication
        self.storytelling = storytelling
        self.charisma = charisma


alex = DataScience()
alex.programming = "python"
alex.firstName = "alex"
alex.lastName = "mercan"
print("alex :\n", alex.firstName, "\n", alex.lastName, "\n", alex.programming)