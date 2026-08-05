---
title: "exchange 2010 upgrade to 365 hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188281/exchange-2010-upgrade-to-365-hybrid
question_id: 2188281
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# exchange 2010 upgrade to 365 hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188281/exchange-2010-upgrade-to-365-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello. i have exchange 2010 sp3 u32 . i am running the hybrid configuration tool . almost at the end of the proccess i get the error :

2024.02.27 20:51:05.132 *ERROR* 10042 [Client=UX, Thread=1] Exception Image: C:\Users\edison\AppData\Roaming\Microsoft\Exchange Hybrid Configuration\20240226_143252.png 

2024.02.27 20:51:05.132 *ERROR* 10251 [Client=UX, Thread=1]  

```
System.NullReferenceException: Object reference not set to an instance of an object. 

                                     at Microsoft.Online.CSE.Hybrid.Common.BaseAuthCredential.AcquireToken(String authority, String resource, String clientId, Uri redirectUri, Boolean promptMode) 

                                     at Microsoft.Online.CSE.Hybrid.Provider.HybridConfigurationService.HybridConfigurationService.AcquireToken(IHostingServiceConfiguration hostingServiceConfiguration, ICredential credential, Boolean promptMode) 

                                     at Microsoft.Online.CSE.Hybrid.App.TenantData.AuthenticateResources(ILogger logger, ICredential credential, Boolean promptMode) 

                                     at Microsoft.Online.CSE.Hybrid.App.TenantData.PromptCredential(IWindowsUserInterface windowsUserInterface, ILogger logger) 

                                     at Microsoft.Online.CSE.Hybrid.App.ViewModel.Pages.Credentials.TenantSignIn() 

                                     at Microsoft.Online.CSE.Hybrid.Windows.Commando.<>c\_\_DisplayClass15\_0.<Thunk>b\_\_0(Object p) 

                                     at MS.Internal.Commands.CommandHelpers.CriticalExecuteCommandSource(ICommandSource commandSource, Boolean userInitiated) 

                                     at System.Windows.Controls.Primitives.ButtonBase.OnClick() 

                                     at System.Windows.Controls.Button.OnClick() 

                                     at System.Windows.Controls.Primitives.ButtonBase.OnMouseLeftButtonUp(MouseButtonEventArgs e) 

                                     at System.Windows.RoutedEventArgs.InvokeHandler(Delegate handler, Object target) 

                                     at System.Windows.RoutedEventHandlerInfo.InvokeHandler(Object target, RoutedEventArgs routedEventArgs) 

                                     at System.Windows.EventRoute.InvokeHandlersImpl(Object source, RoutedEventArgs args, Boolean reRaised) 

                                     at System.Windows.UIElement.ReRaiseEventAs(DependencyObject sender, RoutedEventArgs args, RoutedEvent newEvent) 

                                     at System.Windows.UIElement.OnMouseUpThunk(Object sender, MouseButtonEventArgs e) 

                                     at System.Windows.RoutedEventArgs.InvokeHandler(Delegate handler, Object target) 

                                     at System.Windows.RoutedEventHandlerInfo.InvokeHandler(Object target, RoutedEventArgs routedEventArgs) 

                                     at System.Windows.EventRoute.InvokeHandlersImpl(Object source, RoutedEventArgs args, Boolean reRaised) 

                                     at System.Windows.UIElement.RaiseEventImpl(DependencyObject sender, RoutedEventArgs args) 

                                     at System.Windows.UIElement.RaiseTrustedEvent(RoutedEventArgs args) 

                                     at System.Windows.Input.InputManager.ProcessStagingArea() 

                                     at System.Windows.Input.InputManager.ProcessInput(InputEventArgs input) 

                                     at System.Windows.Input.InputProviderSite.ReportInput(InputReport inputReport) 

                                     at System.Windows.Interop.HwndMouseInputProvider.ReportInput(IntPtr hwnd, InputMode mode, Int32 timestamp, RawMouseActions actions, Int32 x, Int32 y, Int32 wheel) 

                                     at System.Windows.Interop.HwndMouseInputProvider.FilterMessage(IntPtr hwnd, WindowMessage msg, IntPtr wParam, IntPtr lParam, Boolean& handled) 

                                     at System.Windows.Interop.HwndSource.InputFilterMessage(IntPtr hwnd, Int32 msg, IntPtr wParam, IntPtr lParam, Boolean& handled) 

                                     at MS.Win32.HwndWrapper.WndProc(IntPtr hwnd, Int32 msg, IntPtr wParam, IntPtr lParam, Boolean& handled) 

                                     at MS.Win32.HwndSubclass.DispatcherCallbackOperation(Object o) 

                                     at System.Windows.Threading.ExceptionWrapper.InternalRealCall(Delegate callback, Object args, Int32 numArgs) 

                                     at System.Windows.Threading.ExceptionWrapper.TryCatchWhen(Object source, Delegate callback, Object args, Int32 numArgs, Delegate catchHandler)
```

2024.02.27 20:51:08.601         10044 [Client=UX, Thread=1] Opening C:\Users\edison\AppData\Roaming\Microsoft\Exchange Hybrid Configuration\20240226_143252.log

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-28*

Hello Adi Weissman,    

thank you for posting on the Microsoft Community Forums.     

Based on the description, I understand that your issue is related to Exchange.     

Since there are no engineers dedicated to Exchange in this forum. In order to be able to deal with your questions quickly and efficiently, I recommend that you repost your questions in the Q&A forum, where there will be a dedicated engineer to provide you with a professional and effective response.    

Here is a link to the Q&A forum: https://learn.microsoft.com/en-us/answers/questions/    

Have a nice day.    

Best regards,   

Lei
