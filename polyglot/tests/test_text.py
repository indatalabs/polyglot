#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from ..text import Text

en_text = u"""Ernesto "Che" Guevara (Spanish pronunciation: [ˈtʃe ɣeˈβaɾa];[4] June 14,[1] 1928 – October 9, 1967), commonly known as el Che or simply Che, was an Argentine Marxist revolutionary, physician, author, guerrilla leader, diplomat, and military theorist. A major figure of the Cuban Revolution, his stylized visage has become a ubiquitous countercultural symbol of rebellion and global insignia in popular culture. As a young medical student, Guevara traveled throughout South America and was radicalized by the poverty, hunger, and disease he witnessed. His burgeoning desire to help overturn what he saw as the capitalist exploitation of Latin America by the United States prompted his involvement in Guatemala's social reforms under President Jacobo Árbenz, whose eventual CIA-assisted overthrow at the behest of the United Fruit Company solidified Guevara's political ideology. Later, in Mexico City, he met Raúl and Fidel Castro, joined their 26th of July Movement, and sailed to Cuba aboard the yacht, Granma, with the intention of overthrowing U.S.-backed Cuban dictator Fulgencio Batista. Guevara soon rose to prominence among the insurgents, was promoted to second-in-command, and played a pivotal role in the victorious two-year guerrilla campaign that deposed the Batista regime."""


class TestText(unittest.TestCase):

  def setUp(self):
    self.text = Text(en_text)

  def test_sentences(self):
    self.assertEqual(len(self.text.sentences), 6)

  def test_entities(self):
    text_entities = self.text.entities

    sentences_entities = []
    for sent in self.text.sentences:
        sentences_entities.extend(sent.entities)

    self.assertListEqual(text_entities, sentences_entities)


if __name__ == "__main__":
  unittest.main()