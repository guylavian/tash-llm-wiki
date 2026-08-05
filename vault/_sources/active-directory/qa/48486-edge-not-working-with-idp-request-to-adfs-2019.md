---
title: "Edge not working with IdP request to ADFS 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/48486/edge-not-working-with-idp-request-to-adfs-2019
question_id: 48486
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-edge-edge-development", "microsoft-security-security-active-directory-federation-services"]
---
# Edge not working with IdP request to ADFS 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/48486/edge-not-working-with-idp-request-to-adfs-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We're testing to roll out Edge 83.0.478.58.     

If we navigate to https://ourlocaldomain/adfs/ls/idpinitiatedsignon.aspx?LoginToRP=https://partnerserver/partnerservice, Edge redirects to https://ourlocaldomain/adfs/ls/wia?LoginToRP=https://partnerserver/partnerservice&client-request-id=xxxx as expected. But instead of picking up the token when the ADFS 2019 server (running in same domain as users) sends the 200-OK and redirecting to the partner's site, Edge re-sends the GET for the adfs/ls/wia and our users get the below ADFS error page (I assume because the ADFS has already completed that client request). If the user re-enters the original IdP request URL, the process works as expected (I assume picking up the existing token from ADFS). It then works until the token expires.    

    

The problem does not happen in IE11 nor in Chrome 83.0.4103.116. It is specific to Edge. We have this problem on Win7 SP1 as well as several versions of Win10. Edge doesn't have any issue with an SP initiated request, nor does it have a problem if ADFS already has a token cached for that user/machine. I've deleted and recreated the partner in ADFS. They have one claim that I then transform, so it shouldn't be a timeout type issue. I've looked at all the debugging and logs on the ADFS side and it really just looks like Edge is re-requesting the adfs/ls/wia page over again. I've verified that WiaSupportedUserAgents in Get-ADFSProperties has Mozilla/5.0 set (among many others).  I'm really not sure what else to look at - if there are any Edge settings that might correct this, or if it's an actual bug with WIA in Edge. I tried posting in Edge forums, but they sent me to ADFS.    

Any help is appreciated as I'm losing my hair over this.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-24*

I've verified that WiaSupportedUserAgents in Get-ADFSProperties has Mozilla/5.0 set (among many others).

Take a look to this article - https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ad-fs-browser-wia.  

Did you find "Edg/"* in your output from the cmdlet?
