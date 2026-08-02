---
title: "Port 443 incoming is not working on ADFS WAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/112917/port-443-incoming-is-not-working-on-adfs-wap
question_id: 112917
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Port 443 incoming is not working on ADFS WAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/112917/port-443-incoming-is-not-working-on-adfs-wap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,  

Stuck up with a strange issues on WAP server. It is newly built and installed ADFS service communication certificate and trust established with ADFS.  

When we try modern auth from external clients, F5 is giving non-response from WAP. Upon checking F5 is failing when tried <WAP IP>:443 which is not getting response back from WAP.  

Logged on WAP and telnet <WAP IP> 443 is not pass through, its blocked. netsh http show sslcert shows below entries  

Host: 0.0.0.0:443  

Host:sts.address:443  

sts.address:49443  

Anything else missing so that WAP can accept inbound 443 connection.  

I want to update, netstat -anob says 443 is listening on 127.0.0.0:443 instead of WAP IP:443 and telnet 127.0.0.1 443 is working.  

WAP is in workgroup, any other certificate or essential configuration missing here?  

do I need to have another SSL cert for allowing inbound 443  

Thank you in advance

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-09-30*

ADFS and WAP are both using the SNI extension of TLS. It means that the service will respond only if the HTTPS request is made for a specific URL (which is the FQDN of your ADFS farm).   

If your health probing doesn't do SNI (and it seems that F5 does), it will look like the WAP and ADFS servers are offline. To solve this you can either use a non TLS URL for the probe (http://<fqdn of the ADFS farm>/adfs/probe) or configure an SNI fallback.
