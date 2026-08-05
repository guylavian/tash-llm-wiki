---
title: "Exchange Server stopped sending and receiving"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/227216/exchange-server-stopped-sending-and-receiving
question_id: 227216
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Exchange Server stopped sending and receiving

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/227216/exchange-server-stopped-sending-and-receiving (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We had to change ISPs today and reconfigured our MX record, etc. but now Exchange Server will not send or receive either internal or external. What could be causing this? Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-14*

Hi @Sam May   ,  

Did you change any settings of Exchange before this issue occurred?  

Agree with the above opinions.  

1.First, please check whether the updated DNS records are correct, and it will take a while for the updated DNS records to take effect, so please wait for a while and try again.  

2.Please try to send a test mail and run the command line to view the queue, especially the parameter "last error", which will show the reason why the mail is stuck in the queue.

```
Get-queue | fl
```

3.The email failed to send, is there any DNR generated, if so, please share the complete DNR with us. But please pay attention to covering your personal information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-12*

Agreed with Cheong00 & AshokM, I would looks at your DNS and MX records to ensure they are set properly and if your operating your DNS with an external provider like DNS made Easy or other service I would check to see how long replication can take. Depending on whats occurring it can take some time to complete.

-   Use an external provided to check accuracy of DNS, MX records etc like MXToolbox https://mxtoolbox.com/

-   I would also check your internal DNS settings to ensure they have properly updated as well

-   You just changed ISPs and didn't change location or IP of the server, correct?

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-12*

Hi @Sam May   ,    

As per my understanding, these are multiple issues.     

If internal email is not working, then it has to be checked within the Exchange server like services, any recent changes, queues and bounce back messages.    

For issue with sending emails to internet, then Send connector configuration    

-  If the routing is via smarthost, then emails are stuck in queue or any error messages    

-  If its using MX record to outbound, is external DNS resolution working fine    

If the MX record is not updated, then it will cause issues in receiving emails from internet and not sending. If the MX record is still showing the old record then that means TTL value of the old one might be the cause and have to wait till it replicates. If the MX record is not updated properly or showing new one but still an issue in receiving, then what is the error message when you send from external.    

If the above suggestion helps, please click on "Accept Answer" and upvote it

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-01-12*

Assuming your Exchange server is configured correctly(I assume the domain names not changed, so it should stay the same), the DNS record of external network may not have updated their DNS record.  

The other possibility is that the routing to your Exchange server is on one-to-one-NAT, so you need to update the IP mapping for it to work.  

A less common possibility (let's hope this not be the case) is that the new ISP does not allow inbound SMTP port. This will usually occur if you rent an office in residential area, and you accidentally signed up for a "not-for-work" plan.  

Try doing "nslookup" for your domain and look at the MX record setting from a client that known to unable send you email to verify if this is your case. If it's not that case, try take a look at their SMTP server log and see if there is some hint on what happened.  

======  

Usually before moving email servers, we'll set the TTL of DNS record to low value (say, 15 minutes) and restore the value after done with transition . Since most mail server will retry after 5, 15 then 30 minutes when unable to contact destination mail server, this will allow you make the change with minimal disruption to service. Also, we'll use DNS View feature to setup temporary updated records to test machines to make sure the new mail server works correctly before actual act of moving. (Always good to have 2 days to a week of overlapping times on both ISP service contracts)
