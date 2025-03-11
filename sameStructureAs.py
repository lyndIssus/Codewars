import re
def same_structure_as(original,other):
    og = re.sub(r"['\"].*?['\"]|[-0-9]", "", str(original))
    ot = re.sub(r"['\"].*?['\"]|[-0-9]", "", str(other))
    return og==ot

