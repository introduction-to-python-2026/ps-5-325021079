import string_utils 
import equation_utils


def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"

    # 1.parse reaction
    reactants, products = string_utils.parse_chemical_reaction(reaction) # [""Fe2O3", "H2"], ["Fe", "H2O""]
    reactant_atoms = string_utils.count_atoms_in_reaction(reactants) # [{"Fe":2, "O":1}, {"H":2}]
    product_atoms = string_utils.count_atoms_in_reaction(products)

    # 2.build equation and solve
    equations, coefficients = equation_utils.build_equations(reactant_atoms, product_atoms)
    coefficients = equation_utils.my_solve(equations, coefficients) + [1]

    return coefficients # [1/3, 1, 2/3, 1]

