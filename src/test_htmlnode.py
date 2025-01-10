import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()
