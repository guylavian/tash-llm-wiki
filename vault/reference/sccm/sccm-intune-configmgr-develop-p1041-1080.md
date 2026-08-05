---
title: "Configuration Manager SDK documentation — pages 1041-1080"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1041-1080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1041-1080
family: sccm
documentKind: "doc"
abstract: "How to Add a Condition to an Operating System Deployment Task Sequence Step Article • 10/04/2022 Conditions can be added to an operating system deployment step (action and group), in Configuration Manager, by creating a SMS_TaskSequence_Condition class instance and then associat"
---

# Configuration Manager SDK documentation — pages 1041-1080

<!-- p.1041 -->

How to Add a Condition to an
Operating System Deployment Task
Sequence Step
Article • 10/04/2022

Conditions can be added to an operating system deployment step (action and group), in
Configuration Manager, by creating a SMS_TaskSequence_Condition class instance and
then associating it with the step. If the condition operands are all met, then the step is
processed; otherwise it is not. The condition can have one or more operands that are
instances of SMS_TaskSequence_Condition derived classes. You specify operators for the
operands with instances of SMS_TaskSequence_ConditionOperator.

To add a condition to a step
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Obtain a task sequence step object. This can be an SMS_TaskSequence_Group
      object for a group, or a SMS_TaskSequenceAction derived class object for an
      action, for more information, see How to Add an Operating System Deployment
      Task Sequence Action.

   3. Create a new condition by creating an instance of SMS_TaskSequence_Condition .

   4. Create an expression for the condition by creating an instance of an
      SMS_TaskSequence_ConditionExpression derived class. For example,
      SMS_TaskSequence_RegistryConditionExpression.

   5. Populate the expression properties.

   6. Add the expression to the condition Operands property.

   7. Add the condition to the task sequence step class Condition property.

Example
The following example method adds a condition to a supplied step that determines if
the HKEY_LOCAL_MACHINE\MICROSOFT registry key exists. The
SMS_TaskSequenc_RegistryCondition Expression is used to specify the condition.

<!-- p.1042 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddRegistryCondition (connection, taskSequenceStep)

        Dim condition
        Dim registryExpression
        Dim operands

      ' Get or create the condition.
      if IsNull ( taskSequenceStep.Condition) Then
         Set condition =
  connection.Get("SMS_TaskSequence_Condition").SpawnInstance_
      Else
          Set condition = taskSequenceStep.Condition
      End If

      ' Populate the condition.
      Set
  registryExpression=connection.Get("SMS_TaskSequence_RegistryConditionExpress
  ion").SpawnInstance_
      registryExpression.KeyPath="HKEY_LOCAL_MACHINE\MICROSOFT"
      registryExpression.Operator="exists"
      registryExpression.Type="REG_SZ"
      registryExpression.Data=Null

        ' Add the condition.
        operands=Array(registryExpression)
        condition.Operands=operands
        taskSequenceStep.Condition=condition

  End Sub

  c#

  public void AddRegistryCondition(
      WqlConnectionManager connection,
      IResultObject taskSequenceStep)
  {
      try
      {
          IResultObject condition;

          if (taskSequenceStep["Condition"].ObjectValue == null)
          {
               // Create a new condition.
               condition =
  connection.CreateEmbeddedObjectInstance("SMS_TaskSequence_Condition");
          }
          else

<!-- p.1043 -->

              {   // Get the existing condition.
                  condition = taskSequenceStep.GetSingleItem("Condition");
              }

          // Create and populate the expression.
          IResultObject registryExpression =
  connection.CreateEmbeddedObjectInstance("SMS_TaskSequence_RegistryConditionE
  xpression");

          registryExpression["KeyPath"].StringValue =
  @"HKEY_LOCAL_MACHINE\MICROSOFT";
          registryExpression["Operator"].StringValue = "exists";
          registryExpression["Type"].StringValue = "REG_SZ";
          registryExpression["Data"].StringValue = null;

              // Get the operands and add the expression.
              List<IResultObject> operands = condition.GetArrayItems("Operands");
              operands.Add(registryExpression);

              // Add the expresssion to the list of operands.
              condition.SetArrayItems("Operands", operands);

              // Add the condition to the sequence.
              taskSequenceStep.SetSingleItem("Condition", condition);
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to create Task Sequence: " + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter           Type                        Description

 connection          - Managed:                  A valid connection to the SMS Provider.
                     WqlConnectionManager
                     - VBScript: SWbemServices

 taskSequenceStep    - Managed: IResultObject    A valid task sequence step
                     - VBScript: SWbemObject     (SMS_TaskSequenceStep).

Compiling the Code
The C# example has the following compilation requirements:

<!-- p.1044 -->

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Add an Operating System Deployment Task Sequence Action
How to Connect to an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
Task sequence overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1045 -->

How to Enumerate the Steps in an
Operating System Deployment Task
Sequence
Article • 10/04/2022

You enumerate an operating system deployment task sequence, in Configuration
Manager, by using a recursive method to scan through the task sequence steps and
groups.

To enumerate the steps in a task sequence
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Obtain a valid task sequence SMS_TaskSequence object. For more information, see
        How to Create an Operating System Deployment Task Sequence

   3. Enumerate through the steps to display any action (SMS_TaskSequence_Action)
        names. Use recursion to access any groups (SMS_TaskSequence_Group) that are
        found and display their actions.

Example
The following example displays the actions and groups within a task sequence.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub RecurseTaskSequenceSteps(taskSequence, indent)

         Dim osdStep
         Dim i

         ' Indent each new group.
         for each osdStep in taskSequence.Steps

              for i=0 to indent
                   WScript.StdOut.Write " "
              next

              If osdStep.SystemProperties_("__CLASS")="SMS_TaskSequence_Group"

<!-- p.1046 -->

Then
              wscript.StdOut.Write "Group: "
          End If

          WScript.Echo osdStep.Name

          ' Recurse into each group found.
          If osdStep.SystemProperties_("__CLASS")="SMS_TaskSequence_Group"
Then
            If IsNull(osdStep.Steps) Then
                Wscript.Echo "No steps"
            Else
                Call RecurseTaskSequenceSteps (osdStep, indent+3)
            End If
        End If
     Next
End Sub

c#

public void RecurseTaskSequenceSteps(
    IResultObject taskSequence,
    int indent)
{
    try
    {
        // The array of SMS_TaskSequence_Steps.
        List<IResultObject> steps = taskSequence.GetArrayItems("Steps");

          foreach (IResultObject ro in steps)
          {
              for (int i = 0; i < indent; i++)
              {
                  Console.Write(" ");
              }

              if (ro["__CLASS"].StringValue == "SMS_TaskSequence_Group")
              {
                  Console.Write("Group: ");
              }

              Console.WriteLine(ro["Name"].StringValue);

              // Child groups that are found. Use recursion to view them.
              if (ro["__CLASS"].StringValue == "SMS_TaskSequence_Group")
              {
                  this.RecurseTaskSequenceSteps(ro, indent + 3);
              }
           }
       }
       catch (SmsException e)
       {
           Console.WriteLine("Failed To enumerate task sequence items: " +

<!-- p.1047 -->

  e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter      Type                  Description

 taskSequence   - Managed:            A valid task sequence ( SMS_TaskSequence ). The group is
                IResultObject         added to this task sequence.
                - VBScript:
                SWbemObject

 indent         - Managed: Integer    Indent is used to space console output for child groups.
                - VBScript: Integer

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

<!-- p.1048 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Add an Operating System Deployment Task Sequence Action
How to Connect to an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
Task sequence overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1049 -->

How to Reorder an Operating System
Deployment Task Sequence
Article • 10/04/2022

In Configuration Manager, you can reorder the steps (an action or a group) in a task
sequence or group by rearranging the step sequence in the Steps property
SMS_TaskSequence_Step array.

To reorder a task sequence
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Obtain a valid task sequence (SMS_TaskSequence) or task sequence group
        (SMS_TaskSequence_Group). For more information, see How to Read a Task
        Sequence From a Task Sequence Package.

   3. Within the Steps array property, move the SMS_TaskSequence_Step to its new
        location.

   4. Update the task sequence or group.

Example
The following example shows how to move a step up or down within a task sequence or
group.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub MoveTaskSequenceStepDown(taskSequence, stepName)
     Dim index
     Dim osdStep
     Dim temp

         index=0

         ' If found, move the step down.
         for each osdStep in taskSequence.Steps
             If osdStep.Name=stepName Then
                 If index < Ubound (TaskSequence.Steps) Then

<!-- p.1050 -->

                Set temp=osdStep
                taskSequence.Steps(index)=taskSequence.Steps(index+1)
                taskSequence.Steps(index+1)=temp
                Exit For
           End If
        End If

        index=index+1
    next
End Sub

Sub MoveTaskSequenceStepUp(taskSequence, stepName)
    Dim index
    Dim osdStep
    Dim temp

     index=0

     ' If found, move the step up.
     for Each osdStep In taskSequence.Steps
         If osdStep.Name=stepName Then
             If index >1 Then
                 Set temp=osdStep
                 taskSequence.Steps(index)=taskSequence.Steps(index-1)
                 taskSequence.Steps(index-1)=temp
                 Exit For
            End If
         End If

        index=index+1

    next
End Sub

c#

public void MoveTaskSequenceStepDown(
    IResultObject taskSequence,
    string taskSequenceStepName)
{
    try
    {
        // Get the task sequence steps.
        List<IResultObject> steps = taskSequence.GetArrayItems("Steps"); //
Array of SMS_TaskSequence_Steps.

        int index = 0;

        // Scan through the steps to find the step to move down.
        foreach (IResultObject ro in steps)
        {
            if (ro["Name"].StringValue == taskSequenceStepName)
            {

<!-- p.1051 -->

                // Move the step.
                if (index < steps.Count - 1) // Not at end, so we can flip.
                {
                    steps.Insert(index + 2, steps[index]);
                    steps.Remove(steps[index]);
                    taskSequence.SetArrayItems("Steps", steps);
                    break;
                }
            }

            index++;
       }
    }
    catch (SmsException e)
    {
        Console.WriteLine("Failed To enumerate task sequence items: " +
e.Message);
        throw;
    }
}

public void MoveTaskSequenceStepUp(
    IResultObject taskSequence,
    string taskSequenceStepName)
{
    try
    {
        // Get the task sequence steps.
        List<IResultObject> steps = taskSequence.GetArrayItems("Steps"); //
Array of SMS_TaskSequence_Steps.

       int index = 0;

       foreach (IResultObject ro in steps)
       {
           if (ro["Name"].StringValue == taskSequenceStepName)
           {
               if (index > 0) // Not the first step, so you can move it up.
               {
                    steps.Insert(index + 1, steps[index - 1]);
                    steps.Remove(steps[index - 1]);
                    taskSequence.SetArrayItems("Steps", steps);
                    break;
               }
           }
           index++;
       }
    }
    catch (SmsException e)
    {
        Console.WriteLine("Failed To enumerate task sequence items: " +
e.Message);
        throw;
    }
}

<!-- p.1052 -->

The example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter              Type                      Description

 taskSequence           - Managed:                A valid task sequence or task sequence
                        IResultObject             group
                        - VBScript: SWbemObject

 taskSequenceStepName   - Managed: String         The name of the task sequence step to
                        - VBScript: String        move.
 stepName

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security

<!-- p.1053 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Add an Operating System Deployment Task Sequence Action
How to Connect to an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
Task sequence overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1054 -->

How to Create an Operating System
Deployment Task Sequence Group
Article • 10/04/2022

An operating system deployment task sequence group, in Configuration Manager, can
be added to a task sequence by creating an instance of the SMS_TaskSequence_Group
class. The group is then added to the list of steps of the task sequence. The list of steps
is an array of the SMS_TaskSequence_Step derived classes. The array is stored in the task
sequence, SMS_TaskSequence, Steps property.

To create a task sequence group
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Obtain a valid task sequence (SMS_TaskSequence) object. For more information,
        see How to Create an Operating System Deployment Task Sequence.

   3. Create an instance of the SMS_TaskSequence_Group class.

   4. Populate the group with the appropriate properties.

   5. Update the task sequence Steps property with the new group.

Example
The following example method adds a new group to the supplied task sequence.
Because the group is added to the end of the task sequence Steps array, you might
want to reorder its position. For more information, see How to Reorder an Operating
System Deployment Task Sequence.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddTaskSequenceGroup(connection, taskSequence, name, description)

         Dim group

         ' Create and populate the group.
         Set group = connection.Get("SMS_TaskSequence_Group").SpawnInstance_

<!-- p.1055 -->

       group.Name=name
       group.Description=description
       group.Enabled=True
       group.ContinueOnError=False

       ' Resize the task sequence steps array to hold the new group.
       ReDim steps (UBound (taskSequence.Steps)+1)

       ' Add the group.
       taskSequence.Steps(UBound(steps))=group

  End Sub

  c#

  public IResultObject AddTaskSequenceGroup(
      WqlConnectionManager connection,
      IResultObject taskSequence,
      string name,
      string description)
  {
      try
      {
          // Create the new group.
          IResultObject ro =
  connection.CreateEmbeddedObjectInstance("SMS_TaskSequence_Group");

            ro["Name"].StringValue = name;
            ro["Description"].StringValue = description;
            ro["Enabled"].BooleanValue = true;
            ro["ContinueOnError"].BooleanValue = false;

            // Add the group to the task sequence.
            List<IResultObject> array = taskSequence.GetArrayItems("Steps");
            array.Add(ro);

            // Add the new group to the end of the current steps.
            taskSequence.SetArrayItems("Steps", array);

           return ro;
       }
       catch (SmsException e)
       {
           Console.WriteLine("Failed to create Task Sequence: " + e.Message);
           throw;
       }
  }

This example method has the following parameters:

                                                                    ﾉ   Expand table

<!-- p.1056 -->

 Parameter      Type                           Description

 connection     - Managed:                     A valid connection to the SMS Provider.
                WqlConnectionManager
                - VBScript: SWbemServices

 taskSequence   - Managed: IResultObject       A valid task sequence ( SMS_TaskSequence ). The
                - VBScript: SWbemObject        group is added to this task sequence.

 Name           - Managed: String              A name for the new group.
                - VBScript: String

 Description    - Managed: String              A description for the new group.
                - VBScript: String

                                                                                  ﾉ    Expand table

 Parameter      Description

 connection     A WqlConnectionManager object that is a valid connection to the SMS Provider.

 taskSequence   An IResultObject that is a valid task sequence ( SMS_TaskSequence ). The group is
                added to this task sequence.

 name           A string name for the new group.

 description    A string description for the new group.

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Add a Step to an Operating System Deployment Group
How to Connect to an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create an Operating System Deployment Task Sequence
Task sequence overview

<!-- p.1057 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1058 -->

How to Add a Step to an Operating
System Deployment Group
Article • 10/04/2022

You add a step (an action or a group) to an operating system deployment task sequence
group, in Configuration Manager, by adding the step to the
SMS_TaskSequenceGroup.Steps array property.

To add a step to a task sequence group
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_TaskSequenceGroup object that you want to add the step to. For
        more information, see How to Create an Operating System Deployment Task
        Sequence Group.

   3. Create the task sequence step. For an example of creating an action step, see How
        to Add an Operating System Deployment Task Sequence Action.

   4. Add the step to the SMS_TaskSequenceGroup.Steps array property.

   5. Reorder the step within the array property as necessary. For more information, see
        How to Re-order an Operating System Deployment Task Sequence

Example
The following example method adds a command-line action to a task sequence group.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddStepToGroup(taskSequenceStep, group)

         Dim steps

         ' If needed, create a new steps array.
         If IsNull(group.Steps) Then
             steps = Array(taskSequenceStep)
             group.Steps=steps
         Else

<!-- p.1059 -->

         ' Resize the existing steps and add step.
         steps= Array(group.Steps)
         ReDim steps (UBound (group.Steps)+1)
         group.Steps(UBound(steps))=taskSequenceStep
     End if

End Sub

c#

public void AddStepToGroup(
    WqlConnectionManager connection,
    IResultObject taskSequence,
    string groupName)
{
    try
    {
        // Get the group.
        List<IResultObject> steps = taskSequence.GetArrayItems("Steps"); //
Array of SMS_TaskSequence_Steps.

        foreach (IResultObject ro in steps)
        {
            if (ro["Name"].StringValue == groupName &&
ro["__CLASS"].StringValue == "SMS_TaskSequence_Group")
            {
                IResultObject action =
connection.CreateEmbeddedObjectInstance("SMS_TaskSequence_RunCommandLineActi
on");
                action["CommandLine"].StringValue = @"C:\donowtingroup.bat";
                action["Name"].StringValue = "Action in group " + groupName;
                action["Description"].StringValue = "Action in a group";
                action["Enabled"].BooleanValue = true;
                action["ContinueOnError"].BooleanValue = false;

                  // Add the step to the task sequence.
                  List<IResultObject> array = ro.GetArrayItems("Steps");

                  array.Add(action);

                  ro.SetArrayItems("Steps", array);
                  taskSequence.SetArrayItems("Steps", steps);
                  break;
              }
          }
     }
     catch (SmsException e)
     {
         Console.WriteLine("Failed to create Task Sequence: " + e.Message);
         throw;
     }
}

<!-- p.1060 -->

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter          Type                   Description

 connection         - Managed:             A valid connection to the SMS Provider.
                    WqlConnectionManager
                    - VBScript:
                    SWbemServices

 taskSequence       - Managed:             - A valid task sequence (SMS_TaskSequence) that
                    IResultObject          contains the group.
 taskSequenceStep   - VBScript:
                    SWbemObject

 groupName          - Managed: String      The name of the group that the command-line
                    - VBScript: String     action is added to. This is obtained from the
 group                                     SMS_TaskSequenceGroup.Name property.

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming

<!-- p.1061 -->

For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Move a Step to a Different Operating System Deployment Task Sequence Group
How to Create an Operating System Deployment Task Sequence Group
How to Remove a Step From an Operating System Deployment Group
Task sequence overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1062 -->

How to Remove a Step from an
Operating System Deployment Group
Article • 10/04/2022

In Configuration Manager, you delete a step (an action or a group) from an operating
system deployment task sequence group by deleting the step from the group's list of
task sequence steps.

To remove a step from a group
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_TaskSequence_Group object that you want to add the step to. For
        more information, see How to Create an Operating System Deployment Task
        Sequence Group.

   3. Remove the action from the SMS_TaskSequence_Group.Steps array property.

Example
The following example method removes an action from a task sequence group.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub RemoveActionFromGroup(taskSequenceGroup, actionName)

         Dim i

      If taskSequenceGroup.SystemProperties_("__CLASS")
  <>"SMS_TaskSequence_Group" Then
          wscript.echo "Not a group"
          return
      End If

             Dim newArray
             Dim actionStep

             newArray = Array(taskSequenceGroup.Steps)
             ReDim newArray(UBound(taskSequenceGroup.Steps))

<!-- p.1063 -->

        i=0
        for each actionStep in taskSequenceGroup.Steps
            If actionStep.Name = actionName and _
              actionStep.SystemProperties_("__SUPERCLASS") =
"SMS_TaskSequence_Action" Then
                 ReDim preserve newArray(UBound(newArray)-1) ' shrink the
Array
            else
               wscript.echo actionStep.Name
               Set newArray(i)=actionStep ' copy it
               i=i+1
            End If

           Next

           taskSequenceGroup.Steps=newArray

 End Sub

c#

public void RemoveActionFromGroup(
    IResultObject taskSequenceGroup,
    string actionName)
{
    try
    {
        if (taskSequenceGroup["__CLASS"].StringValue !=
"SMS_TaskSequence_Group")
        {
            throw new System.InvalidOperationException("Not a group");
        }

        List<IResultObject> groupSteps =
taskSequenceGroup.GetArrayItems("Steps");
        IResultObject actionFound = null;
        foreach (IResultObject actionStep in groupSteps)
        {
            if (actionStep["Name"].StringValue == actionName &&
actionStep["__SUPERCLASS"].StringValue == "SMS_TaskSequence_Action")
            {
                actionFound = actionStep;
                break;
            }
        }

        groupSteps.Remove(actionFound);
        taskSequenceGroup.SetArrayItems("Steps", groupSteps);
     }
     catch (SmsException e)
     {
         Console.WriteLine("Failed to remove action: " + e.Message);
         throw;

<!-- p.1064 -->

      }
  }

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter           Type            Description

 taskSequenceGroup   - Managed:      The task sequence group containing the action to be
                     IResultObject   deleted.
                     - VBScript:
                     SWbemObject

 actionName          - Managed:      The name of the action to be deleted. This can be
                     String          obtained from the SMS_TaskSequenceAction.Name
                     - VBScript:     property.
                     String

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

<!-- p.1065 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Add a Step to an Operating System Deployment Group
How to Connect to an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Move a Step to a Different Operating System Deployment Task Sequence Group
How to Create an Operating System Deployment Task Sequence Group
Task sequence overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1066 -->

How to Move a Step to a Different
Operating System Deployment Task
Sequence Group
Article • 10/04/2022

You move a step (an action or a group) from one operating system deployment task
sequence group to another, in Configuration Manager, by adding the step to the target
group and then by deleting the step from the source group.

To move a step from one group to another
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the source and target SMS_TaskSequenceGroup objects. Copy a step that you
        want to add the step to. For more information, see How to Create an Operating
        System Deployment Task Sequence Group.

   3. Add the step to the target group. For more information, see How to Add a Step to
        an Operating System Deployment Group.

   4. Reorder the step within the target group array property as necessary. For more
        information, see How to Re-order an Operating System Deployment Task Sequence

   5. Delete the step from the source group. For more information, see How to Remove
        a Step From an Operating System Deployment Group.

Example
The following example method moves a step from one task sequence group to another.

You will need the code snippet in How to Remove a Step From an Operating System
Deployment Group to run this example.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub MoveActionToGroup( taskSequenceStep, sourceGroup,targetGroup)

<!-- p.1067 -->

            Dim steps
            Dim groupSteps

            Steps = Array(targetGroup.Steps)

            If IsNull(targetGroup.Steps) Then
                 groupSteps = Array(taskSequenceStep)
                 targetGroup.Steps = groupSteps
            Else
                 ReDim steps (UBound (targetGroup.Steps)+1)
                 targetGroup.Steps(UBound(steps))=taskSequenceStep
            End If

            Call RemoveActionFromGroup(sourceGroup,taskSequenceStep.Name)

  End Sub

  c#

  public void MoveActionToGroup(
      IResultObject taskSequenceStep,
      IResultObject sourceGroup,
      IResultObject targetGroup)
  {
      try
      {
          // Add the step to the target group.
          // Note. You can use MoveTaskSequenceStepUp and
  MoveTaskSequenceStepDown
          // to place the step in the target group.

            List<IResultObject> groupSteps = targetGroup.GetArrayItems("Steps");
            groupSteps.Add(taskSequenceStep);
            targetGroup.SetArrayItems("Steps", groupSteps);

          // Remove action from the source group.
          this.RemoveActionFromGroup(sourceGroup,
  taskSequenceStep["Name"].StringValue);
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to create Task Sequence: " + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                     ﾉ   Expand table

<!-- p.1068 -->

 Parameter          Type               Description

 taskSequenceStep   - Managed:         A valid task sequence step (Group or action)
                    IResultObject      (SMS_TaskSequence_Step).
                    - VBScript:
                    SWbemObject

 sourceGroup        - Managed:         The group SMS_TaskSequenceGroup the step is copied
                    IResultObject      from.
                    - VBScript:
                    SWbemObject

 targetGroup        - Managed:         The group SMS_TaskSequenceGroup the step is copied
                    IResultObject      to.
                    - VBScript:
                    SWbemObject

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

<!-- p.1069 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Add a Step to an Operating System Deployment Group
How to Connect to an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create an Operating System Deployment Task Sequence Group
How to Remove a Step From an Operating System Deployment Group
Task sequence overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1070 -->

How to Use Task Sequence Variables in a
Running Configuration Manager Task
Sequence
Article • 01/05/2024

In Configuration Manager, you can create, get, and set task sequence variables in a
running task sequence by using the task sequence environment COM automation object
( Microsoft.SMS.TSEnvironment ).

Typically, you use a command-line action that runs a script to access the task sequence
variables. But you can also access them, within a running a task sequence, by using any
programming environment that can use COM automation objects.

  ７ Note

  When you set a task variable on the Configuration Manager client, it becomes
  available to subsequent steps in the task sequence.

To create a custom task sequence variable, you set a Microsoft.SMS.TSEnvironment
property by using the name of the new variable that you want to create. If the variable
doesn't already exist, it's created. If the variable already exists, its value is updated. You
can later get the custom variable value from Microsoft.SMS.TSEnvironment .

When a task sequence variable is an array, it's passed in the following format:

  <base array name><element #><Property>="value".

For example, the OSDPartitions variable is an array of
SMS_TaskSequencePartitionSettings . The following example represents a one element
OSDPartitions Array:

  OSDPartitions0Bootable="true"
  OSDPartitions0FileSystem="NTFS"
  OSDPartition0QuickFormat="false"
  OSDPartitions0Size="100"

<!-- p.1071 -->

  OSDPartitions0SizeUnits="Percent"
  OSDPartitions0Type="Primary"

To access FileSystem in this array, you would use OSDPartitions0FileSystem . If the array
is larger, you would use OSDPartitions1FileSystem for the second element and so on
through the array.

It isn't recommended that you use managed code with the task sequencing
environment because you can't use it in the following environments:

     Windows PE

     Windows Server 2008

     Windows 2000

     Managed code does work when the full operating system is running with the
     correct version of .NET Framework installed.

     The version of .NET Framework that is required depends on the version of Visual
     Studio that you use.

                                                                        ﾉ   Expand table

 Visual Studio                         .NET Framework Version

 Visual Studio 2003                    1.0

 Visual Studio 2005                    2.0

 Visual Studio 2008                    2.0 to 3.5

You'll need to use COM interop to access the TSEnvironment object. You'll need the
following:

     Reference to TSEnvironment 1.0 Type Library.

     The TSEnvironmentLib namespace.

To use task variables in a running task sequence
   1. In a running task sequence, create an instance of Microsoft.SMS.TSEnvironment .

   2. Get or set the required environment variable.

<!-- p.1072 -->

Example
The following example method gets the _SMSTSLogPath variable. It also sets the value of
a custom variable and an array custom variable value.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub UseTaskSequenceVariables()
     dim osd: set env = CreateObject("Microsoft.SMS.TSEnvironment")
     dim logPath

        ' You can query the environment to get an existing variable.
        logPath = env("_SMSTSLogPath")

         wscript.echo logPath

     ' You can also set a variable in the Operating System Deployment
  environment.
     env("MyCustomVariable") = "My Custom Value"

     ' Set the OSDPartitions(0) Bootable array member to 0.
      env("OSDPartitions0Bootable") = "true"
  End Sub

Compiling the Code

Platforms
Operating System Deployment task sequencing environment

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

<!-- p.1073 -->

See Also
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
Task sequence overview How to Set an Operating System Deployment Task Sequence
Variable

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1074 -->

How to Set an Operating System
Deployment Task Sequence Variable
Article • 10/04/2022

In Configuration Manager, you create an operating system deployment task sequence
variable by creating an instance of the SMS_TaskSequence_SetVariableAction class,
adding to a task sequence. You can also create task sequence variables while the task
sequence is running on the client. For more information, see How to Use Task Sequence
Variables in a Running Configuration Manager Task Sequence.

A task sequence variable is a name/value pair that you can access by task sequence
steps. You can also create computer and collection-specific variables. For more
information, see How to Create a Collection Variable in Configuration Manager and How
to Create a Computer Variable in Configuration Manager.

  ７ Note

  Variables that are set with the SMS_TaskSequence_SetVariableAction class override
  variables that are set elsewhere. For example, if a collection variable and a
  SMS_TaskSequence_SetVariableAction have the same name, the value of the
  SMS_TaskSequence_SetVariableAction variable takes precedence.

To set a task sequence variable
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Get a task sequence to add the task sequence variable to. For more information,
      see How to Create an Operating System Deployment Task Sequence.

   3. Create an instance of SMS_TaskSequence_SetVariableAction.

   4. Set the VariableName and VariableValue properties for the variable that you are
      adding.

   5. Add the SMS_TaskSequence_SetVariableAction object to the task sequence.

Example
The following example method sets a task sequence variable name and value.

<!-- p.1075 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddTaskSequenceVariable(connection, taskSequence, variableName,
  variableValue)

        Dim variable
        Dim steps

      Set variable =
  connection.Get("SMS_TaskSequence_SetVariableAction").SpawnInstance_

        variable.Name="MyTaskSequenceVariable"
        variable.Description = "A task sequence variable"
        variable.Enabled=True
        variable.ContinueOnError=False
        variable.VariableName=variableName
        variable.VariableValue=variableValue

        steps= Array(taskSequence.Steps)

        ReDim steps (UBound (taskSequence.Steps)+1)

        taskSequence.Steps(UBound(steps))=variable

  End Sub

  c#

  public void AddTaskSequenceVariable(
      WqlConnectionManager connection,
      IResultObject taskSequence,
      string variableName,
      string variableValue)
  {
      try
      {
          // Create the task sequence variable object.
          IResultObject variable =
  connection.CreateEmbeddedObjectInstance("SMS_TaskSequence_SetVariableAction"
  );

          // Populate the properties.
          variable["Name"].StringValue = "MyTaskSequenceVariable";
          variable["ContinueOnError"].BooleanValue = false;
          variable["Description"].StringValue = "A task sequence variable set
  with SMS_TaskSequence_SetVariableAction";
          variable["Enabled"].BooleanValue = true;
          variable["VariableName"].StringValue = variableName;
          variable["VariableValue"].StringValue = variableValue;

<!-- p.1076 -->

              // Add the step to the task sequence.
              List<IResultObject> array = taskSequence.GetArrayItems("Steps");

              array.Add(variable);
              taskSequence.SetArrayItems("Steps", array);
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to set task sequence variable: " +
  e.Message);
          throw;
      }
  }

This example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter        Type                         Description

 connection       - Managed:                   - A valid connection to the SMS Provider.
                  WqlConnectionManager
                  - VBScript: SWbemServices

 taskSequence     - Managed:                   - The task sequence the variable is added
                  WqlConnectionManager         to.
                  - VBScript: SWbemServices

 variableName     - Managed: String            The name of the variable.
                  - VBScript: String

 variableValue    - Managed: String            The value for the variable.
                  - VBScript: String

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

<!-- p.1077 -->

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
Task sequence overview How to Use Task Sequence Variables in a Running Configuration
Manager Task Sequence
How to Read a Task Sequence from a Task Sequence Package

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1078 -->

About Computer Management
Article • 10/04/2022

Computer management in Configuration Manager operating system deployment covers
the following areas.

Computer Import
To deploy an operating system to a new computer without stand-alone media that is
not currently managed by Configuration Manager, the new computer must be added to
the Configuration Manager database prior to initiating the operating system
deployment process. Although Configuration Manager can automatically discover
computers on your network that have a Windows operating system installed, if the
computer has no operating system installed you must import the new computer
information. For more information, see How to Import a New Computer into
Configuration Manager.

Computer Association
A computer association creates a relationship between a source and destination
computer for the side-by-side migration of user state data. The source computer is an
existing computer that is managed by Configuration Manager, and contains the user
state data and settings that will be migrated to a specified destination computer. For
more information, see How to Create an Association Between Two Computers in
Configuration Manager.

Computer and Machine Variables
Task sequences can be configured to run simultaneously on multiple computers or on
collections. You can specify unique per-computer or per-collection information, such as
specifying a unique operating system product key or joining all the members of a
collection to a domain. These settings can be configured when you create a task
sequence or edit an existing task sequence.

You can assign task sequence variables to a single computer or to a collection. When the
task sequence starts to run on the target computer or the collection, the values that are
specified are applied to the target computer or collection.

For more information, see the following:

<!-- p.1079 -->

                                                                              ﾉ   Expand table

 Task                              How to

 Collection variables              How to Create a Collection Variable in Configuration Manager

 Computer variables                How to Create a Computer Variable in Configuration Manager

 Setting task sequence variables   How to Set an Operating System Deployment Task Sequence
                                   Variable

 Changing variables in a running   How to Use Task Sequence Variables in a Running
 task sequence                     Configuration Manager Task Sequence

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1080 -->

How to Import a New Computer into
Configuration Manager
Article • 10/04/2022

You add a new computer directly to the Configuration Manager database by calling the
ImportMachineEntry Method in Class SMS_Site. This can be used to deploy operating
systems to computers that have not yet been discovered automatically by Configuration
Manager.

   Tip

  You can also use the Import-CMComputerInformation PowerShell cmdlet.

You must provide the following information:

      NETBIOS computer name

      MAC address

      SMBIOS GUID

  ７ Note

  The MAC address must be for a network adapter that has a driver in Windows PE.
  The MAC address must be in colon format. For example, 00:00:00:00:00:00 . Other
  formats will prevent the client from receiving policy.

You should add a newly imported computer to a collection. This allows you to
immediately create advertisements for deploying operating systems to the computer.

You can associate a new computer with a reference computer. For more information, see
How to Create an Association Between Two Computers in Configuration Manager.

To add a new computer
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Call the ImportMachineEntry Method in Class SMS_Site.

   3. Add the resource identifier you get from ImportMachineEntry to a collection.
