###########################
### Pattern re Syntax ######
############################

import re

# This will be the bulk of this lecture on using re with Python. Regular
# expressions supports a huge variety of patterns the just simply finding
# where a single string occurred.
#
# We can use *metacharacters* along with re to find specific types of patterns.
#
# Since we will be testing multiple re syntax forms, let's create a function
# that will print out results given a list of various regular expressions and
# a phrase to parse:


def multi_re_find(patterns,phrase):

    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''

    for pattern in patterns:

        print(" searching the phrase using re check , ",pattern)

        print(re.findall(pattern,phrase))

        print("\n")

# There are five ways to express repetition in a pattern:
#
#     1.) A pattern followed by the meta-character * is repeated zero or more times.
#     2.) Replace the * with + and the pattern must appear at least once.
#     3.) Using ? means the pattern appears zero or one time.
#     4.) For a specific number of occurrences, use {m} after the pattern, where
#         m is replaced with the number of times the pattern should repeat.
#     5.) Use {m,n} where m is the minimum number of repetitions and n is the
#         maximum. Leaving out n ({m,}) means the value appears at least m times,
#         with no maximum.
#
# Now we will see an example of each of these using our multi_re_find function:

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{1,2}',      # s followed by two to three d's
                ]

#multi_re_find("sd","sdsdsds..")

multi_re_find(test_patterns,test_phrase)


#############################
### Character Sets ##########
#############################

# Character sets are used when you wish to match any one of a group of
# characters at a point in the input. Brackets are used to construct character
# set inputs. For example: the input [ab] searches for occurrences of either a or b.

# Let's see some examples:
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ '[sd]',    # either s or d
            's[sd]+']   # s followed by one or more s or d


multi_re_find(test_patterns,test_phrase)


# It makes sense that the first [sd] returns every instance. Also the second
# input will just return any thing starting with an s in this particular case
# of the test phrase input.

#############################
### Exclusion ###############
#############################

# We can use ^ to exclude terms by incorporating it into the bracket syntax
# notation. For example: [^...] will match any single character not in the
# brackets.

# Let's see some examples:

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'


# Use [^!.? ] to check for matches that are not a !,.,?, or space. Add the +
# to check that the match appears at least once, this basically translate into
# finding the words.

re.findall('[^!.? ]+',test_phrase)

#############################
## Character Ranges #########
#############################

# As character sets grow larger, typing every character that should (or should
# not) match could become very tedious. A more compact format using character
# ranges lets you define a character set to include all of the contiguous
# characters between a start and stop point. The format used is [start-end].
#
# Common use cases are to search for a specific range of letters in the alphabet,
#  such [a-f] would return matches with any instance of letters between a and f.
#
# Let's walk through some examples:

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=[ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+'] # one upper case letter followed by lower case letters

multi_re_find(test_patterns,test_phrase)

#############################
### Escape Codes ############
#############################

# You can use special escape codes to find specific types of patterns in your
# data, such as digits, non-digits,whitespace, and more.

# For example:

#
# Escapes are indicated by prefixing the character with a backslash (\).
# Unfortunately, a backslash must itself be escaped in normal Python strings,
# and that results in expressions that are difficult to read. Using raw strings,
# created by prefixing the literal value with r, for creating regular expressions
#  eliminates this problem and maintains readability.
#
# Personally, I think this use of r to escape a backslash is probably one of the
# things that block someone who is not familiar with regex in Python from being
# able to read regex code at first. Hopefully after seeing these examples this
# syntax will become clear.


test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)

#############################
### Conclusion ##############
#############################
# You should now have a solid understanding of how to use the regular expression
# module in Python. There are a ton of more special character instances, but it
# would be unreasonable to go through every single use case. Instead take a look
# at the full [documentation](https://docs.python.org/2/library/re.html#regular-expression-syntax)
# if you ever need to look up a particular case.
#
# You can also check out the nice summary tables at this source :
# (http://www.tutorialspoint.com/python/python_reg_expressions.htm).
#

