---
title: "Exchange admin center: Migrate from Google Workspace; Mail User, Create contact failed (The email address is already being used.)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/275564/exchange-admin-center-migrate-from-google-workspac
question_id: 275564
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
---
# Exchange admin center: Migrate from Google Workspace; Mail User, Create contact failed (The email address is already being used.)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/275564/exchange-admin-center-migrate-from-google-workspac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Am following "Perform a Google Workspace (formerly G Suite) migration" instructions and am now at the step "Provision users in Microsoft 365 or Office 365".    

Am attempting to create Mail Users, in order to add the external email address "@gsuite.mycompany.com" to my active users, as well as the proxy/alias email address "userXYZ@infotech  .mycompany.com", as described in the instructions to the normal email address "@mycompany.com".    

Am getting the "Create contact failed" with "Error: The email address is already being used. Please choose another email address."  I am assuming that is because there are active users with normal email address "******@mycompany.com" (with Microsoft 365 Business Standard license).    

-  How can I add the required email addresses, to my active users, please, so I can continue with the migration process?    

-  Does the process work with active users? Are Mail Users different from Active Users?      

-  Would I need any special rights to add these two additional email addresses to my active users?     

Any input would be greatly appreciated.  My company really wants to move away from Google and over to Microsoft, but of course would like to migrate their existing emails.     

Kind Regards!

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-17*

Hi,    

Can you post the result of the following command:    

```
get-recipient ******@mycompany.com|fl *addre*
```

In my test, an exisiting user with ******@mycompany.com would not cause a error, how did you create the mail user? EAC or powershell? Can you post the snapshot of error info?    

Besides, why do you already have user with ******@mycompany.com?  If the migration success and during the step mailuser converted to user mailbox, you would get same error because there is an existing ******@mycompany.com.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
