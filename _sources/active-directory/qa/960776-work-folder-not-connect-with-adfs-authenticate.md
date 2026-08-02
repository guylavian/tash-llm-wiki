---
title: "work folder not connect with ADFS authenticate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/960776/work-folder-not-connect-with-adfs-authenticate
question_id: 960776
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# work folder not connect with ADFS authenticate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/960776/work-folder-not-connect-with-adfs-authenticate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have configured as ADFS to access work folders,  below link is exact configuration where I followed to to configure ADFS, WorkFolder and Web Application proxy,    

https://techcommunity.microsoft.com/t5/storage-at-microsoft/deploying-work-folders-with-ad-fs-and-web-application-proxy-wap/ba-p/425318    

everything seem correct but when I am trying to connect the work folder from control panel using work folder URL, it is giving me error saying "Trying to enter your latest password" Error Code: 0x80070005. I have tried from domain joined computers and non domain joined computers    

https://myadfs.mydomain.com/adfs/ls/idpinitiatedsignon.htm login success using active directory users as you see in following screenshot    

    

Below screenshot asking username and password for work folder URL when authenticate as federation service URL    

    

    

But when work folder URL authenticate as windows authenticate everything works

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-21*

Hello, Still getting following error when I am trying to connect work folder from a client computer

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-10*

Hi there,     

Check the following settings in Internet Options:    

-On the Advanced tab, make sure that the Enable Integrated Windows Authentication setting is enabled.    

-Following Security > Local intranet > Sites > Advanced, make sure that the AD FS URL is in the list of websites.    

-Following Security > Local intranet > Custom level, make sure that the Automatic logon only in Intranet Zone setting is selected.    

If you use Firefox, Chrome or Safari, make sure the equivalent settings in these browsers are enabled.    

Troubleshoot SSO issues with Active Directory Federation Services (AD FS) https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/troubleshoot-ad-fs-sso-issue    

Troubleshoot AD FS issues in Azure Active Directory and Office 365 https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/troubleshoot-ad-fs-issues    

I hope this information helps. If you have any questions please let me know and I will be glad to help you out.    

--------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
