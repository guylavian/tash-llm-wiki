---
title: "ADFS refusing to authenticate AFTER FL raised to 2019 level, error is \"Logon failure: the user has not been granted the requested logon type at this computer\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/802733/adfs-refusing-to-authenticate-after-fl-raised-to-2
question_id: 802733
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS refusing to authenticate AFTER FL raised to 2019 level, error is "Logon failure: the user has not been granted the requested logon type at this computer"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/802733/adfs-refusing-to-authenticate-after-fl-raised-to-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A 2016 farm has been upgraded following the steps captured here https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/upgrading-to-ad-fs-in-windows-server. While we had a mix of 2016 and 2019 servers and FL was at 2016 no login issue was reported. Soon as 2016 servers were removed and FL raised to 2019 login failure were reported. with event 342 (followed by event 1000 and 264) in AD FS Admin log. here is the error from the AD FS Admin log    

Token validation failed.      

Additional Data     

Token Type:     

http://schemas.microsoft.com/ws/2006/05/identitymodel/tokens/UserName     

%Error message:     

userfirstname.userlastnames@keyman  .com-Logon failure: the user has not been granted the requested logon type at this computer     

When we add the user to local admin group (for testing only) user login to O365 succeeds as normal. Adding the user to "Allow logon locally" does NOT have the same affect.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-04-06*

Thanks Pierre, I've opened a call with MS and collected a network trace for them while the login failure was happening. It seems that RC4 was removed from supported ETYPE on 2019 servers and trace is showing the following, I will check the server for the settings you have noted above and will leave an update here soon as I have a chance.  

 [KERBEROS] kerbtick_cxx5021 __KerbGetTgsTicket() - KerbGetTgsTicket KerbCallKdc: error 0xe  

 [KERBEROS] kerbtick_cxx7153 KerbGetServiceTicketInternal() - Failed to get TGS ticket for service 0xc00002fd  

0xe	14	KDC_ERR_ETYPE_NOTSUPP	14 KDC has no support for encryption type	kerberr.h
