---
title: "DNS Name resolution for “_ldap._tcp.dc._msdcs.fios-router.home” & “wpad” BLOCKED by dnscrypt-proxy! How to fix? And GOOD STUFF here"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3195227/dns-name-resolution-for-ldap-tcp-dc-msdcs-fios-rou
question_id: 3195227
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 12
qa_tags: []
---
# DNS Name resolution for “_ldap._tcp.dc._msdcs.fios-router.home” & “wpad” BLOCKED by dnscrypt-proxy! How to fix? And GOOD STUFF here

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3195227/dns-name-resolution-for-ldap-tcp-dc-msdcs-fios-rou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This first post is a bit long because I've added some updates, but it also has some good stuff for you, so please bear with me.  HOWEVER, please DO NOT post any stock answer.  This query will NOT be fixed by any kind of automatic answer.  PLEASE ABSORB THE
 DETAILS.

On every reboot of my Win 10 Pro 64-bit (version 1803) PC, I get two Warnings in Event Viewer:

**"Name resolution for the name _ldap._tcp.dc._msdcs.fios-router.home. timed out after none of the configured DNS servers responded."**and  

"Name resolution for the name wpad timed out after none of the configured DNS servers responded."

Both are Event 1014, DNS Client Events.  

The first Warning's reference to "fios-router.home" must be to my Quantum G1100 modem-router that was supplied by Verizon for my FIOS 1Gbps service. Also, the DNS name resolution is probably needed for proper functioning of the Quantum G1100's "Active Directory".
 See item #4 at this link: -THIS LINK ON MSDN-  

But I'm not a tech and don't know how to start fixing this.  

EDIT - More info:  

By experimenting, I have determined that these Warnings occur when I have the service dnscrypt-proxy running at startup. It's a great service that encrypts DNS lookup requests so that nobody - not Verizon and not Google and not man-in-the-middle
 bad guys - can see where I am trying to go.  My only "resolver" is cloudflare's newish 1.1.1.1 service.  The dnscrypt-proxy service running on my PC sends needed DNS name lookups only to that resolver, and encrypted.  

First, there's a superb article on ars techinca that explains everything about dnscrypt-proxy and cloudflare's secure 1.1.1.1 DNS lookup service in great detail:
How to keep your ISP’s nose out of your browser history with encrypted DNS  

Second, you can download and get technical info about Simple DNSCrypt - which helps you install and configure dnscrypt-proxy on a Win machine - from github at
github-bitbeans-SimpleDnsCrypt  

Third, apparently (because dnscrypt-proxy is working) the DNS name lookup requests for
_ldap._tcp.dc._msdcs.fios-router.home. and wpad 
are going to cloudflare's 1.1.1.1 resolver but these two can only be resolved INSIDE my LAN network.  
What should I do to continue using dnscrypt-proxy but let "_ldap._tcp.dc._msdcs.fios-router.home" and "wpad" get the needed DNS/name resolution and so not generate the Warnings I describe above? ◄ This is the important question.

UPDATE - 

As to the Event 1014 Warning that "Name resolution for the name _ldap._tcp.dc._msdcs.fios-router.home. timed out after none of the configured DNS servers responded.":  

I've done some more digging, and the dnscrypt-proxy service I am using to encrypt my DNS lookups and send them only to cloudflare's new 1.1.1.1 has a Forwarding feature, maybe especially for cases like this.  

See < THIS PAGE ON GITHUB >  

MORE Update - trying to follow the wiki link about Forwarding -

-  I put forwarding-rules.txt into the same folder as dnscrypt-proxy.toml.

-  I added the line  forwarding_rules = 
"forwarding-rules.txt"  
(using double-quotes not single quotes) to dnscrypt-proxy.toml right after the line cache_neg_ttl = 60

-  The only line I put in forwarding-rules.txt is  
fios-router.home 192.168.1.1

Is that correct?

RESULTS - The above didn't work, and on reboots I continue to get the Event 1014 Warning "Name resolution for the name _ldap._tcp.dc._msdcs.fios-router.home. timed out after none of the configured DNS servers responded."

What next?

## Answer (community) — community member

*upvotes: 0 · updated: 2019-05-09*

I'd probably experiment in the HOSTS file

_ldap._tcp.dc._msdcs.fios-router.home     192.168.1.1

"C:\Windows\System32\drivers\etc\hosts"

you might be interested in this.. run the browser test then follow the continued reading on its    Secure DNS
