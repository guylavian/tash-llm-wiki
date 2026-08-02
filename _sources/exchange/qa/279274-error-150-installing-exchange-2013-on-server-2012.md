---
title: "Error 150 installing Exchange 2013 on Server 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/279274/error-150-installing-exchange-2013-on-server-2012
question_id: 279274
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Error 150 installing Exchange 2013 on Server 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/279274/error-150-installing-exchange-2013-on-server-2012 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all- I am trying to install Exchange 2013 onto my Server 2012 R2 and keep running into a problem where the group check for Organization Management is not able to work due to a DC not being operational currently.  My primary DC is located on my local server stack and it is replicating to another DC at another site (currently down). How do I avoid having the primary DC forward this group rights access check to another DC? Is this a replication issue that I need to disable? If so, how do I do that? Thank you in advance!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-02-25*

Get that DC up or remove it  :)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

Thank you Andy and YukiSun for your help, but unfortunately I still ran into problems.   

I ran the switch like Andy directed and was able to only use the primary GC DC on my local stack.  This local DC still reached out to the other DC on the distant site.  

The specific problems received were that the schema was not up to date, setup detected problem while validating active directory, no DC available at other site to validate Organization Management group access.  This other site DC is currently down and I am looking to avoid having this local DC reach out to the other site.  Not sure if it would create replication problems in doing this or if I should wait until the distant site comes online.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-19*

Hi @Ryan Webb  ,    

To add to what suggested by Andy, here's the official link dedicated for Exchange 2013 which indicates the " /DomainController:<FQDN of domain controller>" works in Exchange 2013:    

Install Exchange 2013 using unattended mode    

The following is a sample command for your reference:    

```
Setup.exe /mode:Install /role:ClientAccess,Mailbox /DomainController:DC01 /IAcceptExchangeServerLicenseTerms
```

Besides, in case it still doesn't work, you can remove any sensitive data involved and then share the detailed error message for further research. It's also suggested to have a look at the setup log file which by default located at <system drive>\ExchangeSetupLogs\ExchangeSetup.log and see if there would be any clues. ac    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
