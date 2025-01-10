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
