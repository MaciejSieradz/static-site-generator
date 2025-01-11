import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        prop = node.props_to_html()
        self.assertEqual(prop, ' href="https://www.google.com"')

    def test_props_to_html_2(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode(props=props)
        prop = node.props_to_html()
        self.assertEqual(prop, ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node=  HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})"
        )

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_to_html_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just a value")
        self.assertEqual("Just a value", node.to_html())

    def test_to_html_no_children(self):
        node = ParentNode("div", [], None)
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_leaf_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_parent_children(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("b", "Text")
                    ]
                )
            ]
        )
        self.assertEqual(node.to_html(), "<div><div><b>Text</b></div></div>")

    def test_text_node_to_html_node_normal_text(self):
        textnode = TextNode("normal_text", TextType.TEXT)
        node = LeafNode(None, "normal_text")
        self.assertEqual(node, text_node_to_html_node(textnode))

    def test_text_node_to_html_node_bold_text(self):
        textnode = TextNode("normal_text", TextType.BOLD)
        node = LeafNode("b", "normal_text")
        self.assertEqual(node, text_node_to_html_node(textnode))

    def test_text_node_to_html_node_italic_text(self):
        textnode = TextNode("normal_text", TextType.ITALIC)
        node = LeafNode("i", "normal_text")
        self.assertEqual(node, text_node_to_html_node(textnode))

    def test_text_node_to_html_node_code_text(self):
        textnode = TextNode("normal_text", TextType.CODE)
        node = LeafNode("code", "normal_text")
        self.assertEqual(node, text_node_to_html_node(textnode))

    def test_text_node_to_html_node_link(self):
        textnode = TextNode("normal_text", TextType.LINK, "https://www.google.com")
        node = LeafNode("a", "normal_text", {"href": "https://www.google.com"})
        self.assertEqual(node, text_node_to_html_node(textnode))

    def test_text_node_to_html_node_img(self):
        textnode = TextNode("img", TextType.IMAGE, "https://www.google.com")
        node = LeafNode("img", "", {"src": "https://www.google.com", "alt": "img"})
        self.assertEqual(node, text_node_to_html_node(textnode))

if __name__ == "__main__":
    unittest.main()
