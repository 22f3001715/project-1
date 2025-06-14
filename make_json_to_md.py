# /// script
# dependencies = [
#   "requests<3",
#   "json",
#   "os",
#   "pathlib"
# ] 
# requires-python = ">=3.11"
# ///
import json
import os
from pathlib import Path

def json_to_markdown(data, level=1):
    """
    Recursively convert JSON to Markdown.
    """
    markdown = ""

    if isinstance(data, dict):
        for key, value in data.items():
            markdown += f"{'#' * level} {key}\n\n"
            markdown += json_to_markdown(value, level + 1)
    elif isinstance(data, list):
        for item in data:
            item_md = json_to_markdown(item, level)
            lines = item_md.strip().splitlines()
            if len(lines) == 1:
                markdown += f"- {lines[0]}\n"
            else:
                markdown += f"- {lines[0]}\n"
                for line in lines[1:]:
                    markdown += f"  {line}\n"
    else:
        markdown += f"{data}\n\n"

    return markdown


def main():
    # Folders
    json_folder = Path("markdowns/discourse")
    md_folder = Path("markdowns/discourse_md")
    md_folder.mkdir(exist_ok=True)  # create if not exist

    # Process all JSON files
    for json_file in json_folder.glob("*.json"):
        print(f"Processing: {json_file.name}")

        # Read JSON
        with open(json_file, "r") as f:
            print(f"Reading: {json_file}")
            data = json.load(f)

        # Convert to Markdown
        markdown = json_to_markdown(data)

        # Save as .md with same base name
        md_file = md_folder / f"{json_file.stem}.md"
        md_file.write_text(markdown)

        print(f"Saved: {md_file}")

if __name__ == "__main__":
    main()
