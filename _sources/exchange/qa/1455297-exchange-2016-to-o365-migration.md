---
title: "Exchange 2016 to O365 migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1455297/exchange-2016-to-o365-migration
question_id: 1455297
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange 2016 to O365 migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1455297/exchange-2016-to-o365-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I would like to ask for an advice to migrate the Exchange 2016 to O365

Current Exchange environment:

-Exchange 2016 and 7 SMTP domains(@Acompany.com,@Bcompany.com,@Ccompany.com....)

-500 mailboxes in total for all those 7 SMTP domains

I need to migrate 2 smtp domains to 2 different O365 tenants

@Ccompany.com and @Dcompany.com

Ccompany.com - 10 mailboxes

Dcompany.com - 140 mailboxes

All these companies have  local AD, as for mail they use other AD in the Exchange location, so it is not SSO (single sign on).Two accounts.One for local domain and one for Exchange authentication.

Given these facts, I think that hybrid migration is out of the question.

IMAP migration is also out of the question for many reasons in my opinion.

The only solution  IMHO is cutover migration.

Does the cutover migration of these two smtp domains affect the other 5 domains that remain on the Exchange server?

It is clear to me that with cutover migration there will be no SSO, i.e. there will be two separate user accounts (onprem and o365 accounts)

but the situation is similar now, since users log on to computers in local domain and access the mailbox on another AD.

I found this "how to" for cutover migration

https://srodonoffice365.files.wordpress.com/2016/04/cutover-migration-guide-step-by-step1.pdf

One of the sentences in this tutorial:

"Unlike an Exchange staged migration, a cutover migration moves your entire on-premises Exchange

organization to Office 365 over a few days."

I do not want to migrate the entire exchange organization, but only 2 SMTP domains

Does the cutover migration of these two smtp domains affect the other 5 domains that remain on the Exchange server?

Any advice for this project?Is cutover migration best best solution for this project?

Thanks

## Answers

_No answers on this thread._
