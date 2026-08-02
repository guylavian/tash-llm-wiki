---
title: "List Active Directory User Attribute OID's"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1499749/list-active-directory-user-attribute-oids
question_id: 1499749
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# List Active Directory User Attribute OID's

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1499749/list-active-directory-user-attribute-oids (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are setting up ADFS to connect with an external vendor. The "names" they user for account attributes does not line up with AD so they sent us the OID's of the objects they accept. One of the OID's they sent comes up as "userID" when I searched online, but what does this line up to in AD? When I looked up the OID for SaMAccount it seems to have a different OID. Is there a way to list the OID's of each attribute on a user account?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-18*

Hi rr-4098,

The Attribute-Id in the attribute list given by JimmySalian-2011 is the same as OID. You can try the PowerShell script like below to list the OIDs of the attributes of a user account. Replace $User with your user name.

```
$User = "test"
$SchemaPath = (Get-ADRootDSE).schemaNamingContext
(Get-ADUser $User -Properties *).PSObject.Properties.Name | ForEach-Object {
    Get-ADObject -SearchBase $SchemaPath -Filter 'lDAPDisplayName -eq $_' -Properties lDAPDisplayName,attributeID | Select-Object -Property lDAPDisplayName,attributeID
}
```

Best Regards,

Ian Xue

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2024-01-17*

HI,

They could be referring to a custom attribute in AD, however you can check the complete list of AD Attributes over here https://learn.microsoft.com/en-us/windows/win32/adschema/attributes-all.

Hope this helps.
JS

==
Please Accept the answer if the information helped you. This will help us and others in the community as well.
