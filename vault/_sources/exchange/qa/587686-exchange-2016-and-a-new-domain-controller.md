---
title: "Exchange 2016 and a new Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/587686/exchange-2016-and-a-new-domain-controller
question_id: 587686
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 and a new Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/587686/exchange-2016-and-a-new-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone, a new domain controller was added to our environment recently and I seem to be getting the following error now when viewing distribution groups in the admin console.    

    

I did identify a firewall problem that was preventing this Exchange server from communicating with the new DC which has now been resolved, but this error persists.  Some articles I've found suggest that restart the IIS or restarting the Exchange server might resolve this, but I wanted to post here for further direction.  Anything I can do to troubleshoot that won't take the Exchange server offline?    

Regards,    

Adam Tyler

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-10-13*

I wouldnt demote the 2019 DC if the 2010 Exch Server is going away. If things are working, I would keep what you have and get the 2010 server out of there as soon as you can  

You can always hard code the 2010 server against that 2012 DC as well if you havent already .

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-13*

@AdamTyler-3751      

Exchange 2010 doesn't supported with Windows Server 2019 DC: Supported Active Directory environments. From the screenshot that you provided, we can know this issue may related with Exchange server system requirements.    

    

I would suggest you uninstall the new DC now. You could reinstall it after uninstall Exchange 2010.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-10-12*

Well, restarting the DSAccess service may fix it but that is about the same as restarting all the Exch Services. I would give it a bounce. Any other errors in the event logs right now?
