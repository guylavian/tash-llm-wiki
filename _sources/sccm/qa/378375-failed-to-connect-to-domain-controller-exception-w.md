---
title: "\"Failed to connect to domain controller\" exception when generating report"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/378375/failed-to-connect-to-domain-controller-exception-w
question_id: 378375
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# "Failed to connect to domain controller" exception when generating report

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/378375/failed-to-connect-to-domain-controller-exception-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This one's odd. I've installed ATA, configured it (seemingly correctly), but I can't seem to generate a basic report. Attempts to do so yield an "ActionStateGeneratingFailure" on-screen error, while inspecting the actual script shows me that the server returned a 500 error code. Looking deeper into the Microsoft.Tri.Gateway-ExceptionStatistics log file, I find the following.  

```
Count: 2
Microsoft.Tri.Infrastructure.Utils.ExtendedException: Failed to connect to domain controller [DomainControllerDnsName=[DC name] ErrorCode=81] ---> System.DirectoryServices.Protocols.LdapException: The LDAP server is unavailable.
   at System.DirectoryServices.Protocols.LdapConnection.Connect()
   at System.DirectoryServices.Protocols.LdapConnection.BindHelper(NetworkCredential newCredential, Boolean needSetCredential)
   at async Microsoft.Tri.Gateway.Resolution.DirectoryServices.DirectoryServicesClient.CreateLdapConnectionAsync(?)
   --- End of inner exception stack trace ---
   at async Microsoft.Tri.Gateway.Resolution.DirectoryServices.DirectoryServicesClient.CreateLdapConnectionAsync(?)
   at async Microsoft.Tri.Gateway.Resolution.DirectoryServices.DirectoryServicesClient.CreateLdapConnectionAsync(?)
   at async Microsoft.Tri.Gateway.Resolution.DirectoryServices.DirectoryServicesClient.TryCreateLdapConnectionAsync(?)
```

Except I'm pretty sure the settings used to connect to the DC are connect (I've tested them and they were OK), the DC seems to be online and working fine as well. Just for good measure I've tried connecting using ADSI Edit from another DC to the one listed in the error and I was able to connect without any issues.  

What's going on here?  

EDIT:  

Some update on this. Still not sure why the gateway log showed what it did, but I had misconfigured the gateways (should be using lightweight on DCs instead of the "regular").  

Anyway, here's the log:  

```
2021-05-03 16:16:15.9900 6032 40  Error [Enumerable] [message=WebApi action failed [ActionArguments={
  "reportType": "Summary",
  "startDate": "2021-04-28T00:00:00Z",
  "endDate": "2021-05-03T00:00:00Z",
  "localeId": "en-us"
}]] System.InvalidOperationException: Sequence contains no matching element
   at System.Linq.Enumerable.Single[TSource](IEnumerable`1 source, Func`2 predicate)
   at Microsoft.Tri.Center.Monitoring.MonitoringAlertExtension.<>c__DisplayClass1_0.b__0(ObjectId _)
   at System.Linq.Enumerable.WhereSelectListIterator`2.MoveNext()
   at System.Collections.Generic.List`1..ctor(IEnumerable`1 collection)
   at System.Linq.Enumerable.ToList[TSource](IEnumerable`1 source)
   at async Microsoft.Tri.Center.Monitoring.MonitoringAlertExtension.GetDescriptionAsync(?)
   at async Microsoft.Tri.Center.Data.EntityExporter.<>c__DisplayClass14_0.b__1(?)
   at async Microsoft.Tri.Center.Data.EntityExporter.GetPropertyNameToValueMappingAsync[](?)
   at async Microsoft.Tri.Center.Data.EntityExporter.<>c__DisplayClass14_0.b__0(?)
   at async Microsoft.Tri.Infrastructure.Extensions.EnumerableExtension.SelectAsync[](?)
   at async Microsoft.Tri.Center.Data.EntityExporter.CreateMonitoringAlertsTableAsync(?)
   at async Microsoft.Tri.Center.Reports.SummaryReport.CreateFileContentAsync(?)
   at async Microsoft.Tri.Center.Data.Excel.CreateFileDataAsync(?)
   at async Microsoft.Tri.Center.Reports.Reporter.CreateAsync(?)
   at async Microsoft.Tri.Center.Management.Controllers.ReportsController.DownloadReport(?)
   at async System.Threading.Tasks.TaskHelpersExtensions.CastToObject[](?)
   at async System.Web.Http.Controllers.ApiControllerActionInvoker.InvokeActionAsyncCore(?)
   at async System.Web.Http.Controllers.ActionFilterResult.ExecuteAsync(?)
   at async System.Web.Http.Filters.AuthorizationFilterAttribute.ExecuteAuthorizationFilterAsyncCore(?)
   at async System.Web.Http.Filters.AuthorizationFilterAttribute.ExecuteAuthorizationFilterAsyncCore(?)
   at async System.Web.Http.Controllers.ExceptionFilterResult.ExecuteAsync(?)
```

Seems as if there isn't anything to display in the report? That, or MS did an oopsie. ;)

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-05-03*

For the report generation, you need to look for the error in the Center's log, not in the Gateway's log.  

As for the error you found in the Gateway (Error code 81) , you found it in the summary, can you check it in the full log file and see if it keeps happening and  what was the last time it happened? if it was a long time ago, then you can ignore it.
