---
title: "Exchange Classic Hybrid Connection Security"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/129575/exchange-classic-hybrid-connection-security
question_id: 129575
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Classic Hybrid Connection Security

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/129575/exchange-classic-hybrid-connection-security (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Looking at the setup Wizard for Exchange Classic Hybrid I'm wondering if once it is setup communications are obviously over 443/35 TLS 1.2 is there any mutual authentication between our Exchange Servers in our DataCentre and the EOL hybrid connection points? If so, how is this done (certificate etc.) ? The reason I ask is we have to open ingress ports on our edge for EOL to send mail inwards as we are keeping mail flow on premise.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-17*

Thanks for taking the time to reply Andy. Much appreciated. I'm getting more concise information from you than the documentation! Is there anywhere in the documentation that explicitly states this? Having a epic time trying to get this past security.  Since I haven't got it up and running I can run a network trace to verify.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-17*

Thanks Andy. In my understanding classic hybrid EOL can open an unsolicited connection to our data-center EX 2016 servers with no SSL inspection (as that's a requirement) i.e. EOL sends a TCP syn on port 25 TLS for mail flow for example. So firewalls aside is exchange holding a certificate for the EOL somewhere to authenticate it ? I would assume so and that this certificate is added to Exchange server when we connect the hybrid. Otherwise the only security layer for 'auth' is just firewall rules allowing in the wide list of EOL IPs.    

So that is to say is EOL to EX using TLS with mutual authentication ?
