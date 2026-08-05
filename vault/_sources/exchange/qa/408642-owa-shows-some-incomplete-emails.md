---
title: "OWA shows some incomplete emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/408642/owa-shows-some-incomplete-emails
question_id: 408642
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# OWA shows some incomplete emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/408642/owa-shows-some-incomplete-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Some of the emails we receive are fully visible in Outlook 2016, but in OWA they are cut off. That is, the email is received on the server without problem, but OWA only shows the first lines. However, that same email, if you open it in Outlook 2016, you can see it without any problem.  

What can be the cause?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-26*

Hi @Jose Antonio Herrera Milanca   ,    

The issue, is it happening on multiple users or only on one or two specific users?    

I think you can try the following methods:    

-  Change a web browser or remove cache and cookies.    

-  Try migrating the problematic users to another database.    

-  Disable the accounts and re-enable them with Connect a mailbox(EAC>recipients>mailboxes>more options>Disable and Connect a mailbox)    

-  Export the users' mailboxes to .pst files, create new mailboxes for them, and import the files to these mailboxes.    

Besides, you could also try re-installing the browser or login from another place.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
