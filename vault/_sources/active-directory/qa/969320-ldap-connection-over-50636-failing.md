---
title: "LDAP Connection over 50636 Failing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/969320/ldap-connection-over-50636-failing
question_id: 969320
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# LDAP Connection over 50636 Failing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/969320/ldap-connection-over-50636-failing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trying to access LDAP Instance via a custom port (SSL 50636). Below steps i have done so far as per "https://techcommunity.microsoft.com/t5/sql-server-blog/step-by-step-guide-to-setup-ldaps-on-windows-server/ba-p/385362" except the Certificate since we have another global tool for Certificate Management.     

-  New 2019 domain member server, installed LDAP instance with 50389 on non-ssl port & 50636 as SSL port.     

-  Able to query LDAP using ldp.exe on port 50389.    

-  To query on SSL port, installed SSLcertificate with Private key & Client Auth, Server Auth, KDC Auth & Smartcard Login as enhanced key usage under Certificates\LocalComputer & Certificates\service account.. Also, provided permissions for Network Service on the Certificate Private keys.    

Below is one event i am seeing under Applications & Services logs     

LDAP over Secure Sockets Layer (SSL) will be unavailable at this time because the server was unable to obtain a certificate.     

Additional Data     

Error value:    

8009030e No credentials are available in the security package    

Not sure what is missing, please help. Thanks in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-19*

Hi    

You can use the details in this post to verify that the certificate is installed correctly, while the post talks about DCs, the same is true for DS LDS, for the certificate store look the under the service name of the LDS instance.    

https://nettools.net/howto-troubleshoot-ad-ldaps-connection-issues/    

Gary.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-08-16*

Hi,    

As you have installed the CS role on the LDAP server, can you check if you can access the IIS website with port 443?    

Check if you have binded the Certificate to the IIS as sometimes it requires binding on the IIS.    

Also I would recommend you to try this URL and check the FQDN of the Domain in the certificate is matching your domain name.    

===    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
