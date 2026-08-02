---
title: "WSUS gpo options"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/622950/wsus-gpo-options
question_id: 622950
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# WSUS gpo options

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/622950/wsus-gpo-options (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

  Trying to work out why the GP options for WSUS do not work for one of our servers.  

  I first tried option 7 - download, notify for install and notify for restart. It didnt notify for install - it just installed automatically.  

  Second I tried option 3 - download, notify for install. This didnt notify for install it installed and restarted automatically!.  

  I checked GP results and can see that the policy is applying correctly.  

 Why dont the options work as advertised please? Anything else I need to configure?  

Thanks  

David Z

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-15*

I am testing the settings on just one server.  

That check box is NOT ticked in my policy.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-12*

@David Zemdegs       

Thanks for your posting on Q&A.    

To avoid misunderstanding, please help to confirm that there is only one Server encounter this issue. Am I right?    

The servers are the same version in your company. Right?    

In addition, I have reviewed the option in my lab and I found something interesting. Please help to check again:    

    

Hope the above will be helpful.    

Regards,    

Rita    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
