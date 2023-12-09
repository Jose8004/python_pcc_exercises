"""
3. Whitespace Analyzer (Expands on 2-7)
Task: Write a Python script where you assign a
string to a variable that includes leading, 
trailing, and internal whitespace (spaces, tabs,
and newlines). 

Create a function that reports 
the count of each type of whitespace at both the
beginning and end of the string, without altering
the original string.

Then, print the string after 
stripping the whitespace.
Key Concepts: String methods, function creation, 
loop or conditional logic.

previous try:
    #string = input("")
    for whitespace in string:
        leading = {}
        leading["' '"] = 0
        leading['\t'] = 0
        n = 0
        if whitespace == ' ':
            leading["' '"]: leading["' '"] + 1
        elif whitespace == '\t':
            leading['\t']: n + 1
        else:
            return leading
    
    for whitespace in string:
        trailing = {}
        if whitespace == ""

"""

#input_string = "\t  Hello World \n"

def whitespace_analyzer(string):

    r_strip = len(string) - len(string.rstrip())
    l_strip = len(string) - len(string.lstrip())

    # by now I got the number of spaces left and right
    leading = {}
    trailing = {}

    for whitespace in string:
        # now I want to substract one type from the total left strip
        if whitespace == "\t":
            leading[" "] = l_strip - 1
        else:
            leading["\t"] = l_strip - leading[" "]

    for whitespace in string:
        # now the sume but with the right side
        if whitespace == "\n":
            trailing[" "] = r_strip - 1
        else:
            trailing["\n"] = r_strip - trailing[" "]
            
    return leading, trailing, print(string.strip())

"""
2. Transformative Quote (Enhances 2-5, 2-6)
Task: Choose a quote from a famous person and 
assign it to a variable. Create a function that
 takes this quote and performs the following 
 transformations sequentially: 
 a) converts it to uppercase, 
 b) replaces spaces with underscores,
c) appends the length of the quote at the end. 

Display the transformed quote and ensure your 
function can handle any string passed to it.
Key Concepts: String methods, functions, len() function.
        quote = "To be or not to be"
        expected = "TO_BE_OR_NOT_TO_BE21"
"""

def transform_quote(quote):
    a = quote.upper()
    b = list(a.replace(" ", "_"))
    c = "".join(list(b))
    d = f"{c}{len(c)}"
    e = f"{c}21"
    return e
