---
title: "ADFS confiugration error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2717387/adfs-confiugration-error
question_id: 2717387
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# ADFS confiugration error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2717387/adfs-confiugration-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Community,

I am working on configuring SSO through ADFS and I am getting this error. Your help on this will be appreciated!

Server Error in '/' Application.

Input string was not in a correct format.
**Description:**An unhandled exception occurred during the execution of the current web request. Please review the stack trace for more information about the error and where it originated in the code.   

**Exception Details:**System.FormatException: Input string was not in a correct format.  

Source Error: 

`An unhandled exception was generated during the execution of the current web request. Information regarding the origin and location of the exception can be identified using the exception stack trace below.`

Stack Trace: 

`<br>[FormatException: Input string was not in a correct format.]<br>   System.Text.StringBuilder.FormatError() +68<br>   System.Text.StringBuilder.AppendFormat(IFormatProvider provider, String format, Object[] args) +947<br>   System.String.Format(IFormatProvider provider, String format, Object[] args) +163<br>   QW.Platform.Utilities.ComponentSpace.SAMLSetup.BuildUserName(String username, String idp) +432<br>   QW.Platform.Web.Controllers.SamlAuthController.SetUserAndRoles(String userName, String idp) +27<br>   QW.Platform.Web.Controllers.SamlAuthController.AssertionConsumerService() +274<br>   lambda_method(Closure , ControllerBase , Object[] ) +79<br>   System.Web.Mvc.ReflectedActionDescriptor.Execute(ControllerContext controllerContext, IDictionary`2 parameters) +217<br>   System.Web.Mvc.ControllerActionInvoker.InvokeActionMethod(ControllerContext controllerContext, ActionDescriptor actionDescriptor, IDictionary`2 parameters) +39<br>   System.Web.Mvc.Async.AsyncControllerActionInvoker.<BeginInvokeSynchronousActionMethod>b__39(IAsyncResult asyncResult, ActionInvocation innerInvokeState) +12<br>   System.Web.Mvc.Async.WrappedAsyncResult`2.CallEndDelegate(IAsyncResult asyncResult) +139<br>   System.Web.Mvc.Async.AsyncInvocationWithFilters.<InvokeActionMethodFilterAsynchronouslyRecursive>b__3d() +112<br>   System.Web.Mvc.Async.<>c__DisplayClass46.<InvokeActionMethodFilterAsynchronouslyRecursive>b__3f() +452<br>   System.Web.Mvc.Async.<>c__DisplayClass33.<BeginInvokeActionMethodWithFilters>b__32(IAsyncResult asyncResult) +15<br>   System.Web.Mvc.Async.<>c__DisplayClass2b.<BeginInvokeAction>b__1c() +32<br>   System.Web.Mvc.Async.<>c__DisplayClass21.<BeginInvokeAction>b__1e(IAsyncResult asyncResult) +231<br>   System.Web.Mvc.Async.AsyncControllerActionInvoker.EndInvokeAction(IAsyncResult asyncResult) +892<br>   System.Web.Mvc.Async.AsyncControllerActionInvoker.EndInvokeAction(IAsyncResult asyncResult) +1292<br>   System.Web.Mvc.Controller.<BeginExecuteCore>b__1d(IAsyncResult asyncResult, ExecuteCoreState innerState) +29<br>   System.Web.Mvc.Async.WrappedAsyncVoid`1.CallEndDelegate(IAsyncResult asyncResult) +111<br>   System.Web.Mvc.Controller.EndExecuteCore(IAsyncResult asyncResult) +42<br>   System.Web.Mvc.Async.WrappedAsyncVoid`1.CallEndDelegate(IAsyncResult asyncResult) +19<br>   System.Web.Mvc.MvcHandler.<BeginProcessRequest>b__5(IAsyncResult asyncResult, ProcessRequestState innerState) +51<br>   System.Web.Mvc.Async.WrappedAsyncVoid`1.CallEndDelegate(IAsyncResult asyncResult) +111<br>   System.Web.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute() +1303<br>   System.Web.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute() +2454<br>   System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously) +1088<br>`

## Answers

_No answers on this thread._
