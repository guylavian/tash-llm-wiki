---
title: "Errors while reading policies from this GPO, not all policies are displayed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3748129/errors-while-reading-policies-from-this-gpo-not-al
question_id: 3748129
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Errors while reading policies from this GPO, not all policies are displayed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3748129/errors-while-reading-policies-from-this-gpo-not-al (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am working on implementing an automatic Quality of Service (QoS) policy creator using the "New-NetQosPolicy" PowerShell command. I have a C++ script that executes this command to limit the bandwidth for specific applications, such as Firefox.

Here is the command I'm using: "New-NetQosPolicy -Name firefox.exe -AppPathNameMatchCondition "firefox.exe" -ThrottleRateActionBitsPerSecond 5MB -IPProtocolMatchCondition Both -NetworkProfile All"

Here is the script:   

```
//create QoS policy

        std::string command = "powershell New-NetQosPolicy -Name " + appName + "  AppPathNameMatchCondition \"" + appName + "\" \ ThrottleRateActionBitsPerSecond " + std::to\_string(bandwidthLimit) + "MB -IPProtocolMatchCondition Both -NetworkProfile All";

        std::cout << command << std::endl;

        system(command.c\_str());

        qosNames.push\_back(appName);

        std::cout << "Bandwidth limit applied for " << appName << ": " << bandwidthLimit << " Kbps" << std::endl;
```

After running the command, I can see the policy in the output of the "Get-NetQosPolicy" command, and it looks to be configured properly.  

Here is the output:

```
Name           : firefox.exe  
      Owner          : Group Policy (Machine)  
      NetworkProfile : All  
      Precedence     : 127  
      AppPathName    : firefox.exe  
      JobObject      :

      IPProtocol     : Both  
      ThrottleRate   : 5.243 MBits/sec
```

However, the QoS policy doesn't seem to be applied to Firefox. When I try to view the policy in the Group Policy Editor, I encounter the error:

"Errors while reading policies from this GPO, not all policies are displayed."

Though, when I manually set up the QoS myself it seems to work just fine. Any insights on why this may be happening would be greatly appreciated.  

PS: if helpful I have a custom view of the event log during my testing, It contains the creation of a QoS with the same command provided above. Though I do not know how I would attach it to this post 😅  

Thank you.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2024-01-28*

My name is Jonathan Deives. I'm an Independent Advisor and I'll be glad to help you today.

This forum is for casual users, as your question is more complex, please use the Microsoft Q&A Forum (The System Administrators and IT Pro Forum) where they can help you better.

https://learn.microsoft.com/en-us/answers/quest...
