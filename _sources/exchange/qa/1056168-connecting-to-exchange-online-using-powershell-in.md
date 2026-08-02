---
title: "Connecting to Exchange Online using PowerShell in VB.NET - changes since Basic Authentication retired"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1056168/connecting-to-exchange-online-using-powershell-in
question_id: 1056168
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-vb", "office-exchange-office-exchange-server-development", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Connecting to Exchange Online using PowerShell in VB.NET - changes since Basic Authentication retired

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1056168/connecting-to-exchange-online-using-powershell-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

Previously used code such as below to connect and query Exchange Online - since basic authentication retirement this now can't be used - can someone please give me some pointers on how I can modify this to work with the new modern authentication requirements?    

Thank you    

```
Dim connectionUri As String = "https://outlook.office365.com/powershell-liveid/"  
  
        Dim credential As New PSCredential(Username_String, Password_SecureString)  
  
        Dim connectionInfo As New WSManConnectionInfo(New Uri(connectionUri), "http://schemas.microsoft.com/powershell/Microsoft.Exchange", credential)  
        connectionInfo.AuthenticationMechanism = AuthenticationMechanism.Basic  
        connectionInfo.MaximumConnectionRedirectionCount = 2  
  
        Dim results As Collection(Of PSObject)  
  
        Try  
            Using runspace As Runspace = RunspaceFactory.CreateRunspace(connectionInfo)  
                Using powershell As PowerShell = PowerShell.Create()  
                    runspace.Open()  
                    powershell.Runspace = runspace  
                    powershell.AddCommand("Get-Mailbox").AddParameter("Identity", MailboxIdentityToCheck)   
                    results = powershell.Invoke()  
                End Using  
  
            End Using  
        Catch ex As Remoting.PSRemotingTransportException  
            Append_tb(TextBox1, "Credentials stored are invalid" & vbCrLf & vbCrLf & "Click Change Credentials, enter correct credentials and then click Test Connection again")  
            Exit Sub  
        Catch ex As Exception  
            Console.WriteLine(ex.Message)  
        End Try
```

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-21*

@Darren Rose      

Before that you could follow this blog to enable basic for remote PowerShell temporarily (not sure whether it could work for VB):    

    

Due to connect to Exchange online with VB related to the development, I will help you add the “office-exchange-server-dev” tag to this thread.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-20*

Found useful C# sample here which I converted to VB and got working both to connect using method suggested by michev and to connect by supplying username and password - so have two methods now working using modern authentication and my app is up and running again.    

https://stackoverflow.com/questions/71784345/connecting-to-exchange-online-with-a-certificate-and-c-sharp

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-20*

The best thing to do here is switch to using certificate-based auth as detailed in this article: https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2?view=exchange-ps
