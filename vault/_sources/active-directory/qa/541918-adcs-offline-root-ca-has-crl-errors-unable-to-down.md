---
title: "adcs offline root ca has crl errors \"unable to download\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/541918/adcs-offline-root-ca-has-crl-errors-unable-to-down
question_id: 541918
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# adcs offline root ca has crl errors "unable to download"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/541918/adcs-offline-root-ca-has-crl-errors-unable-to-down (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Have Microsoft pki running for 2 years SCCM relies upon it at this point as well as the CMG  and Intune. The ca servers are all 2019 as well is AD schema and forest functional level. We have one roots CA off domain and  offline and one subca on the domain.  Have a webserver in our dmz and I am trying to publish the crl there for Windows Hello clients.  How do I update the rootca CRl and get it to the webserver? I have red x on the CDP and AIA locations in pkiveiw for the the http extensions of both and I cant seem to change. Am I screwed ? Do I have to build again?  

Thanks for any help

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-13*

Hello NSC-8481,  

Thank you for your question.  

There is a topic similar to what you are facing, see the link below to check the problem resolution:  

https://social.technet.microsoft.com/Forums/windowsserver/en-US/ef8711cc-b325-4abb-bc50-20f86e2741d0/fix-cdp-location-on-offline-root-ca?forum=winserversecurity#53e581ba- ceac-431e-b2c2-0307523bbaf4  

If the answer was helpful, please don't forget to vote up or accept as an answer, thanks.
