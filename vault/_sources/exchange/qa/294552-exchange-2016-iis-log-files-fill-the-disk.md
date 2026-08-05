---
title: "Exchange 2016 IIS Log files fill the disk"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/294552/exchange-2016-iis-log-files-fill-the-disk
question_id: 294552
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2016 IIS Log files fill the disk

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/294552/exchange-2016-iis-log-files-fill-the-disk (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

Once every 4-5 days we have to clear the log files manually from C:\inetpub\logs\Logfiles\W3SVC1 & W3SVC2, how can we fix this issue either by reducing the events to be logged or by configuring automatic truncation of log files.  

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-02*

Hi @LMS   ,    

You can create the VB script and schedule it to delete the logs files after specific days. Please refer below,    

https://learn.microsoft.com/en-us/iis/manage/provisioning-and-managing-iis/managing-iis-log-file-storage#delete-old-log-files-by-script    

If the above suggestion helps, please click on "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-03*

Hi, @LMS       

The recommended way is to regularly clear the old IIS logs as the logs may be helpful in troubleshooting.    

If you would like to limit the IIS logs, I suppose you may custom the W3C logging fields in IIS .    

    

Here is also a IIS document for your reference: Configure Logging in IIS    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
