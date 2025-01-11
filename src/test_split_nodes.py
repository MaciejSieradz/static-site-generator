import unittest

from split_nodes import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expect = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(expect, text_to_textnodes(text))

    def test_text_to_textnodes_no_links_no_images(self):
        text = "This is **text** with an *italic* word and a `code block`."
        expect = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]

        self.assertListEqual(expect, text_to_textnodes(text))

    def test_text_to_textnodes_only_text(self):
        text = "This is just a standard, plain, boring text."
        expect = [
            TextNode("This is just a standard, plain, boring text.", TextType.TEXT)
        ]

        self.assertListEqual(expect, text_to_textnodes(text))

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expect = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(expect, new_nodes)

    def test_split_nodes_delimiter_no_matching_text_type(self):
        node = TextNode("This is text with a code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expect = [
            TextNode("This is text with a code block word", TextType.TEXT),
        ]
        self.assertEqual(expect, new_nodes)

    def test_split_nodes_delimiter_first(self):
        node = TextNode("**This** is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expect = [
            TextNode("This", TextType.BOLD),
            TextNode(" is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(expect, new_nodes)

    def test_split_nodes_delimiter_not_text_type(self):
        node = TextNode("bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual([node], new_nodes)

    def test_split_nodes_delimiter_multiple_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        expect = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(expect, new_nodes)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expect = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(expect, extract_markdown_images(text))

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expect = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(expect, extract_markdown_links(text))

    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        expect = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        ]
        self.assertListEqual(expect, split_nodes_link([node]))

    def test_split_nodes_links_2(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) text after",
            TextType.TEXT,
        )
        expect = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" text after", TextType.TEXT)
        ]
        self.assertListEqual(expect, split_nodes_link([node]))

    def test_split_nodes_links_3(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        expect = [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        ]
        self.assertListEqual(expect, split_nodes_link([node]))

    def test_split_nodes_links_multiple_nodes(self):
        node = TextNode(
            "This is a text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT
        )
        node2 = TextNode(
            "This is a text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT
        )
        expect = [
            TextNode("This is a text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode("This is a text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")

        ]
        self.assertListEqual(expect, split_nodes_link([node, node2]))

    def test_split_nodes_links_no_links(self):
        node = TextNode(
            "This is a text without links.",
            TextType.TEXT
        )
        expect = [node]
        self.assertListEqual(expect, split_nodes_link([node]))


    def test_split_nodes_images_multiple_nodes(self):
        node = TextNode(
            "This is a text with an image ![to boot dev](https://www.boot.dev)",
            TextType.TEXT
        )
        node2 = TextNode(
            "This is a text with an image ![to boot dev](https://www.boot.dev)",
            TextType.TEXT
        )
        expect = [
            TextNode("This is a text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode("This is a text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev")

        ]
        self.assertListEqual(expect, split_nodes_image([node, node2]))

    def test_split_nodes_images_no_images(self):
        node = TextNode(
            "This is a text without images.",
            TextType.TEXT
        )
        expect = [node]
        self.assertListEqual(expect, split_nodes_image([node]))

    def test_split_nodes_images_multiple_images(self):
        node = TextNode(
            "This is a text with an image ![to boot dev](https://www.boot.dev) and another image ![to secret](https://www.very-secret.key)",
            TextType.TEXT
        )
        expect = [
            TextNode("This is a text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and another image ", TextType.TEXT),
            TextNode("to secret", TextType.IMAGE, "https://www.very-secret.key")

        ]
        self.assertListEqual(expect, split_nodes_image([node]))

    def test_split_nodes_images_image_first(self):
        node = TextNode(
            "![to boot dev](https://www.boot.dev) This is a text with an image",
            TextType.TEXT
        )
        expect = [
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" This is a text with an image", TextType.TEXT)
        ]
        self.assertListEqual(expect, split_nodes_image([node]))
