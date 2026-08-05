---
title: "Unable read credentials for kerberose from shared state."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2731382/unable-read-credentials-for-kerberose-from-shared
question_id: 2731382
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: []
---
# Unable read credentials for kerberose from shared state.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2731382/unable-read-credentials-for-kerberose-from-shared (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,

We have a kerborse setup to connect to our remote host using Java GSS-API . We are trying to generate ticket using credential from LSA cache. But our java call is not able to read credentials from LSA cache. Below is the exception we are getting from the
 call.

javax.security.auth.login.LoginException: Username can not be obtained from sharedstate   

at com.sun.security.auth.module.Krb5LoginModule.promptForName(Unknown Source)  

at com.sun.security.auth.module.Krb5LoginModule.attemptAuthentication(Unknown Source)  

at com.sun.security.auth.module.Krb5LoginModule.login(Unknown Source)  

at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)  

at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)  

at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)  

at java.lang.reflect.Method.invoke(Unknown Source)  

at javax.security.auth.login.LoginContext.invoke(Unknown Source)  

at javax.security.auth.login.LoginContext.access$000(Unknown Source)  

at javax.security.auth.login.LoginContext$4.run(Unknown Source)  

at javax.security.auth.login.LoginContext$4.run(Unknown Source)  

at java.security.AccessController.doPrivileged(Native Method)  

at javax.security.auth.login.LoginContext.invokePriv(Unknown Source)  

at javax.security.auth.login.LoginContext.login(Unknown Source)  

at com.unisys.udt.backend.Kerberos.getTicket(Kerberos.java:104)  

at com.unisys.udt.backend.Kerberos.DoAuthentication(Kerberos.java:303)  

at com.unisys.udt.backend.HostConnection.loginUsingKerberos(HostConnection.java:4083)  

at com.unisys.udt.backend.HostConnection.LogOn(HostConnection.java:395)  

at com.unisys.udt.backend.preferences.HostConnectionDelegate.LogOn(HostConnectionDelegate.java:61)  

at com.unisys.udt.backend.preferences.HostConnectionDelegate.login(HostConnectionDelegate.java:220)  

at com.unisys.udt.backend.ui.views.HostManagerView.logIn(HostManagerView.java:958)  

at com.unisys.udt.backend.ui.views.HostManagerView.connectAs(HostManagerView.java:924)  

at com.unisys.udt.backend.ui.views.HostManagerView.access$9(HostManagerView.java:916)  

at com.unisys.udt.backend.ui.views.HostManagerView$HMVMenuListener.widgetSelected(HostManagerView.java:464)  

at org.eclipse.swt.widgets.TypedListener.handleEvent(TypedListener.java:248)  

at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)  

at org.eclipse.swt.widgets.Display.sendEvent(Display.java:4362)  

at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1113)  

at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:4180)  

at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3769)  

at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$4.run(PartRenderingEngine.java:1127)  

at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:337)  

at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:1018)  

at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:156)  

at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:694)  

at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:337)  

at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:606)  

at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:150)  

at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:139)  

at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)  

at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:134)  

at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:104)  

at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:380)  

at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:235)  

at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)  

at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)  

at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)  

at java.lang.reflect.Method.invoke(Unknown Source)  

at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:669)  

at org.eclipse.equinox.launcher.Main.basicRun(Main.java:608)  

at org.eclipse.equinox.launcher.Main.run(Main.java:1515)  

at org.eclipse.equinox.launcher.Main.main(Main.java:1488)

Could please advise us if there is any restrictions in accessing the LSA cache on windows.

## Answer (community) — community member

*upvotes: 0 · updated: 2016-10-19*

Hi,

Your question is outside the scope of this Community..

Kindly repost in the TechNet Forums:

https://social.technet.microsoft.com/Forums/en-US/home

Or MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
