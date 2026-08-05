---
title: "Validate Hybrid Agent For Exchange Use Keeps Failing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138054/validate-hybrid-agent-for-exchange-use-keeps-faili
question_id: 138054
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Validate Hybrid Agent For Exchange Use Keeps Failing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138054/validate-hybrid-agent-for-exchange-use-keeps-faili (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we upgraded Exchange to CU18, and downloaded the O365 Hybrid Configuration to start the process of doing a Full Hybrid and migrating mailboxes. I've been stuck on one issue for 2 days now - when it checks the green marks for Hybrid Agent Setup the last part - "Validate Hybrid Agent for Exchange use" keeps failing no matter what I try. Per the logs I'm getting a 504 Gateway timeout error.

The connection to the server '1f9.resource.mailboxmigration.his.msappproxy.net' could not be completed., The call to 'https://19.resource.mailboxmigration.his.msappproxy.net/EWS/mrsproxy.svc' timed out. Error details: The request channel timed out while waiting for a reply after 00:00:09.9977695. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a longer timeout. --> The remote server returned an error: (504) Gateway Timeout. --> The remote server returned an error: (504) Gateway Timeout., The request channel timed out while waiting for a reply after 00:00:09.9977695. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a  

longer timeout., The remote server returned an error: (504) Gateway Timeout., The remote server returned an error: (504) Gateway Timeout.  

2020.10.25 12:12:29.642 10390 [Client=UX, Page=HybridConnectorInstall, Thread=13] Test duration 00:06:03.9328749

I spoke with O365 support and they set to reset the MRS proxy and IISRESET - not fixing the issue  

EWS Virtual directory - I tried adding Basic Auth, then removing

I found one blog that said remove MRS proxy, turn it back on then reset IIS  

Set-WebServicesVirtualDirectory –identity \"EWS (Default Web Site)" -MRSProxyEnabled $false  

Set-WebServicesVirtualDirectory –identity EXCHANGESERVER\"EWS (Default Web Site)" -MRSProxyEnabled $true  

Set-WebServicesVirtualDirectory –identity EXCHANGESERVER\"EWS (Default Web Site)" -BasicAuthentication $TRUE

Restart-WebAppPool MSExchangeServicesAppPool

This did not help

I tried the MSFT remote connectivity analyzer and getting the OK for my autodiscover - so not sure if it's looking at the inbound traffic

Does anybody know what this service is trying to accomplish?

I assume it's hitting the O365 URL, trying to authenticate?

If I knew what the process was, I could drill down further.

Thanks!

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-26*

Thanks for taking the time to help us out!

I tried the Powershell test script and received some errors towards the bottom:

PS C:\Powershell> Test-HybridConnectivity -TestO365Endpoints  

Testing connection to mscrl.microsoft.com on port 80  

Testing connection to crl.microsoft.com on port 80  

Testing connection to ocsp.msocsp.com on port 80  

Testing connection to www.microsoft.com on port 80  

Testing connection to login.windows.net on port 443  

WARNING: Ping to login.windows.net failed -- Status: TimedOut  

Testing connection to login.microsoftonline.com on port 443  

WARNING: Ping to login.microsoftonline.com failed -- Status: TimedOut  

Testing connection to watchdog.servicebus.windows.net on port 443  

WARNING: Name resolution of watchdog.servicebus.windows.net failed -- Status: HostNotFound  

Performing GET on https://watchdog.servicebus.windows.net:443  

Invoke-WebRequest : The remote name could not be resolved: 'watchdog.servicebus.windows.net'  

At C:\Powershell\HybridManagement.psm1:196 char:19  

-  $result = Invoke-WebRequest -Method Get -Uri $uri  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-WebRequest], WebExc  

eption  

-  FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeWebRequestCommand

I assumed that the Validation was looking for the MRS proxy to be available from the outside which it is, and I also added Basic Authentication, but it did not make any difference.

Do I also need to add port 8080 inbound to the server? Can I just do it for MSFT servers? I wish there was a more secure way of doing this vs opening ports at will.

Thanks!

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-26*

@Al Tab      

This looks a network configuration problem in your organization.    

I would confirm with you that whether there exist firewall or other network filter tools on your on-premises Exchange, if there are, try to remove them temporary. Then check again, if this error gone, it means the connection with Exchange online blocked by you firewall.    

You can also use steps below to check the connection between your Exchange on-premises and Exchange online: For more detailed information, you can have a look this article Verify connectivity    

-  Download sample script    

-  Switch EMS to the script location and import the cmdlets by running the following command    

 `Import-Module .\HybridManagement.psm1`    

-  Check the connection with command below:    

 `Test-HybridConnectivity -TestO365Endpoints`    

You will could know whether there exist network issue in your organization, it contains the "uniqueGUID.resource.mailboxmigration.his.msappproxy.net" URL(This URL need use 8080 port on your Exchange server).    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-21*

We just went through a full hybrid.  I came across this while looking for an answer to this issue after it broke.    

For me I realized it when I double checked my mx and spf listings.  I realized there was a missing name from the spf that must have been overwritten when we updated and I had an error where the Security Cert 'dislodged' itself after a reboot.  I had to go back in to IIS Manager and reassign the bindings.  There are a few posts out fixing the binding, it will also cause Exchange Powershell to not connect.   

So I've come up with this as troubleshooting steps:  

-  Double check mx AND spf records.  Make sure they include ALL the server names for both  

-  Check Powershell, ensure the bindings on the public mail certs are good  

Get-ExchangeCertificate -Server name  

Get-OABVirtualDirectory | FL server,url  

Enable-Exchangecertificate Services: POP,IMAP,SMTP,IIS  

Thumbprint:  (get from Get-ExchangeCert from above)  

-  Restart IIS, restart server  

When you run the hybrid configuration again, it shows the agent as active (if you already installed it, or tried to), everything goes through  

I double check to ensure the connectors on each side (on prem and o365) do not have duplicates.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-27*

Exact same issue on my side. I am running modern hybrid with the hybrid agent.  

It was running fine until the past days.  

I tried to rerun the HCW but it's getting stuck at the validation with the same 504 error same as on your side.

If I check the connections with Test-HybridConnectivity -TestO365Endpoints  

I get an SSL/TLS error. So it might be an issue on Microsofts AppProxy. (We are not doing any SSL Inspection or offloading)

PS C:\Users\XXXX\Desktop> Test-HybridConnectivity -testO365Endpoints  

Testing connection to mscrl.microsoft.com on port 80  

Testing connection to crl.microsoft.com on port 80  

Testing connection to ocsp.msocsp.com on port 80  

Testing connection to www.microsoft.com on port 80  

Testing connection to login.windows.net on port 443  

Testing connection to login.microsoftonline.com on port 443  

Testing connection to aadap-portcheck-seaus.connectorporttest.msappproxy.net on port 8080  

Performing GET on https://aadap-portcheck-seaus.connectorporttest.msappproxy.net:8080  

Invoke-WebRequest : The underlying connection was closed: Could not establish trust relationship for the SSL/TLS  

secure channel.  

At C:\Program Files\Microsoft Hybrid Service\HybridManagement.psm1:196 char:19  

-  $result = Invoke-WebRequest -Method Get -Uri $uri  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-WebRequest], WebExc  

eption  

-  FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeWebRequestCommand
