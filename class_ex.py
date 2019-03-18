class Car:
    def __init__(self, color_code, wheel_size, gas, owner):
        self.color = color_code         # string
        self.wheel_size = wheel_size    # int
        self.gas = gas                  # boolean
        self.x = 0
        self.y = 0
        self.velocity = 10
        self.owned_by = owner

    def forward(self, sec):
        print(f'going forward for {sec}seconds...')
        self.x += self.velocity * sec

    def backward(self, sec):
        print(f'going backward for {sec}seconds...')
        self.x -= self.velocity * sec

    def change_color(self, new_color):
        self.color = new_color

    def change_owner(self, new_owner):
        print('This car now belongs to', new_owner)
        self.owned_by = new_owner

    def print_info(self):
        print('This car is owned by:', self.owned_by)
        print('The color is', self.color)
        print('Current x position:', self.x)
        print('='*20)


myColor = 'white'
my_wheel_size = 30
gas = True
my_name = 'moon'

mycar = Car(myColor, my_wheel_size, gas, my_name)
mycar.print_info()
mycar.forward(50)
mycar.backward(10)
mycar.print_info()
mycar.change_owner('kim')
mycar.print_info()