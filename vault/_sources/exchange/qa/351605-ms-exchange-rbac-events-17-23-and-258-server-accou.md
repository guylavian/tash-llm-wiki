---
title: "MS Exchange RBAC Events 17, 23, and 258 - Server Account not assigned any management roles"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/351605/ms-exchange-rbac-events-17-23-and-258-server-accou
question_id: 351605
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# MS Exchange RBAC Events 17, 23, and 258 - Server Account not assigned any management roles

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/351605/ms-exchange-rbac-events-17-23-and-258-server-accou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So I'm seeing events mentioned above hitting my event logs every two hours with regularity. I do not know how long it has been going on, as the log rolls over, but it is at least 10 days old. My question is, how do I track what is causing this issue? I've checked Scheduled tasks and I don't see anything there. Here are some snippets of the errors: ![86367-event17.jpg][1] ![86402-event23.jpg][2] ![86375-event258.jpg][3] NOTE: The events say "user <canonical name of object" but it is indeed referring to my Exchange server object in AD. This is only happening on one server in a 5 member DAG. Kind of at a loss. EDIT: I'm adding the events as a txt file, but it is really a CSV file. You can download it as such. [88300-errors.txt][4] EDIT2: Adding IIS log with entries correlated to event log entries [88616-iislogforevents17-23-258.txt][5] [1]: /api/attachments/86367-event17.jpg?platform=QnA [2]: /api/attachments/86402-event23.jpg?platform=QnA [3]: /api/attachments/86375-event258.jpg?platform=QnA [4]: /api/attachments/88300-errors.txt?platform=QnA [5]: /api/attachments/88616-iislogforevents17-23-258.txt?platform=QnA

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-04-22*

I would simply delete all the monitoring mailboxes and recreate them and see if that fixes it. This can be done anytime  

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-2013-2016-monitoring-mailboxes/ba-p/611004  

"Troubleshooting tips"

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-12*

Hi, anonymous user     

Do you have some third party software installed on this Exchange server? For example, some antivirus, backup or monitor software.    

Since the error events are logged regularly on this server, please check if there are specific software running at that time.    

You may also disable or uninstall them to check if the problem persists.    

Besides, do you have other problems with the Exchange server?    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
