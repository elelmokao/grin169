#!/usr/bin/env python3
import os
import sys
import re


BASE_DIR = "grind169"
LANGS = [
    {"lang": "Go", "dir": "golang", "ext": "go", "template": "./template/template.go"},
    {"lang": "C++", "dir": "cpp", "ext": "cpp", "template": "./template/template.cpp"},
    {"lang": "Python", "dir": "python", "ext": "py", "template": "./template/template.py"},
]
LEETCODE_BASE = "https://leetcode.com/problems/"

def slugify(title: str) -> str:
    return title.lower().replace(" ", "_")


def main():

    if len(sys.argv) < 2:
        print("Usage: python add_problem.py two_sum [--lang cpp|python|go]")
        sys.exit(1)

    slug = sys.argv[1].strip().lower()
    title = slug
    url = LEETCODE_BASE + slug
    file_name = slug.replace("-", "_")

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
            difficulty="unknown",
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
