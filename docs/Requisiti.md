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
Dovra' essere previsto un sistema di autenticazione per ogni comunicazione, in modo da mettere in sicurezza i dispositivi

Qui l'elenco di tutti i dispositivi previsti.

### PC

- **API**: \
  Spegni / Riavvia / Sospendi \
  Uptime \
  Notifica

- **GUI**: \
  Integrazione con Assistente \
  Controllo di tutti i dispositivi \
  Storico notifiche

### Telefono

- **API**: \
  Batteria, luminosita', ... \
  Spegni / Riavvia \
  Notifica

- **GUI**: \
  Controllo di tutti i dispositivi

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

## Requisiti sui dati
