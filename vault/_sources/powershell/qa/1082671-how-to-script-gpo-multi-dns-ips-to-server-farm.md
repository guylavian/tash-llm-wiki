---
title: "How to script/GPO multi DNS IPs to server farm"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1082671/how-to-script-gpo-multi-dns-ips-to-server-farm
question_id: 1082671
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
---
# How to script/GPO multi DNS IPs to server farm

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1082671/how-to-script-gpo-multi-dns-ips-to-server-farm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to update our server farm (WinSvr2008, 2012, 2016) with added multiple DNS IPs(Total 4). Is netsh interface ipv4 add dnsserver name=Ethernet address=xx.xx.xx.xx,  adding multple line to a script the only option or do I use a GPO with a script? Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-16*

Hello    

Thank you for your question and reaching out. I can understand you are  having query related  to DNS settings.    

You can use below  GPO settings.    

Computer Configuration > Policies > Administrative Templates > Network > DNS Client    

From there, you can set your DNS servers and any other DNS information you want. EDIT: you can add multiple DNS IP addresses to the DNS Servers entry by putting a space between each IP address.    

--If the reply is helpful, please Upvote and Accept as answer--
