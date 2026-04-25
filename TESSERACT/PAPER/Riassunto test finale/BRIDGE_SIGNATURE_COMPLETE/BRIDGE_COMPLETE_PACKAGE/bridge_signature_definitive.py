"""
BRIDGE SIGNATURE VERIFICATION - DEFINITIVE TEST
================================================
Dataset: C. elegans connectome (Varshney et al.)
Classification: eLife 2024 Supplementary File 2

Result: Modulatory neurons are 3.24x over-represented among bridges (p = 0.00003)
"""

import pandas as pd
import networkx as nx
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

def extract_modulatory_neurons(filepath):
    """Extract modulatory neuron list from eLife 2024 Supplementary File 2"""
    df = pd.read_excel(filepath, skiprows=2)
    df.columns = ['idx', 'Class', 'Neuron', 'Lineage', 
                  'eat-4', 'unc-17', 'unc-25', 'unc-47', 
                  'cat-1', 'tph-1', 'cat-2', 'bas-1', 
                  'tdc-1', 'tbh-1', 'mod-5', 'snf-3', 'oct-1',
                  'GABA_stain', '5HT_stain', 'DA_stain', 
                  'Neurotransmitter', 'NT_detail', 'col22', 'Comments',
                  'Neuron2', 'Class2']
    
    df = df[df['Neuron'].notna() & (df['Neuron'] != 'Neuron')]
    df = df[~df['Neuron'].str.contains('total|percent|Total|\\?', na=False)]
    
    MODULATORY = set()
    
    # Dopaminergic
    da = df[df['Neurotransmitter'].str.match('^DA$', na=False)]['Neuron'].tolist()
    MODULATORY.update(da)
    
    # Serotonergic
    ht = df[(df['Neurotransmitter'].str.contains('5-HT', na=False)) | 
            (df['NT_detail'].str.contains('5-HT', na=False))]['Neuron'].tolist()
    MODULATORY.update(ht)
    
    # Tyraminergic/Octopaminergic
    ta = df[(df['Neurotransmitter'].str.contains('octopamine', case=False, na=False)) |
            (df['NT_detail'].str.contains('tyramine|octopamine', case=False, na=False))]['Neuron'].tolist()
    MODULATORY.update(ta)
    
    # GABAergic
    GABAERGIC = set(df[df['Neurotransmitter'].str.contains('GABA', na=False)]['Neuron'].tolist())
    
    return MODULATORY, GABAERGIC

def load_connectome(filepath):
    """Load C. elegans connectome"""
    df = pd.read_excel(filepath)
    df = df[df['Type'] != 'NMJ']
    
    G = nx.Graph()
    for _, row in df.iterrows():
        n1, n2 = row['Neuron 1'], row['Neuron 2']
        if G.has_edge(n1, n2):
            G[n1][n2]['weight'] += row['Nbr']
        else:
            G.add_edge(n1, n2, weight=row['Nbr'])
    return G

def main():
    print("=" * 70)
    print("BRIDGE SIGNATURE - DEFINITIVE VERIFICATION")
    print("=" * 70)
    
    # Load classification
    MODULATORY, GABAERGIC = extract_modulatory_neurons('elife-95402-supp2-v1.xlsx')
    print(f"\nClassification (eLife 2024):")
    print(f"  Modulatory neurons: {len(MODULATORY)}")
    print(f"  GABAergic neurons: {len(GABAERGIC)}")
    
    # Load connectome
    G = load_connectome('NeuronConnect.xls')
    print(f"\nConnectome: {G.number_of_nodes()} neurons, {G.number_of_edges()} connections")
    
    # Classify
    node_types = {}
    for node in G.nodes():
        if node in MODULATORY:
            node_types[node] = 'M'
        elif node in GABAERGIC:
            node_types[node] = 'I'
        else:
            node_types[node] = 'E'
    
    n_mod = sum(1 for t in node_types.values() if t == 'M')
    print(f"Modulatory in connectome: {n_mod}")
    
    # Compute metrics
    degrees = dict(G.degree())
    betweenness = nx.betweenness_centrality(G)
    clustering = nx.clustering(G)
    
    avg_d = np.mean(list(degrees.values()))
    avg_b = np.mean(list(betweenness.values()))
    avg_c = np.mean(list(clustering.values()))
    
    # Find bridges
    bridges = [n for n in G.nodes() 
               if degrees[n] > avg_d and betweenness[n] > avg_b and clustering[n] < avg_c]
    
    # Statistics
    mod_nodes = [n for n in G.nodes() if node_types[n] == 'M']
    other_nodes = [n for n in G.nodes() if node_types[n] != 'M']
    
    mod_in_bridges = len([n for n in bridges if node_types[n] == 'M'])
    other_in_bridges = len(bridges) - mod_in_bridges
    
    contingency = [[mod_in_bridges, len(mod_nodes) - mod_in_bridges],
                   [other_in_bridges, len(other_nodes) - other_in_bridges]]
    chi2, p_chi, _, _ = stats.chi2_contingency(contingency)
    
    # Results
    print(f"\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"\nBridges: {len(bridges)} ({len(bridges)/G.number_of_nodes()*100:.1f}%)")
    print(f"Modulatory in bridges: {mod_in_bridges}/{n_mod} ({mod_in_bridges/n_mod*100:.1f}%)")
    print(f"Others in bridges: {other_in_bridges}/{len(other_nodes)} ({other_in_bridges/len(other_nodes)*100:.1f}%)")
    
    overrep = (mod_in_bridges/n_mod) / (other_in_bridges/len(other_nodes))
    print(f"\nOver-representation: {overrep:.2f}x")
    print(f"Chi-square: χ² = {chi2:.3f}, p = {p_chi:.6f}")
    print(f"Significant (p<0.05)? {'YES ✓' if p_chi < 0.05 else 'NO'}")

if __name__ == "__main__":
    main()
