---
title: "ADFS 5.0 - SSO and ExtendedProtectionTokenCheck Problems"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1110452/adfs-5-0-sso-and-extendedprotectiontokencheck-prob
question_id: 1110452
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 2
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ADFS 5.0 - SSO and ExtendedProtectionTokenCheck Problems

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1110452/adfs-5-0-sso-and-extendedprotectiontokencheck-prob (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,    

we have the following setup    

2 ADFS Server (Windows Server 2019 based)    

-  ADFS Running under GMSA with SPN for http/<farm fqdn>    

-  farm fqnd is not equivalent to machine names    

-  no duplicated spns    

ADFS VIP hangs on an Loadbalancer (we do NOT terminate tls connection aka tls offloading on them!)    

-  mostly followed chapter 9 on this deployment guide https://pdfs.loadbalancer.org/Microsoft_ADFS_Deployment_Guide.pdf     

Clients (Windows 10 20h2 based)    

-  farm fqdn is in local intranet zone    

Terminalservers (Windows Server 2019 based)    

-  farm fqdn is in local intranet zone    

Browser is on all client machines Edge Chromium in the most recent version, so our WiaSupportedUserAgents looks like this    

MSIE 6.0    

MSIE 7.0; Windows NT    

MSIE 8.0    

MSIE 9.0    

MSIE 10.0; Windows NT 6    

Windows NT 6.3; Trident/7.0    

Windows NT 6.3; Win64; x64; Trident/7.0    

Windows NT 6.3; WOW64; Trident/7.0    

Windows NT 6.2; Trident/7.0    

Windows NT 6.2; Win64; x64; Trident/7.0    

Windows NT 6.2; WOW64; Trident/7.0    

Windows NT 6.1; Trident/7.0    

Windows NT 6.1; Win64; x64; Trident/7.0    

Windows NT 6.1; WOW64; Trident/7.0    

Windows NT 10.0; WOW64; Trident/7.0    

MSIPC    

Windows Rights Management Client    

=~Windows\s*NT.Edg.    

Integrated Windows Authentication is enabled    

Ok now this works perfectly fine for our Windows 10 20h2 Clients, Kerberos is used for sso authentication and everything is wokring as expected    

But now there is a problem with our Terminal Servers (RDS Farm), sso just dont work on them, prompts for credentials are just repeatedly presented to the users even if they put in the correct credentials, it is stuck at http 401 and we dont know why. FBA is not be prestented to the user in this scenario. On ADFS we see Event from Logon Category with the ID 4625 at the time of the authentication requests    

```
Fehler beim Anmelden eines Kontos.  
  
Antragsteller:  
 Sicherheits-ID: NULL SID  
 Kontoname: -  
 Kontodomäne: -  
 Anmelde-ID: 0x0  
  
Anmeldetyp: 3  
  
Konto, für das die Anmeldung fehlgeschlagen ist:  
 Sicherheits-ID: NULL SID  
 Kontoname:  
 Kontodomäne:  
  
Fehlerinformationen:  
 Fehlerursache: Bei der Anmeldung ist ein Fehler aufgetreten.  
 Status: 0xC000035B  
 Unterstatus:: 0x0  
  
Prozessinformationen:  
 Aufrufprozess-ID: 0x0  
 Aufrufprozessname: -  
  
Netzwerkinformationen:  
 Arbeitsstationsname: -  
 Quellnetzwerkadresse: -  
 Quellport: -  
  
Detaillierte Authentifizierungsinformationen:  
 Anmeldeprozess: Kerberos  
 Authentifizierungspaket: Kerberos  
 Übertragene Dienste: -  
 Paketname (nur NTLM): -  
 Schlüssellänge: 0
```

Just to mention, any machine included (rds host, windows 10 client, adfs server) have lmcompatibilitylevel 5. So we just did a blind shot and disabled ExtendedProtectionTokenCheck with    

Set-ADFSProperties -ExtendedProtectionTokenCheck none    

on the ADFS Server. This makes things work on the Server 2019 with edge, too....so we are pretty sure there is no basic misconfguration but we dont get why it does not work WITH extendedprotection and only on windows server 2019. There is no ssl offloading before the adfs server, when we strip it down to a single setup (no loadbalancer) the same behaviour is present...    

Any ideas what we need to do to get it run with extended protection enabled(allow)?

## Answers

_No answers on this thread._
