class Fruit:
    def __init__ (self,fruit_name,color,size):
        self.fruit_name=fruit_name
        self.color=color
        self.size=size

    def description(self):
        return f"I bought {self.color} {self.size} sized {self.fruit_name}"

    def count_fruits(self,total):
        return self.total=total
        