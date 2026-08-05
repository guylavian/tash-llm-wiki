---
title: "How to use this documentation — pages 2281-2320"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2281-2320
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2281-2320
family: powershell
documentKind: "doc"
abstract: "For an example of a complete formatting file that defines a simple list view, see List View (Basic). Defining the Objects That Use the List View There are two ways to define which .NET objects use the list view. You can use the ViewSelectedBy element to define the objects that c"
---

# How to use this documentation — pages 2281-2320

<!-- p.2281 -->

For an example of a complete formatting file that defines a simple list view, see List View
(Basic).

Defining the Objects That Use the List View
There are two ways to define which .NET objects use the list view. You can use the
ViewSelectedBy element to define the objects that can be displayed by all the definitions of the
view, or you can use the EntrySelectedBy element to define which objects are displayed by a
specific definition of the view. In most cases, a view has only one definition, so objects are
typically defined by the ViewSelectedBy element.

The following example shows how to define the objects that are displayed by the list view
using the ViewSelectedBy and TypeName elements. There is no limit to the number of
TypeName elements that you can specify, and their order is not significant.

  XML

  <View>
    <Name>System.ServiceProcess.ServiceController</Name>
    <ViewSelectedBy>
      <TypeName>System.Diagnostics.Process</TypeName>
    </ViewSelectedBy>
    <ListControl>...</ListControl>
  </View>

The following XML elements can be used to specify the objects that are used by the list view:

      The ViewSelectedBy element defines which objects are displayed by the list view.

      The TypeName element specifies the .NET object that is displayed by the view. The fully
      qualified .NET type name is required. You must specify at least one type or selection set
      for the view, but there is no maximum number of elements that can be specified.

For an example of a complete formatting file, see List View (Basic).

The following example uses the ViewSelectedBy and SelectionSetName elements. Use selection
sets where you have a related set of objects that are displayed using multiple views, such as
when you define a list view and a table view for the same objects. For more information about
how to create a selection set, see Defining Selection Sets.

  XML

<!-- p.2282 -->

  <View>
    <Name>System.ServiceProcess.ServiceController</Name>
    <ViewSelectedBy>
      <SelectionSetName>.NET Type Set</SelectionSetName>
    </ViewSelectedBy>
    <ListControl>...</ListControl>
  </View>

The following XML elements can be used to specify the objects that are used by the list view:

      The ViewSelectedBy element defines which objects are displayed by the list view.

      The SelectionSetName element specifies a set of objects that can be displayed by the
      view. You must specify at least one selection set or type for the view, but there is no
      maximum number of elements that can be specified.

The following example shows how to define the objects displayed by a specific definition of the
list view using the EntrySelectedBy element. Using this element, you can specify the .NET type
name of the object, a selection set of objects, or a selection condition that specifies when the
definition is used. For more information about how to create a selection conditions, see
Defining Conditions for Displaying Data.

  XML

  <ListEntry>
    <EntrySelectedBy>
      <TypeName>.NET Type</TypeName>
    </EntrySelectedBy>
  </ListEntry>

The following XML elements can be used to specify the objects that are used by a specific
definition of the list view:

      The EntrySelectedBy element defines which objects are displayed by the definition.

      The TypeName element specifies the .NET object that is displayed by the definition. When
      using this element, the fully qualified .NET type name is required. You must specify at
      least one type, selection set, or selection condition for the definition, but there is no
      maximum number of elements that can be specified.

      The SelectionSetName element (not shown) specifies a set of objects that can be
      displayed by this definition. You must specify at least one type, selection set, or selection
      condition for the definition, but there is no maximum number of elements that can be
      specified.

<!-- p.2283 -->

     The SelectionCondition element (not shown) specifies a condition that must exist for this
     definition to be used. You must specify at least one type, selection set, or selection
     condition for the definition, but there is no maximum number of elements that can be
     specified. For more information about defining selection conditions, see Defining
     Conditions for Displaying Data.

Displaying Groups of Objects in a List View
You can separate the objects that are displayed by the list view into groups. This does not
mean that you define a group, only that Windows PowerShell starts a new group whenever the
value of a specific property or script changes. In the following example, a new group is started
whenever the value of the System.ServiceProcess.ServiceController.ServiceType property
changes.

 XML

 <GroupBy>
   <Label>Service Type</Label>
   <PropertyName>ServiceType</PropertyName>
 </GroupBy>

The following XML elements are used to define when a group is started:

     The GroupBy element defines the property or script that starts the new group and defines
     how the group is displayed.

     The PropertyName element specifies the property that starts a new group whenever its
     value changes. You must specify a property or script to start the group, but you cannot
     specify both.

     The ScriptBlock element specifies the script that starts a new group whenever its value
     changes. You must specify a script or property to start the group, but you cannot specify
     both.

     The Label element defines a label that is displayed at the beginning of each group. In
     addition to the text specified by this element, Windows PowerShell displays the value that
     triggered the new group and adds a blank line before and after the label. This element is
     optional.

     The CustomControl element defines a control that is used to display the data. This
     element is optional.

<!-- p.2284 -->

     The CustomControlName element specifies a common or view control that is used to
     display the data. This element is optional.

For an example of a complete formatting file that defines groups, see List View (GroupBy).

Using Format Strings
Formatting strings can be added to a view to further define how the data is displayed. The
following example shows how to define a formatting string for the value of the StartTime
property.

  XML

  <ListItem>
    <PropertyName>StartTime</PropertyName>
    <FormatString>{0:MMM} {0:DD} {0:HH}:{0:MM}</FormatString>
  </ListItem>

The following XML elements can be used to specify a format pattern:

     The ListItem element specifies the data that is displayed by the view.

     The PropertyName element specifies the property whose value is displayed by the view.
     You must specify either a property or a script, but you cannot specify both.

     The FormatString element specifies a format pattern that defines how the property or
     script value is displayed in the view.

     The ScriptBlock element (not shown) specifies the script whose value is displayed by the
     view. You must specify either a script or a property, but you cannot specify both.

In the following example, the ToString method is called to format the value of the script.
Scripts can call any method of an object. Therefore, if an object has a method, such as
ToString , that has formatting parameters, the script can call that method to format the output

value of the script.

  XML

  <ListItem>
    <ScriptBlock>
      [string]::Format("{0,-10} {1,-8}", $_.LastWriteTime.ToString("d"),
  $_.LastWriteTime.ToString("t"))
    </ScriptBlock>
  </ListItem>

<!-- p.2285 -->

The following XML element can be used to calling the ToString method:

     The ListItem element specifies the data that is displayed by the view.

     The ScriptBlock element (not shown) specifies the script whose value is displayed by the
     view. You must specify either a script or a property, but you cannot specify both.

See Also
Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.2286 -->

Creating a Wide View
A wide view displays a single value for each object that's displayed. The displayed value can be
the value of a .NET object property or the value of a script. By default, there is no label or
header for this view.

A Wide View Display
The following example shows how Windows PowerShell displays the
System.Diagnostics.Process object that's returned by the Get-Process cmdlet when its output is
piped to the Format-Wide cmdlet. (By default, the Get-Process cmdlet returns a table view.) In
this example, the two columns are used to display the name of the process for each returned
object. The name of the object's property isn't displayed, only the value of the property.

 PowerShell

 Get-Process | Format-Wide

 Output

 AEADISRV                          agrsmsvc
 Ati2evxx                          Ati2evxx
 audiodg                           CCC
 CcmExec                           communicator
 Crypserv                          csrss
 csrss                             DevDtct2
 DM1Service                        dpupdchk
 dwm                               DxStudio
 EXCEL                             explorer
 GoogleToolbarNotifier             GrooveMonitor
 hpqwmiex                          hpservice
 Idle                              InoRpc
 InoRT                             InoTask
 ipoint                            lsass
 lsm                               MOM
 MSASCui                           notepad
 ...                               ...

Defining the Wide View
The following XML shows the wide view schema for the System.Diagnostics.Process object.

<!-- p.2287 -->

  XML

  <View>
    <Name>process</Name>
    <ViewSelectedBy>
      <TypeName>System.Diagnostics.Process</TypeName>
    </ViewSelectedBy>
    <GroupBy>...</GroupBy>
    <Controls>...</Controls>
    <WideControl>
      <WideEntries>
        <WideEntry>
          <WideItem>
            <PropertyName>ProcessName</PropertyName>
          </WideItem>
        </WideEntry>
      </WideEntries>
    </WideControl>
  </View>

The following XML elements are used to define a wide view:

      The View element is the parent element of the wide view. (This is the same parent
      element for the table, list, and custom control views.)
      The Name element specifies the name of the view. This element is required for all views.
      The ViewSelectedBy element defines the objects that use the view. This element is
      required.
      The GroupBy element defines when a new group of objects is displayed. A new group is
      started whenever the value of a specific property or script changes. This element is
      optional.
      The Controls elements defines the custom controls that are defined by the wide view.
      Controls give you a way to further specify how the data is displayed. This element is
      optional. A view can define its own custom controls, or it can use common controls that
      can be used by any view in the formatting file. For more information about custom
      controls, see Creating Custom Controls.
      The WideControl element and its child elements define what's displayed in the view. In
      the preceding example, the view is designed to display the
      System.Diagnostics.Process.ProcessName property.

For an example of a complete formatting file that defines a simple wide view, see Wide View
(Basic).

Providing Definitions for Your Wide View

<!-- p.2288 -->

Wide views can provide one or more definitions by using the child elements of the
WideControl element. Typically, a view will have only one definition. In the following example,
the view provides a single definition that displays the System.Diagnostics.Process.ProcessName
property. A wide view can display the value of a property or the value of a script (not shown in
the example).

 XML

 <WideControl>
   <AutoSize/>
   <ColumnNumber></ColumnNumber>
   <WideEntries>
     <WideEntry>
       <WideItem>
         <PropertyName>ProcessName</PropertyName>
       </WideItem>
     </WideEntry>
   </WideEntries>
 </WideControl>

The following XML elements can be used to provide definitions for a wide view:

     The WideControl element and its child elements define what's displayed in the view.
     The AutoSize element specifies whether the column size and the number of columns are
     adjusted based on the size of the data. This element is optional.
     The ColumnNumber element specifies the number of columns displayed in the wide view.
     This element is optional.
     The WideEntries element provides the definitions of the view. In most cases, a view will
     have only one definition. This element is required.
     The WideEntry element provides a definition of the view. At least one WideEntry is
     required; however, there is no maximum limit to the number of elements that you can
     add. In most cases, a view will have only one definition.
     The EntrySelectedBy element specifies the objects that are displayed by a specific
     definition. This element is optional and is needed only when you define multiple
     WideEntry elements that display different objects.
     The WideItem element specifies the data that's displayed by the view. In contrast to other
     types of views, a wide control can display only one item.
     The PropertyName element specifies the property whose value is displayed by the view.
     You must specify either a property or a script, but you can't specify both.
     The ScriptBlock element specifies the script whose value is displayed by the view. You
     must specify either a script or a property, but you can't specify both.

<!-- p.2289 -->

      The FormatString element specifies a pattern that's used to display the data. This element
      is optional.

For an example of a complete formatting file that defines a wide view definition, see Wide View
(Basic).

Defining the Objects That Use the Wide View
There are two ways to define which .NET objects use the wide view. You can use the
ViewSelectedBy element to define the objects that can be displayed by all the definitions of the
view, or you can use the EntrySelectedBy element to define which objects are displayed by a
specific definition of the view. In most cases, a view has only one definition, so objects are
typically defined by the ViewSelectedBy element.

The following example shows how to define the objects that are displayed by the wide view
using the ViewSelectedBy and TypeName elements. There is no limit to the number of
TypeName elements that you can specify, and their order isn't significant.

  XML

  <View>
    <Name>System.ServiceProcess.ServiceController</Name>
    <ViewSelectedBy>
      <TypeName>System.Diagnostics.Process</TypeName>
    </ViewSelectedBy>
    <WideControl>...</WideControl>
  </View>

The following XML elements can be used to specify the objects that are used by the wide view:

      The ViewSelectedBy element defines which objects are displayed by the wide view.
      The TypeName element specifies the .NET that's displayed by the view. The fully qualified
      .NET type name is required. You must specify at least one type or selection set for the
      view, but there is no maximum number of elements that can be specified.

For an example of a complete formatting file, see Wide View (Basic).

The following example uses the ViewSelectedBy and SelectionSetName elements. Use selection
sets where you have a related set of objects that are displayed using multiple views, such as
when you define a wide view and a table view for the same objects. For more information
about how to create a selection set, see Defining Selection Sets.

<!-- p.2290 -->

 XML

 <View>
   <Name>System.ServiceProcess.ServiceController</Name>
   <ViewSelectedBy>
     <SelectionSetName>.NET Type Set</SelectionSetName>
   </ViewSelectedBy>
   <WideControl>...</WideControl>
 </View>

The following XML elements can be used to specify the objects that are used by the wide view:

     The ViewSelectedBy element defines which objects are displayed by the wide view.
     The SelectionSetName element specifies a set of objects that can be displayed by the
     view. You must specify at least one selection set or type for the view, but there is no
     maximum number of elements that can be specified.

The following example shows how to define the objects displayed by a specific definition of the
wide view using the EntrySelectedBy element. Using this element, you can specify the .NET type
name of the object, a selection set of objects, or a selection condition that specifies when the
definition is used. For more information about how to create a selection conditions, see
Defining Conditions for Displaying Data.

 XML

 <WideEntry>
   <EntrySelectedBy>
     <TypeName>.NET Type</TypeName>
   </EntrySelectedBy>
 </WideEntry>

The following XML elements can be used to specify the objects that are used by a specific
definition of the wide view:

     The EntrySelectedBy element defines which objects are displayed by the definition.
     The TypeName element specifies the .NET that's displayed by the definition. When using
     this element the fully qualified .NET type name is required. You must specify at least one
     type, selection set, or selection condition for the definition, but there is no maximum
     number of elements that can be specified.
     The SelectionSetName element (not shown) specifies a set of objects that can be
     displayed by this definition. You must specify at least one type, selection set, or selection
     condition for the definition, but there is no maximum number of elements that can be
     specified.

<!-- p.2291 -->

     The SelectionCondition element (not shown) specifies a condition that must exist for this
     definition to be used. You must specify at least one type, selection set, or selection
     condition for the definition, but there is no maximum number of elements that can be
     specified. For more information about defining selection conditions, see Defining
     Conditions for Displaying Data.

Displaying Groups of objects in a Wide View
You can separate the objects that are displayed by the wide view into groups. This doesn't
mean that you define a group, only that Windows PowerShell starts a new group whenever the
value of a specific property or script changes. In the following example, a new group is started
whenever the value of the System.ServiceProcess.ServiceController.ServiceType property
changes.

 XML

 <GroupBy>
   <Label>Service Type</Label>
   <PropertyName>ServiceType</PropertyName>
 </GroupBy>

The following XML elements are used to define when a group is started:

     The GroupBy element defines the property or script that starts the new group and defines
     how the group is displayed.
     The PropertyName element specifies the property that starts a new group whenever its
     value changes. You must specify a property or script to start the group, but you can't
     specify both.
     The ScriptBlock element specifies the script that starts a new group whenever its value
     changes. You must specify a script or property to start the group, but you can't specify
     both.
     The Label element defines a label that's displayed at the beginning of each group. In
     addition to the text specified by this element, Windows PowerShell displays the value that
     triggered the new group and adds a blank line before and after the label. This element is
     optional.
     The CustomControl element defines a control that's used to display the data. This
     element is optional.
     The CustomControlName element specifies a common or view control that's used to
     display the data. This element is optional.

<!-- p.2292 -->

For an example of a complete formatting file that defines groups, see Wide View (GroupBy).

Using Format Strings
Formatting strings can be added to a wide view to further define how the data is displayed. The
following example shows how to define a formatting string for the value of the StartTime
property.

  XML

  <WideItem>
    <PropertyName>StartTime</PropertyName>
    <FormatString>{0:MMM} {0:DD} {0:HH}:{0:MM}</FormatString>
  </WideItem>

The following XML elements can be used to specify a format pattern:

     The WideItem element specifies the data that's displayed by the view.
     The PropertyName element specifies the property whose value is displayed by the view.
     You must specify either a property or a script, but you can't specify both.
     The FormatString element specifies a format pattern that defines how the property or
     script value is displayed in the view
     The ScriptBlock element (not shown) specifies the script whose value is displayed by the
     view. You must specify either a script or a property, but you can't specify both.

In the following example, the ToString method is called to format the value of the script.
Scripts can call any method of an object. Therefore, if an object has a method, such as
ToString , that has formatting parameters, the script can call that method to format the output

value of the script.

  XML

  <WideItem>
    <ScriptBlock>
      [string]::Format("{0,-10} {1,-8}", $_.LastWriteTime.ToString("d"),
  $_.LastWriteTime.ToString("t"))
    </ScriptBlock>
  </WideItem>

The following XML element can be used to calling the ToString method:

     The WideItem element specifies the data that's displayed by the view.

<!-- p.2293 -->

     The ScriptBlock element (not shown) specifies the script whose value is displayed by the
     view. You must specify either a script or a property, but you can't specify both.

See Also
     Wide View (Basic)
     Wide View (GroupBy)
     Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2294 -->

Creating Custom Controls
Custom controls are the most flexible components of a formatting file. Unlike table, list, and
wide views that define a formal structure of data, such as a table of data, custom controls allow
you to define how an individual piece of data is displayed. You can define a common set of
custom controls that are available to all the views of the formatting file, you can define custom
controls that are available to a specific view, or you can define a set of controls that are
available to a group of objects.

Custom Control Example
The following example shows a custom control that is defined in the Certificates.Format.ps1xml
file. This custom control is used to separate the System.Management.Automation.Signature
objects displayed in a table view.

 XML

 <Controls>
   <Control>
     <Name>SignatureTypes-GroupingFormat</Name>
     <CustomControl>
       <CustomEntries>
         <CustomEntry>
            <CustomItem>
              <Frame>
                <LeftIndent>4</LeftIndent>
                <CustomItem>
                  <Text AssemblyName="System.Management.Automation"
 BaseName="FileSystemProviderStrings"
                    ResourceId="DirectoryDisplayGrouping"/>
                  <ExpressionBinding>
                    <ScriptBlock>Split-Path $_.Path</ScriptBlock>
                  </ExpressionBinding>
                  <NewLine/>
                </CustomItem>
              </Frame>
            </CustomItem>
         </CustomEntry>
       </CustomEntries>
     </CustomControl>
   </Control>
 </Controls>

<!-- p.2295 -->

See Also
Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2296 -->

Loading and Exporting Formatting Data
Once you've created your formatting file, you need to update the format data of the session by
loading your files into the current session. PowerShell loads a predefined set of formats. Once
the format data of the current session is updated, PowerShell uses that data to display the .NET
objects associated with the views defined in the loaded formats. There's no limit to the number
of formats that you can load into the current session. You can also export the format data in
the current session back to a formatting file.

Loading format data
Formatting files can be loaded into the current session using the following methods:

     You can import the formatting file into the current session from the command line. Use
     the Update-FormatData cmdlet as described in the following procedure.

     You can create a module manifest that references your formatting file. Modules allow you
     to package your formatting files for distribution. Use the New-ModuleManifest cmdlet to
     create the manifest, and the Import-Module cmdlet to load the module into the current
     session. For more information about modules, see Writing a Windows PowerShell
     Module.

     You can create a snap-in that references your formatting file. Use the
     System.Management.Automation.PSSnapIn.Formats to reference your formatting files.
     However, best practice recommendation is to use modules to package cmdlets and
     associated formatting and types files.

     If you're invoking commands programmatically, you can add formatting files to the initial
     session state of the runspace where the commands are run. For more information, see the
     System.Management.Automation.Runspaces.SessionStateFormatEntry class.

When a formatting file is loaded, it's added to an internal list that PowerShell uses to choose
the view used when displaying objects in the host. You can prepend your formatting file to the
beginning of the list, or you can append it to the end of the list.

Knowing where your formatting file is added to this list is important.

     If you're loading a formatting file that defines the only view for an object, you can use any
     of the methods described previously.

<!-- p.2297 -->

     If you're loading a formatting file that defines a view for an object that has an existing
     view defined, it must be added to the beginning of the list. You must use the Update-
     FormatData cmdlet and prepend your file to the beginning of the list.

Storing Your Formatting File
You can store formatting files anywhere on disk. However, it's recommended that you store
them in the same folder as your profile script.

Use the following command to determine the location of your profile script.

 PowerShell

 Split-Path -Path $PROFILE -Parent

Loading a format file
   1. Store your formatting file to disk.

   2. Run the Update-FormatData cmdlet using one of the following commands.

     If you're changing how an object is displayed, use the following command to add your
     formatting file to the front of the list.

       PowerShell

       Update-FormatData -PrependPath PathToFormattingFile

     Use the following command to add your formatting file to the end of the list.

       PowerShell

       Update-FormatData -AppendPath PathToFormattingFile

        ７ Note

        Once format data has been loaded in a session it can't be removed. You must open a
        new session without the format data loaded.

Exporting format data

<!-- p.2298 -->

PowerShell includes format definitions for many .NET types. You can use the Get-FormatData
cmdlet to view the format data that's loaded in the current session. You can export the format
data for a type to a file using the Export-FormatData cmdlet.

The following commands export the format data for the System.Guid type to a file named
System.Guid.format.ps1xml in the current directory.

  PowerShell

  Get-FormatData System.Guid | Export-FormatData -Path ./System.Guid.format.ps1xml
  Get-Content ./System.Guid.format.ps1xml

  Output

  <?xml version="1.0" encoding="utf-8"?>
  <Configuration>
    <ViewDefinitions>
      <View>
        <Name>System.Guid</Name>
        <ViewSelectedBy>
          <TypeName>System.Guid</TypeName>
        </ViewSelectedBy>
        <TableControl>
          <TableHeaders />
          <TableRowEntries>
             <TableRowEntry>
               <TableColumnItems>
                 <TableColumnItem>
                   <PropertyName>Guid</PropertyName>
                 </TableColumnItem>
               </TableColumnItems>
             </TableRowEntry>
          </TableRowEntries>
        </TableControl>
      </View>
    </ViewDefinitions>
  </Configuration>

You can edit the exported file create a custom format definition for that type.

 Last updated on 05/20/2025

<!-- p.2299 -->

Defining Selection Sets
When creating multiple views and controls, you can define sets of objects that are referred to
as selection sets. A selection set enables you to define the objects one time, without having to
define them repeatedly for each view or control. Typically, selection sets are used when you
have a set of related .NET objects. For example, The FileSystem formatting file
(FileSystem.format.ps1xml) defines a selection set of the file system types that several views
use.

Where Selection Sets are Defined and Referenced
You define selection sets as part of the common data that can be used by all the views and
controls defined in the formatting file. The following example shows how to define three
selection sets.

 XML

 <Configuration>
   <SelectionSets>
     <SelectionSet>...</SelectionSet>
     <SelectionSet>...</SelectionSet>
     <SelectionSet>...</SelectionSet>
   </SelectionSets>
 </Configuration>

You can reference a selection sets in the following ways:

       Each view has a ViewSelectedBy element that defines which objects are displayed by
       using the view. The ViewSelectedBy element has a SelectionSetName child element that
       specifies the selection set that all the definitions of the view use. There is no restriction on
       the number of selection sets that you can reference from a view.

       In each definition of a view or control, the EntrySelectedBy element defines which objects
       are displayed by using that definition. Typically a view or control has only one definition
       so the objects are defined by the ViewSelectedBy element. The EntrySelectedBy element
       of the definition has a SelectionSetName child element that specifies the selection set. If
       you specify the selection set for a definition, you cannot specify any of the other child
       elements of the EntrySelectedBy element.

<!-- p.2300 -->

     In each definition of a view or control, the SelectionCondition element can be used to
     specify a condition for when the definition is used. The SelectionCondition element has a
     SelectionSetName child element that specifies the selection set that triggers the condition.

     The condition is triggered when any of the objects defined in the selection set are
     displayed. For more information about how to set these conditions, see Defining
     Conditions for when Data is Displayed.

Selection Set Example
The following example shows a selection set that is taken directly from the FileSystem
formatting file provided by Windows PowerShell. For more information about other Windows
PowerShell formatting files, see Windows PowerShell Formatting Files.

 XML

 <SelectionSets>
   <SelectionSet>
     <Name>FileSystemTypes</Name>
     <Types>
      <TypeName>System.IO.DirectoryInfo</TypeName>
      <TypeName>System.IO.FileInfo</TypeName>
      <TypeName>Deserialized.System.IO.DirectoryInfo</TypeName>
      <TypeName>Deserialized.System.IO.FileInfo</TypeName>
     </Types>
   </SelectionSet>
 </SelectionSets>

The previous selection set is referenced in the ViewSelectedBy element of a table view.

 XML

 <ViewDefinitions>
   <View>
     <Name>Files</Name>
     <ViewSelectedBy>
       <SelectionSetName>FileSystemTypes</SelectionSetName>
     </ViewSelectedBy>
     <TableControl>...</TableControl>
   </View>
 </ViewDefinitions>

XML Elements

<!-- p.2301 -->

There is no limit to the number of selection sets that you can define. The following XML
elements are used to create a selection set.

     The SelectionSets element defines the sets of .NET objects that are referenced by the
     views and controls of the formatting file.

     The SelectionSet element defines a single set of .NET objects.

     The Name element specifies the name that is used to reference the selection set.

     The Types element specifies the .NET types of the objects of the selection set. (Within
     formatting files, objects are specified by their .NET type.)

The following XML elements are used to specify a selection set.

     The following element specifies the selection set to use in all the definitions of the view:

        SelectionSetName Element for ViewSelectedBy (Format)

        SelectionSetName Element for EntrySelectedBy for GroupBy (Format)

     The following elements specify the selection set used by a single view definition:

        SelectionSetName Element for EntrySelectedBy for ListControl (Format)

        SelectionSetName Element for EntrySelectedBy for TableControl (Format)

        SelectionSetName Element for EntrySelectedBy for WideControl (Format)

        SelectionSetName Element for EntrySelectedBy for CustomControl for View (Format)

     The following elements specify the selection set used by common and view control
     definitions:

        SelectionSetName Element for EntrySelectedBy for Controls for View (Format)

        SelectionSetName Element for EntrySelectedBy for Controls for Configuration (Format)

     The following elements specify the selection set used when you define which object to
     expand:
        SelectionSetName Element for EntrySelectedBy for EnumerableExpansion (Format)

     The following elements specify the selection set used by selection conditions.

<!-- p.2302 -->

        SelectionSetName Element for SelectionCondition for Controls for Configuration
        (Format)

        SelectionSetName Element for SelectionCondition for Controls for View (Format)

        SelectionSetName Element for SelectionCondition for CustomControl for View
        (Format)

        SelectionSetName Element for SelectionCondition for EntrySelectedBy for
        EnumerableExpansion (Format)

        SelectionSetName Element for SelectionCondition for EntrySelectedBy for ListEntry
        (Format)

        SelectionSetName Element for SelectionCondition for EntrySelectedBy for TableControl
        (Format)

        SelectionSetName Element for SelectionCondition for EntrySelectedBy for WideEntry
        (Format)

        SelectionSetName Element for SelectionCondition for GroupBy (Format)

See Also
SelectionSets

SelectionSet

Name

Types

PowerShell Formatting Files

Defining Conditions for when Data is Displayed

Writing a PowerShell Formatting and Types File

Last updated on 05/20/2025

<!-- p.2303 -->

Defining Conditions for Displaying Data
When defining what data is displayed by a view or a control, you can specify a condition that
must exist for the data to be displayed. The condition can be triggered by a specific property,
or when a script or property value evaluates to true . When the selection condition is met, the
definition of the view or control is used.

Specifying a Selection Condition for a Definition
When creating a definition for a view or control, the EntrySelectedBy element is used to
specify which objects will use the definition or what condition must exist for the definition to
be used. The condition is specified by the SelectionCondition element.

In the following example, a selection condition is specified for a definition of a table view. In
this example, the definition is used only when the specified script is evaluated to true .

 XML

 <TableRowEntry>
   <EntrySelectedBy>
     <SelectionCondition>
       <ScriptBlock>ScriptToEvaluate</ScriptBlock>
     </SelectionCondition>
   </EntrySelectedBy>
   <TableColumnItems>
   </TableColumnItems>
 </TableRowEntry>

There is no limit to the number of selection conditions that you can specify for a definition of a
view or control. The only requirements are the following:

     The selection condition must specify one property name or script to trigger the condition,
     but cannot specify both.

     The selection condition can specify any number of .NET types or selection sets, but
     cannot specify both.

Specifying a Selection Condition for an Item

<!-- p.2304 -->

You can also specify when an item of a list view or control is used by including the
ItemSelectionCondition element in the item definition. In the following example, a selection

condition is specified for an item of a list view. In this example, the item is used only when the
script is evaluated to true .

 XML

 <ListItem>
   <ItemSelectionCondition>
     <ScriptBlock>ScriptToEvaluate</ScriptBlock>
   </ItemSelectionCondition>
 </ListItem>

You can specify only one selection condition for an item. And the condition must specify one
property name or script to trigger the condition, but cannot specify both.

XML Elements
The following XML elements are used to create a selection condition.

     The following elements specify selection conditions for view definitions:

        SelectionCondition Element for EntrySelectedBy for TableControl (Format)

        SelectionCondition Element for EntrySelectedBy for ListControl (Format)

        SelectionCondition Element for EntrySelectedBy for WideControl (Format)

        SelectionCondition Element for EntrySelectedBy for CustomControl (Format)

     The following elements specify selection conditions for common and view control
     definitions:

        SelectionCondition Element for EntrySelectedBy for Controls for Configuration
        (Format)

        SelectionCondition Element for EntrySelectedBy for Controls for View (Format)

     The following element specifies the selection condition for expanding collection objects:
        SelectionCondition Element for EntrySelectedBy for EnumerableExpansion (Format)

     The following element specifies the selection condition for displaying a new group of
     data:

<!-- p.2305 -->

        SelectionCondition Element for EntrySelectedBy for GroupBy (Format)

     The following element specifies an item selection condition for a list view:
        ItemSelectionCondition Element for ListItem for ListControl (Format)

     The following elements specify an item selection condition for controls:

        ItemSelectionCondition Element for ExpressionBinding for Controls for Configuration
        (Format)

        ItemSelectionCondition Element for ExpressionBinding for Controls for View (Format)

        ItemSelectionCondition Element for ExpressionBinding for CustomControl (Format)

See Also
Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2306 -->

Formatting Displayed Data
You can specify how the individual data points in your List, Table, or Wide view are displayed.
You can use the FormatString element when defining the items of your view, or you can use
the ScriptBlock element to call the FormatString method on the data.

Using the FormatString Element
In the following example the value of the TotalProcessorTime property of the
System.Diagnostics.Process object is formatted using the FormatString element. the
TotalProcessorTime property

  XML

  <TableColumnItem>
    <PropertyName>TotalProcessorTime</PropertyName>
    <FormatString>{0:MMM}{0:dd}{0:HH}:{0:mm}</FormatString>
  </TableColumnItem>

 Last updated on 05/20/2025

<!-- p.2307 -->

Windows PowerShell Formatting Files
Windows PowerShell provides several formatting files (.format.ps1xml) that are located in the
installation directory ( $PSHOME ). Each of these files defines the default display for a specific set
of .NET objects. These files should never be changed. However, you can use them as a
reference for creating your own custom formatting files.

Certificate.Format.ps1xml Defines the display of objects in the Certificate store such as x.509

certificates and certificate stores.

DotNetTypes.Format.ps1xml Defines the display of miscellaneous .NET objects such as

CultureInfo, FileVersionInfo, and EventLogEntry objects.

FileSystem.Format.ps1xml Defines the display of file system objects such as file and directory

objects.

Help.Format.ps1xml Defines the different views used by the Get-Help cmdlet, such as the

detailed, full, parameters, and example views.

PowerShellCore.Format.ps1xml Defines the display of the objects generated by Windows

PowerShell core cmdlets, such as the objects returned by the Get-Member and Get-History
cmdlets.

PowerShellTrace.Format.ps1xml Defines the display of trace objects such as those generated by

the Trace-Command cmdlet.

Registry.Format.ps1xml Defines the display of registry objects such as key and entry objects.

See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.2308 -->

How to Create a Formatting File
(Format.ps1xml)
This topic describes how to create a formatting file ( Format.ps1xml ).

  ７ Note

  You can also create a formatting file by making a copy of one of the files provided by
  Windows PowerShell. To protect the users of your Format.ps1xml file, sign the file using a
  digital signature. For more information, see about_Signing.

Create a Format.ps1xml file
   1. Open a new text file using a text editor such as Visual Studio Code.

   2. Copy the following lines into the formatting file.

       XML

       <?xml version="1.0" encoding="utf-8"?>
       <Configuration>
       <ViewDefinitions>
       </ViewDefinitions>
       </Configuration>

           The <Configuration></Configuration> tags define the root Configuration node. All
           additional XML tags will be enclosed within this node.

           The <ViewDefinitions></ViewDefinitions> tags define the ViewDefinitions node. All
           views are defined within this node.

   3. Save the file to a folder of your choice. If you are writing a module, save the file to a
     subfolder of the module folder. Use the following name format when you save the file:
      MyFile.Format.ps1xml . Formatting files must use the .ps1xml extension.

     You are now ready to add views to the formatting file. There is no limit to the number of
     views that can be defined in a formatting file. You can add a single view for each object,
     multiple views for the same object, or a single view that is used by multiple objects.

See also

<!-- p.2309 -->

     Formatting File Overview
     Formatting File Concepts

Last updated on 01/02/2026

<!-- p.2310 -->

Wide View (Basic)
This example shows how to implement a basic wide view that displays the
System.ServiceProcess.ServiceController objects returned by the Get-Service cmdlet. For more
information about the components of a wide view, see Creating a Wide View.

Load this formatting file
   1. Copy the XML from the Example section of this topic into a text file.

   2. Save the text file. Be sure to add the format.ps1xml extension to the file to identify it as a
     formatting file.

   3. Open Windows PowerShell, and run the following command to load the formatting file
     into the current session: Update-FormatData -PrependPath <PathToFormattingFile> .

        ２ Warning

        This formatting file defines the display of an object that is already defined by a
        Windows PowerShell formatting file. You must use the PrependPath parameter when
        you run the cmdlet, and you cannot load this formatting file as a module.

Demonstrates
This formatting file demonstrates the following XML elements:

     The Name element for the view.

     The ViewSelectedBy element that defines what objects are displayed by the view.

     The WideItem element that defines what property is displayed by the view.

Example
The following XML defines a wide view that displays the value of the
System.ServiceProcess.ServiceController.ServiceName property.

 XML

<!-- p.2311 -->

  <?xml version="1.0" encoding="utf-8" ?>

  <Configuration>
    <ViewDefinitions>
      <View>
        <Name>ServiceWideView</Name>
        <ViewSelectedBy>
          <TypeName>System.ServiceProcess.ServiceController</TypeName>
        </ViewSelectedBy>
        <WideControl>
          <WideEntries>
            <WideEntry>
              <WideItem>
                <PropertyName>ServiceName</PropertyName>
              </WideItem>
            </WideEntry>
          </WideEntries>
        </WideControl>
      </View>
    </ViewDefinitions>
  </Configuration>

The following example shows how Windows PowerShell displays the
System.ServiceProcess.ServiceController objects after this format file is loaded.

  PowerShell

  Get-Service f*

  Output

  Fax                          FCSAM
  fdPHost                      FDResPub
  FontCache                    FontCache3.0.0.0
  FSysAgent                    FwcAgent

See Also
Examples of Formatting Files

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2312 -->

Wide View (GroupBy)
This example shows how to implement a wide view that displays groups of
System.ServiceProcess.ServiceController objects returned by the Get-Service cmdlet. For more
information about the components of a wide view, see Creating a Wide View.

Load this formatting file
   1. Copy the XML from the Example section of this topic into a text file.

   2. Save the text file. Be sure to add the format.ps1xml extension to the file to identify it as a
     formatting file.

   3. Open Windows PowerShell, and run the following command to load the formatting file
     into the current session: Update-FormatData -PrependPath <Path to file> .

        ２ Warning

        This formatting file defines the display of an object that is already defined by a
        Windows PowerShell formatting files. You must use the PrependPath parameter
        when you run the cmdlet, and you cannot load this formatting file as a module.

Demonstrates
This formatting file demonstrates the following XML elements:

     The Name element for the view.

     The ViewSelectedBy element that defines what objects are displayed by the view.

     The GroupBy element that defines when a new group is displayed.

     The WideItem element that defines what property is displayed by the view.

Example
The following XML defines a wide view that displays groups of objects. Each new group is
started when the value of the System.ServiceProcess.ServiceController.ServiceType property

<!-- p.2313 -->

changes.

 XML

 <?xml version="1.0" encoding="utf-8" ?>

 <Configuration>
   <ViewDefinitions>
     <View>
       <Name>ServiceWideView</Name>
       <ViewSelectedBy>
         <TypeName>System.ServiceProcess.ServiceController</TypeName>
       </ViewSelectedBy>
       <GroupBy>
         <Label>Service Type</Label>
         <PropertyName>ServiceType</PropertyName>
       </GroupBy>
       <WideControl>
         <WideEntries>
           <WideEntry>
             <WideItem>
               <PropertyName>ServiceName</PropertyName>
             </WideItem>
           </WideEntry>
         </WideEntries>
       </WideControl>
     </View>
   </ViewDefinitions>
 </Configuration>

The following example shows how Windows PowerShell displays the
System.ServiceProcess.ServiceController objects after this format file is loaded.

 PowerShell

 Get-Service f*

 Output

       Service Type: Win32OwnProcess

 Fax                                  FCSAM

       Service Type: Win32ShareProcess

 fdPHost                              FDResPub
 FontCache

       Service Type: Win32OwnProcess

<!-- p.2314 -->

 FontCache3.0.0.0                      FSysAgent
 FwcAgent

See Also
Examples of Formatting Files

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2315 -->

List View (Basic)
This example shows how to implement a basic list view that displays the
System.ServiceProcess.ServiceController objects returned by the Get-Service cmdlet. For more
information about the components of a list view, see Creating a List View.

Load this formatting file
   1. Copy the XML from the Example section of this topic into a text file.

   2. Save the text file. Be sure to add the format.ps1xml extension to the file to identify it as a
     formatting file.

   3. Open Windows PowerShell, and run the following command to load the formatting file
     into the current session: Update-FormatData -PrependPath PathToFormattingFile .

  ２ Warning

  This formatting file defines the display of an object that is already defined by a Windows
  PowerShell formatting file. You must use the PrependPath parameter when you run the
  cmdlet, and you cannot load this formatting file as a module.

Demonstrates
This formatting file demonstrates the following XML elements:

     The Name element for the view.

     The ViewSelectedBy element that defines what objects are displayed by the view.

     The ListControl element that defines what property is displayed by the view.

     The ListItem element that defines what is displayed in a row of the list view.

     The PropertyName element that defines which property is displayed.

Example

<!-- p.2316 -->

The following XML defines a list view that displays four properties of the
System.ServiceProcess.ServiceController object. In each row, the name of the property is
displayed followed by the value of the property.

 XML

 <Configuration>
   <View>
     <Name>System.ServiceProcess.ServiceController</Name>
     <ViewSelectedBy>
       <TypeName>System.ServiceProcess.ServiceController</TypeName>
     </ViewSelectedBy>
     <ListControl>
       <ListEntries>
         <ListEntry>
           <ListItems>
             <ListItem>
               <PropertyName>Name</PropertyName>
             </ListItem>
             <ListItem>
               <PropertyName>DisplayName</PropertyName>
             </ListItem>
             <ListItem>
               <PropertyName>Status</PropertyName>
             </ListItem>
             <ListItem>
               <PropertyName>ServiceType</PropertyName>
             </ListItem>
           </ListItems>
         </ListEntry>
       </ListEntries>
     </ListControl>
   </View>
 </Configuration>

The following example shows how Windows PowerShell displays the
System.ServiceProcess.ServiceController objects after this format file is loaded.

 PowerShell

 Get-Service f*

 Output

 Name        : Fax
 DisplayName : Fax
 Status      : Stopped
 ServiceType : Win32OwnProcess

<!-- p.2317 -->

 Name        : FCSAM
 DisplayName : Microsoft Antimalware Service
 Status      : Running
 ServiceType : Win32OwnProcess

 Name        : fdPHost
 DisplayName : Function Discovery Provider Host
 Status      : Stopped
 ServiceType : Win32ShareProcess

 Name        : FDResPub
 DisplayName : Function Discovery Resource Publication
 Status      : Running
 ServiceType : Win32ShareProcess

 Name        : FontCache
 DisplayName : Windows Font Cache Service
 Status      : Running
 ServiceType : Win32ShareProcess

 Name        : FontCache3.0.0.0
 DisplayName : Windows Presentation Foundation Font Cache 3.0.0.0
 Status      : Stopped
 ServiceType : Win32OwnProcess

 Name        : FSysAgent
 DisplayName : Microsoft Forefront System Agent
 Status      : Running
 ServiceType : Win32OwnProcess

 Name        : FwcAgent
 DisplayName : Firewall Client Agent
 Status      : Running
 ServiceType : Win32OwnProcess

See Also
Examples of Formatting Files

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2318 -->

List View (Labels)
This example shows how to implement a list view that displays a custom label for each row of
the list. This list view displays the properties of the System.ServiceProcess.ServiceController
object that is returned by the Get-Service cmdlet. For more information about the components
of a list view, see Creating a List View.

Load this formatting file
   1. Copy the XML from the Example section of this topic into a text file.

   2. Save the text file. Be sure to add the format.ps1xml extension to the file to identify it as a
     formatting file.

   3. Open Windows PowerShell, and run the following command to load the formatting file
     into the current session: Update-FormatData -PrependPath PathToFormattingFile .

  ２ Warning

  This formatting file defines the display of an object that is already defined by a Windows
  PowerShell formatting file. You must use the PrependPath parameter when you run the
  cmdlet, and you cannot load this formatting file as a module.

Demonstrates
This formatting file demonstrates the following XML elements:

     The Name element for the view.

     The ViewSelectedBy element that defines what objects are displayed by the view.

     The ListControl element that defines what property is displayed by the view.

     The ListItem element that defines what is displayed in a row of the list view.

     The Label element that defines what is displayed in a row of the list view.

     The PropertyName element that defines which property is displayed.

<!-- p.2319 -->

Example
The following XML defines a list view that displays a custom label in each row. In this case, the
label includes the property name with each letter capitalized and the word "property". In each
row, the name of the property is displayed followed by the value of the property.

 XML

 <Configuration>
   <ViewDefinitions>
     <View>
   <Name>System.ServiceProcess.ServiceController</Name>
   <ViewSelectedBy>
     <TypeName>System.ServiceProcess.ServiceController</TypeName>
   </ViewSelectedBy>
   <ListControl>
     <ListEntries>
       <ListEntry>
         <ListItems>
           <ListItem>
             <Label>NAME property</Label>
             <PropertyName>Name</PropertyName>
           </ListItem>
           <ListItem>
             <Label>DISPLAYNAME property</Label>
             <PropertyName>DisplayName</PropertyName>
           </ListItem>
           <ListItem>
             <Label>STATUS property</Label>
             <PropertyName>Status</PropertyName>
           </ListItem>
           <ListItem>
             <Label>SERVICETYPE property</Label>
             <PropertyName>ServiceType</PropertyName>
           </ListItem>
         </ListItems>
       </ListEntry>
     </ListEntries>
   </ListControl>
 </View>

   </ViewDefinitions>
 </Configuration>

The following example shows how Windows PowerShell displays the
System.ServiceProcess.ServiceController objects after this format file is loaded.

 PowerShell

<!-- p.2320 -->

 Get-Service f*

 Output

 NAME property        : Fax
 DISPLAYNAME property : Fax
 STATUS property      : Stopped
 SERVICETYPE property : Win32OwnProcess

 NAME property        : FCSAM
 DISPLAYNAME property : Microsoft Antimalware Service
 STATUS property      : Running
 SERVICETYPE property : Win32OwnProcess

 NAME property        : fdPHost
 DISPLAYNAME property : Function Discovery Provider Host
 STATUS property      : Stopped
 SERVICETYPE property : Win32ShareProcess

 NAME property        : FDResPub
 DISPLAYNAME property : Function Discovery Resource Publication
 STATUS property      : Running
 SERVICETYPE property : Win32ShareProcess

 NAME property        : FontCache
 DISPLAYNAME property : Windows Font Cache Service
 STATUS property      : Running
 SERVICETYPE property : Win32ShareProcess

 NAME property        : FontCache3.0.0.0
 DISPLAYNAME property : Windows Presentation Foundation Font Cache 3.0.0.0
 STATUS property      : Stopped
 SERVICETYPE property : Win32OwnProcess

 NAME property        : FSysAgent
 DISPLAYNAME property : Microsoft Forefront System Agent
 STATUS property      : Running
 SERVICETYPE property : Win32OwnProcess

 NAME property        : FwcAgent
 DISPLAYNAME property : Firewall Client Agent
 STATUS property      : Running
 SERVICETYPE property : Win32OwnProcess

See Also
Examples of Formatting Files

Writing a PowerShell Formatting File
