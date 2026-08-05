---
title: "Iphones cannot connect via ActiveSync since 2016 CU19 and KB500087"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299276/iphones-cannot-connect-via-activesync-since-2016-c
question_id: 299276
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Iphones cannot connect via ActiveSync since 2016 CU19 and KB500087

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299276/iphones-cannot-connect-via-activesync-since-2016-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, have upgraded a client 2016 server to CU19 and installed patch for KB500087 and since then all iphones can no longer connect via activesync using the native mail client. Outlook client connects, I can setup an android device as well but any new or existing iphones fail to connect. The active analyser passes just fine and I can go through the process of setting up an account and verifying the account, but when it comes to actually retrieving email, it just say it cannot get mail as the connection to the server failed. I've tried rebooting the devices, deleting and re-adding the accounts, same issues. If I enable activesync logging, it doesn't show any errors, nothing in the events logs either so baffled. Any help appreciated and it was def working prior to this update.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

Configuration Editor in IIS under the Active Sync Web site. Open that, then system.webserver/serverRuntime there the uploadreadahead setting, I've set it to 500000
