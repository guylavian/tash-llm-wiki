---
title: "Kerberos errors remain after November 2022 update fix"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1095095/kerberos-errors-remain-after-november-2022-update
question_id: 1095095
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Kerberos errors remain after November 2022 update fix

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1095095/kerberos-errors-remain-after-november-2022-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I still get errors in Windows log after installing November update for Server 2016 KB5019964 and its fix KB5021654.    

Before I have installed the fix I got errors with event ID 14 and 27. Now I just get errors with event ID 27:    

While processing a TGS request for the target server XXXX/XXXX:53480, the account XXXX@xxxxxxxxxxxxx   did not have a suitable key for generating a Kerberos ticket (the missing key has an ID of 9). The requested etypes were 23  3  1. The accounts available etypes were 23  18  17.    

Any ideas how to fix it? Anyone else getting this?    

Best regards

## Answer (community) — community member

*upvotes: 2 · updated: 2022-11-21*

Thanks for your answers. RC4 was disabled deliberately for hardening reasons. It's a common recommendation as far as I know.    

The ApplyDefaultDomainPolicy regkey seems to disable applying the Default Domain policy, I want to keep applying.    

Do I need to wait for a fix fix from Microsoft? ;)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-31*

Im also having "login issue:  The login is from untrusted domain and cannot be used with Windows authentication" after installing January 2023 patch on all DCs. Note this happens when trying to connect to old server 2003 that hosts SQL server.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-28*

Hello,     

I am unable to install KB5021654 through a problem with Windows Update.     

Can I apply     

reg add HKLM\System\currentcontrolset\services\kdc /t REG_DWORD /v ApplyDefaultDomainPolicy /d 0 /f     

to solve this issue temporary? Do I have to deinstall KB´s before doing so?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-21*

Try remove the OOB Patch     

Apply :     

reg add HKLM\System\currentcontrolset\services\kdc /t REG_DWORD /v ApplyDefaultDomainPolicy /d 0 /f     

.... to all DC's

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-18*

It seems RC4 encryption is missing on the account in mention. Possibly AD domain has been hardened to use AES encryption. (msDS-SupportedEncryptionTypes value 24 and below)    

RC4 is still a valid encryption method for Kerberos.    

If you change on the AD object in question the msDS-SupportedEncryptionTypes value to 28 should do the trick.
