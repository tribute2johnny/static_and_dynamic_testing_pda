from os import stat_result
import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    
    def test_check_for_ace(self):
        self.card = Card("spades", 1)
        self.assertEqual(True, self.card.value)

    def test_highest_card(self):
        self.card1 = Card("hearts", 7)
        self.card2 = Card("clubs", 5)
        result = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card1, result)

    def test_cards_total(self):
        self.card1 = Card("hearts", 7)
        self.card2 = Card("clubs", 5)
        self.card_game = CardGame()
        self.all_cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 12", self.card_game.cards_total(self.all_cards))
