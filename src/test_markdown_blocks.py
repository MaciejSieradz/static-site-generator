import unittest
from markdown_blocks import block_to_block_type, markdown_to_blocks


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_block_to_block_type_heading(self):
        self.assertEqual("heading", block_to_block_type("# This is a heading"))

    def test_block_to_block_type_code(self):
        self.assertEqual("code", block_to_block_type("```\nThis is the code\n```"))

    def test_block_to_block_type_quote(self):
        self.assertEqual("quote", block_to_block_type(">quote\n>quote\n>quote"))

    def test_block_to_block_type_list_1(self):
        block = "* one\n* two\n* three"
        self.assertEqual("unordered_list", block_to_block_type(block))

    def test_block_to_block_type_list_2(self):
        block = "- one\n- two\n- three"
        self.assertEqual("unordered_list", block_to_block_type(block))

    def test_block_to_block_type_list_3(self):
        block = "1. one\n2. two\n3. three"
        self.assertEqual("ordered_list", block_to_block_type(block))

    def test_block_to_block_type_paragraph(self):
        self.assertEqual("paragraph", block_to_block_type("This is standard paragraph\n. Parapraph."))



if __name__ == "__main__":
    unittest.main()
