---
title: "Mobile devices (and GNOME3) won't connect to Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/173064/mobile-devices-and-gnome3-wont-connect-to-exchange
question_id: 173064
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Mobile devices (and GNOME3) won't connect to Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/173064/mobile-devices-and-gnome3-wont-connect-to-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

It's easier to explain with pictures:    

    

About the time we upgraded to Exchange Server 2019 issues starting popping--well, more like multiplie, Exchange has always been issue-y. We tried a lot of stuff from downgrading to Exchange Server 2016, insanely difficult to do, to going full nuclear doing a full wipe after days of coordinating user backups of files. The rest of directory data is gone.    

But that gave us a clean slate, we have a brand new directory in top condition, not everybody can have that luxury and Exchange still won't work, the one thing I think could've affected our systems is that we federated with Office365. Azure tends to overreach without giving the user/admin and opt-in first. Since then, all services were cancelled and there's no federation or directory sync with Azure but the issue is still there. Mobile clients won't connect. Android's Google Gmail can't be setup at all, it hangs forever until it show a message the server can't be contacting, in the meantime I've watched the firewall logs for activity and there's none. iOS discovers the services and set them up, allegedly, but in reality none would work, Notes, Mail, Contacts and the others we don't use, don't work.    

I figured it must be an ActiveSync error because these is what mobile clients use, but attempting to configure GNOME3 on Fedora (pick any version from around 28 and up) fails too this time hinting at a possible Autodiscover issue. I'm using manual input to setup clients though, I have to because the email and directory domains don't match. …    

–– credentials/server/domain details used for manual config ––    

emai address: test45@tiedtlaw email  .net    

email server: email.net (AKA member "mail" of domain "dirdomain.ex": mail.dirdomain.ex)    

–– credentials breakdown ––    

******@dirdomain.ex (AKA UPN)    

test45@DIRDOMAINEX    

dirdomain.ex\test45    

DIRDOMAINEX\test45    

[test45] (sAMAccountName/alias) + [dirdomain.ex] or [DIRDOMAINEX] in a different field/box    

DNS    

References anywhere used (external/internal DNS for example) to the email server always point to its naked domain name, never to its directory DNS name except [and only for] DNS MX records. A first level wildcard [e.g; *.email.net] point back the naked domain [@] so this server has full control of the domain which is not an Active Directory domain, though it's managed by Active Directory DNS. The naked domain uses A and AAAA records, not CNAMEs.    

In the meantime a relic of a mac Mini with macOS Server and minuscule memory is taking over Exchange's responsibilities (and killing it BTW) but this shouldn't be.    

Mail flow is working both ways. Some third party clients have been able to connect too, but my focus is on first party Exchange-compatible clients because it's what everybody's going to have access to.    

Windows, has none, but for the remaining Windows users we have an RDS server from which Outlook practically configures itself without the users doing anything but accepting what Outlook discovers on its own. We also have made nothing on out part to facilite this, it just happened. On macOS Autodiscover works perfectly setting up Mail, Notes, all that, you eventually need to change one domain name and that's it, but sometimes it just skips this and set things up on its own too. Unlike iOS, these apps are working corrrectly in macOS.    

I tried setting up the OAB because it's the only thing for which I found documentation but it still doesn't work. How can I restore access for mobile devices?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-25*

Hi @Vita-7585 ,  

Much appreciate for the information and screenshots provided, which are of great help in understanding issue background.  

In order to better solve this issue, I want to confirm the following points:  

1.What is your Exchange environment like? Is it currently in a state of hybrid deployment?  

2.According to your penultimate paragraph, I can understand that in both WindowsOS and MacOS, your outlook client can be successfully configured. If I misunderstood, please correct me in time. I noted that you mentioned "change one domain name". What does this process mean? If you could, please introduce it.  

3.->Mail flow is working both ways. Some third party clients have been able to connect too, but my focus is on first party Exchange-compatible clients because it's what everybody's going to have access to.  

What does the first party Exchange-compatible mean?  

4.All users have this issue or specific users have? Where is the user mailbox which has the problem, on-premise Exchange or online?

Please try to following the steps:  

1.In order to avoid policy interference, please check whether there are Device Access Rules or Exchange ActiveSync access settings in your Exchange organization  

2.Please run the following command to check the url of the ActiveSync and Autodiscover service:

```
Get-ActiveSyncVirtualdirectory | fl *url*  
Get-ClientAccessService | fl *uri*
```

3.I noted that you check the firewall logs, if there are no related logs, please check your DNS settings. Make sure they point to correct server.  

-  Please try to add the CNAME record.  

-  You also could following the format to create a SRV record:  

Service: _autodiscover  

Protocol: ._tcp  

Port Number: 443  

Host: mail.contoso.com  

The Outlook server namespace is mail.contoso.com.  

For more information you could refer to: Autodiscover in DNS  

4.Please check if there have any related log in the Event Viewer.

In addition, there is an article about "Troubleshoot ActiveSync with Exchange server" provide by Microsoft，which include check the UPN, check the AD permission and so on.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
