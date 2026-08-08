---
title: "Microsoft Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2047195/microsoft-exchange
question_id: 2047195
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Microsoft Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2047195/microsoft-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Microsoft Team,

We are facing some issues regarding connecting our work email with our Microsoft Exchange account.

How can we properly connect it? Our work domain is ******@profmaris.com . We already have a Microsoft Business Premium account which has full access to Microsoft Exchange. For some reason, this window appears when trying to connect to Microsoft Exchange. Please see the screenshot down below. I will be waiting for your feedback. Appreciate it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-23*

Hi Nojus,

I'm sorry to hear that you're experiencing this issue. The error message you're seeing—"The name on the security certificate is invalid or does not match the name of the site"—typically indicates a problem with the Autodiscover service for your domain. Are you trying to connect to an on-premises Exchange Server or to Exchange Online? If you're trying to access Exchange Online, as I understand it, you can go through some steps to resolve this:

1. Verify Your Autodiscover DNS Records

-  CNAME Record for Autodiscover:

-  Ensure that there's a CNAME record for autodiscover.profmaris.com pointing to autodiscover.outlook.com.

-  This tells Outlook where to find the Autodiscover service for Exchange Online.

-  How to Check:

-  Log in to your domain registrar or DNS hosting provider's management portal.    Look for a CNAME record with the host name autodiscover.    The record should look like:  

    Host: autodiscover    Type: CNAME    Points to: autodiscover.outlook.com

2. Remove Any Conflicting Autodiscover Records

-  If you previously had an on-premises Exchange server or other email services, there might be old DNS records causing conflicts.

-  Delete any Autodiscover A or CNAME records that point to old servers or IP addresses not associated with Microsoft.

3. Test Autodiscover Using Microsoft's Tool

-  Use the Microsoft Remote Connectivity Analyzer to test your Autodiscover configuration.

-  Steps:

-  Go to Microsoft Remote Connectivity Analyzer.    Select "Microsoft 365" > "Outlook Autodiscover".    Enter your email address (******@profmaris.com) and password.    Review the results for any errors or misconfigurations.

4. Clear Outlook Credentials and Autodiscover Cache

-  Sometimes, Outlook caches old Autodiscover settings.

-  Steps:

-  Close Outlook.

-  Go to Control Panel > Credential Manager.      Remove any stored credentials related to your email account.      Delete the Autodiscover cache:      Navigate to `%USERPROFILE%\AppData\Local\Microsoft\Outlook`.      Delete the Autodiscover.xml files.      Restart Outlook and try setting up your account again.

5. Use an SRV Record as an Alternative

-  If the CNAME method isn't working, you can set up an SRV record for Autodiscover.

-  SRV Record Details:  Service: _autodiscover  Protocol: _tcp  Port Number: 443  Host: autodiscover.outlook.com

This method tells email clients to look at autodiscover.outlook.com for Autodiscover services.

6. Ensure There's No Local Redirection

-  Check your local hosts file to ensure there's no entry redirecting Autodiscover queries.

-  Location: C:\Windows\System32\drivers\etc\hosts

-  Open the file with Notepad and look for any lines containing autodiscover.profmaris.com. If found, consider removing them.

7. Contact Your Domain Registrar or DNS Hosting Provider

-  If you're unsure about modifying DNS records, reach out to your domain registrar's support team.

-  They can assist you in verifying and updating your DNS settings to ensure they point correctly to Microsoft Exchange Online.

If after trying these steps you're still experiencing problems, please let me know, and we can explore further options.

Best regards,  

T.
