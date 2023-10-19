class Animal :
    noise = "Rrrr"
    color = "Red"

    def get_noise(self):
        return self.noise
    
    def set_noise(self, new_noise):
        self.noise=new_noise
    
    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color=new_color

class Wolf(Animal) :
    noise = "Trrrr"

class BabyWolf(Wolf) :
    color = "Brown"


obj = BabyWolf()
print(obj.get_noise())
print(obj.get_color())