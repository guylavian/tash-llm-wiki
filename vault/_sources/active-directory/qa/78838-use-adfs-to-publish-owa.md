---
title: "use adfs to publish owa"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/78838/use-adfs-to-publish-owa
question_id: 78838
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# use adfs to publish owa

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/78838/use-adfs-to-publish-owa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dears,  

i have a deployment consisting of exchange server 2016, adfs 2016 and wap 2016.  

i am trying to publish outlook on the web using wap.  

i have followed microsoft documentation, and everything was working fine.  

recenlty, the behavior has changed, when i try to access owa, it is redirecting to adfs page ( thats right) but after signing in it is redirecting again to owa login page in order to insert the credentials again. however, it should after adfs redirect me automatically to the mailbox.  

i dont know what has changed, i checked the config again ( claim rules are created, claim based created too, wap config is green)  

in addition, there is no errors in event viewer.  

im lost i dont know how to proceed  

any suggestions  

thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-28*

I wonder if you search the Event Viewer at right pane and please try enabling logging for ADFS, see if you could find some clues from this:https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-tshoot-logging#admin-log

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-08-27*

I would verify that the OWA and EAC virtual directories are enabled for ADFS and not set to another auth scheme    

Verify Steps 6.-8 again:    

https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019#step-5c-publish-the-claims-relying-party-trusts-for-outlook-on-the-web-and-the-eac-in-web-application-proxy    

If that still doesnt fix it, walk through the entire doc    

https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019    

P.S.     

You have asked a lot of questions in the forums here, but have not marked any as accepted. Its important that you do that if you expect people to help you.     

Please return to these threads and mark any answers as accepted and close those out. Thank you    

https://learn.microsoft.com/en-us/answers/questions/75964/exchange-dag-and-witness-practice.html    

https://learn.microsoft.com/en-us/answers/questions/60625/can-i-add-a-session-host-2016-to-my-environment-if.html    

https://learn.microsoft.com/en-us/answers/questions/60625/can-i-add-a-session-host-2016-to-my-environment-if.html
