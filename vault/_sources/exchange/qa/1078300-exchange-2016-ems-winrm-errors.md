---
title: "Exchange 2016 EMS WINRM errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1078300/exchange-2016-ems-winrm-errors
question_id: 1078300
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 EMS WINRM errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1078300/exchange-2016-ems-winrm-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have a problem with an exchange 2016 cu23 installed in a windows 2016 datacenter.    

Every so often my customer when he reconnects via rdp the EMS reports the following errors:    

    

My customer always leaves the EMS open.    

I tried to verify the binding of the back end site by following this article https://practical365.com/the-winrm-shell-client-cannot-process-the-request/ and it is correct.    

I ran the winrm get winrm / config command and this is the result:    

Config    

    MaxEnvelopeSizekb = 500  

    MaxTimeoutms = 60000  

    MaxBatchItems = 32000  

    MaxProviderRequests = 4294967295  

    Client  

        NetworkDelayms = 5000  

        URLPrefix = wsman  

        AllowUnencrypted = false  

        Auth  

            Basic = true  

            Digest = true  

            Kerberos = true  

            Negotiate = true  

            Certificate = true  

            CredSSP = false  

        DefaultPorts  

            HTTP = 5985  

            HTTPS = 5986  

        TrustedHosts  

    Service  

        RootSDDL = O:NSG:BAD:P(A;;GA;;;BA)(A;;GR;;;IU)S:P(AU;FA;GA;;;WD)(AU;SA;GXGW;;;WD)  

        MaxConcurrentOperations = 4294967295  

        MaxConcurrentOperationsPerUser = 1500  

        EnumerationTimeoutms = 240000  

        MaxConnections = 300  

        MaxPacketRetrievalTimeSeconds = 120  

        AllowUnencrypted = false  

        Auth  

            Basic = false  

            Kerberos = true  

            Negotiate = true  

            Certificate = false  

            CredSSP = false  

            CbtHardeningLevel = Relaxed  

        DefaultPorts  

            HTTP = 5985  

            HTTPS = 5986  

        IPv4Filter = *  

        IPv6Filter = *  

        EnableCompatibilityHttpListener = false  

        EnableCompatibilityHttpsListener = false  

        CertificateThumbprint  

        AllowRemoteAccess = true  

    Winrs  

        AllowRemoteShellAccess = true  

        IdleTimeout = 7200000  

        MaxConcurrentUsers = 2147483647  

        MaxShellRunTime = 2147483647  

        MaxProcessesPerShell = 2147483647  

        MaxMemoryPerShellMB = 2147483647  

        MaxShellsPerUser = 2147483647  

I looked at the PowerShellMaxConcurrency parameter in the ThrottlingPolicy and it is set to 18.    

I tried to see if there was a proxy configured using the information from the article https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/winrm-cannot-process-request and the result is this:    

[PS] C:\Windows\system32>netsh winhttp show proxy    

Current WinHTTP proxy settings:    

```
Direct access (no proxy server)
```

Current WinHTTP proxy settings:    

```
Direct access (no proxy server)
```

I tried to see listening ports with the command:    

netstat -anp tcp    

Active Connections    

  Proto  Local Address          Foreign Address        State    

  TCP    0.0.0.0:25             0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:81             0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:110            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:143            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:443            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:444            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:465            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:475            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:476            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:477            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:587            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:593            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:717            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:808            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:890            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:993            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:995            0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:1801           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:1993           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:1995           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:2103           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:2105           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:2107           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:2525           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3800           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3801           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3803           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3823           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3828           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3843           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3863           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3867           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:3875           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:5060           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:5062           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:5065           0.0.0.0:0              LISTENING    

  TCP    0.0.0.0:5985           0.0.0.0:0              LISTENING    

If I run the winrm quickconfig    

[PS] C:\Windows\system32>winrm quickconfig    

WinRM service is already running on this machine.    

WinRM is already set up for remote management on this computer.    

If the customer closes and reopens the EMS that is in error, it reopens correctly.    

What can be the solution to this problem?    

Thank you    

Greetings

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-14*

Hi LilyLi2-MSFT,    

after adding 16gb of ram the problem never occurred.    

So it was due to a lack of memory.    

Thanks for the support

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-08*

Hi LilyLi2-MSFT,    

Thanks for the reply.    

All exchange services are running.    

There is no antivirus on the server and there are no errors in the event viewer.    

There are a couple of warnings and the first is this:    

A process serving application pool 'MSExchangeOWAAppPool' exceeded time limits during shut down. The process id was '16364'    

The second warning is ESE event id 906:    

A significant portion of the database buffer cache has been written out to the paging file. This may result in severe performance degradation.    

Could the cause be a lack of ram problem?    

I asked my customer to add 16GB of RAM.    

Also, as previously written, the error is random.    

EMS is always kept open by my customer.    

EMS works but those errors pop up every now and then.    

If I close them I can reopen the EMS connection correctly.    

So I don't know if it makes sense to restart the IIS since then by closing the error warning I can open the EMS.    

It almost seems that there is something happening and then it resolves itself.    

Thank you    

Greeting
