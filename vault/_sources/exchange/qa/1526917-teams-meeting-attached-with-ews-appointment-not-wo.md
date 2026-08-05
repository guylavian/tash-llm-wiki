---
title: "Teams Meeting attached with EWS appointment not working for cloud mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1526917/teams-meeting-attached-with-ews-appointment-not-wo
question_id: 1526917
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-development"]
---
# Teams Meeting attached with EWS appointment not working for cloud mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1526917/teams-meeting-attached-with-ews-appointment-not-wo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When we use Teams meeting attached with the EWS meeting, we are facing issues with hybrid environment.

And this issue is happening for the users in the cloud, in on-prem it works fine.
Steps to reproduce:

-  Create an EWS meeting with teams meeting attached for this we add the following teams meeting properties to the EWS appointment.

-  SkypeTeamsMeetingUrl

-  SchedulingServiceMeetingOptionsUrl

-  SkypeTeamsProperties

code Example: appointment.setExtendedProperty(new ExtendedPropertyDefinition(DefaultExtendedPropertySet.PublicStrings, "SkypeTeamsMeetingUrl", MapiPropertyType.String), teamMeetingJoinWebUrl)

-  Later try to update from the teams meeting i.e., delete attendees, edit content, change time of teams meeting.

For updating this we use the following code

-  graphClient.users(userID).onlineMeetings(TeamsMeetingId).buildRequest().patch(onlineMeeting)

-  Then try to call EWS to update the EWS appointment. And we get the following exception.

-  microsoft.exchange.webservices.data.core.exception.service.remote.ServiceResponseException: The operation can't be performed because the item is out of date. Reload the item and try again.

 Tried with different way by updating teams meeting without EWS appointment then tried to update appointment same results.
And this issue is coming up sporadically, we cannot find out which scenario this is happening.

Do anyone know we cannot attach the teams meeting with EWS meeting like in on-prem, or do we need to follow any other step for that.
This code is used in application so we use client authentication for create teams meeting in graph and delegate users

Thanks in advance!

## Answers

_No answers on this thread._
