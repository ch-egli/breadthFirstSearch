# https://medium.com/@yasufumy/algorithm-breadth-first-search-408297a075c9 => adapted by ChE

def nachbarn_von(knoten, graph):
    return graph[knoten]

def breitensuche(graph, start_knoten):
    warteschlange = [start_knoten]
    besuchte_knoten = [start_knoten]
    while warteschlange:
        aktueller_knoten = warteschlange.pop()
        for nachbar in graph[aktueller_knoten]:
            if nachbar not in besuchte_knoten:
                warteschlange.append(nachbar)
                besuchte_knoten.append(nachbar)
    return besuchte_knoten

def kuerzester_weg(graph, start_knoten, end_knoten):
    warteschlange = [start_knoten]
    besuchte_knoten = [start_knoten]
    while warteschlange:
        aktueller_knoten = warteschlange.pop()
        for nachbar in graph[aktueller_knoten]:
            if (nachbar == end_knoten):
                besuchte_knoten.append(nachbar)
                return besuchte_knoten
            elif nachbar not in besuchte_knoten:
                warteschlange.append(nachbar)
                besuchte_knoten.append(nachbar)
    return besuchte_knoten


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['B', 'D']
    }

    print "Breitensuche : ", breitensuche(graph, 'A')
    print "kürzester Weg: ", kuerzester_weg(graph, 'A', 'D')
    print ""
    print "Nachbarn von A: ", nachbarn_von('A', graph)
    print "Nachbarn von B: ", nachbarn_von('B', graph)
    print "Nachbarn von C: ", nachbarn_von('C', graph)
    print "Nachbarn von D: ", nachbarn_von('D', graph)
    print "Nachbarn von E: ", nachbarn_von('E', graph)


