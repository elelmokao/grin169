#!/usr/bin/env python3
import os
import sys
import requests
from dotenv import load_dotenv



BASE_DIR = "grind169"
LANGS = [
    {"lang": "Go", "dir": "golang", "ext": "go", "template": "./template/template.go"},
    {"lang": "C++", "dir": "cpp", "ext": "cpp", "template": "./template/template.cpp"},
    {"lang": "Python", "dir": "python", "ext": "py", "template": "./template/template.py"},
]
LEETCODE_BASE = "https://leetcode.com/problems/"
SUPABASE_URL = "https://raggfqikonlermdpkjcb.supabase.co/rest/v1/rpc/get_problem_metadata"

def slugify(title: str) -> str:
    return title.lower().replace(" ", "_")


def get_problem_metadata(problem_id: int):
    load_dotenv()
    key = os.getenv("ANON_KEY")
    if not key:
        print("Error: ANON_KEY environment variable not set.")
        sys.exit(1)
        
    headers = {
        "Content-Type": "application/json",
        "apikey": key,
        "Authorization": f"Bearer {key}"
    }
    payload = {"input_id": problem_id}
    
    try:
        response = requests.post(SUPABASE_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if not data:
            print(f"No problem found with ID {problem_id}")
            sys.exit(1)
        return data[0]
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        sys.exit(1)


def main():

    if len(sys.argv) < 2:
        print("Usage: python add_problem.py <problem_id> [--lang cpp|python|go]")
        sys.exit(1)

    try:
        problem_id = int(sys.argv[1])
    except ValueError:
        print("Error: Problem ID must be an integer.")
        sys.exit(1)

    metadata = get_problem_metadata(problem_id)
    
    slug = metadata["slug"]
    title = metadata["title"]
    url = LEETCODE_BASE + slug
    file_name = slug.replace("-", "_")
    
    difficulty_map = {1: "Easy", 2: "Medium", 3: "Hard"}
    difficulty = difficulty_map.get(metadata["difficulty"], "Unknown")

    # 預設語言
    lang_name = "Go"
    if len(sys.argv) == 4 and sys.argv[2] == "--lang":
        lang_name = sys.argv[3].capitalize() if sys.argv[3].lower() != "cpp" else "C++"
        if lang_name not in [l["lang"] for l in LANGS]:
            print("Supported languages: go, cpp, python")
            sys.exit(1)
    elif len(sys.argv) > 2:
        print("Usage: python add_problem.py two_sum [--lang cpp|python|go]")
        sys.exit(1)

    lang = next(l for l in LANGS if l["lang"].lower() == lang_name.lower())

    md_path = os.path.join(BASE_DIR, f"{file_name}.md")

    # Markdown
    if not os.path.exists(md_path):
        with open("./template/template.md", "r") as f:
            content = f.read()

        content = content.format(
            Title=title,
            url=url,
            difficulty=difficulty,
            lang=lang["lang"],
            langPath=f"./{lang['dir']}/{file_name}.{lang['ext']}",
        )

        with open(md_path, "w") as f:
            f.write(content)

        print(f"Created {md_path}")
    else:
        print(f"Exists {md_path}")

    # 產生指定語言檔案
    lang_dir = os.path.join(BASE_DIR, lang["dir"])
    lang_path = os.path.join(lang_dir, f"{file_name}.{lang['ext']}")
    os.makedirs(lang_dir, exist_ok=True)
    if not os.path.exists(lang_path):
        with open(lang["template"], "r") as f:
            template_content = f.read()
        with open(lang_path, "w") as f:
            f.write(template_content)
        print(f"Created {lang_path}")
    else:
        print(f"Exists {lang_path}")

    # 若用戶指定語言，才產生其他語言檔案
    if len(sys.argv) > 2:
        extra_langs = [arg.lower() for arg in sys.argv[2:]]
        for lang in LANGS:
            if lang["lang"].lower() in extra_langs and lang["lang"] != "Go":
                lang_dir = os.path.join(BASE_DIR, lang["dir"])
                lang_path = os.path.join(lang_dir, f"{file_name}.{lang['ext']}")
                os.makedirs(lang_dir, exist_ok=True)
                if not os.path.exists(lang_path):
                    with open(lang["template"], "r") as f:
                        template_content = f.read()
                    with open(lang_path, "w") as f:
                        f.write(template_content)
                    print(f"Created {lang_path}")
                else:
                    print(f"Exists {lang_path}")

if __name__ == "__main__":
    main()
