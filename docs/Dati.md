# NjHub | Dati

Descrizione e standard dei dati utilizzati dal sistema, come descritto nella sezione Dati della [Raccolta dei requisiti](Requisiti.md).

## **Comunicazione fra dispositivi**

La comunicazione fra vari dispositivi avviene tramite messaggi scambiati mediante socket TCP/IP.

Un messaggio deve contenere i seguenti dati:

- Da chi è stato inviato il messaggio
- A chi è stato inviato il messaggio
- Quando è stato inviato il messaggio
- Il tipo di messaggio, cioè l'azione che si vuole eseguire
- Il contenuto effettivo del messaggio

Qui di seguito la descrizione di ogni campo.

### 0: Da chi

Usato per identificare il dispositivo che ha creato e inviato il messaggio.
Lunghezza: 1 carattere

#### Elenco dei caratteri previsti e dei relativi dispositivi:

| Carattere | Dispositivo |
| :-------- | :---------- |
| `0`       | Server      |
| `1`       | Computer    |
| `2`       | Smartphone  |
| `3`       | Smartwatch  |

### 1: A chi

Identifica il dispositivo che a cui il messaggio è destinato.
Lunghezza: 1 carattere

#### Elenco dei caratteri previsti e dei relativi dispositivi:

| Carattere | Dispositivo |
| :-------- | :---------- |
| `0`       | Server      |
| `1`       | Computer    |
| `2`       | Smartphone  |
| `3`       | Smartwatch  |
| `A`       | Dina        |
| `B`       | Lucine      |
| `C`       | Smartsocket |
| `D`       | Tapparella1 |
| `E`       | Tapparella2 |
| `F`       | Tapparella3 |
| `G`       | Tapparella4 |
| `H`       | Tapparella5 |
| `I`       | Tapparella6 |
| `J`       | Bobby       |

### 2-11: Quando

Usato per identificare il momento in cui il messaggio è stato inviato.
Formato: UNIX timestamp
Lunghezza: 10 caratteri

### 12: Azione richiesta

Identifica l'azione che si intende svolgere.
Lunghezza: 1 carattere

#### Elenco di ogni carattere previsto e delle relative azioni da svolgere.

| Carattere | Azione    |
| :-------- | :-------- |
| `0`       | Controllo |
| `1`       | Notifica  |

### 13-x: Contenuto

La restante sezione del messaggio è suddivisa e segue uno standard in base all'azione richiesta.

#### **Controllo**

Controllo dello stato del dispositivo.

- x1: Azione richiesta

Azioni previste:

| Carattere | Azione                 |
| :-------- | :--------------------- |
| `0`       | Chiusura del programma |
| `1`       | Spegnimento            |
| `2`       | Riavvio                |
| `3`       | Sospensione            |

#### **Notifica**

Messaggio di notifica al dispositivo.

- x4: Lunghezza della stringa del titolo
- x\*: Titolo della notifica
- x4: Lunghezza della stringa del testo
- x\*: Testo della notifica
- x6: Durata della notifica
- x1: Tipo di notifica (Avviso, Errore, Informazione) (non previsto attualmente)
