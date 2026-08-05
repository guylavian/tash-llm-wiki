---
title: "Install Exchange server 2019 CU12 error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1064924/install-exchange-server-2019-cu12-error
question_id: 1064924
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Install Exchange server 2019 CU12 error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1064924/install-exchange-server-2019-cu12-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there,    

I am trying to install a new Exchange server 2019 CU12, but I couldn't get through this error: In setup process step 6 of 13: Management tools    

Error:    

The following error was generated when "$error.Clear();     

	Set-LocalPermissions  

" was run: "System.UnauthorizedAccessException: Attempted to perform an unauthorized operation.    

   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)    

   at Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target)    

   at Microsoft.Exchange.Management.Deployment.SetLocalPermissions.InternalProcessRecord()    

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()    

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".    

    

Could you please help me with that?    

Thank you very much.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-31*

Have you looked at the ExchangeSetupLogs? They may provide you with more info.    

You can also check this article for more insight - How to Install Exchange 2013/2016/2019 Cumulative Updates?    

Please Note: Since Microsoft does not host the website, the link may change without notice. Microsoft does not guarantee the accuracy of this information.
