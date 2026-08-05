---
title: "[Migrated from MSDN Exchange Dev]Cannot access OWA and ECP after upgrade Exchange 2016 from CU15 to CU17"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/134754/migrated-from-msdn-exchange-dev-cannot-access-owa
question_id: 134754
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Cannot access OWA and ECP after upgrade Exchange 2016 from CU15 to CU17

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/134754/migrated-from-msdn-exchange-dev-cannot-access-owa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After upgrade our Exchange 2016 from CU15 to CU17, got the error below when try to access OWA

"Method not found: 'Void Microsoft.Exchange.Security.Authentication.Utility.DeleteFbaAuthCookies(System.Web.HttpRequest, System.Web.HttpResponse)'"

And we see MS Exchange Front End HTTP Proxy event 1003 error in logs.

Google led me to this article https://social.msdn.microsoft.com/Forums/security/en-US/b0cc4057-34b8-4e18-8b8f-a1144cebaf56/method-not-found?forum=exchangesvrdevelopment

Interestingly the issue in the article is same but with CU18. I tried the SharedWebConfig.config file linked in the article, and I was able to access OWA and ECP to a degree... At least now the login page loads properly and I can authenticate through. But after that, Exchange just shows a blank page...

So now I know my issue is relate to the SharedWebConfig.config file, but the CU18 version of file obviously doesn't work on CU17 properly. Can anyone share some idea how to get CU17 version of the file?

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/2355032a-dd8e-4f63-9213-c0d2bfd86879/cannot-access-owa-and-ecp-after-upgrade-exchange-2016-from-cu15-to-cu17?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

Do you try to follow this article to delete and recreate the SharedWebConfig.config file?     

If you still cannot access ECP and OWA after creating this file, you many need to install a new Exchange in your domain then copy SharedWebConfig.config file from that new Exchange server(The different environment have different configuration information, the file copied from other organization may not suitable for you).    

Remember run IISReset command to restart the IIS service after making change to configuration file.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
