---
title: "Do Shared Mailboxes in Exchange Server On-Premises Require CALs?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2085793/do-shared-mailboxes-in-exchange-server-on-premises
question_id: 2085793
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Do Shared Mailboxes in Exchange Server On-Premises Require CALs?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2085793/do-shared-mailboxes-in-exchange-server-on-premises (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,

I have a specific question about on-premises Exchange Server (Exchange 2019). I understand that users and devices accessing the server generally require Client Access Licenses (CALs). However, I want to clarify how this applies to shared mailboxes in an on-premises environment.

Do shared mailboxes in Exchange Server on-premises need their own CALs, or are they covered as long as the users who access them have their own CALs? Also, are there any specific situations where a shared mailbox might require additional licensing (e.g., for compliance features like archiving)?

Thanks for your assistance!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-04*

There is no need for separate CALs for shared mailbox, if users have their own CALs. For archiving and compliance needs, you will need an additional licensing for specific features.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-02*

Hi,@Kocot K

In an on-premises Exchange Server environment, such as Exchange 2019, shared mailboxes don't require their own Client Access License (CAL). However, any user accessing a shared mailbox must have their own CAL. This means that as long as all users have the appropriate licenses, the shared mailbox itself does not require a separate CAL.

If you're using advanced compliance features such as archiving, legal hold, or data loss prevention (DLP), additional licenses may be required for both the shared mailbox and the users who access it. For example, these advanced features may require an Enterprise CAL (ECAL).

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
