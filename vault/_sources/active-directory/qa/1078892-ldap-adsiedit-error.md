---
title: "LDAP - ADSIEdit error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1078892/ldap-adsiedit-error
question_id: 1078892
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# LDAP - ADSIEdit error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1078892/ldap-adsiedit-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings,    

I am trying to set-up LDAP on an AWS Instance.    

I followed the steps to set-up LDAP, but get an error, when I try to run the Connection Settings.    

    

I would appreciate any tips to resolve this issue.    

Thanks    

Clive

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-11-10*

Hello    

When creating an instance, you must create an application partition with a distinguished naming format, you can look at the following registry key "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\ADAM_instance1\Parameters", then look at the value of "Configuration NC" and try to connect to it.    

You can also go to the CN=Partitions container to find other NCs in this AD LDS instance, right-click it and click New Connection to Naming Context, which will connect ADSIEdit to that NC.    

NDNs in ADLDS have GUIDs as their DNs (as seen in the "Partitions" container)    

Best Regards,    

Wesley Li
