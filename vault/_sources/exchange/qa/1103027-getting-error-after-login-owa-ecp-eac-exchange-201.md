---
title: "Getting Error after login OWA/ECP/EAC Exchange 2016 hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1103027/getting-error-after-login-owa-ecp-eac-exchange-201
question_id: 1103027
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Getting Error after login OWA/ECP/EAC Exchange 2016 hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1103027/getting-error-after-login-owa-ecp-eac-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi,    

I getting a problem after login in to owa/ecp/eac. previously we has update the exchange 2016 to KB5004779. try to revert the update but the same error happens again. try check cert there are no changes.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-28*

It is also possible to experience HTTP ERROR 500 after logging in to EAC or ECP due to incorrect or outdated server configuration after the server upgrade or update.    

To resolve this error, run UpdateConfigFiles.ps1 and UpdateCAS.ps1 PowerShell scripts located in the Exchange Server Bin directory (C:/Program Files/Microsoft/Exchange Server/V15/Bin/).    

Follow these steps to execute these PowerShell scripts:    

To navigate the Exchange 'Bin' directory, open PowerShell as an administrator and use the 'cd' command. As an example,    

"C:/Program Files/Microsoft/Exchange Server/V15/Bin."    

Run the following PowerShell scripts to fix the configuration issues.    

The UpdateConfigFiles.ps1 script    

.\UpdateCAS.ps1    

It may take a while for this to finish. Check if the HTTP 500 error has been resolved and ECP/EAC is accessible after restarting the server.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-25*

It looks like it's listed as a known issue on the Exchange blog, which I didn't see the first time    

https://techcommunity.microsoft.com/t5/exchange-team-blog/released-november-2021-exchange-server-security-updates/ba-p/2933169/highlight/true/page/3"    

"11/11: Added a known issue with OWA redirect for hybrid customers."

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-25*

Hi @hafizuddin shahipurullah  ,    

Since the limited information on your issue, we want to confirm something with you for further troubleshooting:    

Could you see below events information is recorded in the Application log? Event ID: 2004 or Event ID: 1309?    

If you can see above event IDs in application log, it indicates that the Exchange server Auth certificate that's used for OAuth signing is missing from the Exchange server. You could run the following command to check whether the certificate is missing:    

```
Get-ExchangeCertificate (Get-AuthConfig).CurrentCertificateThumbprint
```

To fix the issue, follow the guidance and check if this workaround works for you.    

If an Answer is helpful, please click "Accept Answer" and upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
