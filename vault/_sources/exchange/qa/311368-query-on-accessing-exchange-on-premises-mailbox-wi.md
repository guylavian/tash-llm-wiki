---
title: "Query on accessing Exchange on-premises mailbox with a profile creating with an Exchange online user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/311368/query-on-accessing-exchange-on-premises-mailbox-wi
question_id: 311368
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Query on accessing Exchange on-premises mailbox with a profile creating with an Exchange online user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/311368/query-on-accessing-exchange-on-premises-mailbox-wi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,     

We are working on analysis/development activities for our archiving solution which is planned to support Hybrid MS Exchange as a source. To achieve communication with the exchange server, our application uses the Outlook profile through MAPI. In the profile, we have added the email of the Exchange Online user. Our solution works fine if the archival source is an exchange online user mailbox. When we changed the source to an on-prem user mailbox, our application failed to process the mailbox. Hence we tried the below steps:     

-  Created profile with online user email (say online-user@mathieu.company  .com)     

-  Added O365 license and gave full access on the on-prem user (say onprem-user@mathieu.company  .com) to online-user@mathieu.company  .com     

-  Added onprem-user@mathieu.company  .com mailbox manually to the created profile and logged in with online-user creds in windows creds pop-up    

After performing the above steps, our application was able to process the on-prem user mailbox. We would like to know if the above is the right approach for establishing a connection between online and on-prem users and mailboxes? Or is there any other approach possible? Please advice.     

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Hi @ExUser44   ,    

Does your application work according to using Outlook profile? If so, your solution is feasible, when assigning the "Full access" permission of the on-premises mailbox to the mailbox in Exchange Online. The on-premises Exchange mailbox will be added to the Outlook profile of Exchange online mailbox. Then the mailbox auto-mapping feature uses the Autodiscover to automatically open the mailbox in the delegate’s Outlook profile. But “Full Access” allow the delegate to open the mailbox, and view, add and remove the contents fo the mialbox, so please pay attention to the information security of your on-premises mailbox after assigning permissions.    

In addition, considering that you are in an Exchange Hybrid environment, migrating mailboxes to Exchange online is also a solution.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
