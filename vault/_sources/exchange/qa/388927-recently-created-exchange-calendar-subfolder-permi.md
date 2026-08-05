---
title: "Recently created exchange calendar subfolder permission in mailbox does not update properly (intermittent occurrence)."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/388927/recently-created-exchange-calendar-subfolder-permi
question_id: 388927
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-online-server", "office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Recently created exchange calendar subfolder permission in mailbox does not update properly (intermittent occurrence).

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/388927/recently-created-exchange-calendar-subfolder-permi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Recently created exchange calendar subfolder permission in mailbox does not update properly (intermittent occurrence).   

Steps :   

-  Create the subfolder in the mailbox using EWS Soap API.  

-  Update the permission in the subfolder using EWS Soap API..  

-  For Anonymous and Default user the permission is set to 'None' but for other user permissions are not  getting updated/added though EWS API responding with the 'Success' response code   

-  Check the recently created folder permissions in outlook.   

This behavior is observed intermittently.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-11*

Can you show some of the code your using, in EWS you basically replace the whole DACL in the UpdateFolder request if your getting the current DACL first and just trying to append the entries then that probably you issue. Also how are you testing it ? if Outlook is in Cache mode it can take time for the updates to be shown so you should use something like the EWSEditor https://github.com/dseph/EwsEditor/releases to validate the DACL. You can also enable audit on the Folder itself so you can see when ACL changes are happening and what is making the change in the case some expected process is causing this issue to happen.
