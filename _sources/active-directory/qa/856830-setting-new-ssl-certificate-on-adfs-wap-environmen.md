---
title: "Setting new SSL certificate on ADFS/WAP environment - Get-adfsCertificate shows old service-communication thumbprint"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/856830/setting-new-ssl-certificate-on-adfs-wap-environmen
question_id: 856830
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Setting new SSL certificate on ADFS/WAP environment - Get-adfsCertificate shows old service-communication thumbprint

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/856830/setting-new-ssl-certificate-on-adfs-wap-environmen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm updating the SSL cert on my ADFS/WAP build and unsure if what I'm seeing is typical behaviour. I'm using the following two commands to update the certificate:  

Set-AdfsSslCertificate -Thumbprint 'CKJHASFD87Y98729I4UQHKJHAWFD98ASDF'  

Set-AdfsAlternateTlsClientBinding -Thumbprint 'CKJHASFD87Y98729I4UQHKJHAWFD98ASDF'  

restarting ADFS service  

Running Get-AdfsSslCertificate shows all ports using the new thumbprint  

Running Get-AdfsCertificate show that the Service-Communications certificate thumbprint is still the old one  

I've noted on a blog that Set-AdfsSslCertificate is the one I should be using rather than Set-AdfsCertificate but on looking up the details for Set-AdfsCertificate it shows how I can specify the CertificateType as Service-Communications so I'm unsure if I've just missed that step.   

any advise on the process?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-05-22*

Many thanks for that.   

I ended up just trying a few things as they are VM's so could restore every time something didn't work. Turns out there was a bunch of things which I wasn't aware based on into I was given from someone else at work, various things have forced me to dig deeper into documentation myself so its been a interesting task, after working yesterday afternoon I'm left with 2 ADFS servers and 2 WAP servers, all communicating as expecting, right certificates and up to the latest behaviour level.
