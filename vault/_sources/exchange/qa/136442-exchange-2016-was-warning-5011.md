---
title: "Exchange 2016 WAS Warning 5011"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/136442/exchange-2016-was-warning-5011
question_id: 136442
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 WAS Warning 5011

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/136442/exchange-2016-was-warning-5011 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I am running Exchange 2016 CU18.  It was running well till few days ago when I started getting WAS Warning Log on one of my Exchange Server (part of DAG).  It logged apppool error "A process serving application pool "MSExchangeServicesAppPool' suffered a fatal communication error with the Windows Process Activation Service. The process id was '24704'.  The data field contains the error number.    

May I know what is going on and is there any solution to it?  Thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-26*

Hi @ShannLim-3692,  

 It was running well till few days ago when I started getting WAS Warning Log on one of my Exchange Server (part of DAG).  

Was there any change made to your EXCHANGE environment before the warning logs appeared?   

Do you mean currently this is only affecting ONE of the DAG members?  

Please have a check to see if this Exchange server is experiencing high CPU usage.  

Moreover, it's suggested to try performing an IIS reset and check if there would be any improvement. To do this, you can open an elevated Command Prompt and run the command below:  

```
iisreset /noforce
```

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-23*

Check if 'Exchange Web Services Managed API 2.2' is installed in the server. You may verify it from the control panel>Programs. Install the package if found missing there
