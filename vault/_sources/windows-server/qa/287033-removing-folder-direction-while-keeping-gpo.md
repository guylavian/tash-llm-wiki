---
title: "Removing folder direction while keeping GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/287033/removing-folder-direction-while-keeping-gpo
question_id: 287033
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Removing folder direction while keeping GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/287033/removing-folder-direction-while-keeping-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I've read a lot of info about removing folder redirection but what I've read is usually applicable to a specific GPO that can be changed to reflect the desired scenario. Our GPO cannot really be changed, I'll explain: we have this My Docs folder redirection GPO that applies to certain security groups, let's say   

-  SGfinance   

-  SGdrivers   

-  SGoffice   

The GPO has been set to 'Leave the folder in the new location when policy is removed' when it was created. Due to certain reasons SGdrivers needs to have their My Docs not redirected to the fileserver anymore and have it set back to default location (local My Docs). Because the other groups need to maintain their folder redirection, I can't just set the GPO to 'Not Configured'.   

Therefor, in a test environment I removed SGdrivers from the Security Filtering in the current GPO, created a copy of the current GPO, let it only apply to SGdrivers through security filtering and set the GPO to 'Not Configured'. This doesn't work and the redirection stays place. Probably because the old GPO cannot be read by the client computer anymore and therefor it stays in place.....correct? Ok fine, I'll change the new GPO from 'Not Configured' to 'Redirect to local user profile path'. This does the trick and in this way the old GPO can stay in place for the groups that need their folder redirection to stay active whilst SGdrivers has it disabled because of the new GPO.   

My question is: is this the best approach? Or am I missing something? Anyone maybe who ever had to implement a similar scenario? It involves a lot of data and users and as you can understand, I don't want to mess this up. Thanks in advance. (clients run Win10 Pro)

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-02-25*

Hi,    

Welcome to share here!    

Here is a method just for your reference:    

We will not create a new GPO, all the changes will be on the current GPO.    

On the current GPO ,change the settings from : 'Leave the folder in the new location when policy is removed' to 'Redirect the folder back to the user profile location when policy is removed'.    

Update the gpo changes for the SGdrivers.    

Then removed SGdrivers from the Security Filtering in the current GPO.    

Refresh the group policies for the  SGdrivers by logoff logon (one or 2times).    

Then the redirected folder will redirect back to the local the user profile location as following (desktop folder):    

    

Last, if you want , on the current GPO you can change the settings from : 'Redirect the folder back to the user profile location when policy is removed' to 'Leave the folder in the new location when policy is removed' .    

Refresh the group policy for all the users.
