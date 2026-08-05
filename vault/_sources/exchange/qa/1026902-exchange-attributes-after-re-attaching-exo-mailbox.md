---
title: "Exchange Attributes after re-attaching EXO mailbox to a new account in another forest"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1026902/exchange-attributes-after-re-attaching-exo-mailbox
question_id: 1026902
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange Attributes after re-attaching EXO mailbox to a new account in another forest

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1026902/exchange-attributes-after-re-attaching-exo-mailbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Here is the scenario:

Parent Office 365 tenant with Azure AD connect

Child Domain with their own AD and Exchange On-premises server. Network connectivity between parent Azure AD Connect and child AD to setup hybrid and sync AD object to parent tenant.

Mailboxes were migrated to parent office 365 tenant.

The customer would like to now have AD account from child domain created on parent AD on premises server, disconnect mailboxes from child AD on premises account and re-connect to newly created AD accounts on parent domain.

The parent company's local AD scheme is prepped for Exchange but I'm concerned about the Exchange attributes that are from the child domain Exchange server will not be present in the parent domain and mailboxes will loose required attributes. Also, currently, mailboxes on child Exchange on-premises server are now remote mailboxes. Would be the state of these when the account will no longer be connected to the parent tenant?

I have the process to disconnect mailbox from child AD account and reconnect to new account in parent AD.

-  Create new account on parent AD but keep in non sync OU

-  Get ImmutableID of new account

-  Move old account from child domain to non-sync OU

-  Restore old account from child domain on Office 365 and it changes from synced to Cloud

-  Set ImmutableID of new account with old account - Set-MsolUser -UserPrincipalName * Email address is removed for privacy * -ImmutableId "EFSIjTMY5ESyJb8zHLXxqA=="

-  Add aliases to merge

-  Move child domain new account account from perent AD non sync OU to Synced OU

-  verify mailbox is attached (at this point I'm concerned about the Exchange attribute and what to expect with the remote mailbox on the child Exchange on premises server)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-29*

@KyleXu-MSFT   thank you for your response. The AD accounts are currently residing on the child domain but synced to tenant via Azure AD connect.     

We want to have the accounts re-created on parent AD, reconfigure sync to now sync newly created accounts on parent AD and then ensure the mailboxes are now connected to the newly created accounts.     

Hope this clears it up
