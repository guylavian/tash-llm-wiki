---
title: "Exchange Online bulk delete messages specific folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/264195/exchange-online-bulk-delete-messages-specific-fold
question_id: 264195
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online bulk delete messages specific folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/264195/exchange-online-bulk-delete-messages-specific-fold (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Using Office 365 and I have a shared mailbox that is out of control and the sent items need to be bulk deleted based on date range.  The old search-mailbox has been deprecated so I am unable to figure out how to accomplish the command below using powershell v2.  

search-mailbox -identity <usermailbox> -searchquery {received:mm/dd/yyyy..mm/dd/yyyy} -deletecontent

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

I get an error when I try running that:

Search-Mailbox : The term 'Search-Mailbox' is not recognized as the name of a cmdlet, function, script file, or  

operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try  

again.  

At line:1 char:1  

-  Search-Mailbox -identity Office -SearchQuery {Sent:1-Jan-2013..1-Dec- ...  

-  ~~~~~~~~~~~~~~  

-  CategoryInfo : ObjectNotFound: (Search-Mailbox:String) [], CommandNotFoundException  

-  FullyQualifiedErrorId : CommandNotFoundException

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-08*

Ok, Understood. :)  Last I checked, search-mailbox still works in Exchange Online, so even though deprecated, it should still work:    

```
Search-Mailbox -identity  -SearchQuery {Received:1-May-2016..1-Aug-2020} -DeleteContent
```

Make sure you have the correct perms and log first just to ensure it looks right. Consider copying to another mailbox to cover yourself just in case...    

    

https://learn.microsoft.com/en-us/exchange/search-for-and-delete-messages-exchange-2013-help

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

Way too many emails to delete via Outlook or OWA.  I'd prefer to be able to just bulk delete as opposed to creating a new policy. I have 3 other mailboxes that need to be cleaned up as well but different folders within each mailbox.  (I inherited this mess, I would not have let these mailboxes get this far out of control if I had setup this organization).

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

That doesn't work. It only deletes messages 10 at a time.  I have thousands that need to be deleted.
