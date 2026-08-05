---
title: "Azure AD Connect import with immutableTag changes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5170211/azure-ad-connect-import-with-immutabletag-changes
question_id: 5170211
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 22
qa_tags: []
---
# Azure AD Connect import with immutableTag changes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5170211/azure-ad-connect-import-with-immutabletag-changes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Physical server with Azure AD Connect has had a hard disk failure and we are now in a position where we are unable to recover/restore system. Prior to failure of system, I manged to export a copy of the Azure AD Connect configuration settings. 

We have had to install Azure AD connect on a new server and have now gone through the motions of placing that server is staging mode, no sync, whilst reviewing the newly imported AAD Connect configuration against the old imported one. 

There are three instances where there are changes noted for the "immutiableTags"...I need to verify that these changes will not adversely effect any ad sync if I proceed to take then new Azure AD Connect out of staging mode and start synchronisation. Can anyone advise if the incremental number changes shown below will affect the new Azure AD Connect sync if initiated? The last thing I want to do is set the wheels in motion where ADObjects are deleted, duplicated, or there are property changes etc. 

 The instances where these immutableTag changes have been noted are for the following entries: 

Instance 1

{
"Name": "Out to AAD - User Join","uniqueIdentifier": "#############hashed out###############","immutableTag": "Microsoft.OuttoAADUserJoin.007", Changed to ==> "immutableTag": "Microsoft.OuttoAADUserJoin.012""precedence": 120}

Instance 2

{
"Name": "Out to AAD - Group Writeup Member Limit","uniqueIdentifier": "##########hashed out##############","immutableTag": "Microsoft.OuttoAADGroupWriteupMemberLimit.002", Changed to ==> "immutableTag": "Microsoft.OuttoAADGroupWriteupMemberLimit.003""precedence": 137}

Instance 3

"standardSynchronizationRules": [
{"Name": "In from AD - User Join","uniqueIdentifier": "###########hashed out#############","immutableTag": "Microsoft.InfromADUserJoin.005", Changed to ==> "immutableTag": "Microsoft.InfromADUserJoin.006""precedence": 100},

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-03*

Dear JoseCambio,

Good day. 

Thanks for posting in Microsoft Community.

Regarding your query on Azure AD Connect import with immutable Tag changes.  Please understand that this query is outside of our support boundaries.   

For you to be assisted properly, please reach out to Microsoft Q&A by visiting this website azure-ad-connect - Microsoft Q&A; I am sure that our experts from that team can address your query effectively and accurately. 

Thank you for your cooperation and understanding.  Please do not hesitate to post your queries in Microsoft Community and we will always do our best to assist you! 

Sincerely, 

Simbarashe | Microsoft Community Moderator
