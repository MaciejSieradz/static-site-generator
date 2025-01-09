import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_contains_url(self):
        node = TextNode("This is a text node", TextType.CODE, "https://test.com")
        node2 = TextNode("This is a text node", TextType.CODE, "https://test.com")
        self.assertEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_one_contains_url(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE, "https://test.com")
        self.assertNotEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://test.com")
        self.assertEqual(
            "TextNode(This is a text node, text, https://test.com)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
