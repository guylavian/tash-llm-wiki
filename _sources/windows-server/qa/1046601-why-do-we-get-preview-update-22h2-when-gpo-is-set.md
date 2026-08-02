---
title: "Why do we get preview update 22H2 when GPO is set for Semi-Annual Channel?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1046601/why-do-we-get-preview-update-22h2-when-gpo-is-set
question_id: 1046601
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Why do we get preview update 22H2 when GPO is set for Semi-Annual Channel?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1046601/why-do-we-get-preview-update-22h2-when-gpo-is-set (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Most PC's in our organization have been upgraded to Windows 10 22H2, however according to https://learn.microsoft.com/en-us/windows/release-health/release-information 21H1 is the latest released version. Why is that? How do we avoid getting preview versions?    

We have set up WSUS distribution rings, where ring 0 is set for Release Preview and contains a few PC's in the IT department. The higher rings are set for Semi-Annual Channel, delayed 0, 30 and 60 days.    

To check if the GPO settings works, I checked registry at some of the PC's which was upgraded to 22H2. BranchReadinessLevel is set to 16 (0x10), which means Semi-Annual Channel according to https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.WindowsUpdate::DeferFeatureUpdates so the GPO has set the correct value.    

    

A weird thing is that the GPO GUI has the choices shown below, but after selecting "Semi-Annual Channel" and saving settings the GUI shows "Semi-Annual Channel (Targeted) for 1809 and below (Depreciated)". This may be because both choices use the value of 16 according to the link above.    

    

I am using ADMX for 21H2, which seems to be the newest available.    

Our WSUS is WS2016 version 1607.    

AD domain and forest functional level WS2008R2.    

What am I missing to avoid getting preview updates distributed to all PC's in the organisation?

## Answer (community) — community member

*upvotes: 1 · updated: 2022-10-19*

After 6 days no answer to my question, however I will share what I find during my research in case it is useful to others.

I saw at https://learn.microsoft.com/en-us/windows/release-health/release-information that Windows 10 22H2 has been released yesterday.  

Also, I saw in the table that the term "Semi-Annual Channel" has not been used since 21H1, now it is called "General Availability Channel".

I wonder why my GPO GUI using the ADMX for 21H2 still says "Semi-Annual Channel".

While searching for "General Availability Channel" I found this interesting article dated 2022-07-14:  

https://learn.microsoft.com/en-us/windows/deployment/update/waas-configure-wufb

Searching this page for the registry key "BranchReadinessLevel" reveals something interesting!

1) When using the MDM key BranchReadinessLevel can have the values 2, 4, 8 and 32 - but 16 is not mentioned:

2: systems take feature updates for the Windows Insider build - Fast (added in Windows 10, version 1709)  

4: systems take feature updates for the Windows Insider build - Slow (added in Windows 10, version 1709)  

8: systems take feature updates for the Release Windows Insider build (added in Windows 10, version 1709)  

32: systems take feature updates from General Availability Channel  

Note: Other value or absent: receive all applicable updates

2) When using the GPO key BranchReadinessLevel can have the same values, except 32 is not mentioned:

2: systems take feature updates for the Windows Insider build - Fast (added in Windows 10, version 1709)  

4: systems take feature updates for the Windows Insider build - Slow (added in Windows 10, version 1709)  

8: systems take feature updates for the Release Windows Insider build (added in Windows 10, version 1709)  

Other value or absent: receive all applicable updates

So it seems because our GPO sets BranchReadinessLevel to 16 it means "receive all applicable updates" - so we get everything.  

What I want is "32: systems take feature updates from General Availability Channel".

However, 32 is missing from the GPO table, which means there is no way to get feature updates from General Availability Channel - my guess this is an error in the table.

But it gets more confusing: This article, https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-update dated 2022-10-18 says:

"As of 1903, the branch readiness levels of General Availability Channel (Targeted) and General Availability Channel have been combined into one General Availability Channel set with a value of 16. For devices on 1903 and later releases, the value of 32 isn't a supported value."

However, this article is about MDM, not GPO. But it does not agree with the article dated in July, shown above.

Anyway, I should not worry about registry values, as our GPO with the correct ADMX version should set values correctly.  

I have to check if my 21H1 ADMX is installed correctly, since it still uses the term "Semi-Annual Channel".

To be continued... :-)

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-03-29*

So, first thing, you're post leads me to believe you do not have an updated set of Administrative Templates (ADMX) files

https://www.ajtek.ca/wsus/how-to-setup-manage-and-maintain-wsus-part-3-windows-as-a-service-waas-and-group-policy-administrative-templates/

Once you update your ADMX files, you should see what you're looking for. Always use the LATEST version (Win1122H2 in this case)

I'd also recommend reading my entire series as it too gives you pointers to have a ring-based deployment using WSUS. Part 4 shows the policies, and part 5 the applying of the GPOs for an inheritance setup. Part 6 is the approvals process.

You're specifying WUfB policies when using WSUS - you're creating a dual scan scenario

https://www.ajtek.ca/wsus/dual-scan-making-sense-of-why-so-many-admins-have-issues/
