---
title: "ADFS Web App Proxy Not Allowing External and Backend URLs to Differ"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/784572/adfs-web-app-proxy-not-allowing-external-and-backe
question_id: 784572
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Web App Proxy Not Allowing External and Backend URLs to Differ

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/784572/adfs-web-app-proxy-not-allowing-external-and-backe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to publish a web application on a 2019 Datacenter server using ADFS Web Application Proxy, the older version, not the Azure version. We are replacing an old TMG setup with ADFS Web Application Proxy, that is, trying to.    

When I read the documentation here, https://learn.microsoft.com/en-us/windows-server/remote/remote-access/web-application-proxy/publishing-applications-using-ad-fs-preauthentication it seemed to me that I could use the following configuration and the website would work:    

External URL: https://app.domain.com/website/     

Backend Server URL: https://appserver.domain.com/website/    

I ran the PowerShell script to enable URL translation    

Set-WebApplicationProxyApplication -ID appID -DisableTranslateUrlInRequestHeaders:$false    

but the site still doesn't run. I can get to the site using the Backend Server URL, no problem, but I can't get to it using the External URL. I did publish the web application using the same backend server URL and external URL and that works as expected, but I need to change the external URL so it's not showing the server name.    

All I know is that I set it up exactly as the document told me to, and it doesn't work - Chrome says    

 This site can't be reached. DNS_PROBE_FINISHED_NXDOMAIN    

Are there other steps I need to take within ADFS to allow the reverse proxy functionality of the URLs to work? I just have a basic relying party trust set up for the websites, nothing complicated. Can someone help me figure out what I'm doing wrong?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-03-23*

That works for me as long as the path are identical. Maybe it is indeed a DNS failure? Maybe your test client doesn't know about that published name because it is not in the DNS that it is using?  

The UPN message is irrelevant to this configuration. It is only for device registration using ADFS (which isn't really a thing anymore).
