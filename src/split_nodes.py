from typing import List, Tuple
from textnode import TextNode, TextType
import re

def text_to_textnodes(text: str) -> List[TextNode]:
    nodes = split_nodes_image(split_nodes_link([TextNode(text, TextType.TEXT)]))
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    return nodes

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    if delimiter not in ['`', '**', '_']:
        ValueError("Not supported delimiter")
    new_nodes: List[TextNode] = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            splitted_by_delimiter = split_text_delimiter(node.text, delimiter)
            if len(splitted_by_delimiter) % 2 == 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            new_nodes.extend(list_of_splitted_nodes(splitted_by_delimiter, text_type))

    return new_nodes

def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes: List[TextNode] = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if node.text_type is not TextType.TEXT or len(images) == 0:
            new_nodes.append(node)
        else:
            text = ""
            for image in images:
                if text == "":
                    splitted = node.text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
                else:
                    splitted = text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
                text = splitted[1]
                if splitted[0] != "":
                    new_nodes.append(TextNode(splitted[0], TextType.TEXT))
                new_nodes.append(TextNode(image[0],TextType.IMAGE, image[1]))
            if text != "":
                new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes: List[TextNode] = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if node.text_type is not TextType.TEXT or len(links) == 0:
            new_nodes.append(node)
        else:
            text = ""
            for link in links:
                if text == "":
                    splitted = node.text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
                else:
                    splitted = text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
                text = splitted[1]
                if splitted[0] != "":
                    new_nodes.append(TextNode(splitted[0], TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if text != "":
                new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches: List[Tuple[str, str]] = re.findall(pattern, text)
    return matches

def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches: List[Tuple[str, str]] = re.findall(pattern, text)
    return matches

def split_text_delimiter(text: str, delimiter: str) -> List[str]:
    return text.split(delimiter)

def list_of_splitted_nodes(splitted_nodes: List[str], text_type: TextType) -> List[TextNode]:
    nodes: List[TextNode] = []
    for i in range(len(splitted_nodes)):
        if splitted_nodes[i] == "":
            continue
        if i % 2 == 0:
            nodes.append(TextNode(splitted_nodes[i], TextType.TEXT))
        else:
            nodes.append(TextNode(splitted_nodes[i], text_type))

    return nodes
