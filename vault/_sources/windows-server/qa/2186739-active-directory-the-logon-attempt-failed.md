---
title: "Active Directory: The logon attempt failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186739/active-directory-the-logon-attempt-failed
question_id: 2186739
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 4
qa_tags: ["windows-business-windows-server-directory-services-user-logon-profiles"]
---
# Active Directory: The logon attempt failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186739/active-directory-the-logon-attempt-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a Windows Server 2016 (version 1607) on which I have deployed an Active directory.

Everything was working fine until yesterday when I tried to log in through a remote desktop and it showed the following error "The logon attempt failed"

I tried logging in physically to the server and changing the password, but it keeps showing me the same error when i try to remote desktop.

Any advise please ?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-11-13*

Hello Khalil Mejri,  

You can try the way in the following similar thread.  

Remote desktop connection logon attempt failed. - Microsoft Community  

  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-10*

Hello, 

thanks for your reply,

the server is one domain controller and PCC\Administrator is in fact a Domain Administrator account.

I don't recall changing another account to login remotely, i always use the PCC\Administrator.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-10*

Hello Khalil Mejri,  

Thank you for your reply.  

Is the server one Domain Controller or one member server?  

Is PCC\Administrator a Domain Administrator account or a local Administrator account?  

Please check if you change another domain account to sign in remotely (such as domain account in Administrators group or domain account in Domain Admin group)?  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-09*

This is the screenshot of the error message i receive when i try to login through RDP

Yes, I can sign in to the domain machine locally using the administrator account

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-09*

Hello Khalil Mejri,  

Thank you for posting in Microsoft Community forum.  

Would you please provide the full message about error "The logon attempt failed" or the screenshot about error "The logon attempt failed"?  

So you can sign in the domain machine locally?  

What account did you use to sign in (AD domain admin account or AD domain user account)?

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
