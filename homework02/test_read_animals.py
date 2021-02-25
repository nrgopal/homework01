#!/usr/bin/env python3

import unittest
import sys
from read_animals import breed_animals

class TestReadAnimals(unittest.TestCase):

    def test_breeding_offspring(self):
        self.assertEqual((breed_animals.parent1['head']) + '-' + (breed_animals.parent2['head']), breed_animals.offspring['head'])
        self.assertEqual((breed_animals.parent1['body']) + '-' + (breed_animals.parent2['body']), breed_animals.offspring['body'])
        self.assertEqual((breed_animals.parent1['arms']) + (breed_animals.parent2['arms']), breed_animals.offspring['arms'])
        self.assertEqual((breed_animals.parent1['legs']) + (breed_animals.parent2['legs']), breed_animals.offspring['legs'])
        self.assertEqual((breed_animals.parent1['tails']) + (breed_animals.parent2['tails']), breed_animals.offspring['tails'])

if __name__ == '__main__' :
    unittest.main()
