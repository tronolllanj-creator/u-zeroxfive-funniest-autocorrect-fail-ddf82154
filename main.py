"""Entry point module that writes a specific text line to an output file."""
# Entry validated: output is 1-199 chars, one line, deterministic.

import os
import sys

LINE = "Good morning team please remember to send your daily reports to my nipples before leaving for the weekend"


def main():
    content = LINE + "\n"
    
    # Validate content according to requirements
    if not (1 <= len(content) <= 199 and content.strip()):
        raise ValueError("Content validation failed")
    
    # Determine output directories
    primary_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    directories = [primary_dir]
    if primary_dir != "/output":
        directories.append("/output")
        
    output_path = ""
    for i, d in enumerate(directories):
        try:
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            if i == 0:
                output_path = path
        except Exception:
            if i == 0:
                raise
                
    print(f"{output_path} {len(content)}")


if __name__ == "__main__":
    main()
