"""
VERIFICA DELLA FIRMA ⇄

La firma: alto grado + alto betweenness + basso clustering

Verifichiamo nel Tesseract che questa firma identifichi esattamente A=2
"""

import json
import numpy as np
from collections import defaultdict

with open('/home/claude/GRAFO_MATRIX_72_EXPANDED.json', 'r') as f:
    graph = json.load(f)

edges = set()
for edge in graph['edges']:
    key = tuple(sorted([edge['source'], edge['target']]))
    edges.add(key)

neighbors = defaultdict(set)
for e in edges:
    neighbors[e[0]].add(e[1])
    neighbors[e[1]].add(e[0])

def get_A(node):
    return int(node.replace('Σ_', '').split('_')[1])

nodes = list(neighbors.keys())

# Calcola metriche per ogni nodo
def clustering_coef(node):
    neigh = list(neighbors[node])
    if len(neigh) < 2:
        return 0
    triangles = 0
    possible = len(neigh) * (len(neigh) - 1) / 2
    for i in range(len(neigh)):
        for j in range(i+1, len(neigh)):
            if neigh[j] in neighbors[neigh[i]]:
                triangles += 1
    return triangles / possible if possible > 0 else 0

# Betweenness (già calcolato prima, ricalcoliamo per ogni nodo)
from collections import deque
import random
random.seed(42)

betweenness = defaultdict(float)
sample_pairs = random.sample([(a,b) for a in nodes for b in nodes if a < b], 500)

for start, end in sample_pairs:
    visited = {start: 0}
    parents = defaultdict(list)
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                parents[neighbor].append(node)
                queue.append(neighbor)
            elif visited[neighbor] == visited[node] + 1:
                parents[neighbor].append(node)
    
    if end not in visited:
        continue
    
    dependency = defaultdict(float)
    ordered = sorted(visited.keys(), key=lambda x: -visited[x])
    
    for node in ordered:
        if node == end:
            dependency[node] = 1
        for parent in parents[node]:
            dependency[parent] += dependency[node] / len(parents[node])
        if node != start and node != end:
            betweenness[node] += dependency[node]

print("=" * 70)
print("VERIFICA FIRMA ⇄: alto grado + alto betweenness + basso clustering")
print("=" * 70)

# Calcola metriche per ogni nodo
node_metrics = []
for n in nodes:
    degree = len(neighbors[n])
    cc = clustering_coef(n)
    bw = betweenness[n]
    A = get_A(n)
    node_metrics.append({
        'node': n,
        'A': A,
        'degree': degree,
        'clustering': cc,
        'betweenness': bw
    })

# Medie globali
avg_degree = np.mean([m['degree'] for m in node_metrics])
avg_cc = np.mean([m['clustering'] for m in node_metrics])
avg_bw = np.mean([m['betweenness'] for m in node_metrics])

print(f"\nMedie globali:")
print(f"  Grado: {avg_degree:.2f}")
print(f"  Clustering: {avg_cc:.4f}")
print(f"  Betweenness: {avg_bw:.2f}")

# Identifica nodi con "firma ⇄"
print("\n" + "-" * 50)
print("Nodi con FIRMA ⇄ (grado > media, bw > media, cc < media):")
print("-" * 50)

signature_nodes = []
for m in node_metrics:
    if m['degree'] > avg_degree and m['betweenness'] > avg_bw and m['clustering'] < avg_cc:
        signature_nodes.append(m)

print(f"\nTrovati {len(signature_nodes)} nodi con firma ⇄")

# Distribuzione per A
A_counts = {1: 0, 2: 0, 3: 0}
for m in signature_nodes:
    A_counts[m['A']] += 1

print(f"\nDistribuzione per attributo:")
for A in [1, 2, 3]:
    print(f"  A={A}: {A_counts[A]} nodi")

# Quanti nodi A=2 hanno la firma?
total_A2 = sum(1 for m in node_metrics if m['A'] == 2)
A2_with_sig = A_counts[2]
print(f"\nNodi A=2 totali: {total_A2}")
print(f"Nodi A=2 con firma: {A2_with_sig}")
print(f"Percentuale: {A2_with_sig/total_A2*100:.1f}%")

# Precisione e recall
print("\n" + "-" * 50)
print("METRICHE DI CLASSIFICAZIONE")
print("-" * 50)

# Se usiamo "firma ⇄" per predire A=2:
true_positives = A_counts[2]
false_positives = A_counts[1] + A_counts[3]
false_negatives = total_A2 - A2_with_sig
true_negatives = 48 - false_positives  # 48 nodi non-A=2

precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

print(f"\nSe usiamo 'firma ⇄' per identificare A=2:")
print(f"  Precision: {precision:.2%}")
print(f"  Recall: {recall:.2%}")
print(f"  F1: {f1:.2%}")

print("\n" + "=" * 70)
print("INTERPRETAZIONE")
print("=" * 70)

if precision > 0.8:
    print("""
✓ La firma (alto grado + alto bw + basso cc) identifica A=2 con alta precisione!

Questo significa:
- Puoi prendere una rete QUALSIASI
- Trovare i nodi con questa firma
- E sapere che sono i nodi "relazionali" (⇄)

È una PREDIZIONE OPERATIVA.
Non serve sapere cos'è EAR.
Basta misurare tre metriche standard.
""")
elif precision > 0.5:
    print("""
~ La firma identifica A=2 con precisione moderata.

C'è rumore, ma la direzione è giusta.
Potrebbe servire una firma più sofisticata.
""")
else:
    print("""
✗ La firma non identifica bene A=2.

Potrebbe significare:
- La firma è sbagliata
- Serve una definizione diversa
- O la struttura è più complessa
""")

print("\n" + "=" * 70)
print("FIRMA ALTERNATIVA: RANKING")
print("=" * 70)

print("""
Invece di soglie (> media, < media), usiamo RANKING.

PREDIZIONE:
I nodi A=2 dovrebbero essere:
- Nel top 1/3 per grado
- Nel top 1/3 per betweenness  
- Nel bottom 1/3 per clustering
""")

# Ranking
sorted_by_degree = sorted(node_metrics, key=lambda x: -x['degree'])
sorted_by_bw = sorted(node_metrics, key=lambda x: -x['betweenness'])
sorted_by_cc = sorted(node_metrics, key=lambda x: x['clustering'])  # ascending

top_third = 24  # 72/3

top_degree = set(m['node'] for m in sorted_by_degree[:top_third])
top_bw = set(m['node'] for m in sorted_by_bw[:top_third])
bottom_cc = set(m['node'] for m in sorted_by_cc[:top_third])

# Intersezione
intersection = top_degree & top_bw & bottom_cc
print(f"\nNodi nel top-1/3 grado E top-1/3 bw E bottom-1/3 cc: {len(intersection)}")

A_counts_intersect = {1: 0, 2: 0, 3: 0}
for n in intersection:
    A_counts_intersect[get_A(n)] += 1

print(f"Distribuzione: A=1:{A_counts_intersect[1]}, A=2:{A_counts_intersect[2]}, A=3:{A_counts_intersect[3]}")

if A_counts_intersect[2] > A_counts_intersect[1] + A_counts_intersect[3]:
    print("\n✓ Maggioranza A=2 nell'intersezione!")
