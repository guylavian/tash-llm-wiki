---
title: "Exchange 2019 Microsoft Filtering Management Service won't start"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2005162/exchange-2019-microsoft-filtering-management-servi
question_id: 2005162
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 Microsoft Filtering Management Service won't start

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2005162/exchange-2019-microsoft-filtering-management-servi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Single server Exchange 2019 environment.

My Microsoft Filtering Management Service won't start after a Windows Update.

Upgrading from Cu 13 to Cu 14 did not help.

As a result, transport services won't start. 

What troubleshooting steps are available to get the service to work?

What steps can I do to move the database to a new exchange server?

Can I use my Exchange key to activate the 2nd Exchange server with intent of decommissioning the original?

My last backup was when it was Cu13. Can I restore that backup after upgrading to Cu14 or will AD only accept a backup that is Cu14?

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-26*

Hi,

Welcome to the Microsoft Q&A forum!

Good day! Based on your description, your Microsoft Filtering Management Service won't start after a Windows Update. What usually causes this is a misconfigured A/V solution that doesn't have the proper Exchange exclusions set, and it rips out a needed file.

To solve the problem, please refer to :https://www.exchangeitup.net/2016/10/exchange-2013-filtering-management-and.html

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.
