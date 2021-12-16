import pprint
message = 'omo guy today has been really stressful like im even tired i need sleep this is another day and im still tired ong'
count = {}

for character in message:
     count.setdefault(character, 0)
     count[character] = count[character] + 1

pprint.pprint(count)

