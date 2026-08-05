---
title: "Vulnerabilities on Active Directory Server 2012R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199405/vulnerabilities-on-active-directory-server-2012r2
question_id: 2199405
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Vulnerabilities on Active Directory Server 2012R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199405/vulnerabilities-on-active-directory-server-2012r2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

we have found some vulnerabilities on Active Directory server- Windows Server 2012R2. We troubleshoot to clear following points but not resolved. If you have expertise person in Active Directory domain controller level please let us know. We will pay you if issue resolved. 

Please find the following issue points:-

-  Taken action:- Still result are showing False TLS 1.0 & 1.1 on server after disabled TLS 1.0 & 1.1 on Registry (Using Port:- 636, 3269 & 4706)    Vulnerabilities Desc:- TLS Version 1.0 & 1.1 Protocol Deprecated

-  1)      Vulnerabilities Desc:- SSL Certificate Signed Using Weak Hashing Algorithm (The remote service uses an SSL certificate chain that has been signed using a cryptographically weak hashing algorithm (e.g. MD2, MD4, MD5, or SHA1). These signature algorithms are known to be vulnerable to collision attacks. An attacker can exploit this to generate another certificate with the same digital signature, allowing an attacker to    masquerade as the affected service. Note that this plugin reports all SSL certificate chains signed with SHA-1 that expire after January 1, 2017 as vulnerable. This is in    accordance with Google's gradual sunsetting of the SHA-1 cryptographic hash algorithm. Note that certificates in the chain that are contained in the Nessus CA database (known_CA.inc) have been ignored.)                         Taken Action:- We have tried to AD cetificate protocol tranfer from SHA-1 to SHA-512 but issue not resolved.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-25*

Hi Anil,

I understand your concerns about vulnerabilities on Active Directory servers. Here are some suggestions that may help: 

Issue 1: TLS 1.0 and 1.1 protocols are deprecated Even after disabling TLS 1.0 and 1.1 in the registry, they are still detected on the server. This may be due to some services or applications still using these deprecated protocols. You may want to check your server configuration and make sure all services and applications have been updated to use more secure protocols, such as TLS 1.2 or TLS 1.3.  

Issue 2: SSL certificate signed with a weak hash algorithm You have tried moving the AD certificate protocol from SHA-1 to SHA-512, but the problem persists. This may be due to the fact that the certificates in your chain are still using SHA-1. Make sure all certificates, including root and intermediate certificates, use strong hashing algorithms. Also, make sure your server is configured correctly to use the new certificate chain.  

Please note that these are general recommendations and the exact solutions may vary based on your specific situation. I hope this information is useful to you!  

reference document: 

(1) How to disable TLS 1.0 in Windows Server 2012R2

 https://serverfault.com/questions/1010635/how-to-disable-tls-1-0-in-windows-server-2012r2. 

(2)How to disable TLS 1.0 in Windows 2012 RDP 

https://serverfault.com/questions/733994/how-to-disable-tls-1-0-in-windows-2012-rdp.

(3) SSL certificate signed using weak hash algorithm 

https://answers.microsoft.com/en-us/windows/forum/all/ssl-certificate-signed-using-weak-hashing/cfdc8dd2-d260-4a3b-a078-e52fb48c7859.

Best regards

Qiuyang
