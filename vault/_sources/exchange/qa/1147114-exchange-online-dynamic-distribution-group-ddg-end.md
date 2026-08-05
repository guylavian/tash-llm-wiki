---
title: "Exchange Online Dynamic Distribution Group (DDG) - End-user seeing seeing who message was sent to"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1147114/exchange-online-dynamic-distribution-group-ddg-end
question_id: 1147114
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online Dynamic Distribution Group (DDG) - End-user seeing seeing who message was sent to

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1147114/exchange-online-dynamic-distribution-group-ddg-end (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there any way that an end user sending email to DDG can see who all the email was actually sent to?  We have a lot of user movement and we'd like to use DDGs, but understandably, our very novice end users (admins, clerks, etc.) would like some ability to see the list of recipients so they can confirm the message actually went to everyone who they intended.  Without this ability, the end user is working blind when sending to a DDG.  They know who the email should've gone to, if the AD attributes and filters were correct, but no way to know for sure who it went to.  The end users aren't going to run Exchange PowerShell commands and they shouldn't have to use read receipts.  Thank you!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-02*

Hi @Anonymous   ，    

According to my test, I can open and view the members of distribution group in GAL .However , When I opened the Dynamic Distribution Group in the same way, there was nothing.    

    

In addition, I found the relevant thread for your reference: How to view members of Dynamic Distribution Group via Outlook client? (microsoft.com)    

Also, according to this link, you can only view the member list of DDL through the EMS.     

    

Hope this helps you!    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-30*

After adding the group on the To field, expand and display the members by clicking the + icon.  Or search the group in the Address Book, double click to add to the To line, then from the To field double click on the group again to bring up it's properties which will list all the members.    

    

----------    

Please accept as an answer if this was helpful.
