#!/usr/bin/python3
"""
Script to convert Markdown files to HTML.

This module provides functionality to convert Markdown files to HTML format.
It validates command line arguments and checks file existence before processing.
"""

import sys
import os


def main():
    """Main function to handle markdown to html conversion.
    
    Validates command line arguments and processes the markdown file.
    Exits with code 1 if arguments are invalid or file is missing.
    Exits with code 0 if validation passes.
    """
    
    # Check if the number of arguments is correct
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    # Get the input and output filenames
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Check if the markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # Process the markdown file and convert to HTML
    convert_markdown_to_html(markdown_file, output_file)
    
    # Exit with success
    sys.exit(0)


def convert_markdown_to_html(markdown_file, output_file):
    """Convert markdown file to HTML file.
    
    Args:
        markdown_file (str): Path to the input markdown file
        output_file (str): Path to the output HTML file
    """
    try:
        with open(markdown_file, 'r', encoding='utf-8') as md_file:
            lines = md_file.readlines()
        
        html_lines = []
        
        for line in lines:
            line = line.rstrip('\n')
            
            # Skip empty lines
            if not line.strip():
                continue
            
            # Process heading lines
            if line.startswith('#'):
                html_line = convert_heading(line)
                html_lines.append(html_line)
            else:
                # For now, just keep non-heading lines as is
                # This can be expanded later for other markdown syntax
                html_lines.append(line)
        
        # Write HTML content to output file
        with open(output_file, 'w', encoding='utf-8') as html_file:
            for html_line in html_lines:
                html_file.write(html_line + '\n')
                
    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)
        sys.exit(1)


def convert_heading(line):
    """Convert markdown heading to HTML heading.
    
    Args:
        line (str): A markdown heading line starting with #
        
    Returns:
        str: HTML heading tag
    """
    # Count the number of # symbols
    level = 0
    for char in line:
        if char == '#':
            level += 1
        else:
            break
    
    # Extract the heading text (remove # symbols and leading/trailing spaces)
    heading_text = line[level:].strip()
    
    # Generate HTML heading tag
    return f"<h{level}>{heading_text}</h{level}>"


if __name__ == "__main__":
    main()