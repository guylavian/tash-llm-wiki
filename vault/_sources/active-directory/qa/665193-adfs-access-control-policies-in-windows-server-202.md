---
title: "ADFS Access Control Policies in windows Server 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/665193/adfs-access-control-policies-in-windows-server-202
question_id: 665193
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Access Control Policies in windows Server 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/665193/adfs-access-control-policies-in-windows-server-202 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am testing ADFS in a lab environment on some Windows Server 2022 servers.  

I can't locate up-to-date documentation about "Access Control Policies".  

Let me ask for some clarifications:  

-  After creating a new Access Control Policy, how can I set it to be "in use"?  

-  During the creation of a new Access Control Policy I see two tabs: "General" and "Assigned to": what should I enter in "Assigned to" to assign it to the whole of the ADFS portal?  

Where can I locate detailed documentation about ADFS in Windows Server 2022?  

Regards

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-15*

The Access Control Policy feature has not changed since its creation. The ADFS on Windows Server 2016 documentation is still accurate on this topic.    

The policy can be assigned from the Relying Party Trust section.    

    

If your environment was upgraded from Windows Server 2012 R2 to higher (either to 2016/2019 or directly to 2022) and the Relying Party was created prior this upgrade, it might not display the Access Control Policy window when you click there but this instead:    

    

In that case you can just delete the rules you see there and then apply an Access Control Policy like aforementionned.    

You can also backup the current rules in case you want to go back:    

```
Get-AdfsRelyingPartyTrust -Identifier "" | Select-Object -ExpandProperty IssuanceAuthorizationRules | Out-File IssuanceAuthorizationRules.bk  
Get-AdfsRelyingPartyTrust -Identifier "" | Select-Object -ExpandProperty AdditionalAuthenticationRules | Out-File AdditionalAuthenticationRules.bk
```

And you can restore them this way:    

```
Set-AdfsRelyingPartyTrust -TargetIdentifier "" -IssuanceAuthorizationRulesFile IssuanceAuthorizationRules.bk  
Set-AdfsRelyingPartyTrust -TargetIdentifier "" -AdditionalAuthenticationRulesFile AdditionalAuthenticationRules.bk
```
