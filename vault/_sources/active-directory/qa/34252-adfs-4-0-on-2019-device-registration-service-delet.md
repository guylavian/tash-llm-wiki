---
title: "ADFS 4.0 on 2019, Device Registration Service - deleted Relying Party Trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/34252/adfs-4-0-on-2019-device-registration-service-delet
question_id: 34252
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 4.0 on 2019, Device Registration Service - deleted Relying Party Trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/34252/adfs-4-0-on-2019-device-registration-service-delet (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am really struggling with this one.  I installed ADFS 4 on 2019 (yes, 2019 forest and domain levels), topology is one back-end federation server for the farm, one database server (SQL, not WID).  Haven't even setup the WAP yet...was playing with Device Registration and deleted the OOTB Device Registration Service RP Trust.  Now, no matter what I do I cannot get it to come back.  To make it worse, when I go into Device Registration in ADFS, now it says "Device registration is not configured. You must upgrade your AD FS Farm before you can configured device registration".  

Uninstalled reinstalled the ADFS services, done the initialize-ad and add-adfsdevice blah blah...nothing...that RP just will not come back and it keeps telling me the Farm needs to be upgraded.  On top of that, I have a test AD instance and tried bringing up new there...it's a slightly different config and no internet access and using WID....can't get the RP for Device Registration to show up there either, but it at least doesn't say my Farm needs to be upgraded.  How do I get this RP back - and more importantly, why isn't it naturally showing up on a new install...  How do I get the AD FS Farm upgrade status to change from amber back to green?  And for some lite rhetorical...  Why is there no real documentation for this stuff?  It's like MS is making this stuff up as we go along...VERY little documentation and I can't find any super-verbose logging to turn on to see if something is silently failing...end rhetorical.  

I'm going crazy!  

Quick update, I uninstalled, ADFS and removed the existing databases from SQL and reinstalled/reconfigured, and now it says Device Reg is enabled and configured, and it's green. But I still don't have a Relying Party Trust. Strange thing is that when I run Initialize-ADDeviceRegistration it doesn't error out anymore about not being able to set the mfa access control policy to Device Registration Relying Party trust... It just completes successfully without warning - yet there is no RP trust...

## Answer (community) — community member

*upvotes: 0 · updated: 2020-06-12*

Running that powershell does show the DRS and issuance transforms...but nothing about an RP (unless that IS the RP and just isn't worded that way).  If that is the case then there must have been a bug that allowed it to show up as an RP trust.  

It is very strange...I've been doing this a long time and I know I saw the RP trust...I'm wondering if there is a chance it was an artifact that shows up under the right conditions...I'm sure it was there because I intentionally deleted it.  In fact, the chain of events was that I deployed ADFS4, got curious and enabled Device Registration thinking it would JUST be for ADFS clients, then saw that magically (and very unwanted) I had all of my domain-bound computers starting to try to register with the service - even though I didn't change any policy or configure them to, they just magically started trying to Join.  I immediately started trying to undo the Device Registration enablement.  The first thing I did was Disable Device Registration, which made it go amber from green, but at this point it said the forest was already prepped - and I wanted to un-prep it.  Then because they kept trying to enroll spontaneously and pretty much with an ongoing flood, I deleted the RP from this totally fresh ADFS.  It asked me if I wanted to delete it and I thought, yes, no way to back it up, if I want to put the RP back after more testing, I'll just reinstall ADFS...nope...gone for good.  So, not sure if there was something about my domain/forest that allowed a bug to surface and create the RP and maybe completing the enablement, the first time, of the ADFS install prevented the RP from ever being recreated.  Couldn't reproduce this in the test environment which tells me some VERY specific condition was met originally to result in this RP having been created or at least be exposed visibly in the GUI.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-06-12*

I am not sure about what you deleted. But the RP does no longer show up in the GUI of the ADFS console since 2016.  

You can list in in PowerShell:  

```
Get-AdfsDeviceRegistration
```

You don't see it there either?
