---
title: "Errors while reading policies from this GPO, not all policies are displayed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1515932/errors-while-reading-policies-from-this-gpo-not-al
question_id: 1515932
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-cpp", "windows-business-windows-server-user-experience-powershell"]
---
# Errors while reading policies from this GPO, not all policies are displayed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1515932/errors-while-reading-policies-from-this-gpo-not-al (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I am working on implementing an automatic Quality of Service (QoS) policy creator using the "New-NetQosPolicy" PowerShell command. I have a C++ script that executes this command to limit the bandwidth for specific applications, such as Firefox.

Here is the command I'm using: "New-NetQosPolicy -Name firefox.exe -AppPathNameMatchCondition "firefox.exe" -ThrottleRateActionBitsPerSecond 5MB -IPProtocolMatchCondition Both -NetworkProfile All"

Here is the script:

```
//create QoS policy
std::string command = "powershell New-NetQosPolicy -Name " + appName + " -AppPathNameMatchCondition \"" + appName + "\" -ThrottleRateActionBitsPerSecond " + std::to_string(bandwidthLimit) + "MB -IPProtocolMatchCondition Both -NetworkProfile All";
std::cout After running the command, I can see the policy in the output of the "Get-NetQosPolicy" command, and it looks to be configured properly.

Here is the output:

```
Name: firefox.exe
Owner : Group Policy(Machine)
NetworkProfile : All
Precedence : 127
AppPathName : firefox.exe
JobObject :
IPProtocol: Both
ThrottleRate : 5.243 MBits / sec
```

However, the QoS policy doesn't seem to be applied to Firefox. When I try to view the policy in the Group Policy Editor, I encounter the error:
"Errors while reading policies from this GPO, not all policies are displayed."

Though, when I manually set up the QoS myself it seems to work just fine. Any insights on why this may be happening would be greatly appreciated.  

PS: if helpful I have attached a custom view of the event log during my testing, It contains the creation of a QoS with the same command provided above. EventsForGPOError.xml  

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-01*

I ended up solving my problem by creating my own version of the command I needed, I don't know if the "New-NetQosPolicy" was not meant to do what I was using it to do, or if I misunderstood how to use it. Regardless I never really got the command itself fixed.   

Anyway here is the code I ended up creating and using.

```
void createQoS(std::string QoS_Name, std::string path, std::string ThrottleRate) {
        std::list commandList;

        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v Version /t REG_SZ /d " + "1.0");
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v \"Application Name\" /t REG_SZ /d " + path);
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v Protocol /t REG_SZ /d " + "*");
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v \"Local Port\" /t REG_SZ /d " + "*");
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v \"Local IP\" /t REG_SZ /d " + "*");
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v \"Local IP Prefix Length\" /t REG_SZ /d " + "*");
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v \"Remote Port\" /t REG_SZ /d " + "*");
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v \"Remote IP\" /t REG_SZ /d " + "*");
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v \"Remote IP Prefix Length\" /t REG_SZ /d " + "*");
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v \"DSCP Value\" /t REG_SZ /d " + "-1");
        commandList.push_back("reg add HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /v \"Throttle Rate\" /t REG_SZ /d " + ThrottleRate);
        commandList.push_back("gpupdate /force");

        for (const std::string& command : commandList) {
            std::cout  commandList;

        commandList.push_back("reg delete HKCU\\Software\\Policies\\Microsoft\\Windows\\QoS\\" + QoS_Name + " /f");
        commandList.push_back("gpupdate /force");

        for (const std::string& command : commandList) {
            std::cout It creates a QoS that throttles bandwidth usage with a QoS by adding the QoS directly to the registry. The second commands remove the QoS from the registry. Be cautious as if this remove command isn't used then when the QoS is manually removed from the registry it will still linger and have an effect for some reason.
