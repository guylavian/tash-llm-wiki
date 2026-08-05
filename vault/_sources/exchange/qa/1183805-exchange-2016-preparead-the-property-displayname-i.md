---
title: "Exchange 2016 PrepareAD / The property 'DisplayName' is on a read-only object and can't be modified."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1183805/exchange-2016-preparead-the-property-displayname-i
question_id: 1183805
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 PrepareAD / The property 'DisplayName' is on a read-only object and can't be modified.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1183805/exchange-2016-preparead-the-property-displayname-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trying to run the prepareAD on a new server to install Exchange 2016 in order to replace 2010 hybrid server and it seems the Set-OrganizationConfig is a read-only object but I should be able to set different variables but it is not allowing me to. Any thoughts or has anyone seen this before?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-24*

ExchangeSetup.log this is the log

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-24*

Hi @Joe Hoffman,

Thank you for posting in our forum, let me confirm some information with you first.

What’s the command you used to prepare AD? Have you preparedSchema before?

If not, follow the steps given in the documentation to prepare Active Directory for the new server.

Then please provide the corresponding error report generated during the running process so that we can better troubleshoot the issue.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
