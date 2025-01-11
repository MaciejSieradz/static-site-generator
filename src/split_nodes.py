from typing import List
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    if delimiter not in ['`', '**', '*']:
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
