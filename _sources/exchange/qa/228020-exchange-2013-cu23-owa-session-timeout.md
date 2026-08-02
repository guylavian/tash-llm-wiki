---
title: "Exchange 2013 CU23 OWA session timeout"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/228020/exchange-2013-cu23-owa-session-timeout
question_id: 228020
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 CU23 OWA session timeout

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/228020/exchange-2013-cu23-owa-session-timeout (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As per Get-OrganizationConfig | fl activitybasedauthenticationtimeout*, the timeout is 6 hours. but the session does not timeout. few users reports that once they login to https://mail.compony.com/owa, their session stay active until they signout. where as Admin session (https://mail.company.com/ecp) which i use always timeout on  exchange server.  

I do see  

ActivityBasedAuthenticationTimeoutEnabled                 : True  

ActivityBasedAuthenticationTimeoutInterval                : 06:00:00  

ActivityBasedAuthenticationTimeoutWithSingleSignOnEnabled : True  

our mail.company.com is a LB. i don't know why the session does not timeout after 6 hours. we do not have any Private or Public TimeOut settings for our on Prem Exchange.  

Any help is appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-13*

@Eric Yin-MSFT   , I did a test and left few OWA session on computers.    

All OWA session on Windows server 2012 R2 were timed out and login screen was prompted but on Windows 10 its was still logged in. the behavior of windows 10 was same on Home computer and Company own devices.    

As you said, by default the PWA session assume Private but it should  still timeout. i am bit confuse on this mechanism.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-13*

-   I have not found an article for on-premise Exchange that introduces the function of ActivityBasedAuthenticationTimeoutInterval clearly but I found it also works in O365, it seems it's for users not needed to re-authenticate in the duration of session. For detailed steps, see Organization Config, Session timeouts for Microsoft 365

-   By default, OWA 2013 assumes users are using a private computer the default timeout of 8 hours is used. This timeout specifies how long a user can be inactive before requiring him/her to sign in again. You can use the following command to enable the public/private option in OWA：

```
Set-OwaVirtualDirectory “CAS1\owa (Default Web Site” -LogonPagePublicPrivateSelectionEnabled $True  
IISreset /noforce
```

Then you can configure PrivateTimeout/PublicTimeout with:

```
Set-ItemProperty “HKLM:\SYSTEM\CurrentControlSet\Services\MSExchange OWA” -Name PrivateTimeout -Value  -Type DWORD  
Set-ItemProperty “HKLM:\SYSTEM\CurrentControlSet\Services\MSExchange OWA” -Name PublicTimeout -Value  -Type DWORD
```

3.The ECP timeout should be same as OWA, try clearing the cache on both your server and your users' PC.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
