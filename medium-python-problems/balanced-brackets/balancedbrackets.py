"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""


# def has_balanced_brackets(phrase):
#     """Does a given string have balanced pairs of brackets?

#     Given a string as input, return True or False depending on whether the
#     string contains balanced (), {}, [], and/or <>.
#     """
#     # put all possible pairs in dict
#     pairs = {'}':'{', ']':'[', ')':'(', '>':'<'}
#     # list as stack to hold values
#     stack = []
#     # iterate through each char
#     for char in phrase:
#         # add to stack if open bracket (values)
#         if char in pairs.values():
#             stack.append(char)
#         # else if key value 
#         elif char in pairs:
#           # if empty stack or char doesn't equal what's on top
#           if not stack or pairs[char] != stack.pop():
#               return False
#     return not stack


# solution from interview
def has_balanced_brackets(string):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """
    if not string:
        raise ValueError('String is empty')
    bracket_dict = {')':'(', ']':'[', '>':'<', '}':'{'}
    vals = set(bracket_dict.values())
    stack = []
    for char in string:
        if char in vals:
            stack.append(char)
        elif char in bracket_dict:
            if not stack or bracket_dict[char] != stack.pop():
                return False
    return not stack

# tests = [
#     ("", "String is empty"),
#     ("123[", False),
#     ('123[009]', True),
#     ('123[009]]', False),
#     (']abc', False),
#     ('[]]abc[', False),
#     ('a(b[c)d]', False),
#     ('a(bc[d]ef)g', True)   
# ]

# for i, (t, exp) in enumerate(tests):
#     try:
#         r = balanced_brackets(t)
#     except ValueError as e:
#         r = str(e)
#     print "%d. '%s' -> %s (%s)" % (i + 1, t, r, "SUCCESS" if r == exp else "FAIL") 


# alt solution
# def has_balanced_brackets(phrase):
#     """Does a given string have balanced pairs of brackets?

#     Given a string as input, return True or False depending on whether the
#     string contains balanced (), {}, [], and/or <>.
#     """

#     # START SOLUTION

#     closers_to_openers = {")": "(", "]": "[", "}": "{", ">": "<"}

#     # Set of all opener characters; used to match openers quickly.
#     openers = set(closers_to_openers.values())

#     # Create an empty list to use as a stack.
#     openers_seen = []

#     for char in phrase:

#         # Push open brackets onto the stack.

#         if char in openers:
#             openers_seen.append(char)

#         # For closers:
#         #
#         # - if nothing is open; fail fast
#         # - if we are the twin of the most recent opener, pop & continue
#         # - else we're the twin to a different opener; fail fast

#         elif char in closers_to_openers:

#             if openers_seen == []:
#                 return False

#             if openers_seen[-1] == closers_to_openers.get(char):
#                 openers_seen.pop()

#             else:
#                 return False

#     # An empty stack means the brackets are balanced.
#     return openers_seen == []    
        

        




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n")
