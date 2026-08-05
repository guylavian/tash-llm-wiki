---
title: "In Exchange Admin Center i see not all mailboxes and i have no filters active, in incognito i see all"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2152411/in-exchange-admin-center-i-see-not-all-mailboxes-a
question_id: 2152411
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# In Exchange Admin Center i see not all mailboxes and i have no filters active, in incognito i see all

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2152411/in-exchange-admin-center-i-see-not-all-mailboxes-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear community.

When i go to admin.microsoft.com and then to Exchange - Mailboxes i do not see all mailboxes.  

I see mailboxes from user with the letters from A to Z but in between there are user mailboxes missing.  

I have 7 users where lastname starts with "F but i see only two mailboxes. But then i see a user that starts with "g" as lastname in my list too. I alwasy see 40 items in that list and there is no second page but i should see 168 mailboxes when i use the filter "all mailboxes"  

I have this issue when i use EDGE and Chrome browser, when i use the incognito mode with these two browsers i see all mailboxes again.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-30*

Hi @Tellenbach Stefan  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you are experiencing display issues in the Exchange admin center. Here are a few steps you can try to resolve this issue:

-  Sometimes cached data can cause display issues. Clearing the cache in Edge and Chrome may help.

-  Make sure you have the permissions required to view all mailboxes. Sometimes, missing permissions may cause some mailboxes to be hidden.

-  You can use PowerShell to verify that the mailbox exists and is configured correctly. Connect to Exchange Online PowerShell and run the following command:

```
Get-Mailbox -ResultSize Unlimited | Where-Object { $_.LastName -like "F*" }
```

This will list all mailboxes with a last name that starts with "F".

-  Disable any browser extensions that may interfere with the display of the Exchange admin center.

-  Since you mentioned that Incognito mode works, it may be worth comparing the settings and extensions between normal mode and Incognito mode to determine any differences.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
