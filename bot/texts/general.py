from html import escape


def start() -> str:
    text = "Hello, World!"
    
    return escape(text)