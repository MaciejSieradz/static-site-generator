from __future__ import annotations
from typing import Dict, List, Optional

class HTMLNode():

    def __init__(
            self,
            tag: Optional[str] = None,
            value: Optional[str] = None,
            children: Optional[List[HTMLNode]] = None,
            props: Optional[Dict[str, str]] = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'

        return html

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):

    def __init__(self,
                 tag: Optional[str],
                 value: Optional[str],
                 props: Optional[Dict[str, str]] = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, LeafNode):
            return False

        return (
            self.tag == value.tag
            and self.value == value.value
            and self.props == value.props
        )

class ParentNode(HTMLNode):

    def __init__(self,
                 tag: str,
                 children: List[HTMLNode],
                 props: Optional[Dict[str, str]] = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node has to have a tag")

        if self.children is None:
            raise ValueError("Parent node has to have a child")

        html = f"<{self.tag}>"

        for child in self.children:
            html += child.to_html()

        return f"{html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
