#!/usr/bin/python3
"""This module prints a text with 2 new lines
    after each of these characters: `.`, `?` and `:`
"""


def text_indentation(text):
    """The function prints a text with 2 new lines
        after each of these characters: `.`, `?` and `:`

        Args:
            size: the text to print

        Returns:
            Nothing
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []
    line = ""
    for t in text:
        if t not in (".", "?", ":"):
            line += t
        else:
            line = line.strip()
            if line:
                lines.append(line)
            lines.append(t+"\n\n")
            line = ""

    line = line.strip()
    if line:
        lines.append(line)

    for lne in lines:
        print("{}".format(lne), end="")
