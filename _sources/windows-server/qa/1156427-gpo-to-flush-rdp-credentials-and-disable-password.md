---
title: "gpo to flush rdp credentials and disable password saving"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1156427/gpo-to-flush-rdp-credentials-and-disable-password
question_id: 1156427
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# gpo to flush rdp credentials and disable password saving

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1156427/gpo-to-flush-rdp-credentials-and-disable-password (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Users are saving RDP credentials in their RDP mstsc window. How to remove the saved credentials. I know there is a option to remove REMEMBER ME option. But that is not removing saved credentials.    

Also i created a test machine to test this with test AD    

If i save by calling remotely using IP and save password next time it ask me password giving an error       

“Your system administrator does not allow the user of saved credentials to log on to the remote computer XXX because its identity is not fully verified. Please enter new credentials”.    

then i have to save RDP details in generic credentials in credential manager using TERMSRV     

My aim is to flush saved credentials for RDP and disable the remember me option( this solution i got)**

## Answer (community) — community member

*upvotes: 1 · updated: 2023-01-10*

Hello, 

To delete the credentials, the best option is to access Credential Manager and from there under the Windows Credentials section, tap Windows Credentials, click TERMSRV and click Remove link.

Also, for doing this remotely, you can create a TXT file with computernames (NetBIOS name should be sufficient) and use an automated script to delete the credential store:

ForEach($computer in (Get-Content c:\PClist.txt ))
{ psexec \$computer -s winrm.cmd quickconfig -q
Enter-PSSession -ComputerName $computer
Get-childitem -path “C:\Windows\SoftwareDistribution” -Recurse -force | Remove-item -Recurse
}

To prevent the password saving: you need to Enable the next GPO: 
run gpedit.msc>User Configuration.>Administrative Templates.>Windows Components.>Remote Desktop Services.>Remote Desktop Connection Client.>Setting: Do not allow passwords to be saved

--If the reply is helpful, please Upvote and Accept as answer--
