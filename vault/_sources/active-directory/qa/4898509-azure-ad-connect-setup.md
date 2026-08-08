---
title: "Azure AD Connect Setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4898509/azure-ad-connect-setup
question_id: 4898509
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Azure AD Connect Setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4898509/azure-ad-connect-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi,

i did in-place upgrade adfs server from server 2008 r2 to sever 2012 recently. sso is working after upgrade. when i install aad connect to replace dirsync, i have couple issues.

-  if choose "use an existing windows server 2012 r2 ad fs farm", which we do have, the next button is greyed out on service account page. (username is pre-filled by wizard and i typed correct password)

![](http://fud.community.services.support.microsoft.com/Fud/FileDownloadHandler.ashx?fid=70e53cb1-4e85-4c3b-a363-f5ad08b11ee4)

![](http://fud.community.services.support.microsoft.com/Fud/FileDownloadHandler.ashx?fid=d728bdeb-2e43-4a25-992c-146c61decbcf)

-  if i choose "configure a new windows server 2012 r2 ad fs farm ", it gives an error in the end:

microsoft.online.deployment.powershell.powershellinvocationexception: an error occurred while executing the 'set-msoladfscontext' command. the 'microsoft.adfs.powershell' active directory federation services 2.0 snap-in for windows powershell could not register
 on 'srv-adfs.xxx' computer.  make sure that you either specify the name of the active directory federation services 2.0 server using the -computer parameter or that you are running the installation on the ad fs 2.0 server.

![](http://fud.community.services.support.microsoft.com/Fud/FileDownloadHandler.ashx?fid=fdb95027-c83c-47bb-bf8a-5b7d4b11d0ec)

![](http://fud.community.services.support.microsoft.com/Fud/FileDownloadHandler.ashx?fid=7bc8deed-7156-4dc5-9e24-56a657d5842b)

can someone give me some help?

regards

andrew

## Answer (community) — community member

*upvotes: 0 · updated: 2016-01-07*

Hi Andrew,  

As I understand it after reading your description, you have completed your ADFS configurations before, and now you just want to replace the old DirSync tool with the new AADConnect tool.  

If this is true, then you don’t need to go through the entire ADFS configuration process which is integrated in the AADConnect tool. That process is just for administrators who haven’t deployed the ADFS configuration at all. As you also mentioned, the SSO service
 is actually working fine now. Therefore, you just need to complete the wizard merely as a synchronization tool, and skip the steps regarding ADFS configuration.  

And if I misunderstood anything about the current situation, please feel free to correct me.  

Thanks,  

Allen
