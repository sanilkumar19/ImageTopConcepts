import math

FILE_NAME = 'concept_pool.txt'
OUT_FILE = 'output.txt'
TOP_FILE = 'top_concepts.txt'
def main():
    file = open(FILE_NAME, 'r')
    first = file.readline().strip().strip('(').strip(')')
    concept_pool = first.split(', ')
    pool_size = len(concept_pool)
    semantic_consistency = {}
    concept_count = {}
    sorted_concepts = {}

    for item in concept_pool:
        concept_count[item] = {}
        semantic_consistency[item] = {}
    for init in concept_pool:
        for jinit in concept_pool:
            concept_count[init][jinit] = 0
            semantic_consistency[init][jinit] = 0
    concept_total = 0
    for line in file:
        concept_list = line[9:].strip().strip('(').strip(')').split(', ')
        for i in concept_list:
            for j in concept_list:
                concept_count[i][j] = concept_count[i][j] + 1
        concept_total = concept_total + len(concept_list)
    file.close()
    for i in concept_count:
        for j in concept_count[i]:
            freq_l_l_prime = (concept_count[i][j])
            # Every image in this set contains a dog, so dog can be used to get the total for each concept.
            freq_l = concept_count['dog'][i]
            freq_l_prime = concept_count['dog'][j]
            top = freq_l_l_prime * concept_total
            bottom = freq_l * freq_l_prime
            bound = top / bottom

            # Taking the log of 0 will produce an error.
            if bound != 0:
                sc = math.log(bound, 10)
                semantic_consistency[i][j] = max(sc, 0)
            else:
                semantic_consistency[i][j] = 0
    output = open(OUT_FILE, 'w')

    for i in semantic_consistency:
        output.write(i + '\n')
        for j in semantic_consistency[i]:
            output.write(j + ': ' + str(semantic_consistency[i][j]) + '\n')
        output.write('\n')
    output.close()
    top_output = open(TOP_FILE, 'w')
    for i in semantic_consistency:
        sorted_concepts[i] = sorted(semantic_consistency[i].items(), key=lambda item: item[1], reverse=True)[:3]
    for i in sorted_concepts:
        top_output.write(i + '\n')
        for j in sorted_concepts[i]:
            top_output.write(str(j) + ', ')
        top_output.write('\n')
    top_output.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


