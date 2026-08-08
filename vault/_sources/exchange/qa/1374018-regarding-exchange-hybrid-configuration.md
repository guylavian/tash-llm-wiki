---
title: "Regarding Exchange hybrid Configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374018/regarding-exchange-hybrid-configuration
question_id: 1374018
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Regarding Exchange hybrid Configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374018/regarding-exchange-hybrid-configuration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am facing an issue with the Exchange Hybrid configuration:

We have an Exchange Server 2013 and have Edge transport server and a Reverse proxy server. we are using Edge server for Incoming and ongoing mail.

Now we are going to configure Exchange Hybrid. 

Is it possible to configure Exchange hybrid if we do not allow the required ports in the Exchange server? if allow all required ports in Edge server.

and If you do not allow the required port in the Exchange server, will we migrate the user's local Exchange to Exchange online?

Or is there any way for Hybrid configuration if we do not allow internet for the Exchange server? can we use any client server for installing Exchange Hybrid Wizard?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-22*

Hi @Md. Mahfuzur Rahman,

Is it possible to configure Exchange hybrid if we do not allow the required ports in the Exchange server? if allow all required ports in Edge server.

It is not possible to establish Exchange hybrid with an Exchange server that is not published to the internet or cannot access Exchange Online endpoints.

For more details please refer to : Hybrid deployment prerequisites

and If you do not allow the required port in the Exchange server, will we migrate the user's local Exchange to Exchange online?

If you don't have a hybrid deployment, you may need to migrate mailboxes with other methods than hybrid migration.

Please refer to this link: Ways to migrate multiple email accounts to Microsoft 365 or Office 365

can we use any client server for installing Exchange Hybrid Wizard?

You need to run the Hybrid Configuration Wizard from a computer running the latest release of a supported version of on-premises Exchange, or from any domain-joined server or workstation capable of establishing remote PowerShell connections to the Client Access Server or Mailbox Server chosen for hybrid configuration.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
