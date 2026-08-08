---
title: "KERBEROS refresh clients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/63629/kerberos-refresh-clients
question_id: 63629
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# KERBEROS refresh clients

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/63629/kerberos-refresh-clients (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning, in our infrastructure have all clients windows 10, and 2 DC 2019 Server (FFL 2012 R2), when change (add or remove) users from groups, all client, need to reset manually kerberos token with cmd (klist purge –li 0x3e7). It's the only metod. reboot and disconnect do not work  

Can you help me?   

Regards

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-11*

Hello MatteoDiFrancesco-1737,    

Thank you for posting here.    

1. Usually, if we reboot the machine, all the credential caches (including user credential cache and computer cache) are refreshed.    

2. And from the article, we can see:    

How the Kerberos Version 5 Authentication Protocol Works    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc772815(v=ws.10)?redirectedfrom=MSDN    

Credentials Cache    

On computers running Windows 2000, Windows XP, or Windows Server 2003, tickets and keys obtained from the KDC are stored in a credentials cache, an area of volatile memory protected by the LSA. The credentials cache is never paged to disk. All objects stored there are destroyed when a security principal logs off or when the system is shut down.    

The credentials cache is managed by the Kerberos SSP, which runs in the LSA's security context. Whenever tickets and keys need to be obtained or renewed, the LSA calls the Kerberos SSP to accomplish the task.    

After credentials reach the workstation, the Windows Server 2003 access token creation process is the same as that of Windows NT versions. The LSA on the workstation receives the user's service ticket, decrypts the service ticket with the system key stored in its credentials cache, and then extracts the authorization data. The privilege attribute certificate (PAC) is taken from the service ticket and used to create the user's access token. The LSA then queries the local SAM database to discover whether the user is a member of any security groups local to the computer, and whether memberships in those groups grant the user any special rights on the local computer. It adds any SIDs returned by this query to the list taken from the ticket's authorization data. The entire list is then used to build an access token, and a handle to the access token is returned to Winlogon, along with an identifier for the user's logon session and confirmation that the logon information was valid.    

Winlogon creates a window station and several desktop objects for the user, attaches the user's access token, and starts the shell process the user will use to interact with the computer. The user's access token is subsequently inherited by any application process that the user starts during the logon session.    

When the user logs off, the credentials cache is flushed and all service tickets—as well as all session keys—are destroyed.    

3. We can check if AD replication is working fine between two DCs, or maybe there is replication delay between two DCs, I mean when we change (add or remove) users from groups on one DC, after a while (such as several seconds) the change does not occurs on the other DC.    

If it is not the situation above, would you please tell us how we check reboot or sign out and sign in do not work?    

Thank you for your time and efforts.    

Best Regards,    

Daisy Zhou

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-10*

Hi,

For you information , they are two type of Kerberos ticket cache :

-    the User ticket which contain the list of groups of this user. When you remove or add a user from groups , you should ask user to logoff then to logon to purge all cached ticket for this user , or he can just run the following command klist purge. To display the list all cached user kerberos ticket you can run this command klist purge.

-    the Computer kerberos ticket which contain the list of groups of this computer where the user are connected. When you remove or add a computer account from groups , you should ask user to restart his computer to purge all cached ticket for this computer , or he can just run the following command klist purge –li 0x3e7    It is important to purge the cached tickets in order recent modifications will be taken into account .
