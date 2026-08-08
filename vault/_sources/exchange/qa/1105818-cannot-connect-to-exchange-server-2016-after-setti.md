---
title: "Cannot connect to Exchange Server (2016) after setting ASA credentials"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1105818/cannot-connect-to-exchange-server-2016-after-setti
question_id: 1105818
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Cannot connect to Exchange Server (2016) after setting ASA credentials

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1105818/cannot-connect-to-exchange-server-2016-after-setti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,    

I set up our Exchange Server 2016 for Kerberos authentification using the article:    

https://learn.microsoft.com/en-us/exchange/architecture/client-access/kerberos-auth-for-load-balanced-client-access?view=exchserver-2016#single-active-directory-site    

After this setup, I was not able anymore, to connect to our two Exchange Severs 2016 (on Windows-Server 2016) with PowerShell.    

"Enter-PSSession : Connecting to remote server exch-srv01...com failed with the following error message :    

WinRM cannot complete the operation [...]"    

Do you have any idea how to correct this?    

Thank you and best regards,    

Michael

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-28*

What happens when you connect to the SPN shared name FQDN  instead of the server FQDN?     

I ask because the kerberos ticket is generated based on the shared name:    

https://learn.microsoft.com/en-us/exchange/architecture/client-access/kerberos-auth-for-load-balanced-client-access?view=exchserver-2019

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-28*

Hi @Masuch, Michael       

Please follow this guide and let me know please    

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/winrm-cannot-process-request    

Cheers!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-27*

Thank you @risolis   for your fast answer.    

The Exchange Management Shell (EMS) does work just fine (local) and the WinRm service as well as the command `winrm quickconfig` just stated all fine.    

I realy think, that this behaivor has something to do with the ASA implementation I performed when following this manual:    

https://learn.microsoft.com/en-us/exchange/architecture/client-access/kerberos-auth-for-load-balanced-client-access?view=exchserver-2016#single-active-directory-site    

Best,    

Michael

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-27*

Hello @Masuch, Michael       

Thank you for sharing this question on this community space.    

I have gone though the case scenario description and here are my 2 cents about it...    

https://www.stellarinfo.com/article/fix-the-error-winrm-cannot-complete-operation.php    

I hope you can find this useful to overcome your concern.    

Looking forward to your feedback,    

Cheers,    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
