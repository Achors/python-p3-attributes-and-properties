#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name,):
        self._name = None  
        self._breed = None  
        self.name = name   

    # @property
    def name(self):
        return self._name

    # @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    # @property
    def breed(self):
        return self._breed

    # @breed.setter
    def breed(self, value):
        approved_breeds = APPROVED_BREEDS
        if value not in approved_breeds:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value

# Example usage:
# dog_instance = Dog(name="Buddy", breed="Labrador")

        
        
