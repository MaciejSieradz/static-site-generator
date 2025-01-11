from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
    node = HTMLNode(tag="a", props={"href": "https://www.google.com"})
    print(node)
    print("`This` is a text with a `code block` word".split('`'))

if __name__ == "__main__":
    main()
