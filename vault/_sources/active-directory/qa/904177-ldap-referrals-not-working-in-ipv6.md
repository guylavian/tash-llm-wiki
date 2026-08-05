---
title: "LDAP referrals not working in ipv6"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/904177/ldap-referrals-not-working-in-ipv6
question_id: 904177
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# LDAP referrals not working in ipv6

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/904177/ldap-referrals-not-working-in-ipv6 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to make ldap referrals in ipv6 environment. Everything works well in ipv4 environment. But when we try to chase referral using ldp we get this error    

Getting 0 entries:    

-----------    

***Searching...    

ldap_search_s(ld, "dc=DC_NAME", 0, "objectclass=CLASS_NAME", attrList,  0, &msg)    

Error: Search: Referral. <10>    

Server error: 0000202B: RefErr: DSID-0310074A, data 0, 1 access points    

ref 1: '[::1]:22389'    

Error 0x202B A referral was returned from the server.    

Result <10>: 0000202B: RefErr: DSID-0310074A, data 0, 1 access points    

ref 1: '[::1]:22389'    

Does referral work in ipv6 env? Is there something which can be done to make it work?     

Setup: Our application is installed in Windows server 2016.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-06-28*

Hi there,     

In order to support LDAP over an IPv6 network, transport calls have been modified to support both IPv4 and IPv6 based on the server configuration. It's worth checking your DNS and/or the hosts file(s) in use.    

LDAP API which allows connection through IPv6     

https://social.msdn.microsoft.com/Forums/office/en-US/cabead87-6453-4abb-afc9-89dfeef3ea5f/ldap-api-which-allows-connection-through-ipv6?forum=vcgeneral    

LDAP auth doesn't support IPv6 addresses https:// github.com/metabase/metabase/issues/12879    

--If the reply is helpful, please Upvote and Accept it as an answer--
