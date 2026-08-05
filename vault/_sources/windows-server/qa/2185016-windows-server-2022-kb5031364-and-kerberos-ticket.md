---
title: "Windows Server 2022: KB5031364 and kerberos ticket"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185016/windows-server-2022-kb5031364-and-kerberos-ticket
question_id: 2185016
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 4
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Windows Server 2022: KB5031364 and kerberos ticket

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185016/windows-server-2022-kb5031364-and-kerberos-ticket (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

we use a service user in AD whose account is set as sensitive (account is sensitive and cannot be delegated).

Normal users request a Kerberos ticket through this user. Before the Windows update KB5031364 on the domain controller, the Kerberos ticket was issued as not forwardable. After Windows Update KB5031364, these tickets are issued as forwardable. If you log in with a user whose account is also sensitive, this ticket will be issued as not forwardable. The normal user accounts cannot be set as sensitive. However, this ticket must be issued automatically as not forwardable. Is there a workaround for this, or is this a bug? We urgently need a solution for this problem.

Regards

Artur

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-06*

Hello Artur Gamon,  

Thank you for your reply.  

How many Domain Controllers are there in your domain? And what OS version of these DCs?  

Please make sure all DCs have the same patch level or all DCs have the latest patches.  

Also, you can check if there is the event of KDC source via system log on all DCs.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-02*

Hello Daisy,

this is not a solution. I cannot set the accounts of normal users as sensitive. This has several disadvantages. (e.g. login outside the domain is not possible).

There should be another solution here.

Regards  

Artur

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-02*

Hello Artur Gamon,  

Thank you for your reply.  

It seems now you can only use a normal user account with sensitive set.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-01*

Hello Daisy,

yes we can confirm that the behavior changes again when the update is not installed or when it is uninstalled again. The problem does not occur on a Windows Server 2016 as Domain Controller. 

However, this behavior is not described in the changelog. 

Shouldn't the ticket still be created as "not forwardable", even if the user does not use a sensitive account?

Regards

Artur

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-01*

Hello Artur Gamon,  

Thank you for posting in Microsoft Community forum.  

If you can confirm the Kerberos ticket was issued as not forwardable on one domain controller without installing KB5031364.  

Or if you uninstall the KB5031364, Kerberos ticket was issued as not forwardable.  

Maybe the information below is related to your question.  

October 10, 2023 Security update (KB5031364) - Microsoft Support

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
