---
title: "ADFS external dns setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/957899/adfs-external-dns-setup
question_id: 957899
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Q&A User"]
---
# ADFS external dns setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/957899/adfs-external-dns-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI, I have setup adfs (single Server) which is working fine internally but its not working externally.    

I need to configure external DNS but i'm not sure what I need to do    

Can someone please let me know what I need to do to make my adfs work externally

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-07*

I have install Azure Application proxy as I dont have public IP address but still I cant access adfs server from externally    

Done following    

Download Proxy from azure, install proxy    

Then created application    

then update my domain dns Cname from adfs.domian.co.uk to adfs-domain.msappproxy.net    

firewall is disabled on adfs server

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-07*

And here you will find the DNS and/or Loadbalancer requirements https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/overview/ad-fs-requirements#BKMK_7

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-07*

Hi,    

You have to deploy a WAP in your DMZ.    

Please refer to https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/best-practices-securing-ad-fs    

Regards,
