import nltk
import re
from nltk.tokenize import regexp

# 1 ======================================================
text = """
10 WORK \t lecture
11 PRIV Breakfast
12 WORK laboratories
"""

# 1.1
# tokenizer = regexp.RegexpTokenizer("\d+")
# hours = tokenizer.tokenize(text)
# print(hours)

# 1.2
# match = re.search(r"\b(0[0-9]|1[0-9]|2[0-9])\b", text)
# if match:
#     print(match)
# else: print("not found")

# 1.3
# using split and join
# words = text.split()
# print("".join(words))

# 1.3
# using substitution
# result = re.sub("\s+", "", text)
# print(result)

# 1.4
# using regex
# words = re.findall(r"\b[A-Z]+\b", text)
# print(words)

# 1.4
# using string methods
# words = [i for i in text.split() if i.isupper()]
# print(words)

# 1.5
# words = re.findall(r"\b[A-Za-z][a-z]+\b", text)
# print(words)

# 1.6 only first occurrence
# matches = re.search(r"(\d+)\s+([A-Z]+)\s+(.+)", text)
# print(matches.group(1), matches.group(2), matches.group(3))

# 1.6 all
# matches = re.findall(r"(\d+)\s+([A-Z]+)\s+(.+)", text)
# for match in matches:
#     print(match[0], match[1], match[2])

# 2 ======================================================
html_doc = """
<body>
<h1>My First Heading</h1>
<p>My first paragraph.</p>
</body>
"""

# # 2.1
# print(re.findall(r"</?\w+>", html_doc))
# # 2.2
# print(re.findall(r"</\w+>", html_doc))
# # 2.3
# pattern = r"<[^>]*>"
# raw_text = re.sub(pattern, "", html_doc)
# print(raw_text)

# 3 ======================================================
# 3.1 \b(\w+)\W+\1\b
# 3.2 ^\d+\s+\w+$
# 3.3 ^([A-Z][a-z]*)