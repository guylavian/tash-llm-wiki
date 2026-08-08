---
title: "How to fix exchange ECP pop-up page is unresponsive?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2124069/how-to-fix-exchange-ecp-pop-up-page-is-unresponsiv
question_id: 2124069
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to fix exchange ECP pop-up page is unresponsive?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2124069/how-to-fix-exchange-ecp-pop-up-page-is-unresponsiv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to edit mailbox properties in the Exchange Admin Center (EAC) on exchange server 2016. However, the fields and buttons on the pop-up page (like "general," "mailbox usage," etc.) are not responsive. I have tried on different browsers with different versions on multiple computers.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-29*

From your description, can I understand that when you click on the option in the left navigation bar, the corresponding interface does not pop up on the right side?

There is still some information to confirm for you:

-  When you select different options in the left navigation bar, does the triangle icon move to the front of the corresponding option?

-  If the previous operation is OK, it means you can enter the function option. Then is there nothing displayed on the right (blank page) or other error messages?

-  Did the problem occur suddenly? Have you installed any version updates before?

-  Does the problem exist in all mailboxes or only in certain specific mailboxes?

As a preliminary investigation, you can try the following suggestions:

-  Give priority to using Power Shell to change mailbox properties.

-  Make sure the account you are using has the administrative permissions required to change mailbox properties. Try to re-grant administrative permissions.

-  Try to access EAC in InPrivate (Edge) or Incognito (Chrome) mode, which helps to rule out problems related to cookies and cache files.

-  Restart services related to exchange, especially the World Wide Web Publishing Service, to refresh the web interface.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
