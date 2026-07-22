import os

lines = ""


for file in os.listdir("css"):
    with open(f"css/{file}", encoding="utf-8") as f:
        lines += "".join(f.readlines())

with open("output.css")