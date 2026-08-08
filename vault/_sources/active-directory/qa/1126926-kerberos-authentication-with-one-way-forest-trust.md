---
title: "Kerberos authentication with one-way forest trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1126926/kerberos-authentication-with-one-way-forest-trust
question_id: 1126926
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Kerberos authentication with one-way forest trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1126926/kerberos-authentication-with-one-way-forest-trust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi together,    

We are trying to achieve the following setup:    

    

-  In "prod.local" domain, we have an IIS application running with domain service account as application pool user    

-  This service account will initialize some DCOM access to Windows Enterprise Root CA in the "dev.local" domain    

-  Due to security constraint, we can only have one-way trust between "prod.local" (trusted domain) and "dev.local" (trusting domain), both are running on Windows Server 2019    

Unfortunately, I cannot make it work with Kerberos authentication, and it always falls back to NTLM authentication then this fails too.    

It runs into errors as below all the time:    

On the CA server side:    

System > Security-Kerberos > 3    

`A Kerberos error message was received:      on logon session       Client Time:       Server Time: 8:52:58.0000 12/7/2022 Z      Error Code: 0x7  KDC_ERR_S_PRINCIPAL_UNKNOWN      Extended Error:       Client Realm:       Client Name:       Server Realm: DEV.LOCAL      Server Name: krbtgt/PROD.LOCAL      Target Name: krbtgt/PROD.LOCAL@DEV.LOCAL      Error Text:       File: 9      Line: 1296      Error Data is in record data.`    

System > LSA (LsaSrv) > 40961    

`The Security System could not establish a secured connection with the server LDAP/prod-ad.prod.local/prod.local@prod.local. No authentication protocol was available.`    

Hints I have already tried:    

-  One-way forest trust with forest-wide authentication.    

-  SPNs settings for the service account in "prod.local" domain:    

`>setspn -l prod\svc-ra     Checking domain DC=prod,DC=local     CN=svc-ra, OU=Service-Accounts, OU=prod, DC=prod, DC=local             HTTP/prod-ra.prod.local           HOST/svc-ra           HOST/svc-ra.prod.local`  

-  Delegation settings in "dev.local" domain:    

`$prodSvcUser = Get-ADUser -Identity svc-ra -Server prod-ad.prod.local     Get-ADComputer -Identity dev-ca | Set-ADComputer -PrincipalsAllowedToDelegateToAccount $prodSvcUser`    

-  It is worth to mention that I also try switching to two-way trust and it works immediately, but it is not an option for us in production.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-14*

Hello TonNguyen-6803,    

Thank you for posting in our TechNet forum.     

You can try to select "Selective Authentication" and make service account has to be explicitly granted "Allowed to Authenticate" right on the CA server.     

For more information about Selective Authentication, please read "Authentication Level" in the link below.    

https://social.technet.microsoft.com/wiki/contents/articles/50969.active-directory-forest-trust-attention-points.aspx    

Similar thread.    

https://social.msdn.microsoft.com/Forums/en-US/37ca22d7-9090-4906-8c5a-f1accf684b5d/windows-authentication-and-multiple-domains?forum=iissecurity    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou    

===============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
