---
title: "ADFS Server suddenly starts failing exactly 1 month after a certificate renewal"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1004218/adfs-server-suddenly-starts-failing-exactly-1-mont
question_id: 1004218
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Server suddenly starts failing exactly 1 month after a certificate renewal

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1004218/adfs-server-suddenly-starts-failing-exactly-1-mont (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A month or so ago, my colleague and I did a cert renewal and everything went relatively okay. We have been running smoothly for the past 31 days (since the expiration of the cert)

We got an SSL Certificate from a CA, it was installed into the certificate store of our ADFS server, we binded the cert in IIS and set ADFS to use the new cert (service communications, token-signing, token-decrypting).

(Please note, we aren't adfs experts. we tried our best, but apparently we did something wrong.)

Despite everything working smoothly for the past month, everything has broken now.  

Here are the symptoms:  

-Accessing any of our ADFS endpoints from the browser results in a 503 error  

-The ADFS service is not running and trying to start the service results in an Error 1064.  

When we look in the certificates store, we can see that the new certificate is installed. Here is what is interesting:  

Originally, when we were looking at the errors in the server manager, we were getting pairs of "381 errors" and "102 errors". (These errors showed up after a restart of the server)  

The "381" error reads :  

An error occurred during an attempt to build the certificate chain for configuration certificate identified by thumbprint 'XXXXXXXXXXXD5E85AED342A39EC63523F6AF55AF2'. Possible causes are that the certificate has been revoked or certificate is not within its validity period.  

The following errors occurred while building the certificate chain:  

MSIS2013: A required certificate is not within its validity period when verifying against the current system clock.

The thumbprint that is being referenced is the thumbprint of the OLD cert that had already expired. Naively, we decided to just delete the old certificate from the cert store (maybe then adfs will be forced to use the new cert?... but no)

After deleting the expired cert from the store, we would get pairs of "249 warnings" and "102 errors".  

The 249 warning states:  

The certificate identified by thumbprint 'XXXXXXXXXXXD5E85AED342A39EC63523F6AF55AF2' could not be found in the certificate store. In certificate rollover scenarios, this can potentially cause a failure when the Federation Service is signing or decrypting using this certificate.

So it seems that the ADFS server is TRYING to use the old cert to build the certificate chain, regardless of if it is available or not in the store

We tried to use powershell to force ADFS to use the other certs  

Set-AdfsSslCertificate -Thumprint "<THUMBPRINT_OF_CORRECT_CERT>

but this resulted in getting the following message:  

Get-AdfsCertificate : Could not connect to net.tcp://localhost:1500/policy. The connection attempt lasted for a time  

span of 00:00:02.0499038. TCP error code 10061: No connection could be made because the target machine actively  

refused it 127.0.0.1:1500.  

At line:1 char:1

-  Get-AdfsCertificate

-  ~~~~~~~~~~~~~~~~~~~

-  CategoryInfo : OpenError: (:) [Get-AdfsCertificate], EndpointNotFoundException

-  FullyQualifiedErrorId : Could not connect to net.tcp://localhost:1500/policy. The connection attempt lasted for  

a time span of 00:00:02.0499038. TCP error code 10061: No connection could be made because the target machine acti  

vely refused it 127.0.0.1:1500. ,Microsoft.IdentityServer.Management.Commands.GetCertificateCommand

Thanks in advance for any help. We really are at a loss. It has been working fine for a month (exactly 1 month, if that is a clue to anyone more knowledgeable than myself), but we can't quite pin down the problem

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-19*

Hello there,    

To be honest you must work a lot to find the exact reason for this behavior.  You can start by checking whether the AD FS configuration database is running.    

-If you are using Windows Internal Database (WID) as an AD FS configuration database, open services.msc, and check whether the Windows Internal Database service is running.    

-If you are using the SQL Server service as an AD FS configuration database, open services.msc. Check whether the SQL Server service is running. You can also create a Test.udl file and populate the connection string to test connectivity to Microsoft SQL Server.    

Here are some links to help you out with troubleshooting steps AD FS 2.0 service fails to start https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/adfs-2-service-fails-to-start    

---------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-09-14*

The timing of exactly one month is interesting as it might be an issue with the CRL being expired or something. But that might also be anecdotal.    

Can you check the if the HTTP bindings still use the old one? You can do that with `netsh http show sslcert`. If that's still the old one there, you can update it with `netsh` too: `netsh http add sslcert ipport=<ADFS URL>:443 certhash=<hash of the TLS cert> appid={5d89a20c-beab-4389-9447-324788eb944a}`
