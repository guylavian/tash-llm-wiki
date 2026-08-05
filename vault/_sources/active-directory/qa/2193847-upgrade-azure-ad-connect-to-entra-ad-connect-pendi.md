---
title: "Upgrade: Azure AD Connect to Entra AD connect pending updates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193847/upgrade-azure-ad-connect-to-entra-ad-connect-pendi
question_id: 2193847
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Upgrade: Azure AD Connect to Entra AD connect pending updates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193847/upgrade-azure-ad-connect-to-entra-ad-connect-pendi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am upgrading Azure AD Connect from version 2.2.1.0 to Entra AD Connect v 2.3.20.00 using the swing migration method.

I have installed Entra AD Connect v 2.3.20.00 in staging mode on the new server using the following steps:

Microsoft Entra Connect: Upgrade from a previous version - Microsoft Entra ID | Microsoft Learn

I have exported the config from the active server and imported it into the new staging server. The synchronization service doesn't appear to show any issues.

However step 4 of the guide I followed specifies that I must verify the configuration of the new staging server by exporting a file which lists all changes that will be exported.

I have done this and found for every user there is an Update for the onPremisesObjectIdentifier, please see below - I have replaced values with xxxxx. The OldValue field for all is blank.

ObjectType
DN
OMODT
ChangedAttrCount
AttrName
AMODT
ATYPE
IsMultiValued
ValueChangeCount
ValueAdds
ValueDeletes
OldValue
NewValue

user
xxxxx
update
1
onPremisesObjectIdentifier
add
binary
FALSE
1
1
0

xxxxx

I am unsure if these changes should be expected?

I have read in the release notes for version 2.2.8.0:

-  The attribute onPremisesObjectIdentifier has been added to the default sync rules. This attribute is required by Microsoft Entra Cloud Sync's Group Provisioning to AD feature.

The next step would be to make the active server a staging server and make the staging server active but I'm concerned that these pending updates might cause synchronization issues.

Any help would be appreciated.

Thanks.

## Answers

_No answers on this thread._
