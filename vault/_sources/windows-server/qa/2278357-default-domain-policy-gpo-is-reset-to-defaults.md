---
title: "Default Domain Policy GPO is reset to defaults."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2278357/default-domain-policy-gpo-is-reset-to-defaults
question_id: 2278357
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Independent Advisor", "Q&A User"]
---
# Default Domain Policy GPO is reset to defaults.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2278357/default-domain-policy-gpo-is-reset-to-defaults (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have a recurrent problem in our Active Directory, that we want to fix

Time to time we have a problem with the 'Default Domain Policy' GPO , it is reset to "defaults"

On the 'Default Domain Policy' GPO, is where we have put the settings regarding password policies.

We have been investigating the incident looking at the Events, but we haven't found any real explanation for the incident, we are speculating about some replica problem, or something similar..

Another point that is not clear by us, is that when We check the default domain password policy with the command:

Get-ADDefaultDomainPasswordPolicy

for example, it returns "MinPasswordLength : 6'

the password settings are not the same as we have set on the DDP GPO, We have set the MinPasswordLenght to 10

Are these settings applies on different scopes? Aren't these settings values synced with Default Domain policies?

What is the relationship between these settings and Default Domain Policy? There is some priority for these policies

If both policies should have the same values, why are not in sync?

When Default domain policy is reset 'magically', then it get these values that we got with "Get-ADDefaultDomainPasswordPolicy" that are set on the properties of the main domain Object.

And the last point, when we check a GPRESULT, the password settings that we are receiving comes from the GPO

May you please give some advice about this problem?

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-28*

We have discovered this Deny permission on DOMAIN OBJECT

This setting doesn't allow modify default password settings for domain, and when a property of the domain object is updated it performs a 5136 events that modifies or updates default domain GPO.

But with the Deny ACL that doesn't allow modification of passwords settings, the Default Domain policy gets default values from the Object domain.

Regards

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-05-26*

Hello,

```
Thank you for posting question on Microsoft Windows forum!

Based on your query of running command **Get-ADDefaultDomainPasswordPolicy**, the value for MinPasswordLenght should be 10 as being set in Default Domain Policy instead of 6.  it is reasonable to suspect that you have created a multiple password policy in your environment. Basically, a default password policy in Default Domain Policy at the domain level will be applied. Regardless of other GPO password policies being linked to the same domain level. However, if that GPO password policy being placed on top of Default Domain Policy at the domain level and its Links Order is higher than DDP. the password setting in GPO password policy will take precedence over the one in Default Domain Policy.
```

   As a result, you should make sure and check your environment that the Default Domain Policy is always placed on top at the domain level and its Links Order is higher than any other GPO password policies like below screenshot.

  In addition to that, in your case, it is advisable to check the DFR/Sysvol replication state which should be 4 on all Domain Controllers by using below command to confirm policy replication.

-  For /f %i IN ('dsquery server -o rdn') do @echo %i && @wmic /node:"%i" /namespace:\root\microsoftdfs path dfsrreplicatedfolderinfo WHERE replicatedfoldername='SYSVOL share' get replicationgroupname,replicatedfoldername,state    For more information https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares

Hope the above information is helpful!
