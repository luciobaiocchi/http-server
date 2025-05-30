# Relazione Tecnica

## 1. Introduzione
L’obiettivo del progetto è stato realizzare un server HTTP minimale in Python che fornisse contenuti statici ottimizzati, con gestione avanzata dei MIME types, logging delle richieste, un’interfaccia responsiva e animazioni CSS leggere.

## 2. Specifiche del progetto
- **Linguaggio**: Python 3, per semplicità e rapidità di prototipazione.
- **Sockets**: utilizzo di `socket.socket` per la comunicazione TCP a basso livello.
- **Multithreading**: thread daemon per gestire richieste concorrenti senza blocchi.
- **Logging**: modulo `logging` con scrittura su file per analisi posteriore.

## 3. Gestione MIME Types
Il server utilizza `mimetypes.guess_type` per associare le estensioni a `Content-Type`. Sono supportate nativamente estensioni comuni:
- Testo: `.html`, `.css`, `.js`, `.json`, `.txt`
- Immagini: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`
- Font: `.woff`, `.woff2`, `.ttf`
- Altro: `.pdf`, `.zip`, `.xml`

## 4. Logging delle richieste
Le operazioni di logging includono:
- Timestamp ISO 8601.
- Livello (INFO, WARNING, ERROR).
- Dettagli di richiesta (client, metodo, path).
- Codice di risposta e MIME type.
Queste informazioni sono utili per debugging, metriche di utilizzo e monitoraggio.

## 5. Design responsivo e animazioni CSS
- **Layout a griglia**: uso di CSS Grid con `auto-fit` e `minmax` per adattamento fluido.
- **Animazioni**: fade-in per contenuti e slide-in per l’header.
- **Transizioni**: hover sui link e card con trasformazioni leggere.
- **Responsive breakpoints**: adattamento per mobile (<768px) e tablet.

## 6. Testing e validazione
- Controllo manuale su Chrome, Firefox e Edge.
- Validazione HTML/CSS con W3C Validator.
- Test di concorrenza con `ab` (ApacheBench), 100 richieste concorrenti: latenza media <50ms su ambiente locale.

## 7. Sicurezza e limitazioni
- **Directory traversal**: sanitizzazione di `path` con `lstrip('/')` e `os.path.isfile`.
- **Metodi supportati**: solo GET; POST e altri metodi ignorati.
- **SSL/TLS**: non implementato; consigliato `stunnel` o `nginx` in front-end per HTTPS.

## 8. Immagini
Di seguito alcune immagini che mostrano sia la parte server e il frontend del sito.

Server
![[./img/Screenshot 2025-05-30 at 14.23.42.png]]
Home
![[./img/Screenshot 2025-05-30 at 14.21.38.png]]
Contatti
![[./img/Screenshot 2025-05-30 at 14.21.58.png]]
Galleria
![[./img/Screenshot 2025-05-30 at 14.21.45.png]]


## 8. Conclusioni
Il server soddisfa i requisiti di base e le estensioni richieste. Grazie alla struttura modulare, è immediato aggiungere nuove funzionalità (caching, HTTPS, API).


