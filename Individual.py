#!/usr/bin/python3
from src.Gene import Gene


class Individual:
    # gene count
    __self_gene_count = 100
    # maximum evolution times
    __max_evolution_times = 100
    # gene groups
    genes = []
    # selected genes
    selected_genes = []
    # generation_evolved
    generation_evolved = 0
    # target gene to be compared
    target_gene = None
    # individual fitness
    individual_fitness = 0

    # randomly generate gene
    def __init__(self, target):
        self.target_gene = target
        # assert isinstance(self.target_gene, Gene)
        # if len(target.seq) != Gene.get_gene_length():
        #     print("Target gene length doesn't equal to Gene length, Individual can't be initialized.")
        #     exit(0)
        for index in range(0, self.__self_gene_count):
            self.genes.append(Gene(None))

    @staticmethod
    def sort_gene_by_fitness(gene_tmp):
        return gene_tmp.gene_fitness_grade

    # output individual info
    def output(self):
        print("Individual fitness:" + str(self.individual_fitness))
        for gene in self.genes:
            assert isinstance(gene, Gene)
            print(gene.output())

    # fitness justify function
    def fitness_justify(self):
        self.individual_fitness = 0
        fitness_tmp = 0
        for gene in self.genes:
            gene.gene_fitness_grade = 0
            for index in range(0, Gene.get_gene_length(self)):
                if gene.seq[index] == self.target_gene.seq[index]:
                    gene.gene_fitness_grade += 1
            fitness_tmp += gene.gene_fitness_grade
        self.individual_fitness = fitness_tmp/(self.__self_gene_count*Gene.gene_length)
        self.genes.sort(key=Individual.sort_gene_by_fitness, reverse=True)
        self.selected_genes = []
        for index in range(0, int(self.__self_gene_count/2)):
            self.selected_genes.append(self.genes[index])

    # re-generate individual
    def renew_individual(self):
        # re-initialize
        self.genes = []
        temp_gene_count = int(self.__self_gene_count/2)
        for index in range(0, temp_gene_count):
            son = Gene.gene_multiply(self.selected_genes[index], self.selected_genes[temp_gene_count-index-1])
            son.variate()
            self.genes.append(son)
            # self.genes.append(Gene.gene_multiply(self.selected_genes[temp_gene_count-index-1], self.selected_genes[index]))
            self.genes.append(self.selected_genes[index])
            # self.genes.append(self.selected_genes[temp_gene_count-index-1])


c = Individual(Gene("1111111111"))
c.fitness_justify()
print("0: " + str(c.individual_fitness))
try_times = 0
while try_times < 1000:
    try_times += 1
    c.renew_individual()
    c.fitness_justify()
    print(str(try_times) + ": " + str(c.individual_fitness))
    if c.individual_fitness >= 1:
        break
    # c.output()


# father = Gene("0000000000")
# mother = Gene("1111111111")
# print(str(father.seq[0:5]) + str(mother.seq[5:10]))
# print(Gene.gene_multiply(father, mother))

# son = Gene.gene_multiply(father, mother)
# son.print_gene()
# son.variate()
# son.print_gene()
# c = Individual(Gene("1111111111"))
# print("--------before fitness justify-------")
# c.output()
# c.fitness_justify()
# print("--------after fitness justify-------")
# c.output()
