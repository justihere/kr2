class Organization:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Only type str allowed for name.')
        self.__name = new_name

    @property
    def phone_number(self):
        return self.__phone_number

    @name.setter
    def phone_number(self, new_phone_number):
        if not isinstance(new_phone_number, str):
            raise TypeError('Only type str allowed for phone number.')
        self.__phone_number = new_phone_number

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        if not isinstance(new_address, str):
            raise TypeError('Only type str allowed for address.')
        self.__address = new_address

    def __eq__(self, other):
        if not isinstance(other, Organization):
            raise TypeError('Only type Organization allowed for comparison.')
        return self.name == other.name and self.phone_number == other.phone_number and self.address == other.address

class Kafedra(Organization):
    def __init__(self, name, phone_number, address, specialization, number_bachelors, number_magisters, number_specialists):
        super().__init__(name, phone_number, address)

        if not isinstance(specialization, str):
            raise TypeError('Only type str allowed for specialization.')

        if not all(isinstance(i, int) for i in [number_bachelors, number_magisters, number_specialists]):
            raise TypeError('Number of bachelors, number of magisters and number of specialists must be int type.')

        self.__specialization = specialization
        self.__number_bachelors = number_bachelors
        self.__number_magisters = number_magisters
        self.__number_specialists = number_specialists

    @property
    def numberOfStudents(self):
        return self.__number_bachelors + self.__number_magisters + self.__number_specialists

    def new_bachelors(self, num_new_bachelors):
        if not isinstance(num_new_bachelors, int):
            raise TypeError('Only type int allowed for number of new bachelors.')
        self.__number_bachelors += num_new_bachelors

    def new_magisters(self, num_new_magisters):
        if not isinstance(num_new_magisters, int):
            raise TypeError('Only type int allowed for number of new magisters.')
        self.__number_magisters += num_new_magisters

    def new_specialists(self, num_new_specialists):
        if not isinstance(num_new_specialists, int):
            raise TypeError('Only type int allowed for number of new specialists.')
        self.__number_specialists += num_new_specialists

    def remove_bachelors(self, num_bachelors):
        if not isinstance(num_bachelors, int):
            raise TypeError('Only type int allowed for number of bachelors.')
        if (self.__number_bachelors < num_bachelors):
            raise ValueError('Remove value is too big.')
        self.__number_bachelors -= num_bachelors

    def remove_magisters(self, num_magisters):
        if not isinstance(num_magisters, int):
            raise TypeError('Only type int allowed for number of magisters.')
        if (self.__number_magisters < num_magisters):
            raise ValueError('Remove value is too big.')
        self.__number_magisters -= num_magisters

    def remove_specialists(self, num_specialists):
        if not isinstance(num_specialists, int):
            raise TypeError('Only type int allowed for number of specialists.')
        if (self.__number_specialists < num_specialists):
            raise ValueError('Remove value is too big.')
        self.__number_specialists -= num_specialists


class Facultet:
    def __init__(self):
        self.__data = []

    def add(self, kafedra):
        if not isinstance(kafedra, Kafedra):
            raise TypeError('Only type Kafedra allowed for number of kafedra.')
        self.__data.append(kafedra)

    @property
    def numberOfStudents(self):
        students = 0
        for x in self.__data:
            students += x.numberOfStudents
        return int(students)

k1 = Kafedra('katya', '+389071240062', 'hryshevskogo 14', 'english', 10, 35, 25)
k2 = Kafedra('katya', '+389077528742', 'pokokrovska 117', 'maths', 30, 20, 25)

f = Facultet()

f.add(k1)
f.add(k2)

print(f.numberOfStudents)