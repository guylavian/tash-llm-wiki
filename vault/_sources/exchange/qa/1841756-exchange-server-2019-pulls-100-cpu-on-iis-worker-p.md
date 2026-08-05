---
title: "Exchange Server 2019 pulls 100% CPU on IIS Worker Process -MsExchangeMapiFrontEndAppPool"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1841756/exchange-server-2019-pulls-100-cpu-on-iis-worker-p
question_id: 1841756
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019 pulls 100% CPU on IIS Worker Process -MsExchangeMapiFrontEndAppPool

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1841756/exchange-server-2019-pulls-100-cpu-on-iis-worker-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

At an customer of ours we have an problem that on monday 08:00 the CPU is pulling 100% and Outlook is not workable on the clients. When we dive deeper in this issue we see that the IIS Worker Process is pulling this CPU, more specificly the MsExchangeMapiFrontEndAppPool on the application pool. When we reboot the server everything is solved till the next monday morning 08:00. 

We can't figure out what is causing this issue and why this only happens on monday around 08:00. We can't find any scheduled tasks as far as we know.

I could appreciate some help here.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-29*

Hi,

Welcome to the Microsoft Q&A forum!

I couldn't agree more with the points mentioned by Andy David, in addition, you can also do the following:

Review the Exchange logs located in:  "C:\Program Files\Microsoft\Exchange Server\V15\Logging" They may provide insights into what specific operations Exchange is performing during those peak times.

Check the IIS logs for the MAPI front end:  "C:\inetpub\logs\LogFiles" Look for any unusual activity or spikes in requests around 08:00 on Mondays.

There could be a memory leak or resource exhaustion issue in the "MsExchangeMapiFrontEndAppPool". Review memory consumption patterns and consider recycling the application pool more frequently to mitigate.

Schedule a periodic recycle of the "MsExchangeMapiFrontEndAppPool" closer to the time of the issue but perhaps not during peak hours. This can help clear any transient states that lead to the high CPU usage.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.
