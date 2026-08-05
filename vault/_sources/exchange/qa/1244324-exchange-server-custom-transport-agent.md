---
title: "Exchange server Custom Transport Agent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1244324/exchange-server-custom-transport-agent
question_id: 1244324
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "developer-technologies-dotnet-other-l1", "office-exchange-office-exchange-server-development"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange server Custom Transport Agent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1244324/exchange-server-custom-transport-agent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have Created an Exchange server Custom Transport Agent Using SmtpReceiveAgentFactory, SmtpReceiveAgent class and OnEndOfData event. In my Event Handler iam just writing the mails subject to a local file. when the mail flow through my agent, in the event handler the emails were coming in the same order as it is send, that i came to know from the local file to which i append the mail subject. But when the mail received to the recipient, the first 10 to 15 emails were not received in correct order. I just used the custom agent code from https://learn.microsoft.com/en-us/exchange/client-developer/transport-agents/how-to-create-an-smtpreceiveagent-transport-agent-for-exchange-2013. The Powershell script i used to send 1000 mails is 

```
$user = ""
$pWord = ConvertTo-SecureString -String "" -AsPlainText -Force
$cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $user, $pWord
for($i=1;$i -le 1000; $i++) {
    Send-MailMessage -SmtpServer "" -From '' -To '' -Subject "Mail:$i" -Body "This is: $i" -Credential $cred
}
```

The command i used to install the agent in server is 
`Install-TransportAgent "ManageEngine - Exchange Mail Agent" -TransportAgentFactory "Microsoft.ExchangeServer.CustomAgent.MyAgent" -AssemblyPath "C:\ProgramFiles\Microsoft\ExchangeServer\V15\TransportRoles\agents\Custom\Microsoft.ExchangeServer.CustomAgent.dll" -TransportService Hub`  

To Enable it  

`Enable-TransportAgent "ManageEngine - Exchange Mail Agent" -TransportService Hub`

Even without writing to the file with transport agent installed iam getting the mails received in incorrect order for the first 10 to 15 emails, only after installing the agent. What iam missing here or Is this the behavior of Custom transport agent?

```
namespace Microsoft.ExchangeServer.CustomAgent{
   public class MyAgent : SmtpReceiveAgentFactory
   {
       public override SmtpReceiveAgent CreateAgent(SmtpServer server)
       {
           return new OwnSmtpAget();
       }
   }

   public class OwnSmtpAgent : SmtpReceiveAgent
   {   
       public OwnSmtpAgent()
       {
           this.OnEndOfData += new EndOfDataEventHandler(this.OnEndOfDataHandler);
       }
       public void OnEndOfDataHandler(ReceiveMessageEventSource source, EndOfDataEventArgs e) 
       {
            File.AppendAllText(@"C:\\TransportAgentLogs.txt", "Subject:"+ e.MailItem.Message.Subject);
       }
   }
}
```

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-04-20*

Hi Kannan, I wish I could help you but I'm an editor not a Subject Matter Expert! I'll forward this to a few people who might be able to help.
