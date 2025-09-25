# 🌀 EAR Marketing

> Dal rumore alla risonanza. Un sito che vibra a 432 Hz.

<div align="center">
  <svg width="120" height="120" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 16 Q16 14, 14 14 T10 14 Q10 18, 14 18 T22 18 Q22 10, 14 10 T6 10 Q6 22, 18 22 T30 22 Q30 6, 14 6" 
          stroke="#d4af37" stroke-width="1.5" fill="none"/>
  </svg>
</div>

## 📖 Filosofia

Questo non è solo un sito. È una frequenza.

**EAR** - **E**ssenza, **A**rmonia, **R**isonanza. Non un acronimo, ma un metodo. Come l'orecchio che ascolta prima di parlare, questo sito parte dal silenzio per arrivare alla risonanza naturale.

## 🎨 La Sinfonia Silenziosa

Ogni pagina contiene una "sinfonia visiva" - un canvas generativo che:
- Vibra matematicamente a 432 Hz (la frequenza naturale dell'universo)
- Risponde al movimento del mouse come onde nell'acqua
- Respira con un ritmo di 4 secondi (come il respiro umano a riposo)
- Crea pattern frattali basati sulla sezione aurea (φ = 1.618...)

Non è decorazione. È l'architettura invisibile che accoglie il contenuto.

## 🏗️ Struttura Completa

```
ear-marketing/
├── index.html              # Homepage - Il primo ascolto
├── chi-siamo.html          # Il Nodo 432
├── servizi.html            # Prezzi trasparenti, zero sorprese
├── ear.html                # Il Metodo - scroll narrativo
├── casi-studio.html        # Non promettiamo. Mostriamo.
├── blog.html               # Filosofia applicata
├── contatti.html           # Iniziamo dall'ascolto
├── privacy.html            # GDPR con rispetto
├── 404.html                # Pagina errore filosofica
├── risonanza-test.html     # 🪞 Test nascosto con specchio
├── robots.txt              # Per i bot rispettosi
├── sitemap.xml             # La mappa del silenzio
└── README.md               # Questo file
```

## 🌟 Features Speciali

### 🪞 **Lo Specchio** (`risonanza-test.html`)
- Test della risonanza con intro a specchio
- "Prima di trovare la tua frequenza, guardati"
- 3 domande che calcolano la tua "frequenza" di brand
- Diagnosi e prescrizioni personalizzate

### 🚪 **La Porta Aperta** (in homepage)
- Sezione "Guardati. O continua a scorrere."
- Link nascosto in bella vista al test
- Chi deve trovarla, la trova

### 💻 **Easter Egg Console**
- Messaggio poetico per developer curiosi
- Funzione `EAR.risuona()` che fa pulsare il canvas
- Chi la trova può candidarsi in modo speciale

### 🌀 **Cursore Spirale**
- Cursore normale: punto minimo
- Su elementi interattivi: spirale aurea dorata
- Sottile ma presente

### 📱 **Ottimizzazioni Performance**
- Canvas adattivo (30fps mobile, 60fps desktop)
- Debounce su eventi mouse/scroll
- Pausa animazione quando tab non visibile
- Zero dipendenze esterne (solo font Google)

## ⚡ Performance

- **Zero jQuery, Bootstrap, o framework**
- **Vanilla JS puro** - 100% controllo
- **CSS custom** - nessun Tailwind
- **Target**: 100/100 Lighthouse
- **Peso totale**: < 200KB per pagina
- **GDPR compliant** con Plausible (no cookie)

## 🔧 Setup Tecnico

### 1. Analytics (Plausible)
```bash
# Registrati su https://plausible.io
# Aggiungi dominio: nodo432.com
# Il codice è già integrato in tutte le pagine
```

### 2. Form Handler (Formspree)
```bash
# 1. Vai su https://formspree.io
# 2. Crea un nuovo form
# 3. Sostituisci YOUR_FORM_ID in contatti.html (riga ~440)
#    https://formspree.io/f/YOUR_FORM_ID
```

### 3. Newsletter (Buttondown) - Opzionale
```bash
# 1. Registrati su https://buttondown.email
# 2. Ottieni API key
# 3. Sostituisci YOUR_API_KEY in blog.html (riga ~490)
```

### 4. Deploy su GitHub Pages
```bash
# Inizializza repository
git init

# Aggiungi tutti i file
git add .

# Primo commit
git commit -m "🌀 Dal rumore alla risonanza - EAR Marketing launch"

# Crea repo su GitHub e collegala
git branch -M main
git remote add origin https://github.com/TUO_USERNAME/ear-marketing.git

# Push
git push -u origin main

# Attiva GitHub Pages
# Settings → Pages → Source: Deploy from branch (main) → / (root)

# Per dominio custom, aggiungi file CNAME:
echo "nodo432.com" > CNAME
git add CNAME
git commit -m "Add custom domain"
git push
```

## 📋 Checklist Pre-Lancio Completa

### Configurazioni Tecniche
- [ ] Registrarsi su Formspree e ottenere Form ID
- [ ] Sostituire `YOUR_FORM_ID` in contatti.html
- [ ] Registrarsi su Plausible Analytics
- [ ] Aggiungere dominio nodo432.com su Plausible
- [ ] (Opzionale) Setup Buttondown per newsletter
- [ ] (Opzionale) Sostituire `YOUR_API_KEY` in blog.html

### Dati da Aggiornare
- [x] ~~Email: alessiomarrone@outlook.com~~ ✅ Fatto
- [x] ~~Telefono/WhatsApp: +39 340 841 5770~~ ✅ Fatto
- [ ] P.IVA: sostituire `12345678901` con P.IVA reale
- [ ] Aggiornare indirizzo se necessario

### Asset da Creare
- [ ] **logo.svg** - Salvare questo codice come file:
```svg
<svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 16 Q16 14, 14 14 T10 14 Q10 18, 14 18 T22 18 Q22 10, 14 10 T6 10 Q6 22, 18 22 T30 22 Q30 6, 14 6" 
        stroke="#d4af37" stroke-width="1.5" fill="none"/>
</svg>
```
- [ ] **og-image.jpg** (1200x630px) con logo + "Dal rumore alla risonanza"
- [ ] **favicon.ico** - Generare da logo.svg usando https://realfavicongenerator.net

### Testing
- [ ] Testare form contatti (desktop + mobile)
- [ ] Verificare link WhatsApp
- [ ] Testare tutti i link interni
- [ ] Verificare responsive su mobile
- [ ] Testare canvas su dispositivi diversi
- [ ] Verificare la "porta" nascosta in homepage
- [ ] Testare il test della risonanza con specchio
- [ ] Verificare easter egg console (`EAR.risuona()`)
- [ ] Controllare pagina 404

### SEO & Performance
- [ ] Verificare meta description univoche per pagina
- [ ] Test Lighthouse (target 95-100)
- [ ] Verificare Schema.org markup
- [ ] Controllare sitemap.xml
- [ ] Verificare robots.txt

### Deployment
- [ ] Push su GitHub
- [ ] Attivare GitHub Pages
- [ ] Configurare DNS per dominio custom
- [ ] Verificare HTTPS attivo
- [ ] Test finale su dominio live

## 🎼 La Frequenza del Codice

### Il Canvas Generativo
```javascript
// La formula della risonanza
resonance = Σ(harmonic[n] * sin(432Hz * φ * position))

// Respiro: 4 secondi in, 4 secondi out
opacity = 0.7 + sin(time * π/4) * 0.15
```

### Pattern Filosofico
- **Frasi corte.** Punto.
- **Contrasto**: "Dal rumore alla risonanza"
- **Negazione**: "Non inventiamo. Riveliamo."
- **Ogni elemento** guadagna il diritto di esistere

## 🚀 Informazioni Contatto

**Email**: alessiomarrone@outlook.com  
**WhatsApp**: +39 340 841 5770  
**Sito**: https://nodo432.com (prossimamente)

## 📄 Licenza

Questo progetto è proprietà di EAR Marketing.  
Il codice del canvas generativo può essere riutilizzato con attribuzione.

---

### 💭 Note Filosofiche

> "La perfezione si ottiene non quando non c'è nient'altro da aggiungere,  
> ma quando non c'è nient'altro da togliere."  
> — Antoine de Saint-Exupéry

Questo sito segue questa filosofia. Ogni elemento esiste per necessità, non per ornamento.

Il silenzio tra le note è musica quanto le note stesse.

**Dal rumore alla risonanza. Sempre.**

---

*Creato con amore e matematica da EAR Marketing*  
*Versione 1.0 - Gennaio 2025*  
*La frequenza naturale del web*

---

## 🎯 Quick Start

```bash
# 1. Clona o scarica i file
# 2. Sostituisci YOUR_FORM_ID in contatti.html
# 3. Aggiorna P.IVA
# 4. Deploy su GitHub Pages
# 5. Il sito è live! 🌀
```

## 📖 Filosofia

Questo non è solo un sito. È una frequenza.

**EAR** - Essenza, Armonia, Risonanza. Non un acronimo, ma un metodo. Come l'orecchio che ascolta prima di parlare, questo sito parte dal silenzio per arrivare alla risonanza naturale.

## 🎨 La Sinfonia Silenziosa

Ogni pagina contiene una "sinfonia visiva" - un canvas generativo che:
- Vibra matematicamente a 432 Hz (la frequenza naturale dell'universo)
- Risponde al movimento del mouse come onde nell'acqua
- Respira con un ritmo di 4 secondi (come il respiro umano a riposo)
- Crea pattern frattali basati sulla sezione aurea (φ = 1.618...)

Non è decorazione. È l'architettura invisibile che accoglie il contenuto.

## 🏗️ Struttura

```
ear-marketing/
├── index.html              # Homepage - Il primo ascolto
├── chi-siamo.html          # Il Nodo 432
├── servizi.html            # Prezzi trasparenti, zero sorprese
├── ear.html                # Il Metodo - scroll narrativo
├── casi-studio.html        # Non promettiamo. Mostriamo.
├── blog.html               # Filosofia applicata
├── contatti.html           # Iniziamo dall'ascolto
├── privacy.html            # GDPR con rispetto
├── robots.txt              # Per i bot rispettosi
└── sitemap.xml             # La mappa del silenzio
```

## ⚡ Performance

- **Zero dipendenze esterne** (tranne font Google)
- **Niente jQuery, Bootstrap, o framework**
- **Vanilla JS puro** - 100% controllo
- **CSS custom** - nessun Tailwind
- **Target**: 100/100 Lighthouse
- **Peso totale**: < 200KB

## 🔧 Setup Tecnico

### 1. Analytics (Plausible)
```bash
# Registrati su https://plausible.io
# Aggiungi dominio: nodo432.com
# Il codice è già integrato in tutte le pagine
```

### 2. Form Handler (Formspree)
```bash
# 1. Vai su https://formspree.io
# 2. Crea un nuovo form
# 3. Sostituisci YOUR_FORM_ID in contatti.html:
#    https://formspree.io/f/YOUR_FORM_ID
```

### 3. Newsletter (Buttondown)
```bash
# 1. Registrati su https://buttondown.email
# 2. Ottieni API key
# 3. Sostituisci YOUR_API_KEY in blog.html
```

### 4. Deploy
```bash
# GitHub Pages (consigliato)
git init
git add .
git commit -m "Dal rumore alla risonanza"
git remote add origin https://github.com/tuousername/ear-marketing.git
git push -u origin main

# Settings > Pages > Source: Deploy from branch (main)
```

## 🎯 Checklist Pre-Lancio

- [ ] Sostituire `YOUR_FORM_ID` con ID Formspree reale
- [ ] Sostituire `YOUR_API_KEY` con API Buttondown
- [ ] Aggiornare P.IVA in footer e privacy
- [ ] Verificare email e telefono in contatti
- [ ] Testare form su mobile e desktop
- [ ] Verificare Lighthouse score (target: 100)
- [ ] Configurare dominio nodo432.com
- [ ] Attivare Plausible Analytics

## 🎼 La Frequenza del Codice

### Il Canvas Generativo
Il cuore pulsante del sito. Basato su:
- **432 Hz**: La frequenza convertita in movimento visivo
- **Sezione Aurea** (1.618): Proporziona le spirali
- **Armoniche**: 5 livelli sovrapposti (1, 2, 3, 5, 8 - Fibonacci)
- **Interferenze**: Pattern moiré naturali dall'interazione

```javascript
// La formula della risonanza
resonance = Σ(harmonic[n] * sin(432Hz * φ * position))
```

### Opacità Dinamica
```javascript
// Respiro: 4 secondi in, 4 secondi out
opacity = 0.7 + sin(time * π/4) * 0.15
```

Puoi modificare l'opacità base (0.7) se troppo presente.

## 🌟 Chicche Nascoste

### La Spirale Logo
Non un semplice SVG, ma una spirale aurea che:
- Respira con animazione di 4 secondi
- Ruota leggermente (5°) al picco del respiro
- Rappresenta la crescita organica continua

### Scroll Reveal
Ogni elemento "emerge dal silenzio" con:
- Fade-in dal basso
- Timing cubic-bezier per movimento organico
- Attivazione basata su viewport

### Copy Philosophy
- **Frasi corte.** Punto.
- **Verbi attivi** invece di forme passive
- **Numeri reali** invece di percentuali inventate
- **Contrasto**: "Dal rumore alla risonanza"
- **Negazione**: "Non inventiamo. Riveliamo."

## 🚀 Ottimizzazioni Future

1. **Service Worker** per offline-first
2. **WebP images** con fallback JPG
3. **Critical CSS** inline nel <head>
4. **Lazy loading** per immagini portfolio
5. **Schema.org** markup strutturato

## 📞 Supporto

**Email**: ciao@nodo432.com  
**Issue**: Apri una issue su GitHub  
**Filosofia**: Se aggiunge rumore, taglia. Sempre.

## 📄 Licenza

Questo progetto è proprietà di EAR Marketing.  
Il codice del canvas generativo può essere riutilizzato con attribuzione.

---

### 💭 Note Filosofiche

> "La perfezione si ottiene non quando non c'è nient'altro da aggiungere,  
> ma quando non c'è nient'altro da togliere."  
> — Antoine de Saint-Exupéry

Questo sito segue questa filosofia. Ogni elemento esiste per necessità, non per ornamento.

Il silenzio tra le note è musica quanto le note stesse.

**Dal rumore alla risonanza. Sempre.**

---

*Creato con amore e matematica da EAR Marketing*  
*Versione 1.0 - Gennaio 2025*  
*La frequenza naturale del web*
