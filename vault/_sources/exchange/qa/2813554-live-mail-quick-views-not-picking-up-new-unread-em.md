---
title: "Live Mail Quick Views not picking up  new unread emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2813554/live-mail-quick-views-not-picking-up-new-unread-em
question_id: 2813554
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 21
qa_tags: []
---
# Live Mail Quick Views not picking up  new unread emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2813554/live-mail-quick-views-not-picking-up-new-unread-em (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

Live Mail (2011) Quick View has now stopped picking up new, unread emails from all accounts. Problem started about a week ago. I've looked through the forums and tried "**Repair all Windows Live programs"**twice but the problem remains. I've not added any new software, downloaded any updates (knowingly!) or changed any program settings.

I know I can look in each account... it's just the lack of convenience and time consuming for the 5 accounts email accounts I run....plus it's a feature of the program so why shouldn't I have it working?

Hope someone has got a solution. Thanks folks.

Cheers, Mick

## Answer (community) — community member

*upvotes: 3 · updated: 2018-08-03*

Live Mail (2011) 

Windows Live Mail 2011 has been obsolete since 2012 on all versions of Windows later than Vista. Which version are you using?

Because it's so old, I can't remember whether the Quick Views rebuild hack was incorporated or not. The solution for Quick Views not working properly used to be this:

-  Close down Windows Live Mail

-  Open the Registry Editor (press Windows key + R, type regedit and press
Enter. Give UAC permission when asked.)

-  In the left-hand pane, navigate to   

HKEY_CURRENT_USER\Software\Microsoft\Windows Live Mail  

and click on it to see the values under it in the right-hand pane.
4. Right-click on the value named SearchFolderVersion and select
Delete.
5. Close the Registry Editor, then launch Windows Live Mail. It will take longer than normal for the program to open, because it has to rebuild its Quick Views cache.

I don't think it's possible to repair Windows Live Mail 2011. The repair utility depends on an online source that no longer exists.
