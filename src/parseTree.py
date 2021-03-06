

expression_for_id = {}


class ParseNode(object):
    pass


class DefineNode(ParseNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def __str__(self):
        return "DefineNode(" + str(self.name) + ", " + str(self.expr) + ")"

    def __eq__(self, other):
        return isinstance(other, DefineNode) \
               and self.name == other.name and self.expr == other.expr

    def evaluate(self):
        expression_for_id[self.name] = self.expr.evaluate()


class NumberNode(ParseNode):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return "NumberNode(" + str(self.number) + ")"

    def __eq__(self, other):
        return isinstance(other, NumberNode) and self.number == other.number

    def evaluate(self):
        return self.number


class BooleanNode(ParseNode):
    def __init__(self, boolean):
        self.boolean = boolean

    def __str__(self):
        return "BooleanNode(" + str(self.boolean) + ")"

    def __eq__(self, other):
        return isinstance(other, BooleanNode) and self.boolean == other.boolean

    def evaluate(self):
        return self.boolean


class IdNode(ParseNode):
    def __init__(self, i_d):
        self.i_d = i_d

    def __str__(self):
        return "IdNode(" + str(self.i_d) + ")"

    def __eq__(self, other):
        return isinstance(other, IdNode) and self.i_d == other.i_d

    def evaluate(self):
        return expression_for_id[self.i_d]


class CondNode(ParseNode):
    def __init__(self, cond_expressions):
        self.cond_expressions = cond_expressions

    def __str__(self):
        return "CondNode(" + str(self.cond_expressions) + ")"

    def __eq__(self, other):
        return isinstance(other, CondNode) \
               and self.cond_expressions == other.cond_expressions

    def evaluate(self):
        for cond, expression in self.cond_expressions:
            if cond.evaluate():
                return expression.evaluate()


class PrintNode(ParseNode):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return "PrintNode(" + str(self.expr) + ")"

    def __eq__(self, other):
        return isinstance(other, PrintNode) and self.expr == other.expr

    def evaluate(self):
        print(self.expr.evaluate())


class BinaryFunctionNode(ParseNode):
    def __init__(self, func, expr1, expr2):
        self.func = func
        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self):
        return "BinaryFunctionNode(" + str(self.func) \
               + ", " + str(self.expr1) + ", " + str(self.expr2) + ")"

    def __eq__(self, other):
        return isinstance(other, BinaryFunctionNode) \
               and self.func == other.func and self.expr1 == other.expr1 \
               and self.expr2 == other.expr2

    def evaluate(self):
        return self.func(self.expr1.evaluate(), self.expr2.evaluate())


class UnaryFunctionNode(ParseNode):
    def __init__(self, func, expr):
        self.func = func
        self.expr = expr

    def __str__(self):
        return "UnaryFunctionNode(" + str(self.func) \
               + ", " + str(self.expr) + ")"

    def __eq__(self, other):
        return isinstance(other, UnaryFunctionNode) \
               and self.func == other.func \
               and self.expr == other.expr

    def evaluate(self):
        return self.func(self.expr.evaluate())
