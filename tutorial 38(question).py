# Date 19-3-2021

# Make a program which is using any 2 modules weather internal or external

import wikipedia
import emoji

print("\N{kissing face}")

search = str(input("What you want to search in wikipedia:\n"))
print(wikipedia.summary(search, sentences=2))
