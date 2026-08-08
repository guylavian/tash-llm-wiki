---
title: "Active Directory Replication Status Tool (ADREPLSTATUS) has expired, 2022-07-01."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/916787/active-directory-replication-status-tool-adreplsta
question_id: 916787
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Replication Status Tool (ADREPLSTATUS) has expired, 2022-07-01.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/916787/active-directory-replication-status-tool-adreplsta (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings,    

The Active Directory Replication Status Tool (ADREPLSTATUS) expired on July 1, 2022 and is no longer functional. I understand from past posts that this happens periodically and Microsoft needs to publish an updated version of the tool with a newer expiration date. I cannot find any way to reach someone to let them know this has expired so I'm posting it here.     

TechNet page for the tool can be found here: https://social.technet.microsoft.com/wiki/contents/articles/12707.active-directory-replication-status-tool-adreplstatus-resources-page.aspx    

Thank you.

## Answer (community) — Q&A User

*upvotes: 3 · updated: 2022-09-09*

I also get a .NET Runtime Error from the latest version (doesn't even tell me about a License Expiration).    

Application: repl.exe    

Framework Version: v4.0.30319    

Description: The process was terminated due to an unhandled exception.    

Exception Info: Microsoft.Sirona.PackagingException    

   at Microsoft.Sirona.Packaging.PackageHelper.ValidatePackage(System.IO.Stream, System.String, Boolean, Boolean)    

   at Microsoft.Sirona.Packaging.PackageManager.LoadInternal(System.IO.Stream, Boolean, Boolean, System.String, System.String, Boolean)    

   at Microsoft.Sirona.Packaging.PackageManager.Load(System.String, Boolean, Boolean)    

Exception Info: Microsoft.Sirona.PackagingException    

   at Microsoft.Sirona.Packaging.PackageManager.Load(System.String, Boolean, Boolean)    

   at repl.MainWindow.LoadConfiguration(Microsoft.Sirona.Configuration.ConfigurationManager)    

   at repl.MainWindow.SetupSironaComponents()    

   at repl.MainWindow..ctor()    

Exception Info: System.Windows.Markup.XamlParseException    

   at System.Windows.Markup.XamlReader.RewrapException(System.Exception, System.Xaml.IXamlLineInfo, System.Uri)    

   at System.Windows.Markup.WpfXamlLoader.Load(System.Xaml.XamlReader, System.Xaml.IXamlObjectWriterFactory, Boolean, System.Object, System.Xaml.XamlObjectWriterSettings, System.Uri)    

   at System.Windows.Markup.WpfXamlLoader.LoadBaml(System.Xaml.XamlReader, Boolean, System.Object, System.Xaml.Permissions.XamlAccessLevel, System.Uri)    

   at System.Windows.Markup.XamlReader.LoadBaml(System.IO.Stream, System.Windows.Markup.ParserContext, System.Object, Boolean)    

   at System.Windows.Application.LoadBamlStreamWithSyncInfo(System.IO.Stream, System.Windows.Markup.ParserContext)    

   at System.Windows.Application.DoStartup()    

   at System.Windows.Application.<.ctor>b__1_0(System.Object)    

   at System.Windows.Threading.ExceptionWrapper.InternalRealCall(System.Delegate, System.Object, Int32)    

   at System.Windows.Threading.ExceptionWrapper.TryCatchWhen(System.Object, System.Delegate, System.Object, Int32, System.Delegate)    

   at System.Windows.Threading.DispatcherOperation.InvokeImpl()    

   at MS.Internal.CulturePreservingExecutionContext.CallbackWrapper(System.Object)    

   at System.Threading.ExecutionContext.RunInternal(System.Threading.ExecutionContext, System.Threading.ContextCallback, System.Object, Boolean)    

   at System.Threading.ExecutionContext.Run(System.Threading.ExecutionContext, System.Threading.ContextCallback, System.Object, Boolean)    

   at System.Threading.ExecutionContext.Run(System.Threading.ExecutionContext, System.Threading.ContextCallback, System.Object)    

   at MS.Internal.CulturePreservingExecutionContext.Run(MS.Internal.CulturePreservingExecutionContext, System.Threading.ContextCallback, System.Object)    

   at System.Windows.Threading.DispatcherOperation.Invoke()    

   at System.Windows.Threading.Dispatcher.ProcessQueue()    

   at System.Windows.Threading.Dispatcher.WndProcHook(IntPtr, Int32, IntPtr, IntPtr, Boolean ByRef)    

   at MS.Win32.HwndWrapper.WndProc(IntPtr, Int32, IntPtr, IntPtr, Boolean ByRef)    

   at MS.Win32.HwndSubclass.DispatcherCallbackOperation(System.Object)    

   at System.Windows.Threading.ExceptionWrapper.InternalRealCall(System.Delegate, System.Object, Int32)    

   at System.Windows.Threading.ExceptionWrapper.TryCatchWhen(System.Object, System.Delegate, System.Object, Int32, System.Delegate)    

   at System.Windows.Threading.Dispatcher.LegacyInvokeImpl(System.Windows.Threading.DispatcherPriority, System.TimeSpan, System.Delegate, System.Object, Int32)    

   at MS.Win32.HwndSubclass.SubclassWndProc(IntPtr, Int32, IntPtr, IntPtr)    

   at MS.Win32.UnsafeNativeMethods.DispatchMessage(System.Windows.Interop.MSG ByRef)    

   at System.Windows.Threading.Dispatcher.PushFrameImpl(System.Windows.Threading.DispatcherFrame)    

   at System.Windows.Application.RunDispatcher(System.Object)    

   at System.Windows.Application.RunInternal(System.Windows.Window)    

   at repl.App.Main()

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-07-06*

I reported this here, we'll see what (if anything) happens.    

https://github.com/MicrosoftDocs/feedback/issues/3823

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-27*

Tried, but the same. Expires at 01.07.2022

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-25*

Hi     

new version     

https://www.microsoft.com/en-us/download/details.aspx?id=30005

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-15*

any news abou this. Any free tool that do the same ?
