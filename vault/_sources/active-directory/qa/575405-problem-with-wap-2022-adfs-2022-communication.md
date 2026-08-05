---
title: "Problem with WAP 2022 - ADFS 2022 communication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/575405/problem-with-wap-2022-adfs-2022-communication
question_id: 575405
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Problem with WAP 2022 - ADFS 2022 communication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/575405/problem-with-wap-2022-adfs-2022-communication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have working ADFS, WAP both on Windows server 2019.  

I added ADFS, WAP both on Windows server 2022.  

WAP 2019 is working with ADFS 2019 and also with ADFS 2022.  

WAP 2022 is only working with ADFS 2019.  

When trying to refresh ADFS configuration on WAP 2022 against ADFS 2022 I receive error:  

Description:  

The federation server proxy was not able to authenticate to the Federation Service.   

User Action   

Ensure that the proxy is trusted by the Federation Service. To do this, log on to the proxy computer with the host name that is identified in the certificate subject name and re-establish trust between the proxy and the Federation Service using the Install-WebApplicationProxy cmdlet.   

Additional Data   

Certificate details:   

Subject Name:   

<null>   

Thumbprint:   

<null>   

NotBefore Time:   

<null>   

NotAfter Time:   

<null>   

Install-WebApplicationProxy is not helping. Certificate (wildcard) is the same on all servers - triple checked.  

Anybody with working WAP 2022 against ADFS 2022?  

Thank you  

Richard

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 1 · updated: 2022-04-12*

thanks @Pierre Audonnet - MSFT   disabling the 1.3 tls on wap 2022 helped me as well.  I'm using 2022 servers both for adfs and WAP.    

Cheers,    

Chinmoy

## Answer (community) — community member

*upvotes: 1 · updated: 2021-11-13*

Thank you very much! Works like a charm now.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-10-06*

Hello RichardMlynka,  

From my experience 3 factors can produce the issue:   

a) the certificate thumbprint is not the same ( you have discarded this)  

b) the problematic WAP server has been more than 2 weeks disconnected from the environment, as the proxy trust certificate is a rolling certificate valid for 2 weeks and periodically updated. (being a new installation I would not suspect of it)  

c) for some reason the 2022 version is not able to properly update the registry key corresponding to proxy configuration  

In this case you can check the next key in the problematic server. Ensure that the value is set to 1, and then re-run the post-install config from the Management console.  

HKLM\Software\Microsoft\ADFS  

ProxyConfigurationStatus  

1 (not configured)  

2 (Web Application Proxy is configured)   

--If the reply is helpful, please Upvote and Accept as answer--
