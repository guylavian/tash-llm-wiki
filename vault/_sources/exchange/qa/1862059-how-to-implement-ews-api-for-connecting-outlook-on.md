---
title: "How to implement EWS API for connecting Outlook on-premise user's calendar data"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1862059/how-to-implement-ews-api-for-connecting-outlook-on
question_id: 1862059
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-other-l1"]
---
# How to implement EWS API for connecting Outlook on-premise user's calendar data

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1862059/how-to-implement-ews-api-for-connecting-outlook-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our website(which is built on Rails framework) has Outlook calendar integration through which our client's user can connect their Outlook calendar & then we fetch or push events to their Outlook calendar,

Currently, we are using this API for authenticating users on Outlook: "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=#{AZURE_APP_CLIENT_ID}&redirect_uri=https://our_website.com/auth/microsoft_graph_auth/callback&response_mode=query&response_type=code&scope=calendars.readwrite%20offline_access&state=encrypted_code

Once a user is authenticated we fetch all events using this API: 'https://graph.microsoft.com/v1.0/me/calendarView'

But the problem is some of our clients have "Outlook on-premise" instead of normal cloud-based Outlook, How do we connect users with their Outlook on-premise account, What changes will we have to make in the above implementation?
Please see I am completely new in this & don't have in-depth knowledge

## Answers

_No answers on this thread._
