---
title: "Change interface from static IP to DHCP via GPO startscript/Powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/607295/change-interface-from-static-ip-to-dhcp-via-gpo-st
question_id: 607295
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Change interface from static IP to DHCP via GPO startscript/Powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/607295/change-interface-from-static-ip-to-dhcp-via-gpo-st (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to change the interfaces of all computers of two AD OUs. Currently all interfaces have static IPs and DNS servers. I wrote this Powershell Script:  

```
$getIP = get-netipaddress | Where-Object IPAddress -Like "192.168.18.*"
$index = $getip.InterfaceIndex
Get-NetIPInterface | where-Object InterfaceIndex -like "$index" | Set-NetIPInterface -Dhcp Enabled
$rep = Get-NetIPInterface | where-Object InterfaceIndex -like "$index"
$rep1 = $rep.InterfaceAlias
$Hostn = hostname
$Test = Get-NetIPInterface -InterfaceIndex $index | Where-Object {$_.Dhcp -like "Enabled"}
if ($Test){
$DHCPSTATUS = "DHCP active"
$report = "The Interface $Rep1 on $Hostn was set to DHCP . The DNS Server are resettet"
Set-DnsClientServerAddress -InterfaceIndex "$index" -ResetServerAddresses
}
else{
$DHCPSTATUS = "DHCP_not_active"
$report = "The Interface $Rep1 on $Hostn was NOT set to DHCP . The DNS Server are NOT resettet"
}
$report | Out-File \\Server\d$\DHCP\Result\$Hostn"_"$DHCPSTATUS.txt
```

For the two OUs I enabled a GPO with a Startscript:   https://i.stack.imgur.com/ZSZbV.png  

When I run gpresult, It shows that the GPO was used, but nothing happened to the interface, neither was a txt written.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-25*

Hello!!!    

You must put your .ps1 unde the NETLOGON folder .    

On Windows Server 2012R2 and Windows 8.1 and newer, PowerShell scripts in GPO are run from the NetLogon directory in the Bypass mode. This means that PowerShell Script Execution Policy settings are ignored. If you want to run a script from a different shared folder, or if you still have Windows 7 or Windows Server 2008R2 clients on your network, you need to configure the PowerShell script execution policy.    

By default, Windows security settings do not allow running PowerShell scripts. The current value of the PowerShell script execution policy setting can be obtained using the Get-ExecutionPolicy cmdlet. If the policy is not configured, the command will return Restricted (any scripts are blocked). The security settings for running the PowerShell script can be configured via the “Turn On Script Execution” policy (in the GPO Computer Configuration section -> Administrative Templates -> Windows Components -> Windows PowerShell). Possible policy values:    

Allow only signed scripts (AllSigned) – you can run only signed PowerShell scripts (“How to digitally sign a PowerShell script?”) — this is the best option from a security perspective;    

Allow local scripts and remote signed scripts (RemoteSigned) – you can run any local and signed remote scripts;    

Allow all scripts (unrestricted) – the most insecure option, because allows running any PowerShell scripts.    

Source: http://woshub.com/running-powershell-startup-scripts-using-gpo/#:~:text=If%20you%20want%20to%20run%20the%20PowerShell%20script%20at%20a,Policies%20%2D%3E%20Windows%20Settings%20%2D%3E
