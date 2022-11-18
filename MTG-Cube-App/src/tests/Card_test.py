import unittest
from entities.cube_and_cards import Card, Cube
from unittest.mock import patch


class TestCards(unittest.TestCase):
    def setUp(self):
        self.colored_creature = Card("Spike Rogue")
        self.non_color_spell = Card("Well of Knowledge")

    def test_card_str(self):
        self.assertEqual(str(self.colored_creature),"Spike Rogue")

    def test_colored_creature_attributes(self):
        self.assertEqual([
            self.colored_creature.name,
            self.colored_creature.colors,
            self.colored_creature.color_id,
            self.colored_creature.cmc,
            self.colored_creature.mana_cost,
            self.colored_creature.type,
            self.colored_creature.keywords,
            self.colored_creature.text,
            self.colored_creature.img_uri,
            self.colored_creature.pt
        ],[
            "Spike Rogue",
            "['G']",
            "['G']",
            3,
            "{1}{G}{G}",
            "Creature — Spike",
            '[]',
            "Spike Rogue enters the battlefield with two +1/+1 counters on it.\n{2}, Remove a +1/+1 counter from Spike Rogue: Put a +1/+1 counter on target creature.\n{2}, Remove a +1/+1 counter from a creature you control: Put a +1/+1 counter on Spike Rogue.",
            "https://cards.scryfall.io/png/front/f/0/f0d9b671-344b-460d-8f65-d65129db91c3.png?1562089260",
            "0/0"
            ])
    
    def test_non_color_spell_attributes(self):
        self.assertEqual([
            self.non_color_spell.name,
            self.non_color_spell.colors,
            self.non_color_spell.color_id,
            self.non_color_spell.cmc,
            self.non_color_spell.mana_cost,
            self.non_color_spell.type,
            self.non_color_spell.keywords,
            self.non_color_spell.text,
            self.non_color_spell.img_uri,
            self.non_color_spell.pt
        ],[
            "Well of Knowledge",
            "[]",
            "[]",
            3,
            "{3}",
            "Artifact",
            "[]",
            "{2}: Draw a card. Any player may activate this ability but only during their draw step.",
            "https://cards.scryfall.io/png/front/5/1/5184b967-f474-4c9b-9a20-65ddb0d6e4f8.png?1562800806",
            ""
        ])
    # Tää ei toimi, mut tahtoisin et se toimis
    # @patch('sqlite3.connect(f"src/entities/fetched_cards/fetched_cards.db")', None)
    # def test_fetching_card_data(self):
    #     new_noncreature_card = Card("Doomsday")
    #     new_creature_card = Card("Pit spawn")
    #     self.assertEqual([new_creature_card.name, new_noncreature_card.name],["Pit Spawn","Doomsday"])


class TestCube(unittest.TestCase):
    def setUp(self) -> None:
        self.cube = Cube("TestCube")
    
    def test_cube_named_right(self):
        self.assertEqual(str(self.cube),"TestCube")
    
    def test_empty_cube_is_empty(self):
        self.assertEqual([self.cube.collection,self.cube.card_names],[[],[]])
    
    def test_adding_cards_works(self):
        self.cube.add_card("forest")
        self.assertEqual([self.cube.card_names, len(self.cube.collection)], [["Forest"],1])

    def test_adding_duplicate_cards_doesnt_work(self):
        self.cube.add_card("forest")
        self.cube.add_card("forest")
        self.assertEqual([self.cube.card_names, len(self.cube.collection)], [["Forest"],1])

    