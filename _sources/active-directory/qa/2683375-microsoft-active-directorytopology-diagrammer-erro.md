---
title: "Microsoft Active DirectoryTopology Diagrammer Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2683375/microsoft-active-directorytopology-diagrammer-erro
question_id: 2683375
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 64
qa_tags: []
---
# Microsoft Active DirectoryTopology Diagrammer Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2683375/microsoft-active-directorytopology-diagrammer-erro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello 

the instruction that i recv' on installing ADTD was install on any DC which i did( WS2008 R2 Standard, 64bit)  .net framework 4.5.1

When i click on discover i recv' that Error

"Unhandled exception has occurred in your application"

See the end of this message for details on invoking   

just-in-time (JIT) debugging instead of this dialog box.  

************** Exception Text **************  

System.TypeInitializationException: The type initializer for 'ADTD.Draw' threw an exception. ---> System.IO.FileNotFoundException: Could not load file or assembly 'ADODB, Version=7.0.3300.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a' or one of its dependencies.
 The system cannot find the file specified.  

File name: 'ADODB, Version=7.0.3300.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a'  

   at ADTD.Draw..cctor()  

WRN: Assembly binding logging is turned OFF.  

To enable assembly bind failure logging, set the registry value [HKLM\Software\Microsoft\Fusion!EnableLog] (DWORD) to 1.  

Note: There is some performance penalty associated with assembly bind failure logging.  

To turn this feature off, remove the registry value [HKLM\Software\Microsoft\Fusion!EnableLog].  

   --- End of inner exception stack trace ---  

   at ADTD.frmMain.btnDiscover_Click(Object eventSender, EventArgs eventArgs)  

   at System.Windows.Forms.Control.OnClick(EventArgs e)  

   at System.Windows.Forms.Button.OnClick(EventArgs e)  

   at System.Windows.Forms.Button.OnMouseUp(MouseEventArgs mevent)  

   at System.Windows.Forms.Control.WmMouseUp(Message& m, MouseButtons button, Int32 clicks)  

   at System.Windows.Forms.Control.WndProc(Message& m)  

   at System.Windows.Forms.ButtonBase.WndProc(Message& m)  

   at System.Windows.Forms.Button.WndProc(Message& m)  

   at System.Windows.Forms.Control.ControlNativeWindow.OnMessage(Message& m)  

   at System.Windows.Forms.Control.ControlNativeWindow.WndProc(Message& m)  

   at System.Windows.Forms.NativeWindow.Callback(IntPtr hWnd, Int32 msg, IntPtr wparam, IntPtr lparam)  

************** Loaded Assemblies **************  

mscorlib  

    Assembly Version: 2.0.0.0  

    Win32 Version: 2.0.50727.5485 (Win7SP1GDR.050727-5400)  

    CodeBase: file:///C:/Windows/Microsoft.NET/Framework/v2.0.50727/mscorlib.dll  

ADTD  

    Assembly Version: 2.2.4146.20801  

    Win32 Version: 2.2.4146.20801  

    CodeBase: file:///C:/Program%20Files%20(x86)/Microsoft%20Active%20Directory%20Topology%20Diagrammer/ADTD.exe  

System.Windows.Forms  

    Assembly Version: 2.0.0.0  

    Win32 Version: 2.0.50727.5483 (Win7SP1GDR.050727-5400)  

    CodeBase: file:///C:/Windows/assembly/GAC_MSIL/System.Windows.Forms/2.0.0.0__b77a5c561934e089/System.Windows.Forms.dll  

System  

    Assembly Version: 2.0.0.0  

    Win32 Version: 2.0.50727.5485 (Win7SP1GDR.050727-5400)  

    CodeBase: file:///C:/Windows/assembly/GAC_MSIL/System/2.0.0.0__b77a5c561934e089/System.dll  

System.Drawing  

    Assembly Version: 2.0.0.0  

    Win32 Version: 2.0.50727.5483 (Win7SP1GDR.050727-5400)  

    CodeBase: file:///C:/Windows/assembly/GAC_MSIL/System.Drawing/2.0.0.0__b03f5f7f11d50a3a/System.Drawing.dll  

Microsoft.VisualBasic  

    Assembly Version: 8.0.0.0  

    Win32 Version: 8.0.50727.5483 (Win7SP1GDR.050727-5400)  

    CodeBase: file:///C:/Windows/assembly/GAC_MSIL/Microsoft.VisualBasic/8.0.0.0__b03f5f7f11d50a3a/Microsoft.VisualBasic.dll  

Microsoft.VisualBasic.Compatibility  

    Assembly Version: 8.0.0.0  

    Win32 Version: 8.0.50727.5483  

    CodeBase: file:///C:/Windows/assembly/GAC_MSIL/Microsoft.VisualBasic.Compatibility/8.0.0.0__b03f5f7f11d50a3a/Microsoft.VisualBasic.Compatibility.dll  

Accessibility  

    Assembly Version: 2.0.0.0  

    Win32 Version: 2.0.50727.5483 (Win7SP1GDR.050727-5400)  

    CodeBase: file:///C:/Windows/assembly/GAC_MSIL/Accessibility/2.0.0.0__b03f5f7f11d50a3a/Accessibility.dll  

System.Xml  

    Assembly Version: 2.0.0.0  

    Win32 Version: 2.0.50727.5485 (Win7SP1GDR.050727-5400)  

    CodeBase: file:///C:/Windows/assembly/GAC_MSIL/System.Xml/2.0.0.0__b77a5c561934e089/System.Xml.dll  

************** JIT Debugging **************  

To enable just-in-time (JIT) debugging, the .config file for this  

application or computer (machine.config) must have the  

jitDebugging value set in the system.windows.forms section.  

The application must also be compiled with debugging  

enabled.  

For example:  

<configuration>  

    <system.windows.forms jitDebugging="true" />  

</configuration>  

When JIT debugging is enabled, any unhandled exception  

will be sent to the JIT debugger registered on the computer  

rather than be handled by this dialog box.

## Answers

_No answers on this thread._
