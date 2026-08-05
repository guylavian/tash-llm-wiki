---
title: "Cutover Migration ( From Exchange 2013 to O365 Online)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/247461/cutover-migration-from-exchange-2013-to-o365-onlin
question_id: 247461
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Cutover Migration ( From Exchange 2013 to O365 Online)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/247461/cutover-migration-from-exchange-2013-to-o365-onlin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey Forum,

I'm trying to create a "Migration Batch" from Exchange 2013 to O365 and I'm getting an error message that says the following:

****Batch creation failed!  

The 'TargetDeliveryDomain' parameter isn't supported for migrations using the 'ExchangeOutlookAnywhere' protocol.****

I'm not sure how to fix this, I'm not really sure what this means.

Any help is appreciated.

Techno Guy

## Answer (community) — community member

*upvotes: 1 · updated: 2023-02-09*

How can this be done when the classic has been depricated? 

I am stuck with this error

## Answer (community) — community member

*upvotes: 1 · updated: 2021-10-16*

Today (16-oct-2021) I had the same problem, so I followed the advice of JimGonzalez-7204 (switch to the classic) and everything was ok.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-31*

I had the same problem with Exchange 2010. I switched to classic view in Exchange Admin Center and created the batch without errors

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-28*

Hi @anthony davis      

Agree with the suggestion above from Andy, please make sure you have Prepared for a cutover migration list in the official document.    

In addition, according to this: Use PowerShell to perform a cutover migration to Microsoft 365    

The TargetDeliveryDomain parameter seems not being used in the cutover scenario within New-MigrationBatch. You may also try using powershell to finish the migration.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-27*

Did you follow this doc and enable Outlook Anywhere?    

https://learn.microsoft.com/en-us/exchange/mailbox-migration/cutover-migration-to-office-365#prepare-for-a-cutover-migration    

Follow the entire doc:    

https://learn.microsoft.com/en-us/exchange/mailbox-migration/cutover-migration-to-office-365
