def descending_order(number1, number2):
    if number1 > number2:
        print (number1, number2)
    else:
        print (number2, number1)
    return

def avg_seq_length(filename):
    file_length = int()  # records number of sequences in file
    seq_length = int()  # records ongoing sub-total of sequence length
    seq_length_test = []
    
    with open (filename, 'r') as f:
        for line in f:
            file_length += 1
            seq_length += len(line)
            
    print (seq_length / file_length) # mean average sequence length = sum of all sequence lengths / number of sequences
    return
avg_seq_length (multi_seqs_fname)

import operator
def genus_count(filename):

# reads in file and adds only genus to genus_list object
    genus_list = []
    with open (filename, 'r') as f:
        for line in f:
            (genus, species) = line.split()
            genus_list.append(genus)

# adds each genus to a dictionary with a value of 1 if not in the dictionary and adding a value to the genus if it is
    d = {}
    for genus in genus_list:
        if genus not in d:
            d[genus] = 1
        else:
            d[genus] = d[genus] + 1

# sorts dictionary in descending order by values in key:value pairs, then prints out the genus and genus count if genus count is above 4. 
    for k, v in sorted(d.items(), key=operator.itemgetter(1), reverse = True):
        if v >= 4:
            print (k, v)
            
    return

if __name__ == '__main__':
    descending_order(-5, 3)
    avg_seq_length('../data/multi_seqs.txt')
    genus_count('../data/species1.txt')