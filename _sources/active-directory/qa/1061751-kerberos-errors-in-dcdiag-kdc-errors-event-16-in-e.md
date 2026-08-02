---
title: "Kerberos errors in dcdiag. KDC errors event 16 in event viewer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1061751/kerberos-errors-in-dcdiag-kdc-errors-event-16-in-e
question_id: 1061751
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Kerberos errors in dcdiag. KDC errors event 16 in event viewer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1061751/kerberos-errors-in-dcdiag-kdc-errors-event-16-in-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are running a Windows 2012R2 domain environment which we want to upgrade. While doing prechecks we ran dcdiag and found few Kerberos related errors, for example: "While processing a TGS request for the target server service_account@keyman  .xxx, the account service_account@keyman  .xxx did not have a suitable key for generating a Kerberos ticket (the missing key has an ID of 8). The requested etypes were 18  17. The accounts available etypes were 23  18  17. Changing or resetting the password of service_account will generate a proper key."    

I have verified that the service account is not enabled to use DES. Event log analysis shows KDC errors are from a year back, although we have not experienced any issues so far with the service account. It is a critical account used for many services accessing the same database hence we don't want to make any changes to the password as suggested in dcdiag.     

Could anybody share some thoughts on how to get rid of these events without resetting the password?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-01*

Hi,    

I would like to give my input here... I agree with @Anonymous  , you need to look into the configured DES Encryption Types. I had this same behavior with the same evnts at a customer, who forces the usage of AES  in the domain:    

    

but at the same time all the other encryption options were still enabled:    

    

Hope this helps you on your way towrads a meaningful solution.    

Regards,    

Stoyan

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-25*

Hello there,    

I do not think you can resolve this without resetting the password. To resolve this issue, you must reset the password of the user account that has corrupt Kerberos keys.     

Note: The name of the user account is identified in the event message log.    

A valid Kerberos key is required to get a Kerberos ticket from the Kerberos Key Distribution Center (KDC). To verify that the Kerberos keys are valid and functioning correctly, you should ensure that a Kerberos ticket was received from the KDC and cached on the local computer. You can view cached Kerberos tickets on the local computer by using the Klist command-line tool.    

---------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-25*

Something here could help.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/kdc-event-16-27-des-encryption-disabled    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
