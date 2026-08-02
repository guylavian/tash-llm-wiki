---
title: "Upgrading MS exchange 2016 cu15 to cu18/19"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/236746/upgrading-ms-exchange-2016-cu15-to-cu18-19
question_id: 236746
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Upgrading MS exchange 2016 cu15 to cu18/19

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/236746/upgrading-ms-exchange-2016-cu15-to-cu18-19 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am trying to upgrade my MS exchange 2016 cu15 to cu18/19 via gui.  

Gui window is disappearing in few moments

in log i can see this:

[ERROR] The system cannot find the file specified. (Exception from HRESULT: 0x80070002)  

[Unable to load assembly from file C:\Windows\Temp\ExchangeSetup\Microsoft.Exchange.Setup.GUI.dll using setup arguments /sourcedir:E:./mode:Upgrade, source directory is E:\, target directory is C:\Windows\Temp\ExchangeSetup and Exchange is installed True.

any idea?  

thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

Hi @Martin      

First make sure you have Schema Admins, Enterprise admins, Domain admins and organization management membership.    

And the steps to update the Exchange to latest CU version is list here in the official document: Upgrade Exchange to the latest Cumulative Update. Which introduces both ways using GUI or powershell.    

You could also refer to this thread which discussed the similar issue as yours: Re-Running Exchange 2016 CU13 Installer    

Waiting for your update here about this issue, good luck!    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-19*

Thank you,  

i will test it next week.  

Martin

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-19*

It's a good idea to start the cu upgrade in command line  

```
Setup.exe /mode:upgrade /targetdir:"C:\Program Files\Microsoft\Exchange Server"  /IAcceptExchangeServerLicenseTerms
```
