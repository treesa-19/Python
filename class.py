class Car:
    def __init__(self, model, weight):
        self.model = model
        self.weight = weight

# Create instances of the Car class for Honda and Mazda
honda = Car(model='CSK', weight=134.8)
mazda = Car(model='SomeModel', weight=150.0)

# Access and print the attributes of the Honda car
print('Honda model:', honda.model)
print('Honda weight:', honda.weight)
