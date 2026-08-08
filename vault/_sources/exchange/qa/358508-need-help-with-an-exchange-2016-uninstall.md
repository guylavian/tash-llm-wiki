---
title: "Need Help with an Exchange 2016 Uninstall"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/358508/need-help-with-an-exchange-2016-uninstall
question_id: 358508
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Need Help with an Exchange 2016 Uninstall

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/358508/need-help-with-an-exchange-2016-uninstall (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Im trying to uninstall EX 2016 from a windows server but during the prereq checks its telling me that the server is part of a DAG  

i have removed the server in question from the DAG and the DAG no longer exists?  

any suggestions

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-16*

@MTS      

In addition to the above information, I also suggest you have a check whether there exist Windows cluster in your organization. This Exchange server may be contained in a dead Windows cluster.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-15*

Hi @MTS   ,    

Before uninstalling, remove the below,    

-  Remove mailbox database copies    

-  Remove server from DAG    

-  Check if there are no active or mounted databases on that server    

If still having issue, please share the exact error message by covering your personal information.    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
