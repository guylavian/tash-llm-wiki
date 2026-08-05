---
title: "ADFS 2019 and redirect links"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/727479/adfs-2019-and-redirect-links
question_id: 727479
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 2019 and redirect links

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/727479/adfs-2019-and-redirect-links (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have recently migrated my Win2012 ADFS and ADFS Proxy, to Win2016 ADFS with a Win2019 WAP server. On my ADFS Proxy server, I had an IIS redirect to assist with shortening the ADFS URLs - such as "https://adfs.aaaa.com/o365login" instead of "https://adfs.aaaa.com/adfs/ls/idpinitiatedsignon.aspx?loginToRp=http://www.officeonline.ms.com/blahblah". With WAP, installing IIS is not recommended, how do I go about fixing this and maintaining the older shorter URLs? Any advice or suggestions are appreciated.  

Thank you,  

Sau

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-14*

Hi Piaudonn,  

The O365 was just an example. We are working with O365, and other 3rd party services and all of the services have long URLs for ADFS such as "https://adfs.aaaa.com/adfs/ls/idpinitiatedsignon.aspx?loginToRp=http://www.oracle.com/sso.jsp." Now, I'd rather give my users a  shorter version to remember - say "https://adfs.aaaa.com/oracle" and am trying to understand how I can do that without using IIS.  

You mentioned, I can do that using WAP, and I tried Publishing one, but it won't let me change the URL and prefers the same URL. What am I missing here? How are others with ADFS assisting their users to access the 3rd party applications using SSO with shorter URLs?  

Thanks,  

Sau

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-14*

AD FS and WAP are both agnostic of that redirecation. They just see what hits them. Your redirection service could be hosted anywhere. And is that is meant to be use externally only, you can even publish it with WAP.  

I am not sure about your example though, are you using redirection for Office 365 realted things?
