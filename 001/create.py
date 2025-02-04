import os

import re

BUFFER = "/tmp/buffer.fountain"

def main():
    files = sorted([f for f in os.listdir(".") if re.search(r"^\d{3} ", f)])
    contents = []
    for filename in files:
        with open(filename) as file:
            contents.append(file.read())
    with open(BUFFER, "w") as file:
        file.write("\n\n".join(contents))
    os.system(f"afterwriting --source {BUFFER} --pdf out.pdf")

if __name__ == "__main__":
    main()

