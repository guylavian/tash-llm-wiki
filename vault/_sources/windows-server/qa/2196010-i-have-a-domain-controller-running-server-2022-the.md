---
title: "I have a domain controller running server 2022.  The NPS console crashes every time I open out.  The NPS PowerShell commands still work."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196010/i-have-a-domain-controller-running-server-2022-the
question_id: 2196010
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-network-connectivity-file-sharing"]
---
# I have a domain controller running server 2022.  The NPS console crashes every time I open out.  The NPS PowerShell commands still work.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196010/i-have-a-domain-controller-running-server-2022-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The error messages in the application event log are:

Faulting application name: mmc.exe, version: 10.0.20348.2520, time stamp: 0x72fcf7c3

Faulting module name: clr.dll, version: 4.8.9246.0, time stamp: 0x6614acc6

Exception code: 0xc0000005

Fault offset: 0x000000000006cc99

Faulting process id: 0x2b4c

Faulting application start time: 0x01dac0a4a430eda3

Faulting application path: C:\Windows\system32\mmc.exe

Faulting module path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll

Report Id: 3498b10a-a521-492e-a359-9b117f831475

Faulting package full name: 

Faulting package-relative application ID: 

Application: mmc.exe

Framework Version: v4.0.30319

Description: The process was terminated due to an internal error in the .NET Runtime at IP 00007FFCB93FCC99 (00007FFCB9390000) with exit code 80131506.

Everything else on that server is running fine

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-02*

Looks like this was a problem with the ISO I'd used to build the domain controllers.  I downloaded a newer ISO, created a template from it and the VMs I spun up from that template were fine

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-22*

Hello Keith,

If you or anyone else in your organisation is comfortable using a debugger, then one could try catching the fault. One can use either a native or managed debugger. One does not necessarily need to install any debugging tools - one can just run the tools installed on your personal system:

Even simple use of the debugger would probably give a useful hint about the cause of the problem.

In the absence of such a useful hint, I would check the contents of the 3 configuration files in the directory \Windows\System32\ias: dnary.xml, dnary.xsd and ias.xml (check for XML validity and anything that seems out-of-place).

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-20*

Hi Keith Lynch2,

Thank you for your reply. I suggest you check the event log again to see if the error is the same as before.

Best Regards

Zunhui

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-17*

Hi Zunhui,

That didn't fix it I'm afraid.  When I ran the repair tool I got the following:

I let the repair tool resolve those issues and then I reinstalled the .NET Framework 4.8.1 installer.  NPS still crashes a few seconds after opening.  If I open an MMC and then add the network policy server snap in the MMC won't crash until I try to access the properties of a radius client or policy.

Regards,

Keith

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-17*

Hello,

Based on the information you provided, we suspect that it is related to the corruption of the .NET Framework configuration file. We recommend that you download Microsoft's Microsoft .NET Framework Repair Tool to repair it and then restart to see if the problem can be fixed. 

Download address: Download Microsoft .NET Framework Repair Tool from Official Microsoft Download Center

Best Regards

Zunhui
