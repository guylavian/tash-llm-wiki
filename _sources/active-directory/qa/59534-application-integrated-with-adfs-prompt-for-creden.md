---
title: "Application integrated with ADFS prompt for credential every time"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/59534/application-integrated-with-adfs-prompt-for-creden
question_id: 59534
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Application integrated with ADFS prompt for credential every time

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/59534/application-integrated-with-adfs-prompt-for-creden (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

-  We have a application hosted in cloud infra and its integrated with ADFS which is available at onprem.  

-  ADFS Proxy Servers are placed at front end and NATed with Public IP  

-  Application when accessed from internal Network is working fine with SSO and not prompting for any additional authentication  

-  Same application when accessed from internet is prompting for authentication every time with ADFS page  

-  Office 365 and Teams which are also integrated with ADFS are not having any issue they are working fine with SSO when accessed from internal network of internet.  

Appreciate if any thought around this to fix this behavior.  

Regards  

Mahesh

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-08*

Thank you for response again.  

I was just looking for some article/references to integrate URL with Azure AD.  

Ex: URL is https://empbenifit.companyname.com  

Regards  

Mahesh

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-07*

Hi Pierre Audonnet,  

Thanks a lot for your response. I completely agree with you on the behavior of ADFS when application/URL is accessed from internet and authentication is passed through ADFS Proxy.   

Specific to our case, would like to share more details as below.  

-  We have an Always On VPN-Device tunnel for Windows10 devices  

-  Users are logging in with AD credentials and getting authenticated from AD Servers over AOVPN tunnel  

-  Internal ADFS Server is directly accessible over AOVPN tunnel.  

-  Specific application which i am referring is one of the Portal which is accessible over internet also.  

-  When user is accessing from Windows10 Laptop- AOVPN tunnel is connected and have accessibility to ADFS Server. Was thinking why this is still not taking token from ADFS directly rather than going through ADFS Proxy.  

Now i have 2 queries.  

-  If we need to Publish this through Azure AD Enterprise Application, how can we do this since its only organization specific URL. There is no WebApp or Mobile App.  

-  Assume that if its possible to publish through Azure AD then will it not prompt for credentials when accessed from Hybrid Azure AD joined Windows 10 and Azure AD registered(Intune MAM) mobile as well?  

Appreciate if you can provide details on this.  

Regards  

Mahesh
