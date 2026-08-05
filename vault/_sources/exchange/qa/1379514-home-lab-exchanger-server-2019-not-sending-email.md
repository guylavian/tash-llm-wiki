---
title: "Home lab exchanger server 2019 not sending email"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1379514/home-lab-exchanger-server-2019-not-sending-email
question_id: 1379514
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Home lab exchanger server 2019 not sending email

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1379514/home-lab-exchanger-server-2019-not-sending-email (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have setup exchange server 2019 in home lab.

I created two users with email account on my homelab.local domain.

I sent a test email, but it just gets stuck in Draft folder, any idea how I fix this issue?

I just want to route emails internally, nothing is internet facing. Please advise/help!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-06*

To learn more about the problem, try turning on Exchange tracing. Open the EMC and go to Organisation Configuration > Client Access > Outlook Web App to allow Exchange tracing. Click Edit after choosing the OWA virtual directory you want to enable tracing for. Select the Enable tracing check box under Logging.

Once tracing has been enabled, you can duplicate the problem and gather the trace logs. You can get the trace logs by launching the EMC and going to Monitoring > Mailbox > Activity Logs. To search, select the Trace log type. The results window will display the trace logs.
