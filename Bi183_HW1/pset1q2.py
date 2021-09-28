states = [[0.8, 0.2], [0.05, 0.95]]
bases = { 'A': [0.2, 0.1],
          'C': [0.5, 0.25],
          'G': [0.1, 0.25],
          'T': [0.2, 0.4]
        }
        
p_actg = 0.0

def seq_prob(seq): 
    return 0.5 * bases[seq[0:1]][0] * get_prob(0, 0, seq[1:]) + \
           0.5 * bases[seq[0:1]][0] * get_prob(0, 1, seq[1:]) + \
           0.5 * bases[seq[0:1]][1] * get_prob(1, 1, seq[1:]) + \
           0.5 * bases[seq[0:1]][1] * get_prob(1, 0, seq[1:])
           
def get_prob(prevstate, currstate, base): 
    if len(base) == 1:
        return states[prevstate][currstate] * bases[base][currstate]
    else: 
        curr_base = base[0:1]
        return (states[prevstate][currstate] * bases[curr_base][currstate]) * (get_prob(currstate, 0, base[1:]) + get_prob(currstate, 1, base[1:]))
        
import numpy as np
print(seq_prob("ACGT"))
