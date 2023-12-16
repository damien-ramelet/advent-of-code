import re
import multiprocessing

with open("input") as f:
    content = f.readlines()

instructions, nodes = content[0].strip(), content[2:]

nodes_mapped = {}
for node in nodes:
    current_node, next_elements = node.split("=")
    first_element = re.search(r"\(([\w]+), ([\w]+)\)", next_elements)[1]
    second_element = re.search(r"\(([\w]+), ([\w]+)\)", next_elements)[2]
    nodes_mapped[current_node.strip()] = (first_element.strip(), second_element.strip())

starter_nodes = {}

for node in nodes_mapped:
    if node.endswith("A"):
        starter_nodes[node] = nodes_mapped[node]

i = 0
counts = 0

#while True:
#    if i == 0:
#        nodes = starter_nodes
#    elif i% len(instructions) == 0:
#        i = 0
#
#    if all([node.endswith("Z") for node in nodes]):
#        break
#
#    tmp_next_nodes = []
#
#    for node in nodes:
#        if instructions[i] == "L":
#            tmp_next_nodes.append(nodes_mapped[node][0])
#        elif instructions[i] == "R":
#            tmp_next_nodes.append(nodes_mapped[node][1])
#
#    nodes = tmp_next_nodes
#    print(nodes)
#
#    i += 1
#    counts += 1

def func(instructions, first_node, nodes_mapped, q):
    if instructions == "L":
        q.put(nodes_mapped[first_node][0])
    elif instructions == "R":
        q.put(nodes_mapped[first_node][1])


def func_main():
    results = []
    counts = 0
    jobs = []
    i = 0

    queue = multiprocessing.Queue()
    while True:
        if i == 0:
            nodes = starter_nodes
        elif i % len(instructions) == 0:
            i = 0

        for place, node in enumerate(nodes): 
            #p = multiprocessing.Process(target=func, args=(instructions[i], node, nodes_mapped, queue))
            #p.start()
            #jobs.append(p)
            if instructions[i] == "L":
                if not nodes_mapped[node][0].endswith("Z"):
                    results.append(nodes_mapped[node][0])
                else:
                    print(f"Took {counts+1} to reach {nodes_mapped[node][0]}")

            elif instructions[i] == "R":
                if not nodes_mapped[node][1].endswith("Z"):
                        results.append(nodes_mapped[node][1])
                else:
                    print(f"Took {counts+1} to reach {nodes_mapped[node][1]}")

        if not results:
            break

        #for job in jobs:
        #    job.join()
        #    results.append(queue.get())

        i += 1
        counts += 1
        nodes = results
        results = []

#        for result in results:
#            if result.endswith("Z"):
#                match += 1
#
#        if len(results) == match:
#            print(results)
#            break
#        else:
#            print(f"Only {match} over {len(results)}")
#            nodes = results
#            results = []

    print(counts)

if __name__ == "__main__":
    func_main()
