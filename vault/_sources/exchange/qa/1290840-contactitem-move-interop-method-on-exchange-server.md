---
title: "ContactItem.Move Interop method on Exchange server triggers hard deletion of contact in Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1290840/contactitem-move-interop-method-on-exchange-server
question_id: 1290840
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "developer-technologies-dotnet-other-l1", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# ContactItem.Move Interop method on Exchange server triggers hard deletion of contact in Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1290840/contactitem-move-interop-method-on-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a simple tool built in C# which we use to identify duplicated contacts in Outlook and move them to a subfolder. The tool worked perfectly fine until January 2023, but since then every time we use the tool, the contacts which are moved to the subfolder disappear from there after some seconds (or instantly, if the Use Cached Exchange Mode is disabled) and can only be found doubled in Recover Deleted Items in Outlook.

The code used to move the contacts is attached: Form.txt

Do you have any idea why the contacts are hard deleted after being moved to the subfolder?

Since this happens to all mailboxes in our tenant, we've also checked the log files from the Exchange Server, and there we were able to see that the server receives the command to Soft Delete the contacts, however they are in fact hard deleted since we don't find them in the Deleted Items, but only in Recover Deleted Items, and doubled (two times).

## Answers

_No answers on this thread._
