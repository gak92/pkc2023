# While and For loops

x = 0
while x <= 5:
  print(x)
  x = x + 1

for x in range(11,19):
  print(x)

days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
for d in days:
  if d == "Fri":
    break # stop when "Fri" come and does not print rest of the item
  print(d)


days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
for d in days:
  if d == "Fri":
    continue    # ski "Fri" and print all remaining items
  print(d)