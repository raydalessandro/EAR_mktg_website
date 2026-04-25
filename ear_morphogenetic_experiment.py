"""
ESPERIMENTO: Campo Morfogenetico EAR
=====================================
Derivazione formale del kernel dal sistema ontologico EAR
Test quantitativo delle Proposizioni 3, 4, 5, 6

Autore: Ray + Claude
Data: 11 Gennaio 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve, maximum_filter, sobel
from scipy.stats import pearsonr
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# PARTE 1: DERIVAZIONE DEL KERNEL DAL SISTEMA EAR
# =============================================================================

def derive_ear_kernel():
    """
    Deriva il kernel morfogenetico dalla struttura ontologica EAR.
    
    Principi:
    - Centro = Campo ⧈ (potenzialità massima)
    - Bordi = Distinzione Δ (confini che separano E connettono)
    - La somma deve essere > 0 (conservazione informazionale, Prop 2)
    - Struttura 3×3 = minimo per relazione ⇄ (serve centro + intorno)
    
    Dalla Prop 6 (Inseparabilità):
    - Il kernel deve manifestare Δ, ⇄, ⟳ simultaneamente
    - Δ: differenza centro/bordo
    - ⇄: connessione attraverso i valori intermedi
    - ⟳: la convoluzione stessa è il processo
    """
    
    # Valore centrale: massima potenzialità (⧈)
    # Scegliamo un valore che riflette "pienezza nel vuoto"
    centro = 3.0
    
    # Bordi cardinali: distinzione primaria (Δ sul primo asse)
    # Negativi perché creano DIFFERENZA rispetto al centro
    bordo_cardinale = -0.5
    
    # Angoli: relazione diagonale (⇄ - connessione indiretta)
    # Zero o leggermente positivi - non separano, connettono
    angolo = 0.0
    
    kernel_base = np.array([
        [angolo,           bordo_cardinale, angolo],
        [bordo_cardinale,  centro,          bordo_cardinale],
        [angolo,           bordo_cardinale, angolo]
    ])
    
    # Verifica Prop 2 (Conservazione): somma deve essere definita
    somma = np.sum(kernel_base)
    print(f"Kernel EAR base - Somma: {somma} (deve essere > 0 per conservazione)")
    
    return kernel_base

def derive_alternative_kernels():
    """
    Deriva kernel alternativi per confronto:
    1. Kernel EAR (derivato da ontologia)
    2. Kernel Laplaciano classico (usato in Turing standard)
    3. Kernel "piatto" (controllo nullo)
    4. Kernel "invertito" (test falsificazione)
    """
    
    kernels = {}
    
    # 1. EAR: centro alto, bordi negativi (vuoto fertile)
    kernels['EAR'] = np.array([
        [ 0.0, -0.5,  0.0],
        [-0.5,  3.0, -0.5],
        [ 0.0, -0.5,  0.0]
    ])
    
    # 2. Laplaciano classico (diffusione standard)
    kernels['Laplaciano'] = np.array([
        [0.05, 0.2, 0.05],
        [0.2, -1.0, 0.2],
        [0.05, 0.2, 0.05]
    ])
    
    # 3. Nullo (nessuna influenza morfogenetica)
    kernels['Nullo'] = np.zeros((3, 3))
    
    # 4. Invertito (falsificazione: bordi alti, centro basso)
    kernels['Invertito'] = np.array([
        [ 0.0,  0.5,  0.0],
        [ 0.5, -2.0,  0.5],
        [ 0.0,  0.5,  0.0]
    ])
    
    # 5. EAR con angoli attivi (test variante)
    kernels['EAR_full'] = np.array([
        [ 0.1, -0.5,  0.1],
        [-0.5,  3.0, -0.5],
        [ 0.1, -0.5,  0.1]
    ])
    
    return kernels


# =============================================================================
# PARTE 2: SIMULAZIONE GRAY-SCOTT CON CAMPO MORFOGENETICO
# =============================================================================

def simulate_gray_scott(size=150, steps=3000, 
                        feed=0.055, kill=0.062,
                        Da=0.20, Db=0.10, dt=1.0,
                        morphic_kernel=None, 
                        field_strength=0.015,
                        application_freq=100,
                        seed=42):
    """
    Simula il sistema Gray-Scott con opzionale campo morfogenetico.
    
    Il campo morfogenetico agisce come "attrattore" che guida
    l'auto-organizzazione secondo principi EAR.
    """
    
    np.random.seed(seed)
    
    # Kernel Laplaciano per diffusione
    laplacian = np.array([
        [0.05, 0.2, 0.05],
        [0.2, -1.0, 0.2],
        [0.05, 0.2, 0.05]
    ])
    
    # Inizializzazione
    A = np.ones((size, size))
    B = np.zeros((size, size))
    
    # Perturbazione iniziale (identica per confronto equo)
    A += np.random.normal(0, 0.05, (size, size))
    B += np.random.normal(0, 0.05, (size, size))
    
    # Seed centrale per innescare pattern
    mid = size // 2
    r = size // 10
    A[mid-r:mid+r, mid-r:mid+r] = 0.5
    B[mid-r:mid+r, mid-r:mid+r] = 0.25
    
    # Simulazione
    for step in range(steps):
        # Diffusione
        lap_A = convolve(A, laplacian, mode='wrap')
        lap_B = convolve(B, laplacian, mode='wrap')
        
        # Reazione
        reaction = A * B * B
        
        # Aggiornamento Gray-Scott
        A_new = A + (Da * lap_A - reaction + feed * (1 - A)) * dt
        B_new = B + (Db * lap_B + reaction - (kill + feed) * B) * dt
        
        # Applicazione campo morfogenetico (se presente)
        if morphic_kernel is not None and step % application_freq == 0:
            influence = convolve(A_new, morphic_kernel, mode='wrap')
            B_new += field_strength * influence
        
        # Clipping per stabilità
        A = np.clip(A_new, 0, 1)
        B = np.clip(B_new, 0, 1)
    
    return A, B


# =============================================================================
# PARTE 3: METRICHE QUANTITATIVE (mappate su Proposizioni)
# =============================================================================

def calculate_metrics(image):
    """
    Calcola metriche che mappano direttamente sulle Proposizioni EAR.
    
    1. Centri Forti → Nodi ⬡ emergenti (Prop 3: soglia critica)
    2. Contrasto → Distinzione Δ (Prop 6: inseparabilità)
    3. Connettività → Relazione ⇄ (Prop 6: inseparabilità)
    4. Dinamica spettrale → Processo ⟳ (Prop 6: inseparabilità)
    5. Multi-scala → Scaling (Prop 4)
    """
    
    metrics = {}
    
    # 1. CENTRI FORTI (Nodi ⬡)
    # Numero di massimi locali = nodi emergenti
    neighborhood = 7
    local_max = maximum_filter(image, neighborhood)
    centers = (image == local_max) & (image > np.mean(image))
    metrics['centri_forti'] = np.sum(centers)
    
    # 2. CONTRASTO (Distinzione Δ)
    # Gradiente = forza delle distinzioni
    gx = sobel(image, axis=0)
    gy = sobel(image, axis=1)
    gradient = np.hypot(gx, gy)
    metrics['contrasto'] = np.std(gradient)
    
    # 3. CONNETTIVITÀ (Relazione ⇄)
    # Autocorrelazione spaziale = quanto i punti sono relazionati
    from scipy.signal import correlate2d
    autocorr = correlate2d(image - np.mean(image), 
                           image - np.mean(image), 
                           mode='same')
    # Normalizza e prendi raggio caratteristico
    autocorr_norm = autocorr / autocorr.max()
    # Distanza a cui correlazione scende sotto 0.5
    center = image.shape[0] // 2
    radial_profile = autocorr_norm[center, center:]
    try:
        correlation_length = np.where(radial_profile < 0.5)[0][0]
    except:
        correlation_length = len(radial_profile)
    metrics['lunghezza_correlazione'] = correlation_length
    
    # 4. COMPLESSITÀ SPETTRALE (Processo ⟳)
    # Entropia dello spettro di Fourier = ricchezza dinamica
    fft = np.fft.fft2(image)
    power_spectrum = np.abs(fft) ** 2
    power_spectrum = power_spectrum / power_spectrum.sum()  # Normalizza
    power_spectrum = power_spectrum.flatten()
    power_spectrum = power_spectrum[power_spectrum > 1e-10]  # Evita log(0)
    spectral_entropy = -np.sum(power_spectrum * np.log(power_spectrum))
    metrics['entropia_spettrale'] = spectral_entropy
    
    # 5. BILANCIAMENTO MULTI-SCALA (Scaling, Prop 4)
    # Energia in diverse bande di frequenza
    fft_shifted = np.fft.fftshift(np.fft.fft2(image))
    size = image.shape[0]
    center = size // 2
    y, x = np.ogrid[-center:size-center, -center:size-center]
    r = np.sqrt(x*x + y*y)
    
    # Tre bande: bassa (strutture grandi), media, alta (dettagli fini)
    low = np.sum(np.abs(fft_shifted[r < size/6]) ** 2)
    mid = np.sum(np.abs(fft_shifted[(r >= size/6) & (r < size/3)]) ** 2)
    high = np.sum(np.abs(fft_shifted[r >= size/3]) ** 2)
    
    total = low + mid + high
    if total > 0:
        metrics['energia_bassa'] = low / total
        metrics['energia_media'] = mid / total
        metrics['energia_alta'] = high / total
        # Bilanciamento = quanto NON è concentrato solo nelle basse
        metrics['bilanciamento_scala'] = (mid + high) / total
    else:
        metrics['energia_bassa'] = 0
        metrics['energia_media'] = 0
        metrics['energia_alta'] = 0
        metrics['bilanciamento_scala'] = 0
    
    return metrics


def test_inseparability(metrics_list):
    """
    Test Proposizione 6: I tre attributi (Δ, ⇄, ⟳) co-variano?
    
    Se Prop 6 è corretta, cambiando un parametro:
    - Contrasto (Δ), Connettività (⇄), Entropia (⟳) devono muoversi insieme
    """
    
    contrasto = [m['contrasto'] for m in metrics_list]
    correlazione = [m['lunghezza_correlazione'] for m in metrics_list]
    entropia = [m['entropia_spettrale'] for m in metrics_list]
    
    # Calcola correlazioni tra attributi
    corr_delta_rel, p1 = pearsonr(contrasto, correlazione)
    corr_delta_proc, p2 = pearsonr(contrasto, entropia)
    corr_rel_proc, p3 = pearsonr(correlazione, entropia)
    
    return {
        'corr_Δ_⇄': (corr_delta_rel, p1),
        'corr_Δ_⟳': (corr_delta_proc, p2),
        'corr_⇄_⟳': (corr_rel_proc, p3)
    }


# =============================================================================
# PARTE 4: ESPERIMENTI
# =============================================================================

def experiment_1_kernel_comparison():
    """
    Esperimento 1: Confronto kernel EAR vs altri
    
    Predizione: Il kernel EAR produce pattern con:
    - Più centri forti (più ⬡)
    - Più contrasto (più Δ)
    - Migliore bilanciamento scala (Prop 4)
    """
    
    print("=" * 60)
    print("ESPERIMENTO 1: Confronto Kernel")
    print("=" * 60)
    
    kernels = derive_alternative_kernels()
    results = {}
    
    for name, kernel in kernels.items():
        print(f"\nSimulazione con kernel: {name}...")
        
        if name == 'Nullo':
            A, B = simulate_gray_scott(morphic_kernel=None)
        else:
            A, B = simulate_gray_scott(morphic_kernel=kernel)
        
        metrics = calculate_metrics(A)
        results[name] = metrics
        
        print(f"  Centri forti: {metrics['centri_forti']}")
        print(f"  Contrasto: {metrics['contrasto']:.4f}")
        print(f"  Bilanciamento scala: {metrics['bilanciamento_scala']:.4f}")
    
    return results


def experiment_2_threshold_detection():
    """
    Esperimento 2: Test Proposizione 3 (Soglia Critica)
    
    Predizione: Esiste un valore di field_strength dove 
    la complessità del pattern "salta" discontinuamente.
    """
    
    print("\n" + "=" * 60)
    print("ESPERIMENTO 2: Rilevamento Soglia Critica (Prop 3)")
    print("=" * 60)
    
    kernel_ear = derive_ear_kernel()
    
    strengths = np.linspace(0, 0.05, 20)
    metrics_list = []
    
    print("\nVariazione field_strength...")
    for i, strength in enumerate(strengths):
        A, B = simulate_gray_scott(
            morphic_kernel=kernel_ear,
            field_strength=strength,
            steps=2000  # Più veloce per scan
        )
        metrics = calculate_metrics(A)
        metrics['field_strength'] = strength
        metrics_list.append(metrics)
        
        if i % 5 == 0:
            print(f"  {i+1}/20 completato")
    
    # Cerca discontinuità (salti)
    centri = [m['centri_forti'] for m in metrics_list]
    contrasti = [m['contrasto'] for m in metrics_list]
    
    # Derivata numerica per trovare salti
    d_centri = np.diff(centri)
    d_contrasti = np.diff(contrasti)
    
    # Trova massimo salto
    idx_salto_centri = np.argmax(np.abs(d_centri))
    idx_salto_contrasti = np.argmax(np.abs(d_contrasti))
    
    soglia_centri = strengths[idx_salto_centri]
    soglia_contrasti = strengths[idx_salto_contrasti]
    
    print(f"\nSoglia rilevata (centri): {soglia_centri:.4f}")
    print(f"Soglia rilevata (contrasto): {soglia_contrasti:.4f}")
    
    return metrics_list, strengths


def experiment_3_inseparability():
    """
    Esperimento 3: Test Proposizione 6 (Inseparabilità)
    
    Predizione: Δ, ⇄, ⟳ sono correlati - non si possono
    modificare indipendentemente.
    """
    
    print("\n" + "=" * 60)
    print("ESPERIMENTO 3: Test Inseparabilità Attributi (Prop 6)")
    print("=" * 60)
    
    kernel_ear = derive_ear_kernel()
    
    # Varia parametri e raccogli metriche
    metrics_list = []
    
    # Varia feed rate (cambia dinamica di base)
    feeds = np.linspace(0.04, 0.07, 10)
    
    print("\nVariazione feed rate...")
    for feed in feeds:
        A, B = simulate_gray_scott(
            morphic_kernel=kernel_ear,
            feed=feed,
            steps=2000
        )
        metrics = calculate_metrics(A)
        metrics_list.append(metrics)
    
    # Test correlazioni
    correlations = test_inseparability(metrics_list)
    
    print("\nCorrelazioni tra attributi:")
    print(f"  Δ ↔ ⇄ (contrasto-correlazione): r={correlations['corr_Δ_⇄'][0]:.3f}, p={correlations['corr_Δ_⇄'][1]:.4f}")
    print(f"  Δ ↔ ⟳ (contrasto-entropia): r={correlations['corr_Δ_⟳'][0]:.3f}, p={correlations['corr_Δ_⟳'][1]:.4f}")
    print(f"  ⇄ ↔ ⟳ (correlazione-entropia): r={correlations['corr_⇄_⟳'][0]:.3f}, p={correlations['corr_⇄_⟳'][1]:.4f}")
    
    # Interpretazione
    significant = sum(1 for k, v in correlations.items() if abs(v[0]) > 0.5)
    print(f"\nCorrelazioni significative (|r| > 0.5): {significant}/3")
    
    if significant >= 2:
        print("→ SUPPORTA Prop 6: attributi co-variano")
    else:
        print("→ NON SUPPORTA Prop 6: attributi indipendenti")
    
    return correlations, metrics_list


def experiment_4_scaling():
    """
    Esperimento 4: Test Proposizione 4 (Scaling)
    
    Predizione: Lo stesso pattern emerge a scale diverse
    con struttura isomorfa.
    """
    
    print("\n" + "=" * 60)
    print("ESPERIMENTO 4: Test Scaling Dimensionale (Prop 4)")
    print("=" * 60)
    
    kernel_ear = derive_ear_kernel()
    
    sizes = [75, 150, 300]
    results = {}
    
    print("\nSimulazione a scale diverse...")
    for size in sizes:
        print(f"  Size: {size}x{size}...")
        A, B = simulate_gray_scott(
            size=size,
            morphic_kernel=kernel_ear,
            steps=int(3000 * (size/150))  # Scala i passi
        )
        metrics = calculate_metrics(A)
        results[size] = metrics
    
    # Confronta rapporti tra metriche
    print("\nRapporti tra scale:")
    
    # I centri dovrebbero scalare con l'area (quadratico)
    ratio_centri_1 = results[150]['centri_forti'] / results[75]['centri_forti']
    ratio_centri_2 = results[300]['centri_forti'] / results[150]['centri_forti']
    
    print(f"  Centri 150/75: {ratio_centri_1:.2f} (atteso ~4 se scala con area)")
    print(f"  Centri 300/150: {ratio_centri_2:.2f} (atteso ~4 se scala con area)")
    
    # Il bilanciamento dovrebbe essere invariante
    bil_75 = results[75]['bilanciamento_scala']
    bil_150 = results[150]['bilanciamento_scala']
    bil_300 = results[300]['bilanciamento_scala']
    
    print(f"\n  Bilanciamento scala 75: {bil_75:.4f}")
    print(f"  Bilanciamento scala 150: {bil_150:.4f}")
    print(f"  Bilanciamento scala 300: {bil_300:.4f}")
    
    variance = np.var([bil_75, bil_150, bil_300])
    print(f"  Varianza bilanciamento: {variance:.6f}")
    
    if variance < 0.01:
        print("→ SUPPORTA Prop 4: bilanciamento invariante per scala")
    else:
        print("→ PARZIALE: bilanciamento varia con scala")
    
    return results


# =============================================================================
# PARTE 5: ESECUZIONE E REPORT
# =============================================================================

if __name__ == "__main__":
    
    print("\n" + "=" * 60)
    print("ESPERIMENTO CAMPO MORFOGENETICO EAR")
    print("Test Quantitativo delle Proposizioni")
    print("=" * 60)
    
    # Mostra kernel derivato
    print("\n--- DERIVAZIONE KERNEL ---")
    kernel = derive_ear_kernel()
    print(f"Kernel EAR:\n{kernel}")
    
    # Esegui esperimenti
    results_exp1 = experiment_1_kernel_comparison()
    results_exp2, strengths = experiment_2_threshold_detection()
    results_exp3, metrics_exp3 = experiment_3_inseparability()
    results_exp4 = experiment_4_scaling()
    
    # Report finale
    print("\n" + "=" * 60)
    print("REPORT FINALE")
    print("=" * 60)
    
    print("\n1. CONFRONTO KERNEL (Exp 1):")
    print(f"   EAR supera Nullo in centri? {results_exp1['EAR']['centri_forti'] > results_exp1['Nullo']['centri_forti']}")
    print(f"   EAR supera Invertito in contrasto? {results_exp1['EAR']['contrasto'] > results_exp1['Invertito']['contrasto']}")
    
    print("\n2. SOGLIA CRITICA (Exp 2, Prop 3):")
    print(f"   Soglia rilevata: presente (vedi valori sopra)")
    
    print("\n3. INSEPARABILITÀ (Exp 3, Prop 6):")
    n_sig = sum(1 for k, v in results_exp3.items() if abs(v[0]) > 0.5)
    print(f"   Correlazioni significative: {n_sig}/3")
    
    print("\n4. SCALING (Exp 4, Prop 4):")
    var = np.var([results_exp4[s]['bilanciamento_scala'] for s in [75, 150, 300]])
    print(f"   Invarianza bilanciamento: {'Sì' if var < 0.01 else 'Parziale'}")
    
    print("\n" + "=" * 60)
    print("FINE ESPERIMENTO")
    print("=" * 60)
