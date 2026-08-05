---
title: "Exchange 2016 and 2019 coexistance with F5 bigip"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/315848/exchange-2016-and-2019-coexistance-with-f5-bigip
question_id: 315848
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 and 2019 coexistance with F5 bigip

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/315848/exchange-2016-and-2019-coexistance-with-f5-bigip (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I currently have exchange 216 with DAG, last week I installed an exchange 2019 servers. I heard it can co-exist, so I set both exchange 2016 and 2019 server's VS to https://webmail.domain.com/ for all external and internal urls. Also put all exchange 2016 and 2019 in to F5, using F5's exchange iAPP. All exchange 2016 and 2019 are on the same iAPP VS. After that, I was getting a cert error autodiscover was randomly giving out exhange19.domain.com for internal VS name, I recycled auto discover app pool on all servers and the cert error went away. About 10 to 15 minutes later outlook could not connect, it was in disconnected status , connection status showed exchange directory was connected but having trouble connecting exchange mailbox. it kept on trying and after about 5 minutes later it got connected. Problem was it happening randomly. I rebooted all exchange 2016 and 2019 servers one at a time, still the same. I disabled exchange 2019 from F5 still the same problem. I setup a lab with almost same configuration using virtual servers, and lab outlook connects without problem. I looked at all evet logs and exchange logs but could not find any thing stood up, I ended up uninstalled exchange 2019, and everything came back normal. Questions: 1. Can exchange 2016 and 2019 server have same exchange VSes? eg: https://webmail.domain.com/owa, https://webmail.domain.com/ews etc? 2. Can exchange 2016 and 2019 servers be on the same F5 and same VS? 3. If 1 and 2 are not supported, why my lab exchange servers work? 4. If 1 and 2 are supported, what am I doing wrong? 5. Does any exchange 2016 or 2019 use IPv6? I disabled them. Thank you in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Hi @HyeongWookKim-7855 ,  

What VS you are referring to refers to Virtual directory?  

Have you tried using OWA to log in to the user's mailbox?  

Do all users have this issue? Or is it for users on a specific version of Exchange?

1.Accroding to my test in lab environment, I changed the URLs of the two Exchange virtual directories to be the same. After the mailboxes in the two Exchanges can be successfully logged in. So the Exchange 2016 and Exchange 2019 server could have the same virtual directory.

2.Regarding F5, I suggest you consult the provider of F5 to check the relevant recommended configuration. When you configure the same environment in the lab environment, did you configure F5?

3.Do you still have an Exchange 2019 server? If so, when the problem recurs, you could following the steps to check whether the autodiscover service work normally. Please make sure that certificate include the correct Subject and SAN. In addition, after making any changes to Virutal direcotry, please run the IISRESET in the Run start as Administrator to restart the IIS.  

-  Using the ExRca to check the Outlook connection, if any error occurs, a detailed error report will be generated.  

For more information: Microsoft Remote Connectivity Analyzer  

-  Run the Test E-mail AutoConfiguration.  

4.ccording to the Microsoft official article, it’s not recommend that you disable IPv6 or its components. It’s recommend using “Prefer IPv4 over IPv6” in prefix policier instead fo disabling IPv6. And in Exchange 2013 or later servers fully support IPv6 networks. Therefore, even if you aren't using IPv6, you don't need to disable IPv6 on your Exchange servers.  

For more information you could refer to: IPv6 support in Exchange 2013 and Guidance for configuring IPv6 in Windows for advanced users

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
