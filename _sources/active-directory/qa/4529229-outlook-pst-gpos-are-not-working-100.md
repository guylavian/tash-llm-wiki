---
title: "Outlook PST GPOs are not working 100%"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4529229/outlook-pst-gpos-are-not-working-100
question_id: 4529229
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Outlook PST GPOs are not working 100%

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4529229/outlook-pst-gpos-are-not-working-100 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear colleagues

We are setting new GPOs to limit the access to PSTs Default GPO is working fine. Settings enabled in that GPO are the following:
 -Prevent Users from adding new content to existing PSTs -Prevent users from adding PSTs to Outlook profiles and/or prevent using Sharing-exclusive PSTs

This is working fine. Users cannot: 1. Import new PSTs into their profile 2. Add new content to existing mounted PSTs 3. Create
 new PSTs

We have a second PST for people who have been approved to Import PST in Read-only mode. The setting in that GPO is the following
 -Prevent Users from adding new content to existing PSTs This is working partially fine: 1. Users can import existing PSTs: this is OK 2. Users cannot add content to mounted PST's: this is OK 3. Users can still create PSTs through File-->Account Setting-->Data
 files-->Add . This is NOT OK. 

Users CAN create a new PSTs which is useless because they cannot add content to that newly created PST

Is there a way to prevent this?  

Regards

Ramon

## Answer (community) — community member

*upvotes: 0 · updated: 2019-11-26*

Hi Marvin,

Thanks for the reply.

Even though this is the answer I expected because there is no others settings to do so, I tend to disagree with the rationale.

In my humble opinion, it is a very different action to open an existing PST than creating a new PST.

Both are governed by the same Registry Key: DisablePST and they should be managed by different settings, ni my opinion.

We are not in the Cloud and I need to maintain PSTs for a very reduced set of users.

We will train the users. There is nothing else we can do.

But again, even though I understand the settings, in my opinion those are 2 different actions.

In one, you let the user to Open a existing PST,. whose content growth you can control by GPO.

Another action is creating PSTs.

Thanks again for taking the time in the reply

Ramon

## Answer (community) — community member

*upvotes: 0 · updated: 2019-11-26*

Hi Ramon,

Thank you for contacting us. To my knowledge, it's an expected behavior because the policy "Prevent user from adding new contents to existing PST files" cannot prevent user from creating/adding new PST files to your Outlook profile. It can only
 prevent users from adding new content to existing PST files linked to your Outlook profiles.

When you only enabled "Prevent users from adding PSTs to Outlook profiles and/or prevent using Sharing-Exclusive PSTs", the users cannot create/add new PST files to Outlook profiles. In this scenario, if you don't want to allow users to create new
 PST files in their Outlook profile, you must enable the second policy. However in this way, the approved users cannot import the second PST to their Outlook profile.

From my experience, if you use Office 365 cloud, why not create a shared mailbox for these approved users? You can import the PST file and grant read-only access to this shared mailbox. To achieve this, just connect to Exchange Online PowerShell and run
 the cmdlet "Add-MailboxFolderPermission -Identity <shared mailbox:\folder name> -User <username> -AccessRights Reviewer". For your reference, see
Connect to Exchange Online PowerShell and Add-MailboxFolderPermission.

Regards,

Marvin
