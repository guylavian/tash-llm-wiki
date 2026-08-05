---
title: "New installation of Exchange 2013 ECP/OWA not working HTTP error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202675/new-installation-of-exchange-2013-ecp-owa-not-work
question_id: 202675
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# New installation of Exchange 2013 ECP/OWA not working HTTP error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202675/new-installation-of-exchange-2013-ecp-owa-not-work (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have an exchange 2013 environment. We are doing a project to migrate data center migration of exchange servers to DC1 and DC2. We are just building new Exchange 2013 servers in DC2 and planning to migrate mailboxes from DC1 Exchange boxes to DC2 Exchange boxes. However after installing Exchange servers on DC2, none of the servers OWA/ECP not working and giving HTTP 500 error. Powershell works and using powershell to configure most of the stuffs. However ECP and OWA isn't working. Checked all virtual directories and all seem to be okay. Can someone help?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-29*

There were network/firewall block between old exchange site to new exchange site. The moment restrictions were removed, OWA/ECP started working. Before that none of the instructions were working. Unblocking network restrictions fixed it for me.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

Hi @GoodResource   ,  

Please try to following the steps and see if the issue is resolved:  

1:  

-  Run the following command in CMD started as administrator:    %windir%\Microsoft.NET\Framework\v4.0.30319\aspnet_regiis.exe –i  

2) Open the IIS and go to the Application Pool. Then recycle the “MSExchangeOWAppPool” and “MSExchangeECPAppPool”.  

3) Restart the IIS.

2:  

-  Open the ADSIEDIT.msc, then connect to the “Configuration”.  

-  Go to: CN=Configuration then CN=Services then CN=Microsoft Exchange then CN=Your DOMAIN Name and navigate to CN-Client Access  

-  Right-click [CN=Client Access]and click Properties. Scroll down to look for values  

msExchCanaryData0  

msExchCanaryData1  

msExchCanaryData2  

msExchCanaryData3  

4)Take a backup to be safe and clear all these values to<not set>.  

For the specific steps you could refer to：Exchange 2013 Troubleshooting: Error 500 when login ECP and OWA  

3: Run the UpdateCas.ps1 powershell script located in the C:\Program Files\Microsoft\Exchange Server\V15\Bin folder, then run the IISRESET to start the IIS.  

4: It should be noted that the virtual directory authentication methods of ECP and OWA must be consistent.  

In addition, is there any related logs in the Event Viewer? If so, please share with us, please cover your personal information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
