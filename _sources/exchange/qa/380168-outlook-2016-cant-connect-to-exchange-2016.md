---
title: "Outlook 2016 can't connect to exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/380168/outlook-2016-cant-connect-to-exchange-2016
question_id: 380168
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Outlook 2016 can't connect to exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/380168/outlook-2016-cant-connect-to-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently installed 2 exchange servers and added to existing DAG. The DAG has a total of 3 servers. Now a few users can't connect to exchange. While add the profile, it failed at "Logging on to the mail server".  The error Outlook can't log on. Verify you are connect to network and are using proper server and mailbox name. The connection to Microsoft Exchange is unavailable. Outlook must be online or connected to complete this action.  

What could be the problem? Thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-04*

Hi @alan gao   ,    

Are the problematic users from the new-installed servers? Or do they have some common attributes?    

As I know, joining the DAG will not affect the using for Exchange server and Outlook client. So I think it should be the servers itself.    

You could use the Test-OutlookConnectivity cmdlet to find if there are any messages:    

```
Test-OutlookConnectivity "Outlook.Protocol\OutlookRpcDeepTestProbe\MDB1" -RunFromServerId Exchange2016 -MailboxId ******@contoso.com | FL
```

Replace MDB1,Ex2016 and test@Company portal   .com to the users'.     

Or you can test it by EXRCA: https://testconnectivity.microsoft.com/tests/Ola/input     

Also please try the following methods:    

-  Create a new mailbox from the new servers, or migrate the old, problematic users to other mailboxes/servers.    

-  Check the certificates, make sure it's using the right ones for both frontend and backend.    

-  Try logging in to OWA with these users.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-03*

Have you been adding the third server to the load balancer?  

Compare the results from Test-NetConnection cmdlet of one client successfully connecting to the server name to the result of the failing client.  

You can take the accessed server name by Ctrl+rightclick the outlook icon in the tray, selecting Connection Status.  

Please use the event viewer anf filter for source "Outlook" to check for further information about wanrings or errors.
