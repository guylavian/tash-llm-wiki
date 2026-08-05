---
title: "Renaming a Domain Controller Best Practices"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1602388/renaming-a-domain-controller-best-practices
question_id: 1602388
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Renaming a Domain Controller Best Practices

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1602388/renaming-a-domain-controller-best-practices (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 
What are the best practices for renaming a domain controller?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-07*

You can do like this: https://www.dell.com/support/kbdoc/en-us/000226230/windows-server-how-to-properly-rename-an-active-directory-domain-controller#:~:text=At%20an%20elevated%20command%20prompt%2C%20type%20netdom%20computername,name%20was%20added%2C%20type%20netdom%20computername%20%3Coldname%3E%20%2Fenumerate.?msockid=08a6e76781e064813f6af28380a76506

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-28*

To rename a domain controller, Microsoft recommends that you follow these best practices:

-  Ensure that the domain controller is running the latest supported version of Windows Server for your organization, as recommended in the "Securing Domain Controllers Against Attack" article.

-  Make sure that the domain controller is not a read-only domain controller (RODC), as RODCs cannot be renamed.

-  Verify that the domain controller is not a global catalog server, as global catalog servers cannot be renamed.

-  Ensure that the domain controller is not hosting any operations master roles, as these roles cannot be transferred to a renamed domain controller.

-  Verify that the domain controller is not running any applications or services that rely on the computer name, as these applications or services may not function properly after the rename.

-  Follow the procedures outlined in the "Core network components" article to rename the domain controller.

References:

-  Securing Domain Controllers Against Attack

-  Core network components
