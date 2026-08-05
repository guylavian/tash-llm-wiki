---
title: "GPO for limiting internet access to single site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/159589/gpo-for-limiting-internet-access-to-single-site
question_id: 159589
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO for limiting internet access to single site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/159589/gpo-for-limiting-internet-access-to-single-site (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We are trying to set-up certain workstations to only allow access to our ticketing site.     

I found this    

but couldn't find the setting to create the policy.    

Any help would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-18*

Hi,  

Just checking in to see if the information provided was helpful.  

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-12*

Open up Group Policy Management Console (GPMC).  

Create a New Group Policy Object and name it Restrict Internet Access.  

Edit and navigate to: User Configuration -> Preferences -> Windows Settings -> Registry and create a New Registry Item.  

There are 4 registry items we need to create/update: ProxyEnable, ProxyServer, ProxyOverride, AutoDetect  

The EnableProxy key will check the box to force the browser to use the proxy settings.  

Under the General Tab for the New Registry Properties:  

Action: Update. This will also create the reg key if it doesn’t exist.  

Hive: HKEY_CURRENT_USER  

Key Path: SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings  

Value Name: ProxyEnable  

Value Type: REG_DWORD  

Value Data: 1  

Base: Hexadecimal  

For specific steps, please refer to the article in the link  

https://thesysadminchannel.com/how-to-restrict-internet-access-using-group-policy-gpo/  

Hope this information can help you  

Best wishes  

Vicky
