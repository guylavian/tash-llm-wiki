---
title: "Remove Witness Server from Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199785/remove-witness-server-from-exchange
question_id: 2199785
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-high-availability-storage-other"]
---
# Remove Witness Server from Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199785/remove-witness-server-from-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

Previously I'm running 2 nodes Exchange server and configured 1 Witness server. Recently, I have added 1 node which no longer require a Witness Server.

Is there a command which I could use to remove the Witness Server? Understand that the Witness Server will not be utilize even if it's there.

Thanks in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-15*

Hi Ken,

Hope you're doing well.

Yes, you can remove the witness server configuration from your Exchange Server DAG (Database Availability Group) using the Exchange Management Shell. Here's the command to remove the witness server: 

Set-DatabaseAvailabilityGroup -Identity <DAGName> -WitnessServer $null 

Replace "<DAGName>" with the name of your DAG. This command sets the WitnessServer parameter to "$null", effectively removing the witness server configuration from the DAG. After running this command, Exchange will no longer use the witness server, even if it remains configured. 

Best Regards
