---
title: "Change ADFS and WAP default port"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/18093/change-adfs-and-wap-default-port
question_id: 18093
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Change ADFS and WAP default port

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/18093/change-adfs-and-wap-default-port (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

  I am set up ADFS and WAP in test environment, I can reach the ADFS server when i am in the LAN but not externally. My ISP is blocking port 443. S i would like to know if there is a way to change the default port 443 on ADFS and WAP server to something else.   

  Thanks.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-03-25*

It is very odd to block the port 443. It is usually the only one open even on public kiosk machine or airport WiFi...    

In theory you can change the HTTPS port on the ADFS server with Set-AdfsProperties. But it will require to re-configure all applications as in a passive flow, it is the application redirecting the users to the ADFS farm. Also if you change the port to something different than the 443, you might prevent many users to access the application externally for the same reason as you invoke. It is very possible that they might only connect to specific ports and usually the 443 is the one universally white listed.
