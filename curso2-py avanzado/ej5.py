""" You are given an HTML code snippet of  lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]


The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
All attributes have an attribute value.

Input Format

The first line contains an integer , the number of lines in the HTML code snippet.
The next  lines contain HTML code.

Constraints


Output Format

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.

Format your answers as explained in the problem statement. """


import re

# re es un modulo que proporciona operaciones de coincidencia de expresiones regulares similares.
def parse_html(html_lines):
    tag_pattern = r'<\s*([a-zA-Z]+)([^>]*?)\s*>'
    attribute_pattern = r'([a-zA-Z\-]+)\s*=\s*"([^"]+)"'
    comment_pattern = r'<!--.*?-->'

    html_code = "\n".join(html_lines)
    html_code = re.sub(comment_pattern, "", html_code, flags=re.DOTALL)
    # re sub = re.substituting patteners in strings based on RegEx.

    matches = re.findall(tag_pattern, html_code)
    # re findall intera sobre un string para encontrar un subconjunto de caracteres hasta machear un patron especifico.


    for tag, attributes in matches:
        print(tag)
        
        if attributes.strip():  # suprime los espacios en blanco
            attribute_matches = re.findall(attribute_pattern, attributes)
            for attribute, value in attribute_matches:
                print(f"-> {attribute} > {value}")
        

n = int(input())  # Number of lines
html_lines = [input().strip() for _ in range(n)]
parse_html(html_lines)