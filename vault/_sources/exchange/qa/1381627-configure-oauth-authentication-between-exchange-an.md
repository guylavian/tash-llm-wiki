---
title: "Configure OAuth authentication between Exchange and Exchange Online organizations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1381627/configure-oauth-authentication-between-exchange-an
question_id: 1381627
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Configure OAuth authentication between Exchange and Exchange Online organizations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1381627/configure-oauth-authentication-between-exchange-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Upon setting auto-replies in Outlook, the teams status is not reflecting.

Following https://learn.microsoft.com/en-us/exchange/configure-oauth-authentication-between-exchange-and-exchange-online-organizations-exchange-2013-help to make sure all configurations are in place, getting below error when testing from exchange online powershell 

Tryiing to figure out how to fix connectivity failure

"

```
Exchange Response Details:
              HTTP response message:
              Exception:
              System.Net.WebException: The remote server returned an error: (401) Unauthorized.
                 at System.Net.HttpWebRequest.GetResponse()
                 at Microsoft.Exchange.Monitoring.TestOAuthConnectivityHelper.SendExchangeOAuthRequest(ADUser user,
              String orgDomain, Uri targetUri, String& diagnosticMessage, Boolean appOnly, Boolean useCachedToken,
              Boolean reloadConfig), diagnostics: 2000005;reason="The user specified by the user-context in the token
              does not exist.";error_category="invalid_user"

ResultType  : Error
Identity    : Microsoft.Exchange.Security.OAuth.ValidationResultNodeId
IsValid     : True
ObjectState : New
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-05*

Hi @basharat mir  

Is the account you are testing syncing between your on-premises environment and Exchange Online?  

401 Access denied error when you run the Test-OAuthConnectivity cmdlet

Also, I found this: Announcing Hybrid Modern Authentication for Exchange On-Premises

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
