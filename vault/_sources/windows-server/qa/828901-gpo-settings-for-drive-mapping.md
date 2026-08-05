---
title: "GPO settings for Drive Mapping"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/828901/gpo-settings-for-drive-mapping
question_id: 828901
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO settings for Drive Mapping

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/828901/gpo-settings-for-drive-mapping (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a pretty simple objective here.  Maybe I do understand how things work but not how to best meet my obejctives.  

The big picture is that we have users in various security groups.  Access to file shares is done with Security Groups.  

So, we map drives for those Security Groups / Users.  

Initially we used the option UPDATE.  But, as I recall, UPDATE doesn't create the maps in the first place.  

So, if we have a new User or a User shows up in a new Security Group for fileshare access then I believe that doesn't work.  

Next, we used the option REPLACE.  This meets the objectives that we started with as above.  

But, when the GPO updates occur on a workstation, the action deletes the map and recreates it.  

If no files are open that's fine.  

But if files or shortcuts to files/folders on the fileshare are open, they will be closed in the process.  

I think what we want would be something like:  

IF   

EXIST MAP  

THEN  

UPDATE  

ELSE  

CREATE  

.... something like that.  

I don't really want to have to write and use a script for this - but would want to use one of the selected options.

## Answers

_No answers on this thread._
