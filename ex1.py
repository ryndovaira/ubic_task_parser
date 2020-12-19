import parsimonious
import six
from parsimonious.grammar import Grammar

GRAMMAR = Grammar(
    r""" # Test grammar
    expr = space or space
    or = and   more_or
    more_or = ( space "|" space and )*
    and = term  more_and
    more_and = ( space "&" space term )*
    term = not / value
    not = "!" space value
    value =  contains  / equals / bracketed / name
    bracketed = "(" space expr space ")"
    contains  =  name space "~="  space literal
    equals =  name space "="  space literal
    name       = ~"[a-z]+"
    literal    = "\"" chars "\""
    space    = " "*
    chars = ~"[^\"]*"
    """)

# query = 'name ~=".pdf" & ( from ~= "jack" | from ~= "jim" )'
# result = GRAMMAR.parse(query)
# print(result)


result = parser.parse('name ~=".pdf" & ( from ~= "jack" | from ~= "jim" )')
