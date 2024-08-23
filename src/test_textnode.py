import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "text")
        node2 = TextNode("This is a text node", "text")
        self.assertEqual(node, node2)

    def test_eq_false(self): #texttype is different
        node = TextNode("This is a text node", "text")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self): #text is different
        node = TextNode("This is a text node", "text")
        node2 = TextNode("This is a text node2", "text")
        self.assertNotEqual(node, node2)

    def test_eq_url(self): #with URL
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self): #represetnation method testing
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))


if __name__ == "__main__":
    unittest.main()