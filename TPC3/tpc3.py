import re
import sys


def coversor_mk_to_html(text):

    text = re.sub(r"^#([^#\n]+)$",r"<h1>\1</h1>",text, flags=re.MULTILINE)
    
    text = re.sub(r"^##([^#\n]+)$",r"<h2>\1</h2>",text, flags=re.MULTILINE)
    
    text = re.sub(r"^###(.+)$",r"<h3>\1</h3>",text, flags=re.MULTILINE)
    
    text = re.sub(r"\*\*([^*]+)\*\*",r"<b>\1</b>",text)
    
    text = re.sub(r"\*([^*]+)\*",r"<b>\1</b>",text)
    
    text = re.sub(r"^1.(.+)$",r"<ol>\n<li>\1</li>\n</ol>",text, flags=re.MULTILINE)    
    
    text = re.sub(r"^[2-9].(.+)$",r"<li>\1</li>\n</ol>",text, flags=re.MULTILINE)    

    text = re.sub(r"</li>\n</ol></li>",r"<li>\n</li>",text, flags=re.MULTILINE)    
    
    text = re.sub(r"\[([^\[]+)\]\(([^(]+)\)",r"<a href=\"\2\">\1</a>",text)    
    
    text = re.sub(r"!\[([^\[]+)\]\(([^\)]+)\)", r'<img src="\2" alt="\1">', text)

    return text

if len(sys.argv) != 3:
    print("Twns que dar o nome do ficheiro e o nome do que queres criar")
    sys.exit(1)


with open(sys.argv[1], 'r', encoding='utf-8') as f:
    text = f.read()
    output_file = sys.argv[2]

    text = coversor_mk_to_html(text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Arquivo HTML gerado: {output_file}")
