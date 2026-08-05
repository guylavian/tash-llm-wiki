---
title: "Domain Controllers High CPU Usage Causing Server To Be Unresponsive"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188419/domain-controllers-high-cpu-usage-causing-server-t
question_id: 2188419
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 17
qa_tags: []
---
# Domain Controllers High CPU Usage Causing Server To Be Unresponsive

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188419/domain-controllers-high-cpu-usage-causing-server-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have two Windows Server 2016 Standard Edition Domain Controllers that are having 100% CPU usage causing the systems to become completely unresponsive.  Both of these servers are on Google Cloud Platform in their own subnets. This started happening in the middle of last week. When we finally were able to RDP into the systems we started watching task manager and found that the DNS Server process's CPU usage would rapidly start climbing to 100% usage along with the  AD process, and a process called System Internals. 

We tried multiple things to see what was causing the issue such as disabling anti-virus, monitoring agents, and any other non-essential software. Nothing worked. Only thing we found to stop the processes from using all of the system's CPU resources was to kill the DNS Server process. This would instantly make the server become responsive again. As we obviously can't leave the DNS Server down on both domain controllers we decided to migrate the domain controllers to a new environment which we were going to do anyways. We took two freshly installed Windows Server 2019 Standard Edition servers running on a Redhat KVM environment and prompted them to domain controllers and shut the original domain controllers down. 

The new systems were fine for a day or so but then the same issue occurred to both systems at the same time. At this point we put a script on the servers to restart the DNS Server Service every 5 minutes to keep them running as best as we can but would like to find a solution for this issue. We have not found a lot of people online having this same issue so we are at a loss currently.

Some other things we noticed. There is no increase in network traffic so we are pretty such this isn't any type of DOS attack. The systems sit around 1Mbps of network traffic at all times. The issue will persist between reboots it seems. Sometimes the processes do let up a bit but the systems are still very unresponsive even then. Throwing hardware at the problem will help slightly but it just takes long for the systems to become unresponsive. No other systems are having issues just the two domain controllers. The systems become unresponsive to the point that networking does not work even pings.

We thought about standing up a stand alone DNS server just to point clients two for the time being as it is hard to work on the systems in question at all.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-01*

Hello

Thank you for posting in Microsoft Community forum.

I'm sorry to hear that you are experiencing issues with your Windows Server 2016 and 2019 Domain Controllers. Based on the information you provided, it seems that the DNS Server process is causing the high CPU usage and unresponsiveness of the servers. 

One possible solution is to check the DNS configuration on your servers. Make sure that the DNS settings are correct and that the servers are pointing to the correct DNS servers. You can also try clearing the DNS cache on the servers by running the following command in an elevated command prompt: "ipconfig /flushdns". 

Another possible solution is to check for any updates or patches that need to be installed on your servers. Make sure that your servers are up-to-date with the latest updates and patches from Microsoft. 

If the issue persists, you may want to consider opening a support ticket with Microsoft to get further assistance in troubleshooting the issue. They may be able to provide more specific guidance based on your environment and configuration. 

Best Regards,

Zack Lu
