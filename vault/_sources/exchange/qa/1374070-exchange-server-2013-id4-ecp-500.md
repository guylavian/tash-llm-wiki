---
title: "exchange server 2013 事件ID4，ecp登录打不开邮件流的接收连接器和服务器，报错500"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374070/exchange-server-2013-id4-ecp-500
question_id: 1374070
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange server 2013 事件ID4，ecp登录打不开邮件流的接收连接器和服务器，报错500

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374070/exchange-server-2013-id4-ecp-500 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
日志名称:          Application
来源:            MSExchange Control Panel
日期:            2023/9/21 19:44:58
事件 ID:         4
任务类别:          常规
级别:            错误
关键字:           经典
用户:            暂缺
计算机:           EX1.liye.biz
描述:
当前用户:“liye.biz/Users/Administrator”
对 URL“https://ex1.liye.biz:444/ecp/ConnectorMgmt/ReceiveConnectors.aspx?showhelp=false(https://localhost/ecp/ConnectorMgmt/ReceiveConnectors.aspx?showhelp=false)”的请求失败，出现以下错误:
System.Web.HttpUnhandledException (0x80004005): 引发类型为“System.Web.HttpUnhandledException”的异常。 ---> System.Reflection.TargetInvocationException: 调用的目标发生了异常。 ---> System.InvalidCastException: 无法将类型为“System.DBNull”的对象强制转换为类型“Microsoft.Exchange.Data.ServerVersion”。
   在 Microsoft.Exchange.Management.DDIService.ServerPickerService.GetReceiveConnectorServerListPostAction(DataRow inputRow, DataTable dataTable, DataObjectStore store)
   --- 内部异常堆栈跟踪的结尾 ---
   在 Microsoft.Exchange.Management.ControlPanel.ReceiveConnectors.OnLoad(EventArgs e)
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.HandleError(Exception e)
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.ProcessRequest(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.ProcessRequest()
   在 System.Web.UI.Page.ProcessRequest(HttpContext context)
   在 System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()
   在 System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)
   在 System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)
   在 System.Web.UI.Page.HandleError(Exception e)
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.ProcessRequest(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.ProcessRequest()
   在 System.Web.UI.Page.ProcessRequest(HttpContext context)
   在 System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()
   在 System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)
   在 System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

System.Reflection.TargetInvocationException: 调用的目标发生了异常。 ---> System.InvalidCastException: 无法将类型为“System.DBNull”的对象强制转换为类型“Microsoft.Exchange.Data.ServerVersion”。
   在 Microsoft.Exchange.Management.DDIService.ServerPickerService.GetReceiveConnectorServerListPostAction(DataRow inputRow, DataTable dataTable, DataObjectStore store)
   --- 内部异常堆栈跟踪的结尾 ---
   在 Microsoft.Exchange.Management.ControlPanel.ReceiveConnectors.OnLoad(EventArgs e)
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 Microsoft.Exchange.Management.ControlPanel.ReceiveConnectors.OnLoad(EventArgs e)
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)

System.InvalidCastException: 无法将类型为“System.DBNull”的对象强制转换为类型“Microsoft.Exchange.Data.ServerVersion”。
   在 Microsoft.Exchange.Management.DDIService.ServerPickerService.GetReceiveConnectorServerListPostAction(DataRow inputRow, DataTable dataTable, DataObjectStore store)
   在 Microsoft.Exchange.Management.DDIService.ServerPickerService.GetReceiveConnectorServerListPostAction(DataRow inputRow, DataTable dataTable, DataObjectStore store)

未启用的功能信息: Features:[[Global.DistributedKeyManagement, False],[Global.GlobalCriminalCompliance, False],[Global.MultiTenancy, False],[Global.WindowsLiveID, False],[Eac.AllowMailboxArchiveOnlyMigration, True],[Eac.AllowRemoteOnboardingMovesOnly, False],[Eac.CmdletLogging, True],[Eac.CrossPremiseMigration, False],[Eac.DiscoveryPFSearch, False],[Eac.DlpFingerprint, False],[Eac.GeminiShell, False],[Eac.Office365DIcon, False],[Eac.UnlistedServices, False],],  Flights:[],  Constraints:[[mode, enterprise],[user, Administrator@],[org, ],[loc, zh-CN],], IsGlobalSnapshot: False
事件 Xml:

  
    
    4
    2
    1
    0x80000000000000
    
    26731
    Application
    EX1.liye.biz
    
  
  
    liye.biz/Users/Administrator
    https://ex1.liye.biz:444/ecp/ConnectorMgmt/ReceiveConnectors.aspx?showhelp=false(https://localhost/ecp/ConnectorMgmt/ReceiveConnectors.aspx?showhelp=false)
    System.Web.HttpUnhandledException (0x80004005): 引发类型为“System.Web.HttpUnhandledException”的异常。 ---> System.Reflection.TargetInvocationException: 调用的目标发生了异常。 ---> System.InvalidCastException: 无法将类型为“System.DBNull”的对象强制转换为类型“Microsoft.Exchange.Data.ServerVersion”。
   在 Microsoft.Exchange.Management.DDIService.ServerPickerService.GetReceiveConnectorServerListPostAction(DataRow inputRow, DataTable dataTable, DataObjectStore store)
   --- 内部异常堆栈跟踪的结尾 ---
   在 Microsoft.Exchange.Management.ControlPanel.ReceiveConnectors.OnLoad(EventArgs e)
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.HandleError(Exception e)
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.ProcessRequest(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.ProcessRequest()
   在 System.Web.UI.Page.ProcessRequest(HttpContext context)
   在 System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()
   在 System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)
   在 System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)
   在 System.Web.UI.Page.HandleError(Exception e)
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.ProcessRequest(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 System.Web.UI.Page.ProcessRequest()
   在 System.Web.UI.Page.ProcessRequest(HttpContext context)
   在 System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()
   在 System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)
   在 System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

System.Reflection.TargetInvocationException: 调用的目标发生了异常。 ---> System.InvalidCastException: 无法将类型为“System.DBNull”的对象强制转换为类型“Microsoft.Exchange.Data.ServerVersion”。
   在 Microsoft.Exchange.Management.DDIService.ServerPickerService.GetReceiveConnectorServerListPostAction(DataRow inputRow, DataTable dataTable, DataObjectStore store)
   --- 内部异常堆栈跟踪的结尾 ---
   在 Microsoft.Exchange.Management.ControlPanel.ReceiveConnectors.OnLoad(EventArgs e)
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)
   在 Microsoft.Exchange.Management.ControlPanel.ReceiveConnectors.OnLoad(EventArgs e)
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Control.LoadRecursive()
   在 System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)

System.InvalidCastException: 无法将类型为“System.DBNull”的对象强制转换为类型“Microsoft.Exchange.Data.ServerVersion”。
   在 Microsoft.Exchange.Management.DDIService.ServerPickerService.GetReceiveConnectorServerListPostAction(DataRow inputRow, DataTable dataTable, DataObjectStore store)
   在 Microsoft.Exchange.Management.DDIService.ServerPickerService.GetReceiveConnectorServerListPostAction(DataRow inputRow, DataTable dataTable, DataObjectStore store)

    Features:[[Global.DistributedKeyManagement, False],[Global.GlobalCriminalCompliance, False],[Global.MultiTenancy, False],[Global.WindowsLiveID, False],[Eac.AllowMailboxArchiveOnlyMigration, True],[Eac.AllowRemoteOnboardingMovesOnly, False],[Eac.CmdletLogging, True],[Eac.CrossPremiseMigration, False],[Eac.DiscoveryPFSearch, False],[Eac.DlpFingerprint, False],[Eac.GeminiShell, False],[Eac.Office365DIcon, False],[Eac.UnlistedServices, False],],  Flights:[],  Constraints:[[mode, enterprise],[user, Administrator@],[org, ],[loc, zh-CN],], IsGlobalSnapshot: False
    ActivityId: 
  

我该如何解决，请帮助我，谢谢
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-22*

Hi shunkun 

好的，了解。

请问您最近做过什么更新吗，比如SU或CU版本的更新？

您可以检查一下所有的服务是不是都起来了。对于EMS 如果get-receiverconnector 有什么报错吗？

另外，您还可以用Healthchecker检查一下，看看有什么可用的更新。

https://microsoft.github.io/CSS-Exchange/Diagnostics/HealthChecker/

BTW，exchange2013的生命周期已经结束了，建议尽快升级到主流版本。

如果答案对您有帮助，请点击“接受答案”并点赞。 如果您对此答案还有其他疑问，请点击“评论”。

注意：如果您想接收此主题的相关电子邮件通知，请按照我们的文档中的步骤启用电子邮件通知。
