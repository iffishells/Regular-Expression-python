#######################################
#### Split with regular expressions ###
######################################

import re

# Let's see how we can split with the re syntax. This should look similar to how
# you used the split() method with strings.


split_term="@"

phrase = "what is the domain name of someone domain with the email:iffishells@gmail.com"

#return list at the spliting point..!
print(re.split(split_term,phrase))



# Note how re.split() returns a list with the term to spit on removed and the
# terms in the list are a split up version of the string. Create a couple of
# more examples for yourself to make sure you understand!


############################################
### Finding all instances of a pattern #####
############################################

# You can use re.findall() to find all the instances of a pattern in a string.
# For example:

print(re.findall("domain",phrase))
