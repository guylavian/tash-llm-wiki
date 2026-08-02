---
title: "Configuring Exchange 2019 for Dedicated Bulk Email Handling without Internal Email Flow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1845498/configuring-exchange-2019-for-dedicated-bulk-email
question_id: 1845498
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Configuring Exchange 2019 for Dedicated Bulk Email Handling without Internal Email Flow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1845498/configuring-exchange-2019-for-dedicated-bulk-email (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a scenario where customer requires specific Exchange servers 2019 (Exchange Server 1 and Exchange Server 2) to be dedicated exclusively to handling bulk emails. These servers should not participate in any internal email flow or act as intermediaries for email routing between other Exchange servers. We are seeking a supported method to configure Exchange 2019 to meet these requirements effectively.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-01*

You can setup your Exchange Server 2019 for handling only bulk emails. For doing this, you can –

Firstly, find out from which specific domains or email addresses bulk emails are coming. Then create a dedicated send connector on these servers for this purpose.

Verify that the servers used for handling bulk emails should not handle regular internal emails.

Setup transport rules to direct bulk emails to these servers.

By these steps, you will have a dedicated server for handling only bulk emails and not participate in any internal email flow.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-29*

Hi,

Welcome to the Microsoft Q&A forum.

You can follow the steps below:

-  Create a dedicated delivery connector for bulk email on Exchange Server 1 and Exchange Server 2. This connector should route the e-mail directly to the Internet or to the target delivery server.

-  To prevent these servers from participating in internal e-mail routing, you need to ensure that no internal send or receive connectors include these servers in their scope. You can view all existing send and receive connectors in the EAC

-  On Exchange Server 1 and Exchange Server 2, configure the Receive connector to accept bulk e-mail only. Go to Mail Flow > Receive Connectors in the EAC and create or modify a connector to restrict the types of email accepted.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.
