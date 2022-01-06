import math

NAME_of_FILE = 'concept_pool.txt'
OUTPUT_FILE = 'output.txt'
TOP_FILE = 'top_concepts.txt'
def main():
    file = open(NAME_of_FILE, 'r')
    first = file.readline().strip().strip('(').strip(')')
    concept_pool = first.split(', ')
    pool_size = len(concept_pool)
    semantic_consistency = {}
    count_of_concepts = {}
    sort_concepts = {}

    for item in concept_pool:
        count_of_concepts[item] = {}
        semantic_consistency[item] = {}
    for init in concept_pool:
        for jinit in concept_pool:
            count_of_concepts[init][jinit] = 0
            semantic_consistency[init][jinit] = 0
    concept_total = 0
    for line in file:
        concept_list = line[9:].strip().strip('(').strip(')').split(', ')
        for i in concept_list:
            for j in concept_list:
                count_of_concepts[i][j] = count_of_concepts[i][j] + 1
        concept_total = concept_total + len(concept_list)
    file.close()

    # Step 3: 
    #frequency-based knowledge matrix as shown in the subsection 3.2 of the paper “Object Detection Meets Knowledge Graphs”. 
    #This frequency-based knowledge matrix has the size of all concepts extracted

    for i in count_of_concepts:
        for j in count_of_concepts[i]:
            freq_l_l_prime = (count_of_concepts[i][j])
            # Every image in this set contains a dog, so dog can be used to get the total for each concept.
            freq_l = count_of_concepts['dog'][i]
            freq_l_prime = count_of_concepts['dog'][j]
            top = freq_l_l_prime * concept_total
            bottom = freq_l * freq_l_prime
            bound = top / bottom

            # Taking the log of 0 will produce an error.
            if bound != 0:
                sc = math.log(bound, 10)
                semantic_consistency[i][j] = max(sc, 0)
            else:
                semantic_consistency[i][j] = 0
    output = open(OUTPUT_FILE, 'w')

    for i in semantic_consistency:
        output.write(i + '\n')
        for j in semantic_consistency[i]:
            output.write(j + ': ' + str(semantic_consistency[i][j]) + '\n')
        output.write('\n')
    output.close()
    top_output = open(TOP_FILE, 'w')
    for i in semantic_consistency:
        sort_concepts[i] = sorted(semantic_consistency[i].items(), key=lambda item: item[1], reverse=True)[:3]

        # Step4: Program to retrieve the 10 concepts’ relations with three highest frequencies. 
    for i in sort_concepts:
        top_output.write(i + '\n')
        for j in sort_concepts[i]:
            top_output.write(str(j) + ', ')
        top_output.write('\n')
    top_output.close()

if __name__ == '__main__':
    main()


