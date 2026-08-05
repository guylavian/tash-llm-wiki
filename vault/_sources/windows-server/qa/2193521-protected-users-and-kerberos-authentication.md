---
title: "Protected Users and Kerberos Authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193521/protected-users-and-kerberos-authentication
question_id: 2193521
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-remote-desktop-terminal-services"]
---
# Protected Users and Kerberos Authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193521/protected-users-and-kerberos-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We added service accounts to protected users group and when users try to login to the server, they are getting the following error. So, I tried to ahead and create a GPO as per not allowing NTLM authentication and allowing only Kerberos authentication and denying users if NTLM is used.

  

So, I created a GPO and assigned that GPO to the server with the following settings:

Disable NTLM and Enable Kerberos

Computer Configuration \ Windows Settings\Security Settings\Local Policies\User Rights Assignment - Deny Access to this computer from the network - I added users who should not have access through NTLM.

Enabled Kerberos

Computer Configuration \ Windows Settings\Security Settings\Local Policies\Security Options\Network Security: Configure Encryption types allowed for Kerberos

DES_CBC_CRSC

DES_CBC_MD5 and so on.... I have checked everything.

We still get this error. So, I am not sure where else to look for that the users should be able to login to the Computer which has this policy applied and be able to RDP in. Any help would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-24*

Hello Enfield,

I can not see the images you uploaded.

Best regards

Bblythe Xiao

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-23*

Principal Name (SPN) and Kerberos policies:

-  Check Service Principal Name (SPN) settings:

a. Open Command Prompt on the target computer.

b. Type the command "setspn -L <computername>", where <computername> is the name of the target computer.

FindDomainForAccount: Call to DsGetDcNameWithAccountW failed with return value 0x00000525  

c. Check the output for correct SPN settings. If they are not present, use the "setspn" command to add the correct SPN settings.

-  Check Kerberos policy settings:

a. Open Local Security Policy on the target computer.

b. Go to "Local Policies" > "Security Options".

c. Check the policy settings related to Kerberos authentication, such as "Network security: LAN Manager authentication level" and "Network security: Minimum session security".

Not sure what to set here as both are not enabled

There is for servers and clients

I am not sure what to pick here also below for Network Security: Minimum session security for NTLM..........?  Should I check both options or just one option?. But, my main concern is to block NTLM and allow Kerberos and I should not get that error message about not able to login in specific hours. We are not limiting any hours to login and it is all open. So, why would I still get that message about user account restrictions.

d. If changes to the policy settings are needed, double-click on the corresponding policy and make the changes.

-  Check Kerberos logs:

a. Open Event Viewer on the target computer.

b. Go to "Windows Logs" > "Security".

c. Look for events related to Kerberos authentication.

d. Check the event details for more information about authentication failures.

I hope the above information is helpful to you.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-23*

Hello Enfield,

Thanks for your response.

Here are the steps to further check Kerberos authentication settings, such as Service Principal Name (SPN) and Kerberos policies: 

-  Check Service Principal Name (SPN) settings: 

a. Open Command Prompt on the target computer. 

b. Type the command "setspn -L <computername>", where <computername> is the name of the target computer. 

c. Check the output for correct SPN settings. If they are not present, use the "setspn" command to add the correct SPN settings. 

-  Check Kerberos policy settings: 

a. Open Local Security Policy on the target computer. 

b. Go to "Local Policies" > "Security Options". 

c. Check the policy settings related to Kerberos authentication, such as "Network security: LAN Manager authentication level" and "Network security: Minimum session security". 

d. If changes to the policy settings are needed, double-click on the corresponding policy and make the changes. 

-  Check Kerberos logs: 

a. Open Event Viewer on the target computer. 

b. Go to "Windows Logs" > "Security". 

c. Look for events related to Kerberos authentication. 

d. Check the event details for more information about authentication failures.

I hope the above information is helpful to you.

If you have any doubts, please feel free to let me know.

Best regards

Bblythe Xiao

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-22*

Hi Bblythe Xiao

Thank you for your response. I have checked all that and everything looks fine. This is what I have done on the GPO side.  I am not sure where else to go and what SPN settings or Kerberos authentication I can check l am not sure please let me know. Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-19*

Hello Enfield,

Thank you for posting in the Microsoft Community Forums.

Based on the information you provided, you have added service accounts to the protected users group, but when users try to log in to the server, they encounter an error that says "User account restrictions, such as time restrictions, prevent you from logging on." Therefore, you tried to create a GPO that disables NTLM authentication, only allows Kerberos authentication, and denies users when using NTLM. 

You have checked the encryption types for Kerberos, but the problem persists. If you have ruled out network security and encryption type issues, you can check the user account restriction settings to ensure that no restrictions are set. You can also check the Group Policy settings to ensure that no other settings are blocking user login.

Here are the specific steps:

-  Check user account restriction settings:

   a. Open the user account properties in Active Directory.

   b. Ensure that the "Account is enabled" box is checked.

   c. Ensure that the "Account is locked out" box is not checked.

   d. Ensure that the list of computers in the "Logon to" box is correct.

   e. Ensure that the time restrictions in the "Logon hours" box are correct.

-  Check Group Policy settings:

   a. Open your GPO in Group Policy Management.

   b. Ensure that the settings in "Computer Configuration" and "User Configuration" are correct.

   c. Check the settings in "Security Options" to ensure that nothing is blocking user login.

-  Check if the GPO has been applied correctly to the target computer:

   a. Open Command Prompt on the target computer.

   b. Type the command "gpresult /r" to check if the Group Policy has been successfully applied.

-  Restart the "Netlogon" service:

   a. Open the "Services" manager on the target computer.

   b. Find the "Netlogon" service and right-click on it.

   c. Select the "Restart" option to restart the service.

If the issue still persists, you may need to further check Kerberos authentication settings, such as SPN (Service Principal Name) and Kerberos policies. If you need further assistance, please consult with your network administrator or IT support personnel.

I hope the above information is helpful to you.

If you have any doubts, please feel free to let me know.

Best regards

Bblythe Xiao
