---
title: "How to change an existing GPO firewall rule with PowerShell? Set-NetFirewallRule?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198170/how-to-change-an-existing-gpo-firewall-rule-with-p
question_id: 2198170
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# How to change an existing GPO firewall rule with PowerShell? Set-NetFirewallRule?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198170/how-to-change-an-existing-gpo-firewall-rule-with-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to replace an IP address in an existing GPO firewall rule. I am able to create a new one with "New-NetFirewallRule -GPOSession $GpoSession -DisplayName test -RemoteAddress '192.168.1.99' -Action Block". But "Set-NetFirewallRule -GPOSession $GpoSession -DisplayName test-RemoteAddress '192.168.1.100'" doesn't work. "Set-NetFirewallRule : A parameter cannot be found that matches parameter name 'GPOSession'". Please help. Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-13*

It works. That's what I did. Thank you.
