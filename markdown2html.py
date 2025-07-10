#!/usr/bin/python3
"""
Script to convert Markdown files to HTML.

This module provides functionality to convert Markdown files to HTML format.
It validates command line arguments and checks file existence before processing.
"""

import sys
import os
import re
import hashlib


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
        i = 0
        
        while i < len(lines):
            line = lines[i].rstrip('\n')
            
            # Skip empty lines
            if not line.strip():
                i += 1
                continue
            
            # Process heading lines
            if line.startswith('#'):
                html_line = convert_heading(line)
                html_lines.append(html_line)
                i += 1
            # Process unordered list items
            elif line.startswith('- '):
                # Start of an unordered list
                html_lines.append('<ul>')
                
                # Process all consecutive list items
                while i < len(lines) and lines[i].rstrip('\n').startswith('- '):
                    list_item = lines[i].rstrip('\n')[2:].strip()  # Remove '- ' and strip
                    list_item = convert_bold_emphasis(list_item)  # Apply bold/emphasis formatting
                    html_lines.append(f'<li>{list_item}</li>')
                    i += 1
                
                # Close the unordered list
                html_lines.append('</ul>')
            # Process ordered list items
            elif line.startswith('* '):
                # Start of an ordered list
                html_lines.append('<ol>')
                
                # Process all consecutive list items
                while i < len(lines) and lines[i].rstrip('\n').startswith('* '):
                    list_item = lines[i].rstrip('\n')[2:].strip()  # Remove '* ' and strip
                    list_item = convert_bold_emphasis(list_item)  # Apply bold/emphasis formatting
                    html_lines.append(f'<li>{list_item}</li>')
                    i += 1
                
                # Close the ordered list
                html_lines.append('</ol>')
            else:
                # Handle paragraphs - collect consecutive non-empty lines
                paragraph_lines = []
                
                # Collect all consecutive non-empty lines that don't start with special characters
                while (i < len(lines) and 
                       lines[i].rstrip('\n').strip() and 
                       not lines[i].startswith('#') and 
                       not lines[i].startswith('- ') and 
                       not lines[i].startswith('* ')):
                    paragraph_lines.append(lines[i].rstrip('\n'))
                    i += 1
                
                # If we have paragraph content, wrap it in <p> tags
                if paragraph_lines:
                    html_lines.append('<p>')
                    
                    # Join lines with <br/> tags for line breaks within paragraphs
                    for j, para_line in enumerate(paragraph_lines):
                        if j > 0:
                            html_lines.append('<br/>')
                        para_line = convert_bold_emphasis(para_line)  # Apply bold/emphasis formatting
                        html_lines.append(para_line)
                    
                    html_lines.append('</p>')
                else:
                    # If no paragraph content, just move to next line
                    i += 1
        
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
    
    # Apply bold/emphasis formatting to heading text
    heading_text = convert_bold_emphasis(heading_text)
    
    # Generate HTML heading tag
    return f"<h{level}>{heading_text}</h{level}>"


def convert_bold_emphasis(text):
    """Convert markdown bold and emphasis syntax to HTML.
    
    Args:
        text (str): Text that may contain **bold**, __emphasis__, [[MD5]], or ((remove c)) syntax
        
    Returns:
        str: Text with HTML bold and emphasis tags, MD5 conversion, and character removal
    """
    # Handle MD5 conversion [[text]]
    def md5_replace(match):
        content = match.group(1)
        return hashlib.md5(content.encode()).hexdigest()
    
    text = re.sub(r'\[\[(.*?)\]\]', md5_replace, text)
    
    # Handle character removal ((text)) - remove all 'c' characters (case insensitive)
    def remove_c(match):
        content = match.group(1)
        return re.sub(r'[cC]', '', content)
    
    text = re.sub(r'\(\((.*?)\)\)', remove_c, text)
    
    # Handle bold text **text**
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    
    # Handle emphasis text __text__
    text = re.sub(r'__(.*?)__', r'<em>\1</em>', text)
    
    return text


if __name__ == "__main__":
    main()