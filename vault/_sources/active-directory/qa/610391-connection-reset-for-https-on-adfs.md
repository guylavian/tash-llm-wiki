---
title: "Connection reset for HTTPS on ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/610391/connection-reset-for-https-on-adfs
question_id: 610391
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Connection reset for HTTPS on ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/610391/connection-reset-for-https-on-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have set up a windows server in virtual box with host only network as a labenvironment. I have a problem accessing HTTPS from the host only network.   

I have set up a domain controller and ADFS on a Windows server 2019 using a self signed certificate for ADFS.  

Some tests I have done to try to isolate the problem. Im testing against the metadata url /FederationMetadata/2007-06/FederationMetadata.xml  

-  If I open IE in the VM and go to the metadata endpoint on localhost , I get the message "This site is not secure", but can bypass the warning and get the metadata.  

-  If I go to the host only interface IP, IE just shows a message saying "Can’t connect securely to this page" and it is not possible to bypass.  

-  If I do curl from the host to the host only IP address with -k flag towards port 443 I get connection reset.  

-  If I do curl against port 80 on the host only IP I get a 404 page as expected.  

-  Ping works fine from the host.  

-  Telnet from host to 443 connects  

I have disabled the windows firewall.  

the certificate was generated using this powershell  

```
$selfSignedCert = New-SelfSignedCertificateEx `
    -Subject "CN=adfs.samlsecurity.com" `
    -ProviderName "Microsoft Enhanced RSA and AES Cryptographic Provider" `
    -KeyLength 2048 -FriendlyName 'OAFED SelfSigned' -SignatureAlgorithm sha256 `
    -EKU "Server Authentication", "Client authentication" `
    -KeyUsage "KeyEncipherment, DigitalSignature" `
    -Exportable -StoreLocation "LocalMachine"
```

So there seem to be connectivity as I can get the HTTP 404 page, but for some reason I get connection refused from 443.   

I guessing there is something wrong with the TLS setup on windows, but I can't figure out what.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-04*

ADFS is using the SNI extension of SNI and listen only of specific hosntames. You cannot establish the TLS tunnel if hostname isn't matching the known FQDN of the ADFS farm (the one from the ADFS service properties).  

You can play with using NETSH to show the current listener "netsh http show sslcert" or even add new (or a generic or "fallback" listener): "netsh http add sslcert ..."
