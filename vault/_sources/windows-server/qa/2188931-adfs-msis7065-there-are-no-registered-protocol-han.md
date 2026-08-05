---
title: "ADFS MSIS7065: There are no Registered protocol handlers on path /adfs/ls/idpinitialtedSignon.aspx"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188931/adfs-msis7065-there-are-no-registered-protocol-han
question_id: 2188931
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
---
# ADFS MSIS7065: There are no Registered protocol handlers on path /adfs/ls/idpinitialtedSignon.aspx

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188931/adfs-msis7065-there-are-no-registered-protocol-han (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can anyone suggest what causing this issue and a fix? 

-  The OS is Windows server 2022, hosted on VM workstation 16.5 configuring the ADFS service, I get the following message

```
when accessing [https://adfs.ldlt.com/adfs/ls/idpinitialtedSignon.aspx](https://adfs.ldlt.com/adfs/ls/idpinitialtedSignon.aspx "adfs.ldlt.com") on the **workplace VM**?
```

  

Microsoft.IdentityServer.RequestFailedException: MSIS7065: There are no registered protocol handlers on path /adfs/ls/idpinitialtedSignon.aspx to process the incoming request. at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)

Event ID 364

I tried setting Set-AdfsProperties –EnableIdpInitiatedSignonPage $True, this do not work.

Performing the same steps on  the home VM workstation 17.6 (hardware setting 16.5), I can access the the sign on page?  

I am stumped, what causing it and how to fix the issue?

## Answer (community) — community member

*upvotes: 1 · updated: 2024-12-02*

Thank reposted to Q&A

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-06*

You're welcome!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-02*

Thanks that, worked? I must have copied the link with typo in work, and used another link at home.  Doh! this caused me so much grief.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-02*

Hello

Thank you for posting in Microsoft Community forum.

Based on the description, I understand your question is related to ADFS.

Since there are no engineers dedicated to this topic in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.

Questions - Microsoft Q&A

Click the "Ask a Question" button in the upper right corner to post your question and select any tags related to your productions.

Thank you for your understanding and support. If you have any question or concern, please feel free to let us know.

Have a nice day.

Best Regards,

Molly

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-30*

I'm battling with something similar with setting up M365 federation,

but i can see the URL you have is wrong, please try https://adfs.ldlt.com/adfs/ls/idpinitiatedSignon.aspx  

There was a L in the URL that shouldnt be there
