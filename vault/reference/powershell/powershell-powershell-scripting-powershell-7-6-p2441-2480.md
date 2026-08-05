---
title: "How to use this documentation — pages 2441-2480"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2441-2480
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2441-2480
family: powershell
documentKind: "doc"
abstract: "PropertyCountForTable Element Optional element. Specifies the minimum number of properties that an object must have to display the object in a table view. Schema DefaultSettings Element PropertyCountForTable Element Syntax XML <PropertyCountForTable>NumberOfProperties</PropertyC"
---

# How to use this documentation — pages 2441-2480

<!-- p.2441 -->

PropertyCountForTable Element
Optional element. Specifies the minimum number of properties that an object must have to
display the object in a table view.

Schema
     DefaultSettings Element
     PropertyCountForTable Element

Syntax
 XML

 <PropertyCountForTable>NumberOfProperties</PropertyCountFortable>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyCountForTable element. The default value for this element is 4 .

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                   Description

 DefaultSettings Element   Defines common settings that apply to all the views of the formatting file.

Remarks

<!-- p.2442 -->

See Also
Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2443 -->

ShowError Element
Specifies that the full error record is displayed when an error occurs while displaying a piece of
data.

Schema
        Configuration Element
        DefaultSettings Element
        ShowError Element

Syntax
 scr

 <ShowError/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ShowError element. The default value for this element is false .

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                    Description

 DefaultSettings Element    Defines common settings that apply to all the views of the formatting file.

<!-- p.2444 -->

Remarks

See Also
Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2445 -->

WrapTables Element
Specifies that data in a table cell is moved to the next line if the data is longer than the width
of the column.

Schema
     Configuration Element
     DefaultSettings Element
     WrapTables Element

Syntax
 XML

 <WrapTables/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
WrapTables element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                   Description

 DefaultSettings Element   Defines common settings that apply to all the views of the formatting file.

<!-- p.2446 -->

Remarks

See Also
Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2447 -->

SelectionSets Element
Defines the common sets of .NET objects that can be used by all views of the formatting file.
The views and controls of the formatting file can reference the complete set of objects by using
only the name of the selection set.

Schema
     Configuration Element
     SelectionSets Element

Syntax
 XML

 <SelectionSets>
   <SelectionSet>...</SelectionSet>
 </SelectionSets>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
SelectionSets element. Each child element defines a set of objects that can be referenced by

the name of the set. The order of the child elements is not significant.

Attributes
None.

Child Elements

                                                                                         ﾉ   Expand table

 Element                Description

 SelectionSet Element   Required element.

                        Defines a single set of .NET objects that can be referenced by the name of the set.

<!-- p.2448 -->

Parent Elements

                                                                                         ﾉ   Expand table

 Element                        Description

 Configuration Element          Represents the top-level element of a formatting file.

Remarks
You can use selection sets when you have a set of related objects that you want to reference by
using a single name, such as a set of objects that are related through inheritance. When
defining your views, you can specify the set of objects by using the name of the selection set
instead of listing all the objects within each view.

Common selection sets are specified by their name when defining the views of the formatting
file or the definitions of the views. In these cases, the SelectionSetName child element of the
ViewSelectedBy and EntrySelectedBy elements specifies the set to be used. For more

information about selection sets, see Defining Sets of Objects.

See Also
Configuration Element

Defining Selection Sets

SelectionSet Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2449 -->

SelectionSet Element
Defines a set of .NET objects that can be referenced by the name of the set.

Schema
     Configuration Element
     SelectionSets Element
     SelectionSet Element

Syntax
 XML

 <SelectionSet>
   <Name>SelectionSetName</Name>
   <Types>...</Types>
 </SelectionSet>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
SelectionSet element. Each selection set must have a name, and it must specify the .NET

objects of the set.

Attributes
None.

Child Elements

                                                                                    ﾉ   Expand table

 Element                            Description

 Name Element for SelectionSet      Required element.

                                    Specifies the name used to reference the selection set.

 Types Element                      Required element.

<!-- p.2450 -->

 Element                                Description

                                        Defines the .NET objects that are in the selection set.

Parent Elements

                                                                                          ﾉ   Expand table

 Element                    Description

 SelectionSets Element      Defines the common sets of .NET objects that can be used by all views of the
 Format                     formatting file.

Remarks
You can use selection sets when you have a set of related objects that you want to reference by
using a single name, such as a set of objects that are related through inheritance. When
defining your views, you can specify the set of objects by using the name of the selection set
instead of listing all the objects within each view.

Common selection sets are specified by their name when defining the views of the formatting
file or the definitions of the views. In these cases, the SelectionSetName child element of the
ViewSelectedBy and EntrySelectedBy elements specifies the set to be used. For more

information about selection sets, see Defining Sets of Objects.

Example
The following example shows a SelectionSet element that defines four .NET types.

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

<!-- p.2451 -->

See Also
Defining Selection Sets

Name Element of SelectionSet

SelectionSets Element

Types Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2452 -->

Name Element for SelectionSet
Specifies the name used to reference the selection set.

Schema
     Configuration Element
     SelectionSets Element
     SelectionSet Element
     Name Element

Syntax
 XML

 <Name>Name of selection set</Name>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the Name
Element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                Description

 SelectionSet Element   Defines a single set of .NET objects that can be referenced by the name of the set.

<!-- p.2453 -->

Text Value
Specify the name to reference the selection set. There are no restrictions as to what characters
can be used.

Remarks
The name specified here is used in the SelectionSetName element. The selection set that can be
used by a view, by a definition of a view (views can have multiple definitions), or when
specifying a selection condition. For more information about selection sets, see Defining Sets
of Objects.

Example
This example shows a SelectionSet element that defines four .NET types. The name of the
selection set is "FileSystemTypes".

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

See Also
Defining Selection Sets

SelectionSet Element

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2454 -->

Types Element for SelectionSet
Defines the .NET objects that are in the selection set.

Schema
     Configuration Element
     SelectionSets Element
     SelectionSet Element
     Types Element

Syntax
 XML

 <Types>
   <TypeName>Nameof.NetType</TypeName>
 </Types>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
Types element. There must be at least one child element, but there is no maximum limit to the

number of child elements that can be added.

Attributes
None.

Child Elements

                                                                                        ﾉ   Expand table

 Element                           Description

 TypeName Element of Types         Required element.

                                   Specifies the .NET object that belongs to the selection set.

<!-- p.2455 -->

Parent Elements

                                                                                             ﾉ   Expand table

 Element                      Description

 SelectionSet Element         Defines a set of .NET objects that can be referenced by the name of the set.

Remarks
The objects defined by this element make up a selection set that can be used by a view, by a
definition of a view (views can have multiple definitions), or when specifying a selection
condition. For more information about selection sets, see Defining Sets of Objects.

Example
This example shows a SelectionSet element that defines four .NET types.

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

See Also
Defining Sets of Objects

SelectionSet Element

TypeName Element of Types

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2456 -->

TypeName Element for Types
Specifies the .NET type of an object that belongs to the selection set.

Schema
     Configuration Element
     SelectionSets Element
     SelectionSet Element
     Types Element
     TypeName Element

Syntax
 XML

 <TypeName>Nameof.NetType</Name>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
TypeName element. At least one TypeName element must be included in the selection set.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                  ﾉ   Expand table

 Element                Description

 Types Element          Defines the .NET objects that are in the selection set.

<!-- p.2457 -->

Text Value
Specify the fully qualified name for the .NET type.

Remarks
You can use selection sets when you have a set of related objects that you want to reference by
using a single name, such as a set of objects that are related through inheritance. When
defining your views, you can specify the set of objects by using the name of the selection set
instead of listing all the objects within each view.

Common selection sets are specified by their name when defining the views of the formatting
file. In these cases, the SelectionSetName child element of the ViewSelectedBy element for the
view specifies the set. However, different entries of a view can also specify a selection set that
applies to only that entry of the view. For more information about selection sets, see Defining
Sets of Objects.

Example
The following example shows a SelectionSet element that defines four .NET types.

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

See Also
Defining Selection Sets

SelectionSet Element

SelectionSets Element

<!-- p.2458 -->

Types Element

Writing a Windows PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2459 -->

ViewDefinitions Element
Defines the views used to display .NET objects. These views can display the properties and
script values of an object in a table format, list format, wide format, and custom control format.

Schema
     Configuration Element
     ViewDefinitions

Syntax
 XML

 <ViewDefinitions>
   <View>...</View>
 </ViewDefinitions>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
ViewDefinitions element. There is no limit to the number of views that can be defined in a

formatting file, and they can be added in any order.

Attributes
None.

Child Elements

                                                                                       ﾉ   Expand table

 Element            Description

 View Element       Defines a view that is used to display one or more .NET objects.

Parent Elements

<!-- p.2460 -->

                                                                                       ﾉ   Expand table

 Element                      Description

 Configuration Element        Represents the top-level element of a formatting file.

Remarks
For more information about the components of the different types of views, see the following
topics:

     Creating a Table View

     Creating a List View

     Creating a Wide View

     Custom Controls

Example
This example shows a ViewDefinitions element that contains the parent elements for a table
view and a list view.

 XML

 <Configuration>
   <ViewDefinitions>
     <View>
       <TableControl>...</TableControl>
     </View>
     <View>
       <ListControl>...</ListControl>
     </View>
   </ViewDefinitions>
 </Configuration>

See Also
Configuration Element

View Element

Creating a Table View

<!-- p.2461 -->

Creating a List View

Creating a Wide View

Custom Controls

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2462 -->

View Element
Defines a view that displays one or more .NET objects. There is no limit to the number of views
that can be defined in a formatting file.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element

Syntax
 XML

 <View>
   <Name>Friendly name of view.</Name>
   <OutOfBand />
   <ViewSelectedBy>...</ViewSelectedBy>
   <Controls>...</Controls>
   <GroupBy>...</GroupBy>
   <TableControl>...</TableControl>
   <ListControl>...</ListControl>
   <WideControl>...</WideControl>
   <CustomControl>...</CustomControl>
 </View>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
View element. You must specify one and only one of the control child elements, and you must

specify the name of the view and the objects that use the view. Defining custom controls, how
to group objects, and specifying if the view is out-of-band are optional.

Attributes
None.

Child Elements

<!-- p.2463 -->

                                                                                      ﾉ   Expand table

Element                     Description

Controls Element for View   Optional element.

                            Defines a set of controls that can be referenced by their name from within
                            the view.

CustomControl Element       Optional element.

                            Defines a custom control format for the view.

GroupBy Element for View    Optional element.

                            Defines how the members of the .NET objects are grouped.

ListControl Element         Optional element.

                            Defines a list format for the view.

Name Element for View       Required element.

                            Specifies the name used to reference the view.

OutOfBand                   Optional element

                            When OutOfBand is true, the view applies regardless of previous objects
                            that may have selected a different view.

TableControl Element        Optional element.

                            Defines a table format for the view.

ViewSelectedBy Element      Required element.
for View
                            Defines the .NET objects that this view displays.

WideControl Element         Optional element.

                            Defines a wide (single value) list format for the view.

Parent Elements

                                                                                      ﾉ   Expand table

Element                                 Description

ViewDefinitions Element                 Defines the views used to display objects.

<!-- p.2464 -->

Remarks
For more information about the components of different views and custom controls, see the
following topics:

     Table View Components

     List View Components

     Wide View Components

     Custom Controls

Example
This example shows a View element that defines a table view for the
System.ServiceProcess.ServiceController object.

 XML

 <ViewDefinitions>
   <View>
     <Name>service</Name>
     <ViewSelectedBy>
       <TypeName>System.ServiceProcess.ServiceController</TypeName>
     </ViewSelectedBy>
     <TableControl>...</TableControl>
   </View>
 </ViewDefinitions>

See Also
ViewDefinitions Element

Name Element for View

ViewSelectedBy Element

Controls Element for View

GroupBy Element for View

TableControl Element

<!-- p.2465 -->

ListControl Element

WideControl Element

CustomControl Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2466 -->

Controls Element for View
Defines the view controls that can be used by a specific view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element

Syntax
 XML

 <Controls>
   <Control>...</Control>
 </Controls>

Attributes and Elements
The following sections describe the attributes, child elements, and parent elements of the
Controls element. This element must have at least one child element. There is no maximum

number of child elements, nor is their order significant.

Attributes
None.

Child Elements

                                                                                    ﾉ   Expand table

 Element                                     Description

 Control Element for Controls for View       Defines a control that can be used by the view.

Parent Elements

<!-- p.2467 -->

                                                                                       ﾉ   Expand table

 Element          Description

 View Element     Defines a view that is used to display the members of one or more .NET objects.

Remarks
See Also
Control Element

View Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2468 -->

Control Element for Controls for View
Defines a control that can be used by the view and the name that is used to reference the
control.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element

Syntax
 XML

 <Control>
   <Name>NameOfControl</Name>
   <CustomControl>...</CustomControl>
 </Control>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
Control element.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                                                  Description

 Name Element for Control for View                        Required element.

<!-- p.2469 -->

 Element                                                        Description

                                                                Specifies the name of the control.

 CustomControl Element for Control for Controls for View        Required element.

                                                                Defines the control used by this view.

Parent Elements

                                                                                          ﾉ   Expand table

 Element                 Description

 Controls Element        Defines the view controls that can be used by a specific view.

Remarks
This control can be specified by the following elements:

     CustomControlName Element for ExpressionBinding for Controls for View

     CustomControlName Element for ExpressionBinding for CustomControl for View

     CustomControlName Element for ExpressionBinding for GroupBy

     CustomControlName Element for GroupBy

See Also
CustomControl Element for Control for Controls for View

CustomControlName Element for ExpressionBinding for Controls for View

CustomControlName Element for ExpressionBinding for CustomControl for View

CustomControlName Element for ExpressionBinding for GroupBy

CustomControlName Element for ExpressionBinding for GroupBy

Controls Element

Name Element for Control for Controls for View

Writing a PowerShell Formatting File

<!-- p.2470 -->

Last updated on 05/20/2025

<!-- p.2471 -->

CustomControl Element for Control for
Controls for View
Defines a control that is used by the view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element
     CustomControl Element

Syntax
 XML

 <CustomControl>
   <CustomEntries>...</CustomEntries>
 </CustomControl>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomControl element. You must specify only one child element.

Attributes
None.

Child Elements

                                                                                     ﾉ   Expand table

 Element                                                         Description

 CustomEntries Element for CustomControl for Controls for View   Required element.

<!-- p.2472 -->

 Element                                                          Description

                                                                  Provides the definitions for the control.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                        Description

 Control Element for Controls   Defines a control that can be used by the view and the name that is used
 for View                       to reference the control.

Remarks
See Also
CustomEntries Element for CustomControl for View

Control Element for Controls for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2473 -->

CustomEntries Element for CustomControl
for Controls for View
Provides the definitions for the control. This element is used when defining controls that can
be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element

Syntax
 XML

 <CustomEntries>
   <CustomEntry>...</CustomEntry>
 </CustomEntries>

Attributes and Elements
The following sections describe attributes, child elements, and parent elements of the
CustomEntries element. There is no maximum limit to the number of child elements that can

be specified.

Attributes
None.

Child Elements

                                                                                ﾉ   Expand table

<!-- p.2474 -->

 Element                                                          Description

 CustomEntry Element for CustomEntries for Controls for View      Required element.

                                                                  Provides a definition of the control.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                                       Description

 CustomControl Element for Control for Controls for View       Defines the control used by the view.

Remarks
In most cases, a control has only one definition, which is specified in a single CustomEntry
element. However, it is possible to provide multiple definitions if you want to use the same
control to display different .NET objects. In those cases, you can define a CustomEntry element
for each object or set of objects.

See Also
CustomEntry Element for CustomEntries for Controls for View

CustomControl Element for Control for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2475 -->

CustomEntry Element for CustomEntries for
Controls for View
Provides a definition of the control. This element is used when defining controls that can be
used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element

Syntax
 XML

 <CustomEntry>
   <EntrySelectedBy>...</EntrySelectedBy>
   <CustomItem>...</CustomItem>
 </CustomEntry>

Attributes and Elements
The following sections describe attributes, child elements, and the parent elements of the
CustomEntry element.

Attributes
None.

Child Elements

<!-- p.2476 -->

                                                                                        ﾉ   Expand table

 Element                                Description

 EntrySelectedBy Element for            Optional element.
 CustomEntry for Controls for View
                                        Defines the .NET types that use this control definition or the
                                        condition that must exist for this definition to be used.

 CustomItem Element for CustomEntry     Required element.
 for Controls for View
                                        Defines how the control displays the data.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                                    Description

 CustomEntries Element for CustomControl for View           Provides the definitions for the control.

Remarks
See Also
CustomEntries Element for CustomControl for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2477 -->

CustomItem Element for CustomEntry for
Controls for View
Defines what data is displayed by the control and how it is displayed. This element is used
when defining controls that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element

Syntax
 XML

 <CustomItem>
   <ExpressionBinding>...</ExpressionBinding>
   <NewLine/>
   <Text>TextToDisplay</Text>
   <Frame>...<Frame>
 </CustomItem>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomItem element. For more information, see Remarks.

Attributes
None.

<!-- p.2478 -->

Child Elements

                                                                                          ﾉ   Expand table

 Element                                          Description

 ExpressionBinding Element for CustomItem for     Optional element.
 Controls for View
                                                  Defines the data that is displayed by the control.

 Frame Element for CustomItem for Controls for    Optional element.
 View
                                                  Defines how the data is displayed, such as shifting the
                                                  data to the left or right.

 NewLine Element for CustomItem for Controls      Optional element.
 for View
                                                  Adds a blank line to the display of the control.

 Text Element for CustomItem for Controls for     Optional element.
 View
                                                  Adds text, such as parentheses or brackets, to the
                                                  display of the control.

Parent Elements

                                                                                          ﾉ   Expand table

 Element                                                             Description

 CustomEntry Element for CustomEntries for Controls for View         Provides a definition of the control.

Remarks
When specifying the child elements of the CustomItem element, keep the following in mind:

     The child elements must be added in the following sequence: ExpressionBinding ,
        NewLine , Text , and Frame .

     There is no maximum limit to the number of sequences that you can specify.
     In each sequence, there is no maximum limit to the number of ExpressionBinding
     elements that you can use.

See Also

<!-- p.2479 -->

ExpressionBinding Element for CustomItem for Controls for View

Frame Element for CustomItem for Controls for View

NewLine Element for CustomItem for Controls for View

Text Element for CustomItem for Controls for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2480 -->

ExpressionBinding Element for CustomItem
for Controls for View
Defines the data that is displayed by the control. This element is used when defining controls
that can be used by a view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     Controls Element
     Control Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element

Syntax
 XML

 <ExpressionBinding>
   <CustomControl>...</CustomControl>
   <CustomControlName>NameofCommonCustomControl</CustomControlName>
   <EnumerateCollection/>
   <ItemSelectionCondition>...</ItemSelectionCondition>
   <PropertyName>Nameof.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate></ScriptBlock>
 </ExpressionBinding>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ExpressionBinding element.

Attributes
