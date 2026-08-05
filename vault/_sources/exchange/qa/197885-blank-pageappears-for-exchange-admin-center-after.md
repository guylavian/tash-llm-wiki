---
title: "Blank Pageappears for Exchange Admin Center after install"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197885/blank-pageappears-for-exchange-admin-center-after
question_id: 197885
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Blank Pageappears for Exchange Admin Center after install

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197885/blank-pageappears-for-exchange-admin-center-after (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

OS: Windows Server 2016  

Domain: Windows Server 2016  

Exchange Version: Exchange 2016  

Issue: Exchange Admin Tools do not open after install  

Troubleshooting: I have checked all the services they look good.  I have added my Server admins group to the Server Management Group In the Microsoft Exchange Security Groups.  I tried this tech note.  https://support.microsoft.com/en-us/help/2971270/blank-page-after-login-exchange-eac-owa-ecp. None of it worked.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-17*

Well the answer was the C; Drive was full even though I installed in on the E: Drive.  I also had to upgrade the browser to Chromium also.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-15*

Hi @Kit Eizenga  

What's the CU version of your Exchange server 2016?

Is this the newly installed Exchange 2016, or you just updated it to the later CU?

And after the installation, you are not able to open the EAC which shows blank page. Have you checked the application log to get any related error Eventid? You could share them here for further troubleshooting.

Which url are you using to access the EAC? What about using this link to check the result again? https://localhost/ecp

Please use the command to check the configuration of ECP virtual directory

```
Get-EcpVirtualDirectory | FL
```

In addition, you could also try below methods to resolve this issue.

1.Recycle the MSExchangeECPAppPool in IIS manager. Application Pools > MSExchangeECPAppPool > Recycle.

2.Re-running the UpdateCas.ps1 and UpdateConfigFiles.ps1. C:\Program Files\Microsoft\Exchange Server\V15\Bin

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
