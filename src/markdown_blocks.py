from typing import List


def markdown_to_blocks(markdown: str) -> List[str]:

    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block != "":
            block = block.strip()
            filtered_blocks.append(block)

    return filtered_blocks
