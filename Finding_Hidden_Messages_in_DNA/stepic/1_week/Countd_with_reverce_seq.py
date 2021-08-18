pattern = int(input())
seqwence = input()
d = int(input())

def reverse_chain(seq):
    extra_map = {"A":"T", "G":"C", "T":"A", "C":"G"}
    seq = list(seq)
    for i in range (len(seq)):
        seq[i] = extra_map[seq[i]]
    return "".join(seq[::-1])

def neighbours(seq, d, data_main):
    data_neighbours = []
    
    seq_r = reverse_chain(seq)
    for i in range(0,len(seq)):
        for g in ["A", "C", "G", "T"]:
            seq1 = seq.copy()
            seq1[i] = g
            data_neighbours.append("".join(seq1))

    data_neighbours = set(data_neighbours)
    data_neighbours1 = list(data_neighbours)

    for k in data_neighbours1:
        if k not in data_main:
            data_main.append(k)
    if d > 1:
        for j in data_neighbours1:
            j = list(j)
            neighbours(j,d-1, data_main)
  
    return set(data_main)

def AppPattCount(pat, seq, d):
    Patterns = []
    f_patterns = []
    freqMap = {}
    seq = seq.upper()
    seq = list(seq)
    
    for i in range (0, len(seq)-pat):
        data_main = []
        Patterns = neighbours(seq[i:i+pat],d, data_main)
        for k in Patterns:
            if k not in freqMap.keys():
                freqMap[k]=1    
            else:
                freqMap[k] = freqMap[k] +1
                
            if reverse_chain(k) not in freqMap.keys():
                freqMap[reverse_chain(k)] = 1
            else:
                freqMap[reverse_chain(k)] = freqMap[reverse_chain(k)] +1
                           
    m = max(freqMap.values())
    
    for l in freqMap.keys():
        if freqMap[l] == m:
            f_patterns.append(l)
    
    return f_patterns
  
 AppPattCount(pattern, seqwence, d)
