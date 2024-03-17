s = input('Please enter text for analysis: ')
t = input('Please enter 3 letters: ')
#1

print(f"the letter {t[0]} appears {s.lower().count(t[0].lower())} times")
print(f"the letter {t[1]} appears {s.lower().count(t[1].lower())} times")
print(f"the letter {t[2]} appears {s.lower().count(t[2].lower())} times")

#2

l = s.split()
print(f"There are total of {len(l)} words in text.")

#3

print(f"first letter: {s[0]} \n last letter: {s[-1]}")

#4

l.reverse()
print(" ".join(l))

#5

print("python" in s)