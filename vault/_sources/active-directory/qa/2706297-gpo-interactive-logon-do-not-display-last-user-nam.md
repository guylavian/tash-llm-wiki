---
title: "GPO Interactive logon: Do not display Last User Name not working with KB2934520"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2706297/gpo-interactive-logon-do-not-display-last-user-nam
question_id: 2706297
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# GPO Interactive logon: Do not display Last User Name not working with KB2934520

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2706297/gpo-interactive-logon-do-not-display-last-user-nam (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am testing the following GPO in my Win 8.1 environment
Interactive logon: Do not display last user nameand it seems to be working fine so far.  Updates deployed to client machines prompt for a restart and upon restarting, the username box on Windows logon screen is cleared/empty.

This is working fine except for one particular update, KB2934520.  Upon restart for this update, Windows "appears" to restart but after restarting, it seems to log the user in automatically
 and then proceed to show the Windows logon screen in a Locked state where only the password is required.

I have been able to test & reproduce this on any computer.  Is this a security problem?

## Answer (community) — community member

*upvotes: 0 · updated: 2015-10-02*

Hi Algar,

Thank you for posting your query in Microsoft Community.

As per the description of the issue, your issue needs troubleshooting on Group Policies Object (GPO). So, I would recommend posting your query in the TechNet Forums. TechNet is looked at by other IT professionals who would
 more than likely be able to assist you.

TechNet Forum

Hope this information is helpful.
