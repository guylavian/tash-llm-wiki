---
title: "ExchangeOnline Powershell: cannot update Inbound Connector type"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1622346/exchangeonline-powershell-cannot-update-inbound-co
question_id: 1622346
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
---
# ExchangeOnline Powershell: cannot update Inbound Connector type

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1622346/exchangeonline-powershell-cannot-update-inbound-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I suddenly started receiving an error when tried to update Inbound Connector:

`Set-InboundConnector -Identity "test" -ConnectorType OnPremises`

I receive an error:

`Set-InboundConnector: |Microsoft.Exchange.Management.Tasks.ErrorInboundConnectorConnectorTypeCannotChangeException|Cannot change the connector type of Inbound connector 'test'`

It fails to update only "ConnectorType" for both OnPremises/Partner and only for Inbound Connectors. This problem appeared only a few month ago, before that the update worked. Is it some new change in the Microsoft rules and policies?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-19*

@Mark Babayev  

Do you have any operations before this issue occurred?

Have you tried to use New-InboundConnector command to see if it works?

Based on my knowledge, Exchange Online is ready to send and receive email from the internet right away. You don't need to set up connectors unless you have standalone Exchange Online Protection (EOP) or other specific circumstances that are described in the following article:

使用 Exchange Online 中的连接器配置邮件流 |Microsoft 学习

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
