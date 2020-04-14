
def damage(atk, atkmod, rate, flat_mod, flat2_mod, pow):
    dmg = (((atk*atkmod*rate) + flat_mod) * 1.871 + flat2_mod) * pow
    return dmg