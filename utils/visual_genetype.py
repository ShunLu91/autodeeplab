import sys
import genotypes
from graphviz import Digraph


def plot(genotype, filename):
    g = Digraph(
        format='png',
        edge_attr=dict(fontsize='20', fontname="times"),
        node_attr=dict(style='filled', shape='rect', align='center', fontsize='20', height='0.5', width='0.5',
                       penwidth='2', fontname="times"),
        engine='dot')
    g.body.extend(['rankdir=LR'])

    g.node("H_{l-2}", fillcolor='gray89')
    g.node("H_{l-1}", fillcolor='gray89')
    assert len(genotype) % 2 == 0
    steps = len(genotype) // 2

    for i in range(steps):
        g.node(str(i), fillcolor='pink')

    index = 0
    edge_dict = {}
    for i in range(steps):
        for j in range(i + 2):
            edge_dict[index] = j
            index += 1

    for i in range(steps):
        for k in [2 * i, 2 * i + 1]:
            j, op = genotype[k]
            op = genotypes.PRIMITIVES[op]
            j = edge_dict.get(j)
            if op == 'none':
                continue
            if j == 0:
                u = "H_{l-2}"
            elif j == 1:
                u = "H_{l-1}"
            else:
                u = str(j - 2)
            v = str(i)
            g.edge(u, v, label=op, fillcolor="gray")

    g.node("concat", fillcolor='palegoldenrod')
    for i in range(steps):
        g.edge(str(i), "concat", fillcolor="gray")

    g.node("H_{l}", fillcolor='gray89')
    g.edge("concat", "H_{l}", fillcolor="gainsboro")

    g.render(filename, view=False, cleanup=True)


if __name__ == '__main__':
    # genotype_name = 'ad0_s'
    # genotype = eval('genotypes.{}'.format(genotype_name))
    #
    # plot(genotype, 'figure/' + genotype_name)

    genotype_list = genotypes.generate_random_genotypes(n=40)
    for i, _geno in enumerate(genotype_list):
        plot(_geno, 'figure/' + 'geno_%d' % i)
