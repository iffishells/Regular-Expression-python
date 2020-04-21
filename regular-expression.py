import re

#list of pattern to search for
patterns =  ["term1" , "term2"]

#text to parse
text = "Hi am term1  I am a string and what about you!"

for pattern in patterns:

    print(pattern,text)


#re.search is built function in re pkg
#which take 2 parameter one for search 
#one for which you want to search

    if re.search(pattern,text):
        print("Match was found")
    else:
        print("Match was not found!")

# Now we've seen that re.search() will take the pattern, scan the text, and then
# returns a Match object. If no pattern is found, a None is returned.
# To give a clearer picture of this match object, check out the code below:

pattern = "term1"

text = "This is a string with term1 ,but it does not have the term2"

match=re.search(pattern,text)

print("the type of return : ",type(match))

# This Match object returned by the search() method is more than just a Boolean
# or None, it contains information about the match, including the original input
# string, the regular expression that was used, and the location of the match.
# Let's see the methods we can use on the match object:


#show start of the match
print(match.start())

#show end
print(match.end())

#######################################
####  ###
#######################################


