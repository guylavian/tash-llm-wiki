---
title: "EWS managed API is not returning meeting resources details for native Outlook initiated meeting."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1080216/ews-managed-api-is-not-returning-meeting-resources
question_id: 1080216
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# EWS managed API is not returning meeting resources details for native Outlook initiated meeting.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1080216/ews-managed-api-is-not-returning-meeting-resources (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We need to fetch all Exchange rooms added as attendee in Outlook  meeting.     

EWS managed API is not returning Exchange rooms details added in native Outlook native meeting, but same is working fine when meeting is created in OWA and Mac Outlook .     

Same resources details are also available to get using Graph API for same meeting     

Below is a sample code which is being used get Appointment details using EWS managed API:    

   PropertySet PropertySetToLoad = new PropertySet(BasePropertySet.FirstClassProperties);    

            PropertySetToLoad.Add(ItemSchema.Subject);  

            PropertySetToLoad.Add(AppointmentSchema.Start);  

            PropertySetToLoad.Add(AppointmentSchema.End);  

            PropertySetToLoad.Add(AppointmentSchema.TimeZone);  

            PropertySetToLoad.Add(AppointmentSchema.Organizer);  

            PropertySetToLoad.Add(AppointmentSchema.RequiredAttendees);  

            PropertySetToLoad.Add(AppointmentSchema.OptionalAttendees);  

            PropertySetToLoad.Add(AppointmentSchema.Resources);  

Appointment _appointment = Appointment.Bind(exchangeService, Appointment.Id, PropertySetToLoad);    

As a observation , we noticed, when Exchange rooms are added in meeting, it adds those rooms in meeting location and EWS managed API does not return those rooms details either in attendee details or in resource details.

## Answers

_No answers on this thread._
