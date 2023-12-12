import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def readFile2Data():
  f=open("day8_input.txt", "r")

  data = [line.strip() for line in f]
  instructions = data[0]

  data.pop(0)
  data.pop(0)

  data = [line.split(" ") for line in data]
  data = {line[0] : (line[2].strip("(,"), line[3].strip(")")) for line in data}

  f.close
  return(instructions, data)

def build_graph(data):
    G = nx.DiGraph()
    for node, moves in data.items():
        G.add_node(node)
        for move, neighbor in enumerate(moves):
            G.add_edge(node, neighbor, move=move)
    return G

def perform_moves(graph, start_nodes, instructions):
    current_nodes = set(start_nodes)
    step = 0
    #print(f"current nodes = {current_nodes} at {step} steps ")
    

    while True:
        i = instructions[step]
        next = 0 if i == "L" else 1
      
        new_nodes = set()
        for node in current_nodes:
            neighbors = list(graph.successors(node))
            #print(f"{node} => {neighbors} ")
            #y = input("enter a key: ")
            if neighbors:
              if len(neighbors)==2:
                #print(f"neighbours {neighbors} ")
                new_nodes.add(neighbors[next])
                #print(f"new_nodes {new_nodes} ")
                #y = input("enter a key: ")
              elif len(neighbors)==1:
                neighbors.append(neighbors[0])
                #print(f"neighbours {neighbors} ")
                new_nodes.add(neighbors[next])
                #print(f"new_nodes {new_nodes} ")
                #y = input("enter a key: ")

        current_nodes = new_nodes
        step += 1

        if all(node[2] == "Z" for node in current_nodes):
            break
        elif step == len(instructions) - 2:
            instructions *= 2

    return step

instructions, data = readFile2Data()
#print(data.items())
#y=input("enter a key: ")
graph = build_graph(data)
start_nodes = [node for node in data if node[2] == "A"]

result = perform_moves(graph, start_nodes, instructions)
print(result)