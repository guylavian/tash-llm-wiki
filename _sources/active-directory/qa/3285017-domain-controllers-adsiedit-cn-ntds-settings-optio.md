---
title: "Domain Controllers ADSIEdit CN=NTDS Settings Options Attribute Value"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3285017/domain-controllers-adsiedit-cn-ntds-settings-optio
question_id: 3285017
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Domain Controllers ADSIEdit CN=NTDS Settings Options Attribute Value

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3285017/domain-controllers-adsiedit-cn-ntds-settings-optio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am going through my domain controllers and looking at the Options attribute in ADSIEdit under:

"CN=GUID,CN=NTDS Settings,CN=SERVER-NAME2,CN

=Servers,CN=SITE-NAME,CN=Sites,CN=Configuration,DC=DOMAIN,DC=COM"

I have seen three values in the Options field:

0x0 = ( )

0x1 = ( IS_GENERATED )

0x5 = ( IS_GENERATED | OVERRIDE_NOTIFY_DEFAULT )

To my knowledge, this attribute reflects how the KCC treats the connection object in AD Sites and Services.  If the Options attribute is 0x0, the connection object was manually create and the KCC will not manage it.  If the Options attribute is 0x1, the
 connection object was automatically created by the KCC and the KCC will manage the object.  But I do not know what 0x5 means.  Is anyone aware of what this value is?  Can I change the value to 0x1?  If I do change it to 0x1, are there any negative consequences? 
 Thanks.

## Answers

_No answers on this thread._
