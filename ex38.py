ten_things = "Apples Oranges Crows Telephone Light Sugar" # string

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') # lists
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] # lists

while len(stuff) != 10:
    next_one = more_stuff.pop() # last word
    print "Adding: ", next_one
    stuff.append(next_one) # add to lists
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool! string
print '#'.join(stuff[3:5]) # super stellar!  string
