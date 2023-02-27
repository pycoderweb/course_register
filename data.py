class User_data:

    def __init__(self,id):
        self.id = id
        self.fanlar = []

    def set_ism(self,ism):
        self.ism = ism

    def set_familya(self,familya):
        self.familya = familya

    def add_fan(self,fan):
        self.fanlar.append(fan)

    def get_info(self):
        return f"ID {self.id} Ism: {self.ism} familya: {self.familya} fanlar: {[fan for fan in self.fanlar]}"

    def get_name_surname(self):
        return f"{self.ism} {self.familya} (ID : {self.id})"
