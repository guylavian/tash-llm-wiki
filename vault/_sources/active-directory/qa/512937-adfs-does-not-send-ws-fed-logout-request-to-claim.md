---
title: "ADFS does not send ws-fed logout request to Claim Provider if there is an active SAML session"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/512937/adfs-does-not-send-ws-fed-logout-request-to-claim
question_id: 512937
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS does not send ws-fed logout request to Claim Provider if there is an active SAML session

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/512937/adfs-does-not-send-ws-fed-logout-request-to-claim (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The problem is as follows.    

If the user does not log in to SP 2 and the SAML session does not appear, then if I send sign-out request to My ADFS, it makes sign-out request to Claim Provider.    

However, SP 2 was visited, and the SAML session is open, then when I send the sing-out query to My ADFS, it does not send a sing-out request to the Claim Provider, but instead forms a SAML request to SP 2 ( external ADFS), while generates an error:    

```
MSIS7055: Not all SAML session participants logged out properly. It is recommended to close your browser that not all SAML sessions have been completed.
```

To avoid this I added the wa=wsingout1.0 parameter to the POST SAML Logout Endpoint of the SP 2 registered as relying party trust 2, and the error disappears, but the browser stops at the external ADFS (RP-2) exit page, and does not send the ws-fed sing-out request to the my Claim Provider (IP). Therefore, the logout was not performed from the Claim Provider, and the user cannot change their account.     

How to further force my ADFS not to interrupt the chain and make a logout to the ClaimProvider?    

Also my Claim Provider is a separate web service (Identity Server 4) and between My ADFS and Claim Provider is ws-fed only!    

This question also my: https://stackoverflow.com/questions/68688204/adfs-do-not-forward-the-logout-request-to-the-identity-provider-if-there-is-an    

But I still don't have a solution.    

Thanks in advance!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-08-20*

I did some test with a colleague and this is what we see:  

ADFS-A <-- WS-Fed--> ADFS-B <-- SAML2 --> SP  

If I sign out from the SP, it does send the signout request to the IDPs:  

-  https://ADFS-A/adfs/ls/?wa=wsignout1.0  

-  https://ADFS-B/adfs/ls/?wa=wsignout1.0  

-  https://ADFS-A/adfs/ls/?wa=wsignoutcleanup1.0  

And if the token for the SP has a NameID issued in it, then also try to signout reaching to the SAML signout endpoint.  

In my case that's:  

-  https://SP/signout  

However, if there were no NameID issued, then we don't keep track of things and don't try to contact the SP endpoint.  

And all this is assuming that the protocol used between ADFS-A and ADFS-B IS WS-Fed. By default it will not be the case between two ADFS farms if the SP is using SAML. If the SP is using SAML, the ADFS logic will be to use SAML between ADFS-A and ADFS-B. In my case I forced it to use WS-Fed between the two farm by deleted the SAML endpoints on my claim provider trust on ADFS-B.  

Now the endpoint for the SP MUST be hosted and managed by the SP. Else you will not be able to perform a full sign-out in all circumstances. If you configure your relying party trust with a SAML Log Out endpoint pointing to the ADFSfarm itself, you will not be able to perform an IDP initiated signout. Nor a full log out if that is coming from another SP trusted by the IDP.
