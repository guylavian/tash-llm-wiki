---
title: "EWS - custom extended properties and PidLidPropertyDefinitionStream?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/289601/ews-custom-extended-properties-and-pidlidpropertyd
question_id: 289601
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# EWS - custom extended properties and PidLidPropertyDefinitionStream?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/289601/ews-custom-extended-properties-and-pidlidpropertyd (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I am setting some extended properties through EWS. Below is the code I have. Now, I have to also set the "PidLidPropertyDefinitionStream" in order to get my code woking properly, but that property is a binary type. Can anyone give me sample code for setting that binary property? Any help would be hugely appreciated!     

https://learn.microsoft.com/en-us/office/client-developer/outlook/mapi/pidlidpropertydefinitionstream-canonical-property    

```
var myCustomProp = new ExtendedPropertyDefinition(  
                                          DefaultExtendedPropertySet.PublicStrings,  
                                         "SkypeTeamsProperties",   
                                         MapiPropertyType.String);  
  
appointment.SetExtendedProperty(myCustomProp, "test value");
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-28*

To set a Binary property just pass in a BinArray as the value and the Managed API will handle the rest. The value side of PidLidPropertyDefinitionStream is non-trival and you need to either copy an existing static value you know will always be the same or build your own code to construct the stream. (The stream itself contain underlying mapi properties of varying types).

```
Byte[] StreamValue;
            var PidLidPropertyDefinitionStream = new ExtendedPropertyDefinition(
                                          DefaultExtendedPropertySet.Common,
                                         0x8540,
                                         MapiPropertyType.Binary);

            appointment.SetExtendedProperty(PidLidPropertyDefinitionStream, StreamValue);
```
