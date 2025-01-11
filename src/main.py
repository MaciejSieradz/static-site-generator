from split_nodes import split_nodes_images
from textnode import TextNode, TextType


def main():
    text = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
    print(split_nodes_images([text]))
if __name__ == "__main__":
    main()
