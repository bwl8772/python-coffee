# Coffee Machine

A Python command-line coffee machine simulator completed as a learning project in [Hyperskill's Coffee Machine project](https://hyperskill.org/projects/68). This is the accepted final-stage implementation.

## Run

Requires Python 3.6 or newer. No third-party packages are needed.

```sh
git clone https://github.com/bwl8772/python-coffee.git
cd python-coffee
python3 coffee_machine.py
```

## Commands

- `buy`: choose espresso (`1`), latte (`2`), or cappuccino (`3`); enter `back` to return to the menu.
- `fill`: add water, milk, coffee beans, and disposable cups. Enter a non-negative whole number for each amount.
- `take`: collect all money from the machine.
- `remaining`: show current supplies and money.
- `exit`: quit.

The machine checks resources before making coffee and reports shortages without charging or consuming supplies. State is kept only for the current run and resets when the program restarts.

## Structure

`CoffeeMachine` stores resources and interaction state. `handle_input()` processes one input at a time; the external main loop handles console input and output. Refill inputs are expected to be valid integers, matching the learning project's requirements.
