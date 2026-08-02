---
title: "Renew public ADFS SSL Certificate - Server 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/645964/renew-public-adfs-ssl-certificate-server-2012-r2
question_id: 645964
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Renew public ADFS SSL Certificate - Server 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/645964/renew-public-adfs-ssl-certificate-server-2012-r2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

 I'm planning on renewing our public SSL certificate (service communications) on our 2012 R2 ADFS & WAP arrays. For O365, I believe the service will automatically acknowledge the new public SSL certificate once installed. Do I need to prepare other federation resource partners such as ServiceNow about the certificate change?   

Will there be much downtime?  

Here are the steps I'm planning:  

- 	Install the new ADFS certificate in the local computer store of both ADFS servers and both WAP servers   

- 	Run the following command on each ADFS server (use appropriate certificate thumbprint):  

a.	 “Set-AdfsSslCertificate –Thumbprint <thumbprint>” (this will apply private key read permissions – see link below).  

- 	Check bindings on ADFS servers with:  

a.	 “netsh http show sslcert”.  

- 	On the primary ADFS server run:  

a.	 “Set-AdfsCertificate -CertificateType Service-Communications –Thumbprint <thumbprint>”  

- 	On the WAP servers, run:  

a.	 “Set-WebApplicationProxySslCertificate -Thumbprint <thumbprint>”  

- 	On the ADFS servers ensuring that the HTTPS bindings are correct. Remove the old default binding IF NEEDED:  

a.	netsh http delete sslcert ipport=0.0.0.0:443  

b.	netsh http add sslcert ipport=0.0.0.0:443 certhash=<hash> appid={5d89a20c-beab-4389-9447-324788eb944a} *  

https://blog.rmilne.ca/2016/03/21/updating-windows-server-2012-r2-adfs-ssl-and-service-certificates/  

Thanks in advance

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-30*

Federation partners are not affected by the TLS certificate change. As long as the new certificate is also trusted by the clients, they will be able to access the service.   

Federation partners are affected by the Token Signing certificate (and potentially the Token Decrypting certificate) change.
