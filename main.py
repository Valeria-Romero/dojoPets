from Ninja import Ninja
from Pet import Pet


mando = Pet("Mando", "Dog", "Gives you the paw", "Woof woof")
pia =Pet("Pia", "Cat", "Sleep all day", "Mew mew prrrrr")
max = Ninja ("Max", "Rodriguez", ["bacon snacks","turkey snacks"], "Dry food", mando )
valeria = Ninja("Valeria", "Romero", "Soft salmon", ["Wet food", "Dry food"], pia)

valeria.feed().walk().bathe
max.feed().walk().bathe