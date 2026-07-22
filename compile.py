import os
import re

lines = ""


for file in os.listdir("css"):
    with open(f"css/{file}", encoding="utf-8") as f:
        lines += "".join(f.readlines()) + "\n"

with open("out.min.css", "w", encoding="utf-8") as f:
    f.write(re.sub(" +", " ", lines.replace("\n", "")))

with open("out.css", "w", encoding="utf-8") as f:
    f.write(lines)
