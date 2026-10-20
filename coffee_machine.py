class CoffeeMachine:
    MENU = 'menu'
    BUY = 'buy'
    WATER = 'fill_water'
    MILK = 'fill_milk'
    BEANS = 'fill_beans'
    CUPS = 'fill_cups'
    EXIT = 'exit'

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = self.MENU

    def prompt(self):
        prompts = {
            self.MENU: 'Write action (buy, fill, take, remaining, exit):',
            self.BUY: 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:',
            self.WATER: 'Write how many ml of water you want to add:',
            self.MILK: 'Write how many ml of milk you want to add:',
            self.BEANS: 'Write how many grams of coffee beans you want to add:',
            self.CUPS: 'Write how many disposable cups you want to add:'
        }
        return prompts.get(self.state, '')

    def remaining(self):
        return (f'The coffee machine has:\n'
                f'{self.water} ml of water\n'
                f'{self.milk} ml of milk\n'
                f'{self.beans} g of coffee beans\n'
                f'{self.cups} disposable cups\n'
                '$' + f'{self.money} of money')

    def buy(self, choice):
        self.state = self.MENU
        if choice == 'back':
            return ''
        recipes = {'1': (250, 0, 16, 4), '2': (350, 75, 20, 7), '3': (200, 100, 12, 6)}
        if choice not in recipes:
            return ''
        water, milk, beans, price = recipes[choice]
        for name, available, needed in (
            ('water', self.water, water),
            ('milk', self.milk, milk),
            ('coffee beans', self.beans, beans),
            ('disposable cups', self.cups, 1)
        ):
            if available < needed:
                return f'Sorry, not enough {name}!'
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= 1
        self.money += price
        return 'I have enough resources, making you a coffee!'

    def take(self):
        result = 'I gave you $' + str(self.money)
        self.money = 0
        return result

    def handle_input(self, text):
        if self.state == self.MENU:
            if text == 'buy':
                self.state = self.BUY
            elif text == 'fill':
                self.state = self.WATER
            elif text == 'take':
                return self.take()
            elif text == 'remaining':
                return self.remaining()
            elif text == 'exit':
                self.state = self.EXIT
        elif self.state == self.BUY:
            return self.buy(text)
        elif self.state == self.WATER:
            self.water += int(text)
            self.state = self.MILK
        elif self.state == self.MILK:
            self.milk += int(text)
            self.state = self.BEANS
        elif self.state == self.BEANS:
            self.beans += int(text)
            self.state = self.CUPS
        elif self.state == self.CUPS:
            self.cups += int(text)
            self.state = self.MENU
        return ''


if __name__ == '__main__':
    machine = CoffeeMachine()
    while machine.state != machine.EXIT:
        print(machine.prompt())
        output = machine.handle_input(input())
        if output:
            print(output)
