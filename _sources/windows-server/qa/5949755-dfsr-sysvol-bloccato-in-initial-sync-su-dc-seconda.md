---
title: "DFSR SYSVOL bloccato in Initial Sync su DC secondario (BK1) – errori 1753/1722 e mancata replica con PDC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5949755/dfsr-sysvol-bloccato-in-initial-sync-su-dc-seconda
question_id: 5949755
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor", "Q&A User"]
---
# DFSR SYSVOL bloccato in Initial Sync su DC secondario (BK1) – errori 1753/1722 e mancata replica con PDC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5949755/dfsr-sysvol-bloccato-in-initial-sync-su-dc-seconda (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Titolo: DFSR SYSVOL bloccato in Initial Sync su DC secondario (BK1) – errori 1753/1722 e mancata replica con PDC

Buongiorno,

nel dominio TREERRESERVICE.local ho due controller di dominio Windows Server 2022:

-  PDC: ML350-G10 (tutti i ruoli FSMO, SYSVOL integro)

-  DC secondario: ML350-G10-BK1

Il problema riguarda BK1: SYSVOL non replica e rimane in stato “Initial Sync”. Il comando dcdiag /v mostra che BK1 NON supera il test DFSREvent, mentre il PDC è sano.

Errori principali su BK1:

-  DFSR: 1753 “Nessun endpoint disponibile nel mapping degli endpoint”

-  DFSR: 1722 “Server RPC non disponibile”

-  DFSR: 1723 “Server RPC troppo impegnato”

-  DFSR: 0x80001206 “SYSVOL inizializzato, in attesa della replica iniziale”

-  DFSR: 0x80001A94 “Nessuna connessione configurata per il gruppo Domain System Volume”

-  AD: 0xc000018b “Il database SAM non ha un account computer per la relazione di trust”

-  GPO: 0x000003EE “Impossibile eseguire l’autenticazione con il servizio Active Directory”

Il PDC vede BK1 come partner DFSR ma non riesce a comunicare (errore 1753). BK1 non riesce a leggere la configurazione DFSR-GlobalSettings e non completa la replica SYSVOL.

Chiedo:

-  Qual è la procedura corretta per ripristinare BK1?  

-  D2 non-autorevole su BK1?  

-  D4 autorevole sul PDC?  

-  È necessario ricreare gli oggetti DFSR-GlobalSettings in AD?  

-  È consigliabile rimuovere BK1 dal dominio e promuoverlo nuovamente?

Grazie.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-07-17*

1. Panoramica del problema

Il dominio TREERRESERVICE.local è composto da:

PDC: ML350‑G10

DC secondario: ML350‑G10‑BK1

Il problema principale è la mancata replica SYSVOL su BK1, causata da errori DFS‑R e RPC che impediscono la sincronizzazione del contenuto SYSVOL e l’inizializzazione del database DFS‑R.

2. Diagnostica completa (da documenti caricati)

✔ Replica AD

La replica Active Directory tra PDC e BK1 è funzionante. I test AD (repadmin, dcdiag) mostrano:

replica dei naming context OK

Kerberos OK

Netlogon OK

DNS OK

NTDS OK

Questo elimina problemi di AD come causa primaria.

✔ Stato SYSVOL

PDC

SYSVOL presente

DFS‑R operativo

subscription corretta

GUID coerenti

BK1

SYSVOL vuoto

nessun database DFS‑R

nessuna cartella DFSR in System Volume Information

nessuna replica SYSVOL

dumpmachinecfg vuoto

Documento lista.txt conferma:

“SYSVOL completamente vuoto su BK1, 1 file (0 byte), 26 directory.”

✔ Stato DFS‑R

PDC

DFS‑R RUNNING

porta 5722 aperta

replica SYSVOL attiva

BK1

DFS‑R RUNNING

porta 5722 non aperta

nessun endpoint RPC

nessuna replica SYSVOL

eventi DFS‑R con errori 1753, 1722, 1723

Documento Server in fase di test conferma:

“Nessun endpoint disponibile nel mapping degli endpoint (1753). Server RPC non disponibile (1722). Replica iniziale non completata.”

✔ Stato RPC

PDC

tutti i servizi RPC presenti

BK1

rpcss RUNNING

netlogon RUNNING

ntds RUNNING

dfsr RUNNING

❌ rpcepmap NON ESISTE (errore 1060)

Documento Windows PowerShell.txt conferma:

“Impossibile contattare il controller di dominio per informazioni di configurazione (1355).”

1. Panoramica del problema

Il dominio TREERRESERVICE.local è composto da:
PDC: ML350‑G10
DC secondario: ML350‑G10‑BK1
Il problema principale è la mancata replica SYSVOL su BK1, causata da errori DFS‑R e RPC che impediscono la sincronizzazione del contenuto SYSVOL e l’inizializzazione del database DFS‑R.

2. Diagnostica completa (da documenti caricati)

✔ Replica AD

La replica Active Directory tra PDC e BK1 è funzionante. I test AD (repadmin, dcdiag) mostrano:
replica dei naming context OK
Kerberos OK
Netlogon OK
DNS OK
NTDS OK
Questo elimina problemi di AD come causa primaria.

✔ Stato SYSVOL

PDC
SYSVOL presente
DFS‑R operativo
subscription corretta
GUID coerenti
BK1
SYSVOL vuoto
nessun database DFS‑R
nessuna cartella DFSR in System Volume Information
nessuna replica SYSVOL
dumpmachinecfg vuoto
Documento lista.txt conferma:

“SYSVOL completamente vuoto su BK1, 1 file (0 byte), 26 directory.”

✔ Stato DFS‑R

PDC

DFS‑R RUNNING

porta 5722 aperta

replica SYSVOL attiva

BK1

DFS‑R RUNNING

porta 5722 non aperta

nessun endpoint RPC

nessuna replica SYSVOL

eventi DFS‑R con errori 1753, 1722, 1723

Documento Server in fase di test conferma:

“Nessun endpoint disponibile nel mapping degli endpoint (1753). Server RPC non disponibile (1722). Replica iniziale non completata.”

✔ Stato RPC

PDC

tutti i servizi RPC presenti

BK1

rpcss RUNNING

netlogon RUNNING

ntds RUNNING

dfsr RUNNING

❌ rpcepmap NON ESISTE (errore 1060)

Documento Windows PowerShell.txt conferma:

“Impossibile contattare il controller di dominio per informazioni di configurazione (1355).”

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-07-17*

Hi piero facchetti,

When a secondary domain controller’s SYSVOL is stuck in Initial Sync with DFSR errors like 1753/1722, it usually points to a replication or RPC communication problem rather than a hardware fault. The fact that your PDC is healthy but BK1 cannot read DFSR-GlobalSettings confirms that the replication partnership is broken.

The recommended recovery path is to first verify that the DFSR service is running and that RPC connectivity between BK1 and the PDC is stable (firewall, ports, and DNS resolution are common culprits). If connectivity checks out, you can proceed with a non‑authoritative (D2) restore on BK1, which forces it to pull a fresh copy of SYSVOL from the PDC. The PDC itself should remain authoritative (D4) only if you suspect corruption on the primary, which doesn’t seem to be the case here.

It’s not usually necessary to recreate DFSR-GlobalSettings objects manually unless they’ve been deleted. If the D2 restore fails, then yes, removing BK1 from the domain and re‑promoting it can be a clean way to reset replication, but that’s more disruptive and should be a last resort.

I’d also recommend checking the Event Viewer on BK1 for DFSR and NTFRS logs to confirm whether the replication group is initializing correctly after the D2 restore. Monitoring with `Get-DfsrBacklog` can help validate progress once replication resumes.

I hope the response provided some helpful insight. If you find this answer useful, please hit “accept answer” so I know it addressed your concern.

Jason.
