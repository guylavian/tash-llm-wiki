---
title: "I get locked out of my Active Directory account because Orion is storing old password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/471983/i-get-locked-out-of-my-active-directory-account-be
question_id: 471983
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# I get locked out of my Active Directory account because Orion is storing old password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/471983/i-get-locked-out-of-my-active-directory-account-be (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I don't have full access to everything in Orion so I get prompted for a username and password when I go into the System Configuration tab. When I enter my username and password it gives me an error message. "The specified credentials are invalid. Please specify a valid AD Account keeps locking out Orion NCM user and password" I have access to other tabs but not the configs tab. When I have to change my AD password and then open Orion my AD password gets locked out. I suppose because the old password is still in the configs tab.  If I try to clear the username and password in the configs tab it won't let me. error: The Orion server cannot access the SolarWinds Information Service. The exact error was 'The username cannot be empty.'  

I can put the new password in every time my AD password changes but since I don't have access to the configs tab anyway it just seems annoying.  

Any help on this will be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-13*

Hello @mr kavin  ,    

Thank you so much for posting here.    

So sorry that I am not professional with Orion server. According to the error messages, it is more related to Orion issue. It is suggested that we could kindly contact the vendor of Orion server to check whether they could provide some assistance.     

Besides, as mentioned, when we changed our AD password, our account would get locked out. As supposed, the old password is stored in the configuration tab. If so, I would suggest clearing the cached credentials or the stored credentials. But we got error when trying to clear the credential.    

As suggested, please kindly contact the vendor or supplier of Orion server for more professional assistance firstly.     

Thank you so much for your understanding and support.    

Best regards,    

Hannah Xiong

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-12*

I'd try asking for help here in dedicated forums.  

https://thwack.solarwinds.com/  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
