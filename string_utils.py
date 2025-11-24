
def split_before_uppercases(formula):
    up_list = []
    currrent_part = ""
    for char in formula:
        if char.isupper() and current_part :
            up_list.append(current_part)
            current_part = char
        else:
            current_part += char
    if current_part:
        up_list.append(current_part)
    return up_list 
    
        
def split_at_digit(formula):
    for char_index, char in enumerate(formula):
        if char.isdigit():
            return formula[:char_index], int(formula[char_index:])
    return formula, 1
  

def count_atoms_in_molecule(molecular_formula):
    my_dic = {} 
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        my_dic[atom_name] = my_dic.get(atom_name, 0) + atom_count
    return my_dic



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
