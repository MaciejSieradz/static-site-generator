import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_to_html_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just a value")
        self.assertEqual("Just a value", node.to_html())

if __name__ == "__main__":
    unittest.main()
