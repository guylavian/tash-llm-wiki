---
title: "Active Directory Optional Features not being enabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1368591/active-directory-optional-features-not-being-enabl
question_id: 1368591
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory Optional Features not being enabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1368591/active-directory-optional-features-not-being-enabl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey Team!  

I am facing an issue for some days already that has me puzzled. I am trying to enable 'Privileged Access Management Feature' in our AD, but I keep getting the error 'The parameter is incorrect'.

The command I am using is 
`Enable-ADOptionalFeature -Identity 'Privileged Access Management Feature' -Scope ForestOrConfigurationSet -Target (Get-ADForest)`

We have a second forest and it worked like a charm, but for some reason I do not get it fails in this one.

Requirements are fulfilled:

-  Elevated PowerShell

-  Forest functional level 2016

-  All DCs in at least Windows Server 2016.

The only errors I could find are 

-  Event Viewer Administrative Events

-  Source: `ActiveDirectory_DomainServices`

-   Level:  `Error`

-  Event ID: `2959`

-  Message:

- 

Optional feature name:  

[]  

Optional feature guid:  

ec43e873-cce8-4640-b4ab-07ffe4ab5bcd  

Scope of optional feature:  

CN=Partitions,CN=Configuration,DC=intapps,DC=it  

Error value:  

57  

Internal ID (DSID):  

3210e76

-  PowerShell Error details

- 

Exception : Microsoft.ActiveDirectory.Management.ADInvalidOperationException: The parameter is incorrect ---> System.ServiceModel.FaultException`1[schemas.microsoft.com._2008._1.ActiveDirectory.CustomActions.ChangeOptionalFeatureFault]: Active Directory returned an error processing the operation.

Just in case it is relevant, this problematic AD shows 3 optional features:

-  Recycle Bin Feature (Enabled)

-  Privileged Access Management Feature. (Disabled - Trying to get it up)

-  Expiring Group Membership Feature. (Disabled)   In the parallel working forest there are only 2 features available:

-  Recycle Bin Feature (Enabled)

-  Privileged Access Management Feature. (Enabled)   I also find quite intriguing that the third feature that does not appear anywhere in the documentation. And it shares the same Feature ID with the one I want to enable:

Name        : Privileged Access Management Feature  

FeatureGUID : ec43e873-cce8-4640-b4ab-07ffe4ab5bcd  

ObjectGUID  : 211d2d6b-d4df-409c-bedc-0279992d2638

Name        : Expiring Group Membership Feature  

FeatureGUID : ec43e873-cce8-4640-b4ab-07ffe4ab5bcd  

ObjectGUID  : 6bdba10d-d7bb-45e6-abd1-8419f8094149

Does anyone have any advise about how can I sort this situation?

Thanks in advance for your attention people!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-16*

So, I could solve it.

I am not sure how the record arrived there but that 3rd Optional Feature was causing the issue. My best guess is that it arrived there after an schema update. What I did was:

-  Open LDP.exe and bind my Schema Admin to it.

-  Navigate to CN=Optional Features,CN=Directory Service,CN=Windows NT,CN=Services,CN=Configuration,DC=X

-  Remove 'Expiring Group Membership' object.

After that, I could enable 'Privileged Access Management Feature' without any issues.

I ran some checks to ensure everything was still in its place -> https://windowstechno.com/how-to-check-the-active-directory-database-integrity/

As a note: in my case was easy because my AD was not big and I could take it down entirely during out of office hours and get a proper backup of it. But in general, it is not a good idea nor simple to play around with the schemas due to replication across DCs. Be always as cautious as you can and a bit more.
