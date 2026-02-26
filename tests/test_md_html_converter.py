import pytest
from src.md_html_converter import markdown_to_text

@pytest.fixture
def markdown_samples():
    return {
        "header": "# This is a header",
        "bold": "This is **bold** text",
        "italic": "This is *italic* text",
        "link": "Click [here](https://example.com)",
        "code_block": "```\nprint('Hello')\n```",
        "inline_code": "Use `print()` function",
        "complex": "# Header\nSome **bold** and *italic* text with a [link](https://example.com)\n```\ncode\n```"
    }

def test_header(markdown_samples):
    assert markdown_to_text(markdown_samples["header"]) == "This is a header"

def test_bold(markdown_samples):
    assert markdown_to_text(markdown_samples["bold"]) == "This is bold text"

def test_italic(markdown_samples):
    assert markdown_to_text(markdown_samples["italic"]) == "This is italic text"

def test_link(markdown_samples):
    assert markdown_to_text(markdown_samples["link"]) == "Click here"

def test_code_block(markdown_samples):
    assert markdown_to_text(markdown_samples["code_block"]) == ""

def test_inline_code(markdown_samples):
    assert markdown_to_text(markdown_samples["inline_code"]) == "Use  function"

def test_complex(markdown_samples):
    expected = "Header\nSome bold and italic text with a link"
    assert markdown_to_text(markdown_samples["complex"]) == expected