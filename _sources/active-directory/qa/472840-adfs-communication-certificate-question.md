---
title: "ADFS Communication Certificate Question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/472840/adfs-communication-certificate-question
question_id: 472840
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Communication Certificate Question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/472840/adfs-communication-certificate-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

The Communication certificate on our ADFS (server 2012 R2) has been expired for 2 years and does not appear to be negatively impacted at all by it. I still want to change it. Most docs say that the IIS Certificate and the Communication Certificate should be the same Cert. In our environment we use an alias DNS for convenience so the binding is not our server FQDN. Its a truncated DNS name. The IIS Cert is a valid wildcard for the truncated name. Example  

FQDN Domain name: <adfs-servername>.part1.part2.part3.com  

Truncated alias name: adfs.part2.part3.com  

Question. Should I create a self signed subordinate cert for the communication cert using the FQDN or can I use the same wildcard cert so they match?    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-19*

The IIs Service is on and the SSL Cert that is in the bindings is Valid. It matches the DNS alias I mentioned and when I use the ADFS test url it returns a valid Cert and login window.  

If I use the FQDN (expired Sevice Communication cert) url, It also returns a proper Login page but with the expired Cert Warning. Somehow, this server has been configure to use IIS for ADFS alias name, I believe.   

The URL's are not the same. The Certs are not the same.  

Test URL:  

 https://<ADFS FQDN>/adfs/ls/IdpInitiatedSignon.aspx

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-19*

ADFS on Windows Server 2012 R2 does not use IIS.    

If you have IIS installed in the same server with expired certificates, it is possible that there are not the one used by ADFS.    

To know the current certificates used by ADFS, run the following command on the ADFS server:    

```
Get-AdfsCertificate -CertificateType Service-Communications
```

It should be the same you see in the output of this other command that is telling you what certificate is used in the HTTP/TLS binding setting of your server:    

```
Get-AdfsSslCertificate
```

Instructions to update the TLS certificate can be found here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/manage-ssl-certificates-ad-fs-wap
