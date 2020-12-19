from parsimonious.grammar import Grammar

grammar = Grammar(
    r"""
    S = Expression
    Expression = (SubExpression "&&" Expression) / (SubExpression "||" Expression) / SubExpression
    SubExpression = ("(" Expression ")") / RoleName
    RoleName = ~"[a-zA-Z]+"
    """)

query = "Expert && (ReadWrite || ReadOnly)"
result = grammar.parse(query)
print(result)
