---
title: "Exchange Online Powershell - JSON Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1159724/exchange-online-powershell-json-error
question_id: 1159724
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online Powershell - JSON Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1159724/exchange-online-powershell-json-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I'm currently attempting to extract Auditlog records via Powershell, however I'm regularly getting errors in relation to a JSON conversion error. I am using a slightly modified version of this script. The small changes relate to date periods, and an addition of a User variable. I'm currently running EXO v3.0.0 too. The error found in the Powershell window along with the error within the cmdlet log can be found below.

Powershell window error

```
ConvertFrom-Json : Invalid JSON primitive: .
At C:\Users\...\AppData\Local\Temp\tmpEXO_0q1mvkwr.0ub\tmpEXO_0q1mvkwr.0ub.psm1:576 char:35
+ ... etailsToPSObject = ConvertFrom-Json $ErrorObject.ErrorDetails.Message
+                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [ConvertFrom-Json], ArgumentException
    + FullyQualifiedErrorId : System.ArgumentException,Microsoft.PowerShell.Commands.ConvertFromJsonCommand
```

cmdlet Error Log message

```
Invalid JSON primitive: .-   at System.Web.Script.Serialization.JavaScriptObjectDeserializer.DeserializePrimitiveObject()	   at System.Web.Script.Serialization.JavaScriptObjectDeserializer.DeserializeInternal(Int32 depth)	   at System.Web.Script.Serialization.JavaScriptObjectDeserializer.BasicDeserialize(String input  Int32 depthLimit  JavaScriptSerializer serializer)	   at System.Web.Script.Serialization.JavaScriptSerializer.Deserialize(JavaScriptSerializer serializer  String input  Type type  Int32 depthLimit)	   at Microsoft.PowerShell.Commands.JsonObject.ConvertFromJson(String input  ErrorRecord& error)	   at Microsoft.PowerShell.Commands.ConvertFromJsonCommand.ConvertFromJsonHelper(String input)	   at System.Management.Automation.CommandProcessorBase.Complete();
```

I'm assuming the error relates to the EXO module itself, but I'm unsure.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-12*

Hi @MS ,

How did you modify the parameters? Is there a double quote enclosing the values?

In my tests, the script can be run successfully, you can refer to the following:

(Note: The red box is the modification section.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
