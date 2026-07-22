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


class_lines = ""
for line in lines.split("\n"):
    if "{" in line and not any([x in line for x in ["%", "@", ":root"]]):
        line = line[:-1].strip() + ".fs {"
    class_lines += line + "\n"


with open("classes.css", "w", encoding="utf-8") as f:
    f.write(class_lines)
