---
title: "Error during Exchange 2019 installation (ID 1002, 4027)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/367794/error-during-exchange-2019-installation-id-1002-40
question_id: 367794
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Error during Exchange 2019 installation (ID 1002, 4027)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/367794/error-during-exchange-2019-installation-id-1002-40 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

My environment:  

Active Directory – 2 domain controllers on Windows 2016, 2016 Domain level, 2012 R2 Forest Level  

Exchange 2013 – 2 serwers. One Front, one mailbox.  

We want to migrate to Exchange 2019.

During the installation of new Exchange 2019 CU9 on the new Windows 2019 Server (Full update), we get below error (Event ID 1002 in Windows application logs):

Error:  

The following error was generated when "$error.Clear();  

$maxWait = New-TimeSpan -Minutes 8  

$timeout = Get-Date;  

$timeout = $timeout.Add($maxWait);  

$currTime = Get-Date;  

$successfullySetConfigDC = $false;  

while($currTime -le $timeout)  

{  

$setSharedCDCErrors = @();  

try  

{  

Set-SharedConfigDC -DomainController $RoleDomainController -ErrorVariable setSharedCDCErrors -ErrorAction SilentlyContinue;  

$successfullySetConfigDC = ($setSharedCDCErrors.Count -eq 0);  

if($successfullySetConfigDC)  

{  

break;  

}  

Write-ExchangeSetupLog -Info ("An error ocurred while setting shared config DC. Error: " + $setSharedCDCErrors[0]);  

}  

catch  

{  

Write-ExchangeSetupLog -Info ("An exception ocurred while setting shared config DC. Exception: " + $_.Exception.Message);  

}  

> Write-ExchangeSetupLog -Info ("Waiting 30 seconds before attempting again.");  

Start-Sleep -Seconds 30;  

$currTime = Get-Date;  

}  

> if( -not $successfullySetConfigDC)  

{  

Write-ExchangeSetupLog -Error "Unable to set shared config DC.";  

}  

" was run: "System.Exception: Unable to set shared config DC.  

at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  

at Microsoft.Exchange.Management.Deployment.WriteExchangeSetupLog.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

There is alsa en error with the ID 4027 in the system logs> Windows Logs> Aplication

Process ExSetupUI.exe (PID=2068). WCF request (Set Config DC DOMAIN.NAIM) to the Microsoft Exchange Active Directory Topology service on server (TopologyClientTcpEndpoint (localhost)) failed. Make sure that the service is running. In addition, make sure that the network ports that are used by Microsoft Exchange Active Directory Topology service are not blocked by a firewall. The WCF call was retried 3 time(s). Error Details  

System.ServiceModel.EndpointNotFoundException: Could not connect to net.tcp://localhost:890/Microsoft.Exchange.Directory.TopologyService.  

„The connection attempt lasted for a time span of 00:00:02.0468699. TCP error code 10061: No connection could be made because the target machine actively refused it 127.0.0.1:890. ---> System.Net.Sockets.SocketException: No connection could be made because the target machine actively refused it 127.0.0.1:890  

at System.Net.Sockets.Socket.DoConnect(EndPoint endPointSnapshot, SocketAddress socketAddress)  

at System.Net.Sockets.Socket.Connect(EndPoint remoteEP)  

at System.ServiceModel.Channels.SocketConnectionInitiator.Connect(Uri uri, TimeSpan timeout)  

--- End of inner exception stack trace ---

Server stack trace:  

at System.ServiceModel.Channels.SocketConnectionInitiator.Connect(Uri uri, TimeSpan timeout)  

at System.ServiceModel.Channels.BufferedConnectionInitiator.Connect(Uri uri, TimeSpan timeout)  

at System.ServiceModel.Channels.ConnectionPoolHelper.EstablishConnection(TimeSpan timeout)  

at System.ServiceModel.Channels.ClientFramingDuplexSessionChannel.OnOpen(TimeSpan timeout)  

at System.ServiceModel.Channels.CommunicationObject.Open(TimeSpan timeout)  

at System.ServiceModel.Channels.ServiceChannel.OnOpen(TimeSpan timeout)  

at System.ServiceModel.Channels.CommunicationObject.Open(TimeSpan timeout)

Exception rethrown at [0]:  

at System.Runtime.Remoting.Proxies.RealProxy.HandleReturnMessage(IMessage reqMsg, IMessage retMsg)  

at System.Runtime.Remoting.Proxies.RealProxy.PrivateInvoke(MessageData& msgData, Int32 type)  

at System.ServiceModel.ICommunicationObject.Open()  

at Microsoft.Exchange.Net.ServiceProxyPool`1.GetClient(Int32 retry, Boolean& doNotReturnProxyAfterRetry, Boolean useCache)      at Microsoft.Exchange.Net.ServiceProxyPool`1.TryCallServiceWithRetry(Action`1 action, String debugMessage, WCFConnectionStateTuple proxyToUse, Int32 numberOfRetries, Boolean doNotReturnProxyOnSuccess, Exception& exception)

In C:\ExchangeSetupLogs\ExchangeSetup.txt we got

[04.21.2021 10:15:41.0245] [2] Active Directory session settings for 'Set-SharedConfigDC' are: View Entire Forest: 'True', Configuration Domain Controller: 'NTAD01.DOMAIN.NAME', Preferred Global Catalog: 'NTAD01.DOMAIN.NAME', Preferred Domain Controllers: '{ NTAD01.DOMAIN.NAME }'  

[04.21.2021 10:15:41.0245] [2] User specified parameters: -DomainController:'NTAD01.DOMAIN.NAME' -ErrorVariable:'setSharedCDCErrors' -ErrorAction:'SilentlyContinue'  

[04.21.2021 10:15:41.0245] [2] Beginning processing Set-SharedConfigDC  

[04.21.2021 10:15:41.0433] [2] The call to Microsoft Exchange Active Directory Topology service on server 'TopologyClientTcpEndpoint (localhost)' returned an error. Error details No Suitable Directory Servers Found in Forest DOMAIN.NAME Site Default-First-Site-Name and connected Sites..  

[04.21.2021 10:15:41.0433] [2] No Suitable Directory Servers Found in Forest DOMAIN.NAME Site Default-First-Site-Name and connected Sites.

Additional information:  

-  IPv6 is enabled on all Exchange serwers and domain controllers.  

-  We recovered the default domain controller policy because it was modified by a previous IT employee  

-  we have verified DNS configuration, it looks ok. Domain controllers have correct entries, nslookup replies with correct addresses.  

-  we deleted usused site in AD Site and Services.  

-  no firewall on Exchange and Active Directory (Windows firewall off)

any ideas ?

Regards  

Daniel

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-04-22*

how bout this?  

https://thejespernilsson.wordpress.com/2017/01/14/an-exception-ocurred-while-setting-shared-config-dc/  

Solution: Added the group “<domain>\Exchange Servers” to the user right assignment “Manage auditing and security log” on the custom GPO with the higher Link Order (precedence) and Exchange installed just fine after performing GPUpdate on the Domain Controllers.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-05*

Installation of Cu23 on EX02-2013 has failed. Error related to VirtualFolder ECP (Exchange Back End) - did not exist in adsiedit.  

We got the exchnge server and domain controllers back. We don't want to try to update it again.  

I installed the new server EX13 (Exchange 2013 CU23). I will want to migrate all mailboxes to it and then uninstall problematic EX02-2013.   

I am thinking of creating a DAG between the problematic EX02-2013 and new EX13 (CU23). Then perform database replication (copy), disable and delete the databases on the old server EX02-2013, and uninstall the server. Then install new Exchange 2019 servers and migrate mailobxes to them.  

Do you think such a scenario is possible (DAD on 2013 SP1 and 2013 CU23)? Exchange DAG supports servers with different CU version , this is how servers are updated, i.e. sequentially.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-28*

The first problem was solved by installing Exchange 2019 CU8. The installation went smoothly.

Unfortunately, right after the installation on new servers there was a problem with access to OWA / ECP / Autodiscover etc. htttp error 500 after entering OWA or ECP.
Again, try to solve the problem by recreating OWA / ECP and backend among others. Without success.
Due to many different unusual bugs and the fact that I do not know the history of the Active Directory / Exchange environment, I decided to check a few things more closely.

I decided to check Exchange 2013 versions

C:\>Get-ExchangeServer | Format-List Name, Edition, AdminDisplayVersion
Name : EX01-2013
Edition : Standard
AdminDisplayVersion : Version 15.0 (Build 1497.2)
Name : EX02-2013
Edition : Standard
AdminDisplayVersion : Version 15.0 (Build 1497.2)

Here everything looks ok. Both Exchange 2013 CU23, with the newest CU (CU 22 i requiered to install 2019 in Exchange 2013 orgnization)

But here I found a problem, file versions different than Exchange AdminDisplayVersion

On EX01-2013 C:\>Get-Command Exsetup.exe | ForEach-Object {$_.FileVersionInfo}

ProductVersion FileVersion FileName
-------------- ----------- --------
15.00.1497.012 15.00.1497.012 C:\Program Files\Microsoft\Exchange Server\V14\bin\ExSetup.exe

On EX02-2013 C:\>Get-Command Exsetup.exe | ForEach-Object {$_.FileVersionInfo}

ProductVersion FileVersion FileName
-------------- ----------- --------
15.00.0847.012 15.00.0847.012 C:\Program Files\Microsoft\Exchange Server\V14\bin\ExSetup.exe

It turned out that the EX02-2013 server has different file versions than the system shows. I asked the administrators and it turned out that some time ago during the update of Exchange 2013 to CU23 the EX01-2013 server was updated without any problems and on the EX02-2013 server the update failed and it was recovered from the backup.
Now Active Directory / Exchange Organization has version CU23 entered but one of the servers (EX02-2013) has files Exchange Server 2013 SP1 February 25, 2014 15.0.847.32 15.00.0847.032 This version (Exchange 2013 SP1) is not compatible with Exchange 2019. Could it be all these problems?

I wonder what you can do with it?
Two options come to mind.

1) Try to update again on server EX02-2013 to CU23? I don't know what went wrong the first time.
The link on the MS site is not working https://www.microsoft.com/download/details.aspx?id=58392
I'm trying to enter from the site https://learn.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019

2) Install a new Exchange 2013 with CU23, migrate the mailboxes from problematic EX02-2013 to a new server, uninstall "broken" EX02-2013. Try installing Exchange 2019 again.

regards
Daniel

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-23*

Hi @Daniel-8736,    

When the error occurs, please have a go by manually starting the "Microsoft Exchange Active Directory Topology service" and see if it could help.     

Furthermore, the blog below shares a solution to the first error you stated above, and in the comment section, a user mentioned that after adding the key MinSuitableServer = "1" to the Microsoft.Exchange.Directory.TopologyService.exe.config file as suggested in the blog, the error 4027 stopped("I added that key then the 4027 & 2142 are stopped ,all exchange servers worked."):    

Exchange 2013 Setup Fails With Error "An exception ocurred while setting shared config DC"    

So I would recommend have a look at the article and give it a try to see the result.    

By the way, according to Exchange 2019 system requirements, the supported coexistence scenario between Exchange 2019 and Exchange 2013 requirs Exchange 2013 CU21 or later, so please ensure that this requirement has been met in your environment.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
