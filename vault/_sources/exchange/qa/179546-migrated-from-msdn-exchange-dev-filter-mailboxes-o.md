---
title: "[Migrated from MSDN Exchange Dev] Filter Mailboxes on Property 'IsInactiveMailbox'"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/179546/migrated-from-msdn-exchange-dev-filter-mailboxes-o
question_id: 179546
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Filter Mailboxes on Property 'IsInactiveMailbox'

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/179546/migrated-from-msdn-exchange-dev-filter-mailboxes-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/04134158-8e92-4b94-8e83-98213274e42e/filter-mailboxes-on-property-isinactivemailbox?forum=exchangesvrdevelopment  

I am trying to filter all ACTIVE mailboxes into a variable for the purpose of examining outlook rules for data exfiltration.  Currently, all mailboxes are pulled and even with robustcloudcommand I am waiting days for the script to complete.  I have tried:  

Get-Mailbox -ResultSize unlimited -Filter ($_.IsInactiveMailbox -eq '$False')  

Get-Mailbox -ResultSize unlimited  | where {$_.IsInactiveMailbox -eq '$False'}  

Using 'where', I get zero results in the data set.  

Using 'filter', I get 'Cannot bind parameter 'Filter' to the target. Exception setting "Filter": ""False" is not a recognized filterable property. Valid property names are:'  

Then it lists 'isinactivemailbox' as a filterable property.  I found a post to sort mailboxes by last login but that result doesn't account for things like staff tha tis on leave of absence.   

How can I filter and return my active mailboxes only?  Thank you for any help!  :)  

~Eric

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

Correct, at least that is what I thought.  I have a count of 20957 when using the get-exomailbox and the count goes to 35604 when i include -includeinactivemailbox.    

I think I see where my confusion come from.  When we initially did our migration to exchange online we used a service from quadrotech call archive shuttle.  This took mailboxes from a 3rd party archive solution and migrated them.  I never realized it created onmicrosoft accounts for these.  So all of these were showig in my get-mailbox return, but they have no accounts in our AD and they are not using licenses in 365.    

So I'm an idiot lol.  I appreciate your help.  I'll work to remove those onmicrosoft accounts in MSOL and verify they become inactive.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-30*

Thank you that is pulling inactive and active as well.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-30*

We can use the following command to list the inactive mailboxes:    

```
Get-Mailbox -InactiveMailboxOnly | FT DisplayName,PrimarySMTPAddress,WhenSoftDeleted
```

Please check this for more details: View a list of inactive mailboxes.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
