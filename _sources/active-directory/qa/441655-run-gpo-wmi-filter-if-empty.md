---
title: "run gpo wmi filter if empty"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/441655/run-gpo-wmi-filter-if-empty
question_id: 441655
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# run gpo wmi filter if empty

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/441655/run-gpo-wmi-filter-if-empty (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have wmi filter script that i need him run gpo if filter is empty  

Is there a syntax that can run this?  

my syntax is   

Get-wmiobject -query 'select licensestatus from softwarelicensingproduct where LicenseStatus like 1'  

and i dont want to run gpo in computers that have LicenseStatus =1  

in the computers with LicenseStatus =1  has all the numbers that the computer does not have  LicenseStatus =1  

I am looking for a way to run gpo on all computers where there is no haveLicenseStatus =1

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-05*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-30*

Hi，  

Thank you for your understanding and support.  

Did you follow the correct steps provided?  

It can be successful in my environment, so you can follow this step  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-21*

under:  User Config > Policies > Admin Templates  

Depending on the setting you want to deploy, you can replace ADM  

templates with GPP Registry - the registry keys can be found either in  

the ADMX files or at http://gpsearch.azurewebsites.net  

Sample for that scenario:  

http://evilgpo.blogspot.de/2012/03/how-to-save-my-screen.html
