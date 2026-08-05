---
title: "Users are unable to view exchange resources on their outlooks"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1383440/users-are-unable-to-view-exchange-resources-on-the
question_id: 1383440
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Users are unable to view exchange resources on their outlooks

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1383440/users-are-unable-to-view-exchange-resources-on-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Users are unable to view exchange resources on their outlooks. 

Users can schedule a resource in outlook, but they can't see the availability. The calendar doesn't show on their outlook. All users have reviewer permissions and I've verified that the resources are up and running. They will get an email saying this resource isn't available at this time when trying to book, but how are they supposed to know when it's available if they can't even see it's availability anywhere? 

The only way their availability shows, is if I give them full access to the calendar, which should not be the case. They should be able to see availability as a reviewer. I can't find any documentation on this. Everything is so convoluted on these exchange resources documentation.

I've confirmed the resources are showable in the address book and are available for anybody to use. This portion works, again, it's just being able to see the availability of the resource.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-09*

Hi @Cesar Diaz

First, just to rule out that you are not having a hybrid deployment.

 Try adding additional "free/busy time" permissions.

Also, when you mentioned "give them full access to the calendar", did you mean "full details"?

<<Every time we onboard new employees, this should be a standard thing added to their outlook.

If you want to automate this process for new employees, you can create a group in Outlook and add the new employees to the group. Then, you can set the permissions(reviewer) for the group instead of individual users. This way, any new employees added to the group will automatically have access to the resources without you having to manually add them. I hope this helps!

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
