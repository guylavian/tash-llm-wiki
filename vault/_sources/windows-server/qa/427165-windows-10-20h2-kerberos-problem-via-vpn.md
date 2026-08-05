---
title: "Windows 10 20h2 Kerberos problem via VPN"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/427165/windows-10-20h2-kerberos-problem-via-vpn
question_id: 427165
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Windows 10 20h2 Kerberos problem via VPN

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/427165/windows-10-20h2-kerberos-problem-via-vpn (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

we've got a business environment (Active directory) with two Domain Controller (both running Win Server 2016, 1607; but latest Updates). Our clients are still on Windows 10 1903. Now we want to upgrade the clients to Windows 10 20h2.  

The upgrade process works fine and being in the LAN we can connect to all file server, sql server, ... . But when we are working remote via VPN (Microsoft Azure Always On) we can't connect to the server. The authentication the servers doesn't seem to work (the VPN authentication works).    

In Windows Explorer the users gets the error message:  

"Microsoft Windows Network: The user name could not be found" (translated from German)   

In SQL Management Studio (SQL Server) the user gets the error message:  

"The target Principal Name is incorrect. The SSPI context could not be generated).  

Can anyone give us a hint where we could look for the error?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-28*

Hello @Thies  ,

The following text, taken from https://learn.microsoft.com/en-us/windows/security/identity-protection/vpn/vpn-conditional-access, might be relevant:

Currently, it is required that certificates used for obtaining Kerberos tickets must be issued from an on-premises CA, and that SSO must be enabled in the user’s VPN profile. This will enable the user to access on-premises resources.

In the case of AzureAD-only joined devices (not hybrid joined devices), if the user certificate issued by the on-premises CA has the user UPN from AzureAD in Subject and SAN (Subject Alternative Name), the VPN profile must be modified to ensure that the client does not cache the credentials used for VPN authentication. To do this, after deploying the VPN profile to the client, modify the Rasphone.pbk on the client by changing the entry UseRasCredentials from 1 (default) to 0 (zero).

Gary

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-09*

Hello @Thies  ,

Thank you for posting here.

Please troubleshoot as below:

1.Based on "The user name could not be found", did you use the domain user name? If so, check if the user name is indeed in the AD domain.

2.Check for the same domain-joined machine (upgraded Windows 10 20h2), if you change a domain user name in Windows Explorer, did you receive the same error message.

3.For Windows 10 1903 (everything should be working fine on Windows 10 1903), check if all users receive the same error message in Windows Explorer.

From three point above, please check if the issue occurs on all upgraded Windows 10 20h2 machines or only one machine or several machines.

Please check if one user or all users will receive the same error message on all upgraded Windows 10 20h2 machines or only one machine.

4.Please check if DNS is working fine on the upgraded Windows 10 20h2 machine.

After you confirm the issue scope, you can try to capture the netnom trace based on working case and non-working case.

I assume users on Windows 10 1903 is working fine, but users on the upgraded Windows 10 20h2 is not working fine.

On Windows 10 1903(working)

1.Choose the version for your system to download, install it as typical:  

https://www.microsoft.com/en-US/download/details.aspx?id=4865  

2.Run Network Monitor as administrator.  

3.In the bottom left-hand, choose the NIC or NICs you want to capture.  

4.Then click New Capture and Start button,.  

5.Run command: run command ipconfig /flushdns to clean DNS cache, run command nbtstat -RR to clean NETBIOS cache, and run command klist purge to clear credential cache.

6.In Windows Explorer, reproduce the issue (working case).  

Then go back to network monitor tool, click "Stop" on the Capture menu, and click "File"->"Save as" to save the captured files (Tip: Please remember the IP address, computer name of the source machine and target machine, the time that the issue reoccurs).

On the upgraded Windows 10 20h2(non-working)

1.Choose the version for your system to download, install it as typical:  

https://www.microsoft.com/en-US/download/details.aspx?id=4865  

2.Run Network Monitor as administrator.  

3.In the bottom left-hand, choose the NIC or NICs you want to capture.  

4.Then click New Capture and Start button,.  

5.Run command: run command ipconfig /flushdns to clean DNS cache, run command nbtstat -RR to clean NETBIOS cache, and run command klist purge to clear credential cache.

6.In Windows Explorer, reproduce the issue (non-working case).  

Then go back to network monitor tool, click "Stop" on the Capture menu, and click "File"->"Save as" to save the captured files (Tip: Please remember the IP address, computer name of the source machine and target machine, the time that the issue reoccurs).

Please Compare the working capture and non-working capture ( view the log at the point in time when the problem occurred ).

Tip: As security or privacy information may be involved, the forum does not collect any logs and network packets. It is recommended that you or your team try to compare and analyze the network packets to see if you can find any clues.

Thank you for your understanding and support.

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
