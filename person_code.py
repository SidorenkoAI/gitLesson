class Person:
    '''
    Реализуйте класс для человека, поддерживающий историю изменений человеком своих фамилии и имени.
    Считайте, что в каждый год может произойти не более одного изменения
    фамилии и не более одного изменения имени.
    При этом с течением времени могут открываться всё новые факты из прошлого человека,
    поэтому года́ в последовательных вызовах методов *ChangeLastName* и *ChangeFirstName*
    не обязаны возрастать.
    Строка, возвращаемая методом *GetFullName*, должна содержать разделённые одним пробелом
     имя и фамилию человека по состоянию на конец данного года.
    Если к данному году не случилось ни одного изменения фамилии и имени, верните строку "Incognito".
    Если к данному году случилось изменение фамилии,
    но не было ни одного изменения имени, верните "last_name with unknown first name".
    Если к данному году случилось изменение имени,
    но не было ни одного изменения фамилии, верните "first_name with unknown last name".
    '''
    def __init__(self):
        self.name = []

    def ChangeFirstName(self, year, first_name):
        while(True):
            try:
                year = int(input())
            except ValueError:
                print('Введите число')

            if type(year) == int:
                break

            self.name[0] = first_name

    def ChangeLastName(self, year, last_name):
        while(True):
            try:
                year = int(input())
            except ValueError:
                print('Введите число')

            if type(year) == int:
                break

            self.name[1] = last_name


    def GetFullName(self, year):
        if self.name == '':
            print(f"Incognito, {year}")
        if self.name[0] == '':
            print(f"last_name with unknown first name, {year}")
        if self.name[1] == '':
            print(f"first_name with unknown last name, {year}")