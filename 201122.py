class Device:
    def __init__(self):
        self.__type = ''
        self.__memory = ''
        self.__year = 0

    def info(self):
        print(f'устроство - {self.__type}\nпамят - {self.__memory}\nгод выпуска - {self.__year}')

    def set_type(self, type):
        self.__type = type
    def set_memory(self, memory):
        self.__memory = memory
    def set_year(self, year):
        self.__year = year

    def get_type(self):
        return self.__type
    def get_memory(self):
        return self.__memory
    def get_year(self):
        return self.__year

class Phone(Device):

    def __init__(self, brand, model):
        super().__init__()
        self.__brand = ''
        self.__model = ''

    def set_brand(self,brand):
        self.__brand = brand
    def set_model(self, model):
        self.__model = model

    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model

    def info(self):
        super().info()
        print(f'марка телефона - {self.__brand}\nмодель - {self.__model}')

iphone = Phone('iPhohe', 'XR')
iphone.set_type('Телефон')
iphone.set_memory('2гига')
iphone.set_year('2020')
iphone.set_brand('iPhone')
iphone.set_model('XR')
iphone.info()
print()
droid = Phone('Honor', '64654')
droid.set_type('Телефон')
droid.set_memory('4гига')
droid.set_year('2018')
droid.set_brand('Honor')
droid.set_model('64654')
droid.info()

print('Hello World')