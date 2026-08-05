---
title: "exchange server 添加邮箱报错"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/277651/exchange-server
question_id: 277651
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange server 添加邮箱报错

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/277651/exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Microsoft.Exchange.Provisioning.ProvisioningException: ScriptingAgent: 对 OnComplete API 调用 Scriptlet 时引发了异常: 使用“1”个参数调用“Send”时发生异常:“事务失败。 服务器响应为:5.6.0 Invalid message content”。 ---> System.Management.Automation.MethodInvocationException: 使用“1”个参数调用“Send”时发生异常:“事务失败。 服务器响应为:5.6.0 Invalid message content” ---> System.Net.Mail.SmtpException: 事务失败。 服务器响应为:5.6.0 Invalid message content 在 System.Net.Mail.DataStopCommand.CheckResponse(SmtpStatusCode statusCode, String serverResponse) 在 System.Net.Mail.DataStopCommand.Send(SmtpConnection conn) 在 System.Net.ClosableStream.Close() 在 System.Net.Mail.SmtpClient.Send(MailMessage message) 在 CallSite.Target(Closure , CallSite , Object , Object ) --- 内部异常堆栈跟踪的结尾 --- 在 System.Management.Automation.ExceptionHandlingOps.ConvertToMethodInvocationException(Exception exception, Type typeToThrow, String methodName, Int32 numArgs, MemberInfo memberInfo) 在 CallSite.Target(Closure , CallSite , Object , Object ) 在 System.Dynamic.UpdateDelegates.UpdateAndExecute2T0,T1,TRet 在 System.Management.Automation.Interpreter.DynamicInstruction`3.Run(InterpretedFrame frame) 在 System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame) --- 内部异常堆栈跟踪的结尾 --- 在 Microsoft.Exchange.ProvisioningAgent.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-18*

Hi @卡尔 笛   ,    

Happy new year!    

Sorry but currently in Microsoft Q&A we only support English questions, could you please edit your question into English？Then we can help you to solve your issues.    

And also you can post the question on the right Chinese forum: TechCN, so we can discuss in Chinese there.    

I've read the error messages and seems like you're using the script to create mailbox right? What about creating them with EAC or EMS? We can go on here with English.     

But it's suggested to open a new thread on the TechCN forum for a better troubleshooting.    

Thanks for your understanding!    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
