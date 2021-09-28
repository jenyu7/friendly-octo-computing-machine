import numpy as np

def viterbi(seq, transition, emission, initial, labels):
    # converts sequence to an array
    seq = np.array([int(i) for i in seq])
    # number of distinct states
    n_states = len(labels)
    # length of sequence (n value)
    N = len(seq)
    # Matrix that contains the max probability of reaching each state
    max_probs = np.zeros((n_states, N + 1))
    max_probs[:,0] += initial * emission[:, seq[0]]
    # max_probs[initial, 0] = 1
    # Matrix that contains the previous state which corresponds 
    # to the maximum probability of reaching the current state
    max_state_combs = np.zeros((n_states, N + 1), dtype='int')
    for i in range(1, N + 1):
        for j in range(n_states):
            # obtain probability from the maximal jump (transition)
            max_probs[j, i] = np.max(max_probs[:, i - 1] * transition[:, j])
            # Store this jump for later reference
            max_state_combs[j, i] = np.argmax(max_probs[:, i - 1] * transition[:, j])
            # multiply with probability of current state (emission)
            max_probs[j, i] *= emission[j, seq[i - 1]]
    # obtain the maximal state sequence
    max_states = np.zeros(N + 1, dtype='int')
    max_states[N] = np.argmax(max_probs[:, N])
    # tracing backwards for the desired sequence 
    for n in range(N, 1, -1):
        max_states[n - 1] = max_state_combs[max_states[n], n - 1]
    retstr = ''
    for s in max_states[1:]: 
        retstr += labels[s]
    return retstr
    
    
# k = l = 2, n = 100
transition = np.array([
    [0.2, 0.8],
    [0.4, 0.6]
])
emission = np.array([
    [0.5, 0.5],
    [0.7, 0.3]
])

transition2 = np.array([
    [0.1, 0.9],
    [0.1, 0.9]
])
emission2 = np.array([
    [0.1, 0.9],
    [0.1, 0.9]
])

seq = "0100010010111100111111111000000000011001000010111111111110011111111111110111111010010100001000000000"
initial = [0.5, 0.5]
#initial = 0
names = ['A', 'B']
print(viterbi(seq, transition2, emission2, initial, names))