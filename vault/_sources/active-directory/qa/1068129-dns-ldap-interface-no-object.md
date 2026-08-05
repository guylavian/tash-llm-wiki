---
title: "DNS - LDAP interface NO_OBJECT"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1068129/dns-ldap-interface-no-object
question_id: 1068129
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# DNS - LDAP interface NO_OBJECT

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1068129/dns-ldap-interface-no-object (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all

I am getting LDAP errors in the Directory Service logs on my Domain Controller.  

I've done a clean install, the server is pointing to itself and is promoted to DC.

DNS is installed and the ip address is: 10.8.8.4

I want to log LDAP queries.  

In addition to the server, I have a domain computer who joined the domain and a total of 2 Domain Users(1 Administrator).  

I'm using Virtual Box in Nat Network Mode in order to rollback fast. (PoC environment)  

The errors listed under event ID 1535 are these:

*Error value:  

0000208D: NameErr: DSID-03100288, problem 2001 (NO_OBJECT), data 0, best match of:  

'DC=8.8.10.in-addr.arpa,CN=MicrosoftDNS,DC=ForestDnsZones,DC=DOMINIO,DC=local'  

as well as  

'DC=_msdcs.DOMINIO.local,CN=MicrosoftDNS,DC=ForestDnsZones,DC=DOMINIO,DC=local'  

and  

'DC=DOMINIO.local,CN=MicrosoftDNS,DC=DomainDnsZones,DC=DOMINIO,DC=local'*

I've disabled ipv6 address ("unchecked")

I had also changed the dns server from localhost to: 10.8.8.4 and setup a reverse ip address too.

ipconfig /all  

Windows IP Configuration  

Host Name . . . . . . . . . . . . . : DCPROVA  

Primary Dns Suffix . . . . . . . . : DOMINIO.local  

Node Type . . . . . . . . . . . . . : Hybrid  

IP Routing Enabled. . . . . . . . . : No  

WINS Proxy Enabled. . . . . . . . . : No  

DNS Suffix Search List. . . . . . . : DOMINIO.local  

Scheda Ethernet:  

Connection-specific DNS Suffix:  

Description. . . . . . . . . . . . . . : Intel(R) PRO/1000 MT Desktop Adapter  

Physical Address . . . . . . . . . . . : 08-00-27-4D-46-B3  

DHCP enabled . . . . . . . . . . . . . : No  

Autoconfiguration Enabled. . . . . . . : Sì  

Link-local IPv6 Address. . . . . . . . : fe80::8088:2589:5012:2552%4(Preferred)  

IPv4 Address. .. . . . . . . . . . . . : 10.8.8.4(Preferred)  

Subnet mask. . . . . . . . . . . . . . : 255.255.255.0  

Default Gateway. . . . . . . . . . . . : 10.8.8.1  

DHCPv6 IAID. . . . . . . . . . . . . . : 67633191  

DHCPv6 Client DUID. . .. . . . . . . . : 00-01-00-01-2A-D1-A1-56-08-00-27-4D-46-B3  

DNS Server. . . . . . . . . . . . . . : 10.8.8.4  

NetBIOS over TCP/IP . . . . . . . . . : Enabled

In the registry editor I've set the log level to 2, I did set also '15 Field Engineering' to '5' in order to enable Expensive and Inefficient LDAP calls to be logged in Event Viewer.

I tried to execute a LDAP query with "cn=users, dc=DOMINIO, DC=local" in the base DN fieldwith the search filter and it worked.(it's been done from the domain Host(logged as Admin) and I can get the entry).

During the Active Directory Lightweight Directory Services Setup Wizard I specified to create an application directory partition"CN=DCPROVA,DC=DOMINIO,DC=local"(I add this in case would be useful).In the wizard I left the Network service account. And the Domain users group with administrative privileges assigned, for the instance of AD LDS.

I noticed Firewall couldn't resolve 8.8.8.8 or 1.1.1.1(when I set them as DNS forwarders) when I was connected to my Company. (I'm doing an intern)  

I found that dcdiag /test:dns passed at home with my network and with no VPN.

dcdiag /fix logs me:

```
Inizio test: SystemLog  
         Si è verificato un evento di avviso. ID evento: 0x000003F6  
            Data e ora generazione: 10/29/2022   12.10.49  
            Stringa evento: Timeout della risoluzione dei nomi per il nome wpad. Nessun server DNS configurato ha risposto.  
         Si è verificato un evento di avviso. ID evento: 0x000003F6  
            Data e ora generazione: 10/29/2022   12.10.51  
            Stringa evento: Timeout della risoluzione dei nomi per il nome _ldap._tcp.Default-First-Site-Name._sites.dc._msdcs.DOMINIO.local.. Nessun server DNS configurato ha risposto.  
         Si è verificato un evento di avviso. ID evento: 0x00000081  
            Data e ora generazione: 10/29/2022   12.10.51  
            Stringa evento:  
            NtpClient: impossibile impostare un peer di dominio da utilizzare come origine ora a causa di un errore di individuazione. Verrà eseguito un nuovo tentativo tra 15 minuti, quindi l'intervallo tra i nuovi tentativi verrà raddoppiato. Errore: Connessione in corso interrotta forzatamente dall'host remoto. (0x80072746)  
         Si è verificato un evento di avviso. ID evento: 0x00001695  
            Data e ora generazione: 10/29/2022   12.18.29  
            Stringa evento:  
            Registrazione dinamica o eliminazione di uno o più record DNS associati al dominio DNS 'DOMINIO.local.' non riuscita. Questi record sono utilizzati da altri computer per individuare questo server come controller di dominio (se il dominio specificato è un dominio di Active Directory) o come server LDAP (se il dominio specificato è una partizione applicativa).  
         Si è verificato un evento di avviso. ID evento: 0x00001695  
            Data e ora generazione: 10/29/2022   12.18.29  
            Stringa evento:  
            Registrazione dinamica o eliminazione di uno o più record DNS associati al dominio DNS 'ForestDnsZones.DOMINIO.local.' non riuscita. Questi record sono utilizzati da altri computer per individuare questo server come controller di dominio (se il dominio specificato è un dominio di Active Directory) o come server LDAP (se il dominio specificato è una partizione applicativa).  
         Si è verificato un evento di avviso. ID evento: 0x00001695  
            Data e ora generazione: 10/29/2022   12.18.29  
            Stringa evento:  
            Registrazione dinamica o eliminazione di uno o più record DNS associati al dominio DNS 'DomainDnsZones.DOMINIO.local.' non riuscita. Questi record sono utilizzati da altri computer per individuare questo server come controller di dominio (se il dominio specificato è un dominio di Active Directory) o come server LDAP (se il dominio specificato è una partizione applicativa).  
         Si è verificato un evento di errore. ID evento: 0x0000272C  
            Data e ora generazione: 10/29/2022   12.30.47  
            Stringa evento:  
            DCOM: impossibile comunicare con il computer 1.1.1.1 utilizzando i protocolli configurati. Richiesta PID     1568 (C:\Windows\system32\dcdiag.exe) durante l'attivazione di CLSID {8BC3F05E-D86B-11D0-A075-00C04FB68820}.  
         Si è verificato un evento di errore. ID evento: 0x0000272C  
            Data e ora generazione: 10/29/2022   12.31.08  
            Stringa evento:  
            DCOM: impossibile comunicare con il computer 8.8.8.8 utilizzando i protocolli configurati. Richiesta PID     1568 (C:\Windows\system32\dcdiag.exe) durante l'attivazione di CLSID {8BC3F05E-D86B-11D0-A075-00C04FB68820}.  
         ......................... CRISIRDC non ha superato il test SystemLog  
      Inizio test: VerifyReferences  
         ......................... CRISIRDC ha superato il test VerifyReferences  

   Test partizione in esecuzione su: DomainDnsZones  
      Inizio test: CheckSDRefDom  
         ......................... DomainDnsZones ha superato il test CheckSDRefDom  
      Inizio test: CrossRefValidation  
         ......................... DomainDnsZones ha superato il test CrossRefValidation  

   Test partizione in esecuzione su: ForestDnsZones  
      Inizio test: CheckSDRefDom  
         ......................... ForestDnsZones ha superato il test CheckSDRefDom  
      Inizio test: CrossRefValidation  
         ......................... ForestDnsZones ha superato il test CrossRefValidation  

   Test partizione in esecuzione su: Schema  
      Inizio test: CheckSDRefDom  
         ......................... Schema ha superato il test CheckSDRefDom  
      Inizio test: CrossRefValidation  
         ......................... Schema ha superato il test CrossRefValidation  

   Test partizione in esecuzione su: Configuration  
      Inizio test: CheckSDRefDom  
         ......................... Configuration ha superato il test CheckSDRefDom  
      Inizio test: CrossRefValidation  
         ......................... Configuration ha superato il test CrossRefValidation  

   Test partizione in esecuzione su: DOMINIO  
      Inizio test: CheckSDRefDom  
         ......................... DOMINIO ha superato il test CheckSDRefDom  
      Inizio test: CrossRefValidation  
         ......................... DOMINIO ha superato il test CrossRefValidation  

   Test organizzazione in esecuzione su: DOMINIO.local  
      Inizio test: LocatorCheck  
         ......................... DOMINIO.local ha superato il test LocatorCheck  
      Inizio test: Intersite  
         ......................... DOMINIO.local ha superato il test Intersite
```

Any help would be really appreciated, I've been working around for almost a month, I'm finishing my degree.  

Maybe a Virtualbox network card configuration setting? It is a Nat Network mode:  

the DC and the other host can ping each other and they can test nslookup correctly.

I'm italian, if you need further translations, tell me

Can someone help me understanding what's going on?

## Answers

_No answers on this thread._
