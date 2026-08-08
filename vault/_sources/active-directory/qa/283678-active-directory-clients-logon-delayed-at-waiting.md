---
title: "Active Directory Clients Logon delayed at \"waiting for user profile service\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/283678/active-directory-clients-logon-delayed-at-waiting
question_id: 283678
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Clients Logon delayed at "waiting for user profile service"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/283678/active-directory-clients-logon-delayed-at-waiting (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Work@/c/   Slow User Logon „waiting for user profile service” approx. 1,5 to 2 minutes waiting    

 For notebook and desktop users who using credential caching policy for work@/c/   and use the Azure VPN tunnel too, there is maybe some long logon time.    

After type in credentials for the domain the user has to wait approx. 2 to 3 minutes before logging in completely with the message “waiting for user profile service”. In that case, there is no VPN connection established before logging in. All our DC's are in Azure Infra as IaaS. Clients are running Windows 10 & DC are 2016 Datacenter Server. We have Azure AD & AD Infra on Iaas in Azure & they do not sync with each other.    

The behavior is starting approx. after 18.01.2021. The event viewer show nothing bad or waiting for some responses or timeouts a long time. We checked and had a look at changed domain policies or windows updates with no impact of our issue.    

If you’re connecting through Cisco VPN and connect with VPN before logging in you’ll have no long login time because the domain controller is available. Here everything is fine.    

I figured out first that this problem is solved if I delete the entry “Home Folder” in my AD object. Then I connect via Cisco VPN first and logon (normal logon time) – then I reboot and try connection without VPN before logon -> Login time is about 5 seconds. I change back to the entry in my AD object and logon time is still approx.. 2 minutes.    

After boot I login with my AD Account: Ankit001 .    

My Home Folder path is  \internaldomain.net\users\Controller__Data01\Ankit001\Homeshare.    

If I change from DFS path to local fileserver path \descspcwfs01.internaldomain.net\Controller_Data01$\Ankit001\Homeshare  and connect first via Cisco VPN then reboot and login again with Ankit001 the login is fast (5 seconds).    

If I change back to the DFS path and log in again through Cisco VPN, boot client and logon takes up to 2 minutes.    

Then I put focus on DFS and username. In my constellation my Pre-Windows 2000 prefix is ankit001.internaldomain.net and User logon name (UPNP) is ******@externaldomain.com . I try logging in without VPN with my UPNP ******@externaldomain.com the logon time is about 5 seconds.    

Logoff and try logging in without VPN with pre2000 name is about 2 minutes waiting time.    

So I change back my UPNP from ******@externaldomain.com to ******@internaldomain.net, boot and connect with Cisco VPN – login – boot and try logging in with no VPN connection takes 2 minutes.    

Workaround for Azure VPN users who are using ******@externaldomain.com in User Logon Name:    

1st – Login with UPNP ******@externaldomain.com and not with Pre-Windows 2000 Logon Name    

2nd – Change DFS to the local path in “home folder”. But that contains the possibility to login first through Cisco VPN and after change, you can use Azure VPN without long login    

Seems that recently using pre2000 logon name in combination with DFS path in home folder path and credential caching to login without domain connectivity gets the long waiting time.    

Do you have any idea about this logon time? This is affecting multiple locations.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-25*

@Anonymous       

Thank You for your devoting you time to respond & outlining the steps to Capture the netmon traces but i guess that will require quite a lot time to analyze the logs and will still not provide a solution to the problem.     

I would also like to update you that on the client when users logon then they are getting Event ID 6006 in Application Log:    

------------------------------------------------------------------------------------------------------------------    

The login notification subscriber profiles has 198 seconds to process this logon notification event.    

------------------------------------------------------------------------------------------------------------------    

The domain controllers are in Azure & the client are connecting using AZURE VPN. Unlike Cisco VPN the Azure VPN Client does not gives an option to connect before the user logs IN.     

Can you advise #1) How can I make Azure VPN client available at the logon screen before user logs ON so that user can connect to VPN first.    

If I use a local file server path even then the client is still connecting from Home, thus the local file server is unreachable during logon as they is no VPN but still the logon is quick. Any clue why does the issue happens only when DFS share is provided and not with local server when both are unreachable at Logon? The same logon process was working fine uptill january 18, 2021 and this issue started happening all of a sudden. I have a requirement to use DFS share and cannot use local file server.    

Can you advise #2) If somehow I can force the client to login without checking for the remote dfs pathduring logon & the client can silently continue to complete its path check process in the background so that users can quickly login without this delay. Once the user logsIn the user will connect VPN.    

Would appreciate if you can provide more clarity on my point #1 & #2. Incase you have any other suggestion then kindly let me know.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-23*

Hello @Micro_Techie  ,

Thank you for posting here.

If you set DFS path for "Home folder", it seems it is looking for path \internaldomain.net\users\Controller__Data01\Ankit001\Homeshare when user is sign in, but because there is no VPN connection, it can not find such path after looking for, so the takes 2-3 mins.

As you mentioned, we suggest you can set local path for "Home folder" or connect to VPN before user sign in.

If you want to find the possible casue for such case, I suggest you can capture the netmon during the issue reproduce and try to check where the 2-3 mins took in the netmon.

About how to capture network traffic:  

1.Logon the machine with local Administrator account.  

2.Choose the version for your system to download, install it as typical: https://www.microsoft.com/en-US/download/details.aspx?id=4865  

3.Run Network Monitor as admin  

4.In the bottom left-hand, choose the NIC or NICs you want to capture.  

5.Then start capture.  

6.Run the following commands to clear credentials.  

ipconfig /flushdns  

nbtstat -R  

klist purge  

klist purge -li 0x3e7

7.Switch user account and logon with domain account.  

8.After the necessary information is collected, click stop.

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
