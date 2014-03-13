from __future__ import unicode_literals

from node import Node
from syllables import Syllables
from tokenizer import Tokenizer

class Haiku:
    phrase_counts = (5, 7, 5)
    max_syllables = sum(phrase_counts)
    tokenizer = Tokenizer()
    level_maxes = [5, 12, 17]

    def __init__(self, text):
        self.text = self.tokenizer.tokenize(text)
        self.phrases = self.phrases()

    def sum_syllables(self, words, node, level=0):
        if not words:
            return
        if level == len(self.level_maxes):
            return
        word = words[0]
        remnants = words[1:]
        for count in Syllables(word).counts:
            total = node.value + count
            if total > self.level_maxes[level]:
                continue
            elif total == self.level_maxes[level]:
                level += 1
            new_node = Node(total)
            node.children.append(new_node)
            self.sum_syllables(remnants, new_node, level)

    def has_valid_haiku(self, root):
        for child in root.children:
            if child.value == self.level_maxes[-1]:
                return True
            else:
                return self.has_valid_haiku(child)
        return False

    def is_valid(self):
        root = Node()
        self.sum_syllables(self.text, root)
        return self.has_valid_haiku(root)

    def is_valid2(self):
        return sum(Syllables(word).counts[0] for word in self.text) == sum(self.phrase_counts)

    def phrases(self):
        return ()
