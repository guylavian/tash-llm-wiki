---
title: "Changing the subnet of domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/232066/changing-the-subnet-of-domain-controller
question_id: 232066
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Changing the subnet of domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/232066/changing-the-subnet-of-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

Currently the IP of my primary DC is 10.64.X.X and subnet 255.0.0.0. I would like to have your advice on changing the subnet of my primary domain controller to 255.255.254.0.   

Please advice me the steps if anyone has done it before.  

Thank you,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-15*

Shouldn't be a problem, just do an ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service. Then also recreate the reverse lookup zone via wizard.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/configure-secondary-name-server#configure-the-reverse-lookup-zone    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-15*

Hi,    

you can do this, you will most probably have a minor disruption (seconds).    

You just need to ensure that the DC can communicate with all your domain clients from the new network segment. So, please pay attention to the Firewall in bteween and also check your rules in the Windows Firewall. Here are some püosts for your reference:    

Change the static IP address of a domain controller    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc758579(v=ws.10)?redirectedfrom=MSDN    

old article, but everxthing still applies.     

Impact of Changing IP Address of Domain Controller, Exchange Mailbox Server, DHCP Server and ADCS server.    

https://learn.microsoft.com/en-us/answers/questions/92607/impact-of-changing-ip-address-of-domain-controller.html    

Just ensure that DNS records are updated and everything will work out just fine.    

----------    

Please don't forget to Accept as answer if the reply is helpful    

Regards,    

Stoyan
