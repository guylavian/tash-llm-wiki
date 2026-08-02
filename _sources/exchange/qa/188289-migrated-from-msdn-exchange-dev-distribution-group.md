---
title: "[Migrated from MSDN Exchange Dev] Distribution group Sturcture"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/188289/migrated-from-msdn-exchange-dev-distribution-group
question_id: 188289
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Distribution group Sturcture

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/188289/migrated-from-msdn-exchange-dev-distribution-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] Distribution group Sturcture  

[Original post]  

I want to  DL structure to be more organised in my org  ..as of now We have 7000 DLs   

Goal is to have standard naming convention   

Need to have Nested DLs, so it can be added in other DLs   

What approach i should keep eg: create sitewise DLs ?????  

any help will be highly appreciated

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-07*

Hi,    

Goal is to have standard naming convention    

For the currently existing distribution lists, you may consider renaming their display names using powershell script:    

-  Prepare a CSV file which includes both the old and new display names  of the distribution lists, for example:    

    

-  Bulk rename the display names using the powershell command below:            $Groups = Import-CSV Sample.csv  

       ForEach($Group in $groups) {Set-DistributionGroup -Identity $Group.OldName  -DisplayName $Group.Newname}  

After that, you can create a distribution group naming policy to manage the names of new distribution groups created by users or by administrators via EMS (naming policy isn't applied to distribution group created using EAC). For more details, see Create a distribution group naming policy.    

Regarding your concern about adding the DLs into the other DLs, based on my test, this is by default supported.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
