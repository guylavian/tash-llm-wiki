---
title: "Windows Security Center \"Dismiss\" through GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3220004/windows-security-center-dismiss-through-gpo
question_id: 3220004
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 9
qa_tags: []
---
# Windows Security Center "Dismiss" through GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3220004/windows-security-center-dismiss-through-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to figure out if there's a way to widely distribute the dismissal of a Security Center yellow exclamation point. The most recent nuisance is the tamper protection feature. Our customers are not comfortable with warnings like this and we often
 get complaints or questions about them. I can't see anything related to dismissing or disabling tamper protection through a GPO, which I'm not sure Microsoft will ever make possible. However, in an Enterprise environment I imagine there must be a way to widely
 dismiss a message like this or otherwise make it invisible to our customers. It also concerns me if they get used to seeing an exclamation point that if there is a different problem they won't contact us for assistance because they won't notice it.

The main goal here is to leave the basic Defender anti-virus protection enabled and not distract our customers with a concerning yellow exclamation point on their task bar related to Tamper Protection in this case. Any ideas are welcome here as I know this
 can be approached from different directions.

## Answer (community) — community member

*upvotes: 0 · updated: 2019-08-27*

Hi Gwen

My name is Andre Da Costa; an Independent Consultant, Windows Insider MVP and Windows & Devices for IT MVP.  I'm here to help you with your problem.

I found this article which discusses support for Windows Defender Tamper protection in managed environments. It seems the functionality is yet to be implemented, but it is coming:

https://www.urtech.ca/2019/08/solved-everything...

Sorry for the inconvenience of having to suggest the re-route, but Technet has a lot of experts there that know the ins and outs of enterprise issues; especially domain configurations for clients, Windows 10 deployment and migration and Group Policy. So, they will be better able to diagnose and determine whats causing the problem

Thanks for your corporation.

Technet forums - Group Policy - Microsoft

https://social.technet.microsoft.com/Forums/en-...

Information in the above link is sourced from a trusted Microsoft MVP blog.
