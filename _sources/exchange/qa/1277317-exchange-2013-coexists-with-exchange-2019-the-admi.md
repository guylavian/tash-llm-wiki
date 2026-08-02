---
title: "Exchange 2013 coexists with Exchange 2019  the administrator uses the delivery report to view the user status and report the following error message."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1277317/exchange-2013-coexists-with-exchange-2019-the-admi
question_id: 1277317
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 coexists with Exchange 2019  the administrator uses the delivery report to view the user status and report the following error message.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1277317/exchange-2013-coexists-with-exchange-2019-the-admi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Hello HI Engineer,

Exchange 2013 coexists with Exchange 2019, after migrating Exchange 2013 admin users to 2019, the administrator uses the delivery report to view the user status and report the following error message.

The Exchange 2019 Application log reports Event ID: 4

Current user: 'contoso.com/Special_Account/testadmin'
Request for URL 'https://ex.contoso.com:444/ecp/PersonalSettings/DeliveryReportDetail.aspx?isNarrow=t&id=Message-Id= ,Server=ex.contoso.com,Internal-Id=0, Sender=b09bef73-9330-4e2f-bc84-e1350e571e80,Domain=contoso.com,Recip=******@contoso.com( https://mail.contoso.com/ecp/PersonalSettings/DeliveryReportDetail.aspx?isNarrow=t&id=Message-IdSystem.Web.HttpUnhandledException (0x80004005): Raise type " System.Web.HttpUnhandledException". ---> Microsoft.Exchange.Management.ControlPanel.CannotAccessOptionsWithBEParamOrCookieException: There was a problem opening Options in Outlook Web App. Click Sign Out below, and then sign in to Options in Outlook Web App again. If that doesn't work, sign out, delete your browser cookies, and sign in again.
  

Microsoft.Exchange.Management.ControlPanel.HttpContextExtensions.ThrowIfViewOptionsWithBEParam(HttpContext context, FeatureSet featureSet)
   in Microsoft.Exchange.Management.ControlPanel.EcpContentPage.OnLoad(EventArgs e)
   in System.Web.UI.Control.LoadRecursive()
  in System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   in System.Web.UI.Page.HandleError(Exception e)
  in System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   in System.Web.UI.Page.ProcessRequest(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
  in System.Web.UI.Page.ProcessRequest()
   in System.Web.UI.Page.ProcessRequest(HttpContext context)
   ta System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()
   in  System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)
   in System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)
   in System.Web.UI.Page.HandleError(Exception e)
   in System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   in System.Web.UI.Page.ProcessRequest(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   in System.Web.UI.Page.ProcessRequest()
   in System.Web.UI.Page.ProcessRequest(HttpContext context)
   at System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()
   in System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)
   in System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-12*

This issue was solved and Microsoft replied as a bug.

Access ECP URLs cannot be carried ?exchclientver=15。

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-10*

HI Konstantinos,

   Using localhost and domain names is not feasible, and using IP addresses is also not feasible.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-08*

HI ，

   I still reported the same error after configuring using the above method

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-05-06*

Hello @超 邓 !

Here are a few troubleshooting steps that you can try:

- 

```
Clear cookies and cache: Ask the user to clear their browser's cookies and cache, then try accessing the delivery report again.
```

- 

```
Check BackEnd parameter: Make sure that the BE parameter is correctly set. You can check this by reviewing the URL in the address bar of your browser when you access the delivery report.
```

- 

```
Verify user permissions: Ensure that the user has the correct permissions to access the delivery report. Check that the user has the necessary roles assigned, such as the Mail Recipient and Mailbox Import Export roles.
```

- 

```
Restart services: Try restarting the Microsoft Exchange Transport and Microsoft Exchange Mailbox Transport services on the Exchange 2019 server.
```

- 

```
Review logs: Review the application logs on the Exchange 2019 server for any additional error messages or clues as to what might be causing the issue.
```

Assisting Source: ChatGPT Subscription

Kindly mark the answer as Accepted and Upvote in case it helped or post your feedback to help !

Regards
