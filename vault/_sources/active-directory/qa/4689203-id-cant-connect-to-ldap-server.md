---
title: "$ID can't connect to LDAP server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4689203/id-cant-connect-to-ldap-server
question_id: 4689203
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 4
qa_tags: []
---
# $ID can't connect to LDAP server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4689203/id-cant-connect-to-ldap-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows 11 with latest updates and outlook365 latest updates.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-31*

Dear DonLeslie

Thanks for your post in Microsoft Community.

According to the error message you provided, $ID Unable to connect to LDAP server usually indicates that Outlook or other mail clients encountered a problem when trying to connect to a server based on LDAP (Lightweight Directory Access Protocol). LDAP servers are often used for directory services, such as Active Directory, to authenticate users or look up contact information.

To further understand your question, I need to confirm some details from you.

Could you please tell me which email account you are using(Gmail/Outlook)?

Are you using a work or school account, a Microsoft 365 Enterprise or Exchange account, or a personal account?

What version of Outlook do you currently have installed?

What version of Outlook do I have? - Microsoft Support

What operation did you perform when the error occurred?

You can perform the following solutions to troubleshoot:

-  Check server status: Make sure the LDAP server is running and accessible. If you are not the server administrator, contact your IT support team to check the server status.

-  Test network connectivity: Try to ping the LDAP server from the client device to check if there is a network connectivity issue. If the network is down, contact your network administrator.

-  Check LDAP configuration: Make sure the server address, port number (default LDAP is 389, LDAPS is 636), and base DN are configured correctly.

-  Check if the client is correctly configured with the bind credentials (username and password) for LDAP.

-  Verify credentials: Confirm that the credentials used have permission to access the LDAP server.     Here are the steps on how to clear credentials in the Credential Manager in Windows operating system:

-  Steps: Clear credentials in the Credential Manager     Open the Credential Manager:     Type Credential Manager or Credential Manager in the search box on the Windows taskbar, and then select the Credential Manager application to open.     Select the credential type:     There are two types of credentials in the Credential Manager: Windows Credentials and Web Credentials. You need to select the appropriate type of credentials to clear. For example, if you want to delete credentials associated with a website, select Web Credentials; if you want to delete local Windows or application credentials, select Windows Credentials.     Find the credentials you need to delete:     Browse the list and find the credential entry you want to delete. For example, the credentials for a specific website, network device, or application.     Delete the credentials:     Click the credential entry you want to delete and select "Delete".     The system will ask for confirmation, click "Yes" to confirm the deletion.     Repeat steps 3 and 4:     If there are multiple credentials to delete, repeat the above steps.     Restart the system (optional):     After deleting the credentials, it is recommended to restart the computer to ensure that the changes take effect.     After clearing the credentials in the Credential Manager, you will need to re-enter your username and password when you visit the relevant website or application again.

-  Check firewall settings: Make sure the firewall between the client and the LDAP server allows LDAP traffic (port 389 or 636).

-  Update certificates: If LDAP uses LDAPS, make sure both the server and the client have the SSL/TLS certificates properly installed.

These steps will help you troubleshoot and resolve the "Cannot connect to LDAP server" issue. We look forward to hearing from you, as your response will determine our direction.

Best Regards

Clara G| Microsoft Community Support Specialist
