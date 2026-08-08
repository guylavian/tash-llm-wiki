---
title: "Contacts missing in OWA after migration to Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1283618/contacts-missing-in-owa-after-migration-to-exchang
question_id: 1283618
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Contacts missing in OWA after migration to Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1283618/contacts-missing-in-owa-after-migration-to-exchang (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We migrated onprem mailboxes to exchange online.  

Now migrated users have the problem, that contacts are not visible in EXO owa.  

They are present in outlook, with and without cache mode active.  

They can be synchronized to the mobile device.  

Running get-mailboxfolderstatistics on the contacts folder in Exchange Online shows 200 items in the contacts folder, but contacts in OWA are empty.  

When the user edits a contact in outlook or on the mobile device, then this contact is visible in OWA, but the contacts folder still shows 200 items by checking it using powershell. So ist's not a new contact that has been created. Editing the existing contact just made it visible in EXO owa.  

Any ideas?  

Regards  

Peter

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-22*

Hi @Peter  ,

What if adding a new contact in Outlook or mobile device? Can it show up in OWA? 

Probably you can try on one affected user's Outlook by exporting the contacts and then importing them back(Choose replace duplicates...) and see if it can make any difference. 

-  Export or backup email, contacts, and calendar to an Outlook .pst file

-  Import email, contacts, and calendar from an Outlook .pst file

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-15*

Sounds like the contacts were in local PST files and not within their old Exchange. Look around for PST and OST files on the old computers.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-15*

Hi @Peter,

 

Based on research, it is recommended that you can try to reimport the contacts.

First, you need to export contacts to a CSV file from on-prem EAC, and then bulk import them step by step via this guidance: Bulk import external contacts to Exchange Online - Microsoft Purview (compliance) | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
