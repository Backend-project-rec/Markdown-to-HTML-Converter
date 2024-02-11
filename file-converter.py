import sys
import markdown
from markdown.extensions.extra import ExtraExtension

def convert_markdown_to_html(input_file_path, output_file_path):
    # Read markdown
    with open(input_file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Convert markdown to html only using markdown library
    html = markdown.markdown(text, extensions=[ExtraExtension()])
    
    # Write html
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    # Validate command line
    if len(sys.argv) < 4 or sys.argv[1].lower() != 'markdown':
        print("Usage: python3 file-converter.py markdown inputfile.md outputfile.html")
    else:
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        convert_markdown_to_html(input_file, output_file)
