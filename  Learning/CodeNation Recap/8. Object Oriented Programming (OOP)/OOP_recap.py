class Person():
    def __init__(self, person_name, person_age, person_height ):
        self.name = person_name
        self.age = person_age
        self.height = person_height

    def set_hair(self, person_hair):
        self.hair = person_hair

    def get_hair(self):
        print(self.hair)