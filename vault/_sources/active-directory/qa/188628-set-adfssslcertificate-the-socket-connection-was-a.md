---
title: "Set-AdfsSslCertificate : The socket connection was aborted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/188628/set-adfssslcertificate-the-socket-connection-was-a
question_id: 188628
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Set-AdfsSslCertificate : The socket connection was aborted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/188628/set-adfssslcertificate-the-socket-connection-was-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I´m trying to install new certificate on my ADFS-server (version: Windows Server 2016 AD FS).  

It,s used to verify athentication to external intranet and was working prior to this certificate installation.

Imported the certificate with all intermediates in local machine/personal/Certificates  

Set read rights on private keys for the ADFS-serviceaccount

Set-AdfsCertificate -CertificateType Service-Communications -Thumbprint ******

Updated fine. New cert is displayed in ADFS Manager.

When I try to bind i get error:  

Set-AdfsSslCertificate -Thumbprint ******  

Set-AdfsSslCertificate : The socket connection was aborted. This could be caused by an error processing your message or a receive timeout being exceeded by the remote host, or an  

underlying network resource issue. Local socket timeout was '00:01:00'.

When I run netsh http show sslcert, everything has the correct thumbprint.

When I run Get-AdfsSslCertificate, all 3 certs show the correct thumbprint.

I ran Run Get-AdfsFarmInformation but we only got one ADFS-node:  

Get-AdfsFarmInformation

CurrentFarmBehavior FarmNodes FarmRoles

```
3   {adfs-server.xxx.xx}                    {UserState}
```

Have searched but i´m lost.

Regards Nils

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-08*

Hi Piaudonn,  

I did a recheck and saw that even though its throwing an error when "Set-AdfsSslCertificate  -Thumbprint **" the certificate got registered.  

I tested with another certificate and that got registered as well.   

The solution to get the Intranet working was probably not related to the ADFS, even though I updated the Token-Signing certificate and sent that to the Website supplier, but to one of their server that needed a restart for updates. Well Well...  

Anyway thanks for your reply and I will check for Updates on our ADFS-server.  

Cheers   

Nils
