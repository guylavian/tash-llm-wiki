---
title: "Unable to update Windows 10 via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/756331/unable-to-update-windows-10-via-gpo
question_id: 756331
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Unable to update Windows 10 via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/756331/unable-to-update-windows-10-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have about 250 laptops and 160 desktops in my organization    

I am not using SCCM for windows update yet. I do not mind them connecting to internet to download updates from Microsoft    

The issue is I am unable to force them to update via GPO that I configured    

Computer Config \ Policies \ Admin. Templates \ Windows Components \ Windows Update \ Configure Automatic Updates \ Option number 4. Download and schedule Install    

First Issue    

When I do Group Policy update from GPMC, I get    

a. The remote procedure call was cancelled.    

b. The RPC server is unavailable.    

Second Issue    

When I go to user PC for success of Group Policy update, they do not have option to "Check online for Microsoft Update"    

As per the image below, 19041.1348 is not the latest path for 19041 version of windows.     

The latest version is 19041.1415.    

    

Though I would like the machines to be updated to Windows 10 21H2 (19044.1566)    

Please help assist in updating the PCs and Laptops    

Thank you

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2022-03-03*

You have left out Active Hours.  

You've enabled - Do not allow update deferral policies to cause scans against Windows Update  

You've enabled - No auto-restart with logged on users for scheduled automatic updates installations  

You've set a manual registry setting for DoNotEnforceEnterpriseTLSCertPinningForUpdateDetection  

Follow my guide:  

https://www.ajtek.ca/wsus/how-to-setup-manage-and-maintain-wsus-part-4-creating-your-gpos-for-an-inheritance-setup/  

FYI - you have a lot of "Local Group Policy" entries - you're going to come to hate those. I assume it's baked into the image that you've deployed out. Whoever did that didn't have the foresight that it may cause problems later.  

GPO will 'overwrite' these, however GPOs are accumulative and if you don't overwrite these, they are the sum of the policies.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2022-03-02*

From an Administrative Command Prompt on an affected client, run the following:  

gpresult /h gpo.htm  

and share the result with your favourite method or pastebin it so that we can see it.  

Also,   

From PowerShell, run:  

```
$(New-Object -ComObject "Microsoft.Update.ServiceManager").Services | Select-Object Name, IsDefaultAUService
```

And post the output.
