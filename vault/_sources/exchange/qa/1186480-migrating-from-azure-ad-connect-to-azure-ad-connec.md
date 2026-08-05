---
title: "Migrating from Azure AD Connect to Azure AD Connect cloud sync and remove exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186480/migrating-from-azure-ad-connect-to-azure-ad-connec
question_id: 1186480
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migrating from Azure AD Connect to Azure AD Connect cloud sync and remove exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186480/migrating-from-azure-ad-connect-to-azure-ad-connec (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are currently migrating from Azure AD Connect to Cloud Sync.

Does anyone know if it's safe to uninstall old exchange server after this or is it better to follow the guides and shut it down? It's a Exchange 2013 server to easiest way forward would be to uninstall it.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-08*

Hi  @ Mattias Frykstrand ，

If you don't need to use Exchange Server to manage Exchange properties, it is recommended that you can shut down the servers first.

 And run Exchange online for a while to make sure everything is working correctly. Then you can then choose to uninstall the on-premises server.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-05*

Hello Mattias,

If I am understanding you correctly, as long as you do not use your Exchange server for any mail protocols you can safely remove your Exchange server and just use your on-premises Active Directory to manager users (creation, editing, etc).

You will be utilizing Exchange Online for all of your Exchange needs when all of your users exist in Azure Active Directory and if your MX records are being pointed to Office 365.

If this is helpful please accept answer.
