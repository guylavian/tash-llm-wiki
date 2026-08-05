---
title: "Lockdown EAC from external access Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1162843/lockdown-eac-from-external-access-exchange-2019
question_id: 1162843
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Lockdown EAC from external access Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1162843/lockdown-eac-from-external-access-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a on premise exchange server 2019.  I need to block all external network access to EAC.

I have created the access control rule to Deny Access:

New-ClientAccessRule -Name "Allow ECP only for loopback" -Action DenyAccess -AnyOfProtocols ExchangeAdminCenter -ExceptAnyOfClientIPAddress 127.0.0.1 -Priority 2

Issue is there appears to be a redirect from OWA that is still getting through.

Any advise would be appreciated

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-01-23*

Hi @Will Weston  ,

Please follow the steps below to block external network access to EAC and see if it effectively blocks redirection from OWA：

-  Select the ECP in the Default Web Site in IIS Manager

-  Double-click IP Address and Domain Restrictions.

- 

-  Select the “Add Allow Entry” and Add IP or Range then click Ok.

-  Click on “Edit Feature Settings”, in “Access for Unspecified clients” Select Deny and you could select the “Deny Action Type”.

- 

-  Please run the IISreset in CMD start as administrator to reset the IIS.

（Kindly note :To set up the Restrict external network access EAC in IIS, first install the IP and Domain Restriction role in the server management.）

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-23*

`New-ClientAccessRule -Name “Block-ECP Outside ORG” -Action DenyAccess -AnyOfProtocols ExchangeAdminCenter -ExceptAnyOfClientIPAddressesOrRanges 10.190.65.1/24 -Priority 1`

The command will create a rule which allows access for connections ONLY from IP addresses which belongs to 10.190.65.1–10.190.65.254 (Class C).

You can configure any combination of IP addresses:

-  A Single IP address (10.190.65.34)

-  IP address range (10.190.65.1–10.190.65.50)

-  Classless Inter-Domain Routing (CIDR) IP (10.190.65.1/24)

In order to view the full details of the rule you have just created, run the next command:

`Get-ClientAccessRule “Block-ECP Outside ORG” | fl`

Check this detailed article for more insight - https://tkolber.medium.com/blocking-ecp-remote-powershell-access-in-exchange-2019-2d0f71e5820d

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-20*

To block all external network access to Exchange Admin Center (EAC) in Exchange Server 2019 using PowerShell, you can use the `New-WebServicesVirtualDirectory` cmdlet to create a new virtual directory for EAC and configure it to only listen on the internal network interface. Here is an example of how to do this:

```
Copy code
# Connect to Exchange Server
$session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://your-exchange-server-fqdn/PowerShell/
Import-PSSession $session

# Create a new virtual directory for EAC
$EACVD = New-WebServicesVirtualDirectory -Name "EAC" -InternalUrl "https://your-exchange-server-fqdn/EAC" -BasicAuthentication $true

# Configure the virtual directory to only listen on the internal network interface
Set-WebServicesVirtualDirectory -Identity $EACVD.Identity -InternalUrl $EACVD.InternalUrl -InternalAuthenticationMethods Basic

# Remove external access to EAC
Remove-WebServicesVirtualDirectory -Identity "EAC" -Confirm:$false
```
