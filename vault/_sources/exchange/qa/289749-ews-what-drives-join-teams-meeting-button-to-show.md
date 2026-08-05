---
title: "EWS - What drives \"Join Teams Meeting\" button to show"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/289749/ews-what-drives-join-teams-meeting-button-to-show
question_id: 289749
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# EWS - What drives "Join Teams Meeting" button to show

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/289749/ews-what-drives-join-teams-meeting-button-to-show (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I am using EWS to schedule a meeting with a teams link info. I can get the "join teams meeting" button (outlook plug-in) to show for a single instance meeting, by adding teams data to the appointment's extended properties. Code below. But, for some reason, this doesn't work for meeting series. Any ideas? Is there any other extended property I have to set?     

    

```
appointment.SetExtendedProperty(new ExtendedPropertyDefinition(  
                        DefaultExtendedPropertySet.PublicStrings,  
                        "OnlineMeetingConfLink",  
                        MapiPropertyType.String), "test");  
    appointment.SetExtendedProperty(new ExtendedPropertyDefinition(  
                        DefaultExtendedPropertySet.PublicStrings,  
                        "SchedulingServiceUpdateUrl",  
                        MapiPropertyType.String), "test");  
    appointment.SetExtendedProperty(new ExtendedPropertyDefinition(  
                        DefaultExtendedPropertySet.PublicStrings,  
                        "SkypeTeamsMeetingETag",  
                        MapiPropertyType.String), "test");  
    appointment.SetExtendedProperty(new ExtendedPropertyDefinition(  
                        DefaultExtendedPropertySet.PublicStrings,  
                        "SkypeTeamsMeetingUrl",  
                        MapiPropertyType.String), "test");  
    appointment.SetExtendedProperty(new ExtendedPropertyDefinition(  
                        DefaultExtendedPropertySet.PublicStrings,  
                        "SkypeTeamsProperties",  
                        MapiPropertyType.String), "test");  
    appointment.SetExtendedProperty(new ExtendedPropertyDefinition(  
                        DefaultExtendedPropertySet.PublicStrings,  
                        "TeamsVtcConferenceId",  
                        MapiPropertyType.String), "test");  
    appointment.SetExtendedProperty(new ExtendedPropertyDefinition(  
                        DefaultExtendedPropertySet.PublicStrings,  
                        "TeamsVtcTenantId",  
                        MapiPropertyType.String), "test");  
    appointment.SetExtendedProperty(new ExtendedPropertyDefinition(  
                        DefaultExtendedPropertySet.PublicStrings,  
                        "SchedulingServiceMeetingOptionsUrl",  
                        MapiPropertyType.String), "test");
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-12*

I m not able to get join meeting url as its read only in ews
