---
title: "I am getting an error upgrading Azure AD Connect to the Entra AD Connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191212/i-am-getting-an-error-upgrading-azure-ad-connect-t
question_id: 2191212
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 21
qa_tags: ["windows-business-windows-server-windows-cloud-windows-cloud-other"]
---
# I am getting an error upgrading Azure AD Connect to the Entra AD Connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191212/i-am-getting-an-error-upgrading-azure-ad-connect-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

unable to validate credentials due to an unexpected error. restart azure ad connect with the /interactiveauth option to further diagnose this issue. (extenedmessage: an error occorred while sending the request. | The underlying connection was closed: An existing connection was forcibly closed by the remote host.  webException: the underlying connection was closed: an unexpected error occured on a send. STS endpoint HTTPS://Login.micosoftonline.com/ourdomain.

## Answer (community) — community member

*upvotes: 23 · updated: 2024-08-16*

I too got it resolved by enabling TLS 1.2.

I just want to add where the instructions are, that I followed (as it took some time to find those):

https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-tls-enforcement

## Answer (community) — community member

*upvotes: 11 · updated: 2024-08-14*

Enabling TLS 1.2 resolved the issue.

## Answer (community) — community member

*upvotes: 1 · updated: 2024-08-14*

I've been having the same issue for over a week. I also launch the installer using the /interactiveauth switch.  

Checking the trace log files, I see this:   

[09:44:43.721] [  9] [ERROR] AzureConfigurationFromPrincipalName: Unable to determine the Azure instance for UPN (myemail@mydomain.com). Defaulting to the WorldWide instance which may result in authentication failures.  Resolution Method [DomainSuffixMapping]: Unknown MOERA domain suffix. Defaulting to WorldWide which may result in subsequent authentication failures.  Resolution Method [AzureInstanceDiscovery]: Unexpected failure.  An error occurred while sending the request..  Continuing resolution.   

[09:44:43.733] [  9] [INFO ] ResolveAzureInstance [Default]: authority=HTTPS://LOGIN.MICROSOFTONLINE.COM/MYDOMAIN.COM,  Resolution Method [DomainSuffixMapping]: Unknown MOERA domain suffix. Defaulting to WorldWide which may result in subsequent authentication failures.   Resolution Method [AzureInstanceDiscovery]: Unexpected failure.  An error occurred while sending the request..  Continuing resolution.   

[09:44:43.770] [  9] [INFO ] Authenticate-MSAL [Acquiring token]: STS endpoint (HTTPS://LOGIN.MICROSOFTONLINE.COM/MYDOMAIN.COM), scope (https://graph.windows.net/user\_impersonation), userName (myemail@mydomain.com).   

[09:44:43.771] [  9] [INFO ] MSAL.ClearTokenCache [Clearing Token Cache]   

[09:44:43.845] [  9] [INFO ] MSAL: False MSAL 4.36.0.0 MSAL.Desktop 4.8 or later Windows Server 2016 Datacenter [08/14 14:44:43.84 - 11********-7**c-4**3-8**4-e***********25] [Region discovery] Azure region was not configured or could not be discovered. Not using a regional authority.   

[09:44:43.854] [  9] [INFO ] MSAL: False MSAL 4.36.0.0 MSAL.Desktop 4.8 or later Windows Server 2016 Datacenter [08/14 14:44:43.85] Found 0 cache accounts and 0 broker accounts   

[09:44:43.855] [  9] [INFO ] MSAL: False MSAL 4.36.0.0 MSAL.Desktop 4.8 or later Windows Server 2016 Datacenter [08/14 14:44:43.85] Returning 0 accounts   

[09:44:43.855] [  9] [INFO ] Authenticate-MSAL [InteractionMode.Desktop]: user interaction required to complete authentication. [09:44:43.860] [  9] [INFO ] Authenticate-MSAL: acquiring token using interactive authentication.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-06*

Hi Derek Kelsheimer,

Thank you for posting in the Microsoft Community Forums.

Here are some possible solution steps and checkpoints to help you diagnose and resolve the issue:  

-  Check network connectivity Ensure that your server has access to Azure's STS (Security Token Service) endpoint https://login.microsoftonline.com This includes checking your network firewall, proxy settings, and any security software that may be blocking outbound HTTPS connections.  

-  Verify credentials Ensure that you are using the correct Azure administrator credentials and have sufficient permissions to perform the upgrade operation. Try to re-authenticate using another Azure administrator account with the appropriate permissions.

-  Use the /interactiveauth option As suggested by the error message, you can try restarting the Azure AD Connect (or Entra AD Connect) wizard using the /interactiveauth option. This option allows you to authenticate through the graphical user interface (GUI) and may help diagnose the problem. 

-  Check the log files Check the %ProgramData%\AADConnect\trace-*.log files, which typically contain detailed information about errors that occurred during the upgrade process. Look for error messages related to credential validation, network connectivity, or STS endpoints.

-  Updating and configuring the server Make sure your server has all the latest security updates and patches installed. Check that the server's date and time settings are correct, as incorrect date and time settings can affect the authentication of SSL/TLS connections.

-  Check the configuration of Azure AD Connect/Entra AD Connect Ensure that the configuration of Azure AD Connect or Entra AD Connect is correct and does not have any known compatibility issues before upgrading. If you have previously customized the configuration, make sure that these customizations were properly handled during the upgrade.

Best regards

Neuvi Jiang
