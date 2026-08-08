---
title: "Exchange 2010 mailbox not available in EAC for migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/259068/exchange-2010-mailbox-not-available-in-eac-for-mig
question_id: 259068
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange 2010 mailbox not available in EAC for migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/259068/exchange-2010-mailbox-not-available-in-eac-for-mig (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an organization with a good hybrid configuration and have successfully migrated test users and production staff for testing.  

Here are the issues:  

We have two UPNs, <legacydomain>.org and <productiondomain>.org, default smtp addresses match <productiondomain>.org.   

Following successful migration, email users could not send successfully to recipients on-prem with the <legacydomain>.org UPN.   

After we change the UPN to <productiondomain>.org and ensure the user re-authenticates to the domain, migrated email users still cannot see the affected mailbox in the GAL, nor is the on-prem mailbox that was changed available for batch migration to O365 in the EAC.  

On-prem mailboxes not yet migrated can send to the recipient in question without issue.  

Here is what we have tried:  

Forcing the Offline Address Book update and restarted the Exchange AD Topology service.  

Verified the ShowInAddressBook attribute in ADUC for the user is correct.  

Verified the mailbox is not hidden from Address Books in EMC and PowerShell.  

On-prem mailboxes not yet migrated can see the recipient in question in the GAL and OAB without issue.  

Here is what we are considering:  

Removing the affected user from M365 and AAD, then waiting for the next scheduled sync to re-create the affected user.  

Creating a completely new mailbox on-prem and assigning the affected user to that mailbox, along with the existing smtp addresses.  

Is there another solution?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-04*

Update- the affected account was also configured for email on an additional mobile device, but removing the account didn't force the re-authentication to the domain, as one may expect to pick up the change to the UPN.  

We tried removing the license and Azure AD account from the tenant and ran a full sync, but the account was not automatically created by the sync. Account was restored in AAD and the license reapplied. At this point we will likely be creating a new user mailbox on-prem and assigning the user account and smtp addresses to that mailbox.  

One caveat- prior to changing the UPN, the mailbox was a linked mailbox instead of a user mailbox. This is the only disparity for this particular mailbox.
