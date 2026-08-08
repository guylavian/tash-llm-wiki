---
title: "Exchange server custom settings related"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/317503/exchange-server-custom-settings-related
question_id: 317503
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange server custom settings related

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/317503/exchange-server-custom-settings-related (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi.  

exchange You want to upgrade your on-premises 2013 cu. (cu8 to cu23)  

When I upgrade, the custom settings are overwritten. What do I need to back up?  

What I backed up were IIS backup and the FrontEnd folder in the exchange installation directory, and the Bin folder.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-17*

Hi @ititmem  ,     

To backup the customization files before upgrading Exchange, please check the file locations listed below, make a backup for the files you have customized:    

-  %ExchangeInstallPath%Bin\MSExchangeMailboxReplication.exe.config	     

-  %ExchangeInstallPath%FrontEnd\HttpProxy\Sync\web.config    

-  %ExchangeInstallPath%ClientAccess\Sync\web.config	     

-  %ExchangeInstallPath%FrontEnd\HttpProxy\ews\web.config    

-  %ExchangeInstallPath%ClientAccess\exchweb\ews\web.config	     

-  %ExchangeInstallPath%FrontEnd\HttpProxy\owa\web.config    

-  %ExchangeInstallPath%ClientAccess\Owa\web.config    

In addition, it's recommended to see the Upgrade Exchange to the latest Cumulative Update article for the other best practices when installing Exchange Cumulative Updates.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
