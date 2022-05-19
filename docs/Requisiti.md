# NjHub | Raccolta requisiti sistema

## Descrizione

Sistema formato da un server sempre attivo e vari dispositivi: PC, telefono android, orologio android, luci e altri dispositivi smart. \
Ogni dispositivo si connette al server, che gestisce tutte le connessioni con tutti i dispositivi. \
Ogni dispositivo puo' vedere lo stato di ogni altro dispositivo e controllarne diverse funzioni. \
Esempio: orologio vede se una lampada e' attiva o meno, puo' accenderla, spegnerla o cambiarne colore.

## Requisiti funzionali

Ogni dispositivo e' completamente personalizzato e non comunica con nessuno se non con il server. \
Ogni dispositivo deve fornire un'API per vederne lo stato e eseguire funzioni su di esso. \
Ogni dispositivo deve avere un'interfaccia grafica per permettere all'utente di mandare comandi al server. \
Dovra' essere previsto un sistema di autenticazione per ogni comunicazione, in modo da mettere in sicurezza i dispositivi \
Funzionalità comuni (API) che devono provvedere tutti i dispositivi:

- Poter spegnere, riavviare o sospendere il dispositivo
- Poter mostrare una notifica (sui dispositivi che lo permettono ovvero non luci smart)
- Poter visualizzare le informazioni sul dispositivo (attivo o meno, batteria, uptime, ecc)

Qui l'elenco e descrizioni di tutti i dispositivi previsti.

### PC

OS: Windows 11 \
Linguaggio: Python 3.9.5

Questo dispositivo corrisponde al mio PC desktop di casa. \
L'unica GUI prevista per ora sarà quella dell'Assistente, che permetterà di visualizzare informazioni varie, quali ora, meteo, musica in riproduzione ecc., e infomzioni sui dispositivi, permettendo di controllarli.

### Telefono

OS: Android 13 \
Linguaggio: Kotlin 1.6.x

Il mio telefono.

### Orologio

- **API**: \
  Batteria, luminosita', ... \
  Notifica

- **GUI**: \
  Controllo di luci smart

### Dispositivi smart

- **API**: \
  Controllo intero del dispositivo
  - Luci: On/Off, luminosita', colore, scena, programmazione \
  - Socket: On/Off, programmazione \
  - Tapparelle: Su/Stop/Giu', programmazione
