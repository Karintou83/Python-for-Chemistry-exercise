# 例のコード
def get_element_symbols(formula):
    """Return all the element symbols in the string formula."""
    n = len(formula)
    i = 0
    symbols = []
# Iterate over the string, noting the capital letters , which indicate
# the start of an element symbol.
    while i < n:
        if formula[i].isupper():
# A new element symbol
            symbols.append(formula[i])
        elif formula[i].islower():
# If we encounter a lowercase letter, it is the second character
# of an element symbol.
            symbols[-1] += formula[i]
        i += 1
    return symbols

# 例のコード

# 関数	入力	出力
# get_stoichiometry(formula)	'CClH2CBr2COH'	{'C': 3, 'Cl': 1, 'H': 3, 'Br': 2, 'O': 1}(辞書)
# get_stoichiometric_formula(formula)	同上	'C3ClH3Br2O'(文字列)