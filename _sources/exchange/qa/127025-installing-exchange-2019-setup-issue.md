---
title: "Installing Exchange 2019 Setup Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/127025/installing-exchange-2019-setup-issue
question_id: 127025
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Installing Exchange 2019 Setup Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/127025/installing-exchange-2019-setup-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey All,

Installing Exchange 2019 on Server 2019.  

This is the first Exchange in this domain as we are 100% O365.  

I have done the /PrepareAD as per the guide. Installing gets to Step 6 of 12: Mailbox role: Transport service with the below error.  

Error:  

The following error was generated when "$error.Clear();  

$maxWait = New-TimeSpan -Minutes 8  

$timeout = Get-Date;  

$timeout = $timeout.Add($maxWait);  

$currTime = Get-Date;  

$successfullySetConfigDC = $false;

```
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

        Write-ExchangeSetupLog -Info ("Waiting 30 seconds before attempting again.");
        Start-Sleep -Seconds 30;
        $currTime = Get-Date;
      }

      if( -not $successfullySetConfigDC)
      {
        Write-ExchangeSetupLog -Error "Unable to set shared config DC.";
      }
    " was run: "System.Exception: Unable to set shared config DC.
```

at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  

at Microsoft.Exchange.Management.Deployment.WriteExchangeSetupLog.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

I have rebooted the new Exchange server. i can access the AD server from the Exchange. Not sure what else to try i have googled a bit but nothing has helped so far.

Thanks,  

Ben

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-29*

Hey Eric,  

Yes that link worked well. i got exchange installed with Mailbox and Management and setup the Hybrid connection to O365 Exchange.  

i have a question about this. Can i manage Office365 mailboxes from on Prem?   

We are 100% Exchange online so no on-Prem mailboxes are needed, we just want to be able to manage our Office365 Mailboxes and such from on prem, use of Exchange management Shell and such. Also to use the Schema for Exchange, hide from address lists ect...  

Did i install the right version of Exchange? im not seeing the Office365 mailboxes in recipients.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

Hey Sorry for the Late reply.  

I have tried the suggest fixes and all do not work.  

Event ID 4027 - Exchange server has firewall off and AD i have opened 890 UDP and TCP.  

Process MSExchangeHMWorker.exe (ExHMWorker) (PID=4240). WCF request (Get Servers for XXXXXXX.com.au) to the Microsoft Exchange Active Directory Topology service on server (TopologyClientTcpEndpoint (localhost)) failed. Make sure that the service is running. In addition, make sure that the network ports that are used by Microsoft Exchange Active Directory Topology service are not blocked by a firewall. The WCF call was retried 3 time(s). Error Details   

 System.ServiceModel.EndpointNotFoundException: Could not connect to net.tcp://localhost:890/Microsoft.Exchange.Directory.TopologyService. The connection attempt lasted for a time span of 00:00:02.0470326. TCP error code 10061: No connection could be made because the target machine actively refused it 127.0.0.1:890.  ---> System.Net.Sockets.SocketException: No connection could be made because the target machine actively refused it 127.0.0.1:890  

   at System.Net.Sockets.Socket.DoConnect(EndPoint endPointSnapshot, SocketAddress socketAddress)  

   at System.Net.Sockets.Socket.Connect(EndPoint remoteEP)  

   at System.ServiceModel.Channels.SocketConnectionInitiator.Connect(Uri uri, TimeSpan timeout)  

   --- End of inner exception stack trace ---  

Event ID 6  

Cmdlet failed. Cmdlet Set-SharedConfigDC, parameters -DomainController "xxxxxxxxxxxxx" -ErrorVariable "setSharedCDCErrors" -ErrorAction "SilentlyContinue".  

Not found any event ID 2112.
