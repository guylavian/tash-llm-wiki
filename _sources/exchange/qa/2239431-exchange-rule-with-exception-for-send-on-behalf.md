---
title: "Exchange rule with exception for \"Send on behalf\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2239431/exchange-rule-with-exception-for-send-on-behalf
question_id: 2239431
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange rule with exception for "Send on behalf"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2239431/exchange-rule-with-exception-for-send-on-behalf (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have the below Exchange rule that is mostly working:

Rule description

Apply this rule if

Is sent to '*****@company.com'*

and Is message type 'Calendaring'

Do the following

Redirect the message to '*****@company.com'*

Except if

Is received from '*****@radiancetech.com'*

The scenario is the CEO wants all of his meeting requests screened by multiple admin assistants in case one is out of office.  All the admin assistants are configured as delegates on the CEO's calendar and the resource account R-CEO-ALT-Calendar. 

The meeting requester submits the invitation.  It redirects correctly to R-CEO-ALT-Calendar.  The admin assistant reviews all meeting requests with the CEO, and the CEO advises which ones he wants to accept.  The admin assistant then forwards the meeting invitation from R-CEO-ALT-Calendar to the real CEO calendar and accepts it.  

Everything except the last step is working the way they want it to work.  When that invitation is forwarded the message shows "Delegate_Name sent on behalf of Meeting_Organizer".  Exchange is treating the organizer as the sender and not the delegate, so the rule fires again and redirects to R-CEO-ALT-Calendar.  The invitation never gets to the real CEO calendar.

Is there a way to add a secondary exception maybe using the message header where it sees the message is being forwarded from a delegate which is already listed in the first exception, so that the message would deliver successfully to the real CEO calendar?

Or if you have a better approach altogether, any suggestions are welcome.  Thanks.

## Answers

_No answers on this thread._
