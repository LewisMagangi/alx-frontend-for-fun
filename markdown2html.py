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
    
    # If we reach here, everything is valid
    # For now, just exit with success (0)
    # Later, actual conversion logic would go here
    sys.exit(0)


if __name__ == "__main__":
    main()
