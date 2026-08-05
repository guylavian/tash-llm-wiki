---
title: "SAP SuccessFactors to Active Directory user provisioning not updating attribute in on-premises Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1184252/sap-successfactors-to-active-directory-user-provis
question_id: 1184252
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# SAP SuccessFactors to Active Directory user provisioning not updating attribute in on-premises Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1184252/sap-successfactors-to-active-directory-user-provis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Success Factors Inbound Provisioning is not updating attribute values when differences exist between source and target. 

In this case, we have a rule to direct flow the Success Factors attribute businessUnitId to Active Directory attribute extensionAttribute12. When manually invoking 'Provision On Demand', we see the value from Success Factors is different from the Active Directory value; however, the value is not updated. The Active Directory value reported by the provisioning agent is the old value. No update is reported by the agent and the value in Active Directory remains unchanged with the old value.

If I delete the value in Active Directory and execute 'Provision On Demand,', the new value is populated.

The attribute flow is configured as below. We expect the "apply this mapping: Always" to always update the attribute when different.

This is repeatable and affects multiple records.

(FWIW, I have experienced numerous instances where a value is not reported as flowing by the "provision on demand" report even though the value is populated in Active Directory. I have not been able to reliably repeat this condition.)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-07*

Unfortunately, I haven't found a fix yet. As I state earlier, it appears to be a reporting error in the portal so likely something Microsoft needs to fix up in the back end.
