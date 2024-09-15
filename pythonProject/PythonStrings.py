# Python Strings
# multiple line string
story='''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(story)
print(len(story))
print(story[5])
print("sit" in story)
print("sunny" not in story)

# for c in story[:5]:
#     print(c)

if "sunny" in story:
    print("ok")
else:
    print("not available")
myName="Rabius Sunny"
print(myName[0:2])
print(myName[3:8])
print(myName[:6])
print(myName[2:])
