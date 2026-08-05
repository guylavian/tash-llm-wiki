---
title: "Deny GPO based on IP Range"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/548521/deny-gpo-based-on-ip-range
question_id: 548521
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Deny GPO based on IP Range

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/548521/deny-gpo-based-on-ip-range (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

I am testing a new gpo for all users connecting on wifi. The wifi ip range is different than the LAN IP range.  

I want to prevent the a current proxy setting gpo from applying for users connecting to the wifi IP range.  

Can this be achieved?   

Thanks all.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-09-13*

Hi @Admin Travis       

I suppose you can try out an Item level target to Deny GPO. I have also found an Interesting Forum for the same query and you can check if the suggestion there are helpful for you     

https://social.technet.microsoft.com/Forums/ie/en-US/2c88acbb-7ef0-405b-8869-c3b72a12cf28/ie-proxy-connection-settings-policy-filtering?forum=winserverGP    

Hope this answers all your queries, if not please do repost back.     

If an Answer is helpful, please click "Accept Answer" and upvote it : )

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-09-12*

I think that if you create a new site and define the ip range as a subnet in AD Sites & Services and if you create the GPO and link it yo that site, it should work.  

You may need to enforce thi GPO because Sites GPO are applied before Domain and OU GPO's.  

Don't forget to create a new site link.  

Another option would be to use Group Policy Preferences with Item Level Targetting.  It's possible to define. Ip range  

Hth
