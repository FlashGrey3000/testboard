import re

def markdown_to_text(md: str) -> str:
    """
    Convert a Markdown string to plain text.
    Supports headers, bold, italics, links, and code blocks.
    """
    
    # code blocks
    text = re.sub(r'```.*?```', '', md, flags=re.DOTALL)

    # code inline
    text = re.sub(r'`.*?`', '', text)

    # bold and italics
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)

    # headers
    text = re.sub(r'^#+\s*(.*)', r'\1', text, flags=re.MULTILINE)

    # links
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

    # white spaces
    text = text.strip()
    return text