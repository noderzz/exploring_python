#Quick Python Script to rename a bunch of files in a directory.
import os
import re

pattern = re.compile(r"mouth0(\d{1})\.png")
for filename in os.listdir("."):
    match = pattern.match(filename)
    print(match)
    if match:
        new_filename = "mouth{}.png".format(match.group(1))
        os.rename(filename, new_filename)