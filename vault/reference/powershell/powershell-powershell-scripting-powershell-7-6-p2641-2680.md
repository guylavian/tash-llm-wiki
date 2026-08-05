---
title: "How to use this documentation — pages 2641-2680"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2641-2680
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2641-2680
family: powershell
documentKind: "doc"
abstract: "PropertyName Element for SelectionCondition for GroupBy Specifies the .NET property that triggers the condition. When this property is present or when it evaluates to true , the condition is met, and the definition is used. This element is used when defining how a new group of o"
---

# How to use this documentation — pages 2641-2680

<!-- p.2641 -->

PropertyName Element for
SelectionCondition for GroupBy
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the definition is used. This element is used when
defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

Child Elements

<!-- p.2642 -->

None.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines a condition that must exist for the control
 for GroupBy                                      definition to be used.

Text Value
Specify the .NET property name.

Remarks
The selection condition must specify a least one property name or a script, but cannot specify
both. For more information about how selection conditions can be used, see Defining
Conditions for Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for GroupBy

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2643 -->

ScriptBlock Element for SelectionCondition
for EntrySelectedBy for GroupBy
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the definition is used. This element is used when defining how a new
group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

Child Elements

<!-- p.2644 -->

None.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines a condition that must exist for the control
 for GroupBy                                      definition to be used.

Text Value
Specify the script that is evaluated.

Remarks
The selection condition must specify a least one script or property name to evaluate, but
cannot specify both. For more information about how selection conditions can be used, see
Defining Conditions for Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2645 -->

SelectionSetName Element for
SelectionCondition for GroupBy
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met, and the object is displayed by using this control. This element is
used when defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None.

Child Elements

<!-- p.2646 -->

None.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines a condition that must exist for the control
 for GroupBy                                      definition to be used.

Text Value
Specify the name of the selection set.

Remarks
Selection sets are common groups of .NET objects that can be used by any view that the
formatting file defines. For more information about creating and referencing selection sets, see
Defining Selection Sets.

When this element is specified, you cannot specify the TypeName element. For more
information about defining selection conditions, see Defining Conditions for Displaying Data.

See Also
TypeName Element for SelectionCondition for GroupBy

SelectionCondition Element for EntrySelectedBy for GroupBy

Defining Conditions for When Data Is Displayed

Defining Selection Sets

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2647 -->

TypeName Element for SelectionCondition
for GroupBy
Specifies a .NET type that triggers the condition. This element is used when defining how a new
group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     TypeName Element

Syntax
 XML

 <TypeName>Nameof.NetType</TypeName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
TypeName Element.

Attributes
None.

Child Elements

<!-- p.2648 -->

None.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines a condition that must exist for the control
 for GroupBy                                      definition to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
When this element is specified, you cannot specify the SelectionSetName element. For more
information about defining selection conditions, see Defining Conditions for Displaying Data.

See Also
SelectionCondition Element for EntrySelectedBy for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2649 -->

SelectionSetName Element for
EntrySelectedBy for GroupBy
Specifies a set of .NET objects for the list entry. There is no limit to the number of selection sets
that can be specified for an entry. This element is used when defining how a new group of
objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None.

Child Elements
None.

<!-- p.2650 -->

Parent Elements

                                                                                        ﾉ     Expand table

 Element                               Description

 EntrySelectedBy Element for           Defines the .NET types that use this custom entry or the
 CustomEntry for GroupBy               condition that must exist for this entry to be used.

Text Value
Specify the name of the selection set.

Remarks
Each custom control definition must have at least one type name, selection set, or selection
condition defined.

Selection sets are typically used when you want to define a group of objects that are used in
multiple views. For example, you may want to create a table view and a list view for the same
set of objects. For more information about defining selection sets, see Defining Selection Sets.

For more information about the components of a custom control view, see Creating Custom
Controls.

See Also
EntrySelectedBy Element for CustomEntry for GroupBy

Creating Custom Controls

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2651 -->

TypeName Element for EntrySelectedBy for
GroupBy
Specifies a .NET type that uses this definition of the custom control. This element is used when
defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element
     TypeName Element

Syntax
 XML

 <TypeName>Nameof.NetType</TypeName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
TypeName element.

Attributes
None.

Child Elements
None.

<!-- p.2652 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                            Description

 EntrySelectedBy Element for        Defines the .NET types that use this control definition or the
 CustomEntry for GroupBy            condition that must exist for this definition to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
Each control definition must have at least one type name, selection set, or selection condition
defined.

For more information about the components of a custom control view, see Creating Custom
Controls.

See Also
Creating Custom Controls

EntrySelectedBy Element for CustomEntry for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2653 -->

CustomControlName Element for GroupBy
Specifies the name of a custom control that is used to display the new group. This element is
used when defining a table, list, wide or custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControlName Element

Syntax
 XML

 <CustomControlName>ControlName</CustomControlName>

Attributes and Elements
The following sections describe the attributes, child elements, and parent elements of the
CustomControlName element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                               ﾉ   Expand table

<!-- p.2654 -->

 Element                      Description

 GroupBy Element for View     Defines how Windows PowerShell displays a new group of objects.

Text Value
Specify the name of the custom control that is used to display a new group.

Remarks
You can create common controls that can be used by all the views of a formatting file, and you
can create view controls that can be used by a specific view. The following elements specify the
names of these custom controls:

      Name Element for Control for Controls for Configuration

      Name Element for Control for Controls for View

See Also
GroupBy Element for View

Name Element for Control for Controls for Configuration

Name Element for Control for Controls for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2655 -->

Label Element for GroupBy
Specifies a label that is displayed when a new group is encountered.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     Label Element

Syntax
 XML

 <Label>DisplayedLabel</Label>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the Label
element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                      ﾉ   Expand table

 Element                           Description

 GroupBy Element for View          Defines how a new group of objects is displayed.

<!-- p.2656 -->

Text Value
Specify the text that is displayed whenever Windows PowerShell encounters a new property or
script value.

Remarks
In addition to the text specified by this element, Windows PowerShell displays the new value
that starts the group, and adds a blank line before and after the group.

Example
The following example shows the label for a new group. The displayed label would look similar
to this: Service Type: NewValueofProperty

  XML

  <GroupBy>
    <Label>Service Type</Label>
    <PropertyName>ServiceType</PropertyName>
  </GroupBy>

For an example of a complete formatting file that includes this element, see Wide View
(GroupBy).

See Also
GroupBy Element for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2657 -->

PropertyName Element for GroupBy
Specifies the .NET property that starts a new group whenever its value changes.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                           Description

 GroupBy Element for View          Defines how a group of .NET objects is displayed.

<!-- p.2658 -->

Text Value
Specify the .NET property name.

Remarks
Windows PowerShell starts a new group whenever the value of this property changes.

When this element is specified, you cannot specify the ScriptBlock element to start a new
group.

Example
The following example shows how to start a new group when the value of a property changes.

 XML

 <GroupBy>
   <Label>Service Type</Label>
   <PropertyName>ServiceType</PropertyName>
 </GroupBy>

For an example of a complete formatting file that includes this element, see Wide View
(GroupBy).

See Also
GroupBy Element for View

ScriptBlock Element for GroupBy

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2659 -->

ScriptBlock Element for GroupBy
Specifies the script that starts a new group whenever its value changes.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                           Description

 GroupBy Element for View          Defines how a group of .NET objects is displayed.

<!-- p.2660 -->

Text Value
Specify the script that is evaluated.

Remarks
PowerShell starts a new group whenever the value of this script changes.

When this element is specified, you cannot specify the PropertyName element to start a new
group.

See Also
PropertyName Element for GroupBy

GroupBy Element for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2661 -->

ListControl Element
Defines a list format for the view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element

Syntax
 XML

 <ListControl>
   <ListEntries>...</ListEntries>
 </ListControl>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
ListControl element. This element must contain only a single child element.

Attributes
None.

Child Elements

                                                                                   ﾉ   Expand table

 Element                              Description

 ListEntries Element                  Required element.

                                      Provides the definitions of the list view.

Parent Elements

<!-- p.2662 -->

                                                                                        ﾉ   Expand table

 Element            Description

 View Element       Defines a view that is used to display the members of one or more objects.

Remarks
For more information about creating a list view, see Creating a List View.

Example
This example shows a list view for the System.ServiceProcess.ServiceController object.

  <View>
    <Name>System.ServiceProcess.ServiceController</Name>
    <ViewSelectedBy>
      <TypeName>System.ServiceProcess.ServiceController</TypeName>
    </ViewSelectedBy>
    <ListControl>
      <ListEntries>
         <ListEntry>...</ListEntry>
      </ListEntries>
    </ListControl>
  </View>

See Also
View Element

ListEntries Element

Creating a List View

Writing a Windows PowerShell Formatting and Types File

 Last updated on 05/20/2025

<!-- p.2663 -->

ListEntries Element
Provides the definitions of the list view. The list view must specify one or more definitions.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element

Syntax
 XML

 <ListEntries>
   <ListEntry>...</ListEntry>
 </ListEntries>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
ListEntries element. At least one child element must be specified.

Attributes
None.

Child Elements

                                                                                  ﾉ   Expand table

 Element                           Description

 ListEntry Element                 Provides a definition of the list view.

Parent Elements

<!-- p.2664 -->

                                                                            ﾉ   Expand table

 Element                              Description

 ListControl Element                  Defines a list format for the view.

Remarks
For more information about list views, see List View.

Example
This example shows the XML elements that define the list view for the
System.ServiceProcess.ServiceController object.

  XML

  <View>
    <Name>System.ServiceProcess.ServiceController</Name>
    <ViewSelectedBy>
      <TypeName>System.ServiceProcess.ServiceController</TypeName>
    </ViewSelectedBy>
    <ListControl>
      <ListEntries>
        <ListEntry>
          <ListItems>...</ListItems>
        </ListEntry>
      </ListEntries>
    </ListControl>
  </View>

See Also
ListControl Element

ListEntry Element

List View

Writing a Windows PowerShell Formatting and Types File

 Last updated on 05/20/2025

<!-- p.2665 -->

ListEntry Element
Provides a definition of the list view.

      Configuration Element
      ViewDefinitions Element
      View Element
      ListControl Element
      ListEntries Element
      ListEntry Element

Syntax
 XML

 <ListEntry>
   <EntrySelectedBy>...</EntrySelectedBy>
   <ListItems>...</ListItems>
 </ListEntry>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
ListEntry element.

Attributes
None.

Child Elements

                                                                                          ﾉ    Expand table

 Element                       Description

 EntrySelectedBy Element for   Optional element.
 ListEntry
                               Defines the .NET objects that use this list view definition or the condition
                               that must exist for this definition to be used.

<!-- p.2666 -->

 Element                      Description

 ListItems Element            Required element.

                              Defines the properties and scripts whose values are displayed by the list
                              view.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                           Description

 ListEntries Element               Provides the definitions of the list view.

Remarks
A list view is a list format that displays property values or script values for each object. For
more information about list views, see Creating a List View.

Example
This example shows the XML elements that define the list view for the
System.ServiceProcess.ServiceController object.

 XML

 <View>
   <Name>System.ServiceProcess.ServiceController</Name>
   <ViewSelectedBy>
     <TypeName>System.ServiceProcess.ServiceController</TypeName>
   </ViewSelectedBy>
   <ListControl>
     <ListEntries>
       <ListEntry>
         <ListItems>...</ListItems>
       </ListEntry>
     </ListEntries>
   </ListControl>
 </View>

See Also
Creating a List View

<!-- p.2667 -->

EntrySelectedBy Element for ListEntry

ListEntries Element

ListItems Element

Writing a Windows PowerShell Formatting and Types File

 Last updated on 05/20/2025

<!-- p.2668 -->

EntrySelectedBy Element for ListEntry
Defines the .NET types that use this list view definition or the condition that must exist for this
definition to be used. In most cases only one definition is needed for a list view. However, you
can provide multiple definitions for the list view if you want to use the same list view to display
different data for different objects.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     EntrySelectedBy Element

Syntax
 XML

 <EntrySelectedBy>
   <TypeName>Nameof.NetType</TypeName>
   <SelectionSetName>NameofSelectionSet</SelectionSetName>
   <SelectionCondition>...</SelectionCondition>
 </EntrySelectedBy>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
EntrySelectedBy element.

Attributes
None.

Child Elements

<!-- p.2669 -->

                                                                                          ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Optional element.
 for ListControl
                                                  Defines the condition that must exist for this list view
                                                  definition to be used.

 SelectionSetName Element for EntrySelectedBy     Optional element.
 for ListControl
                                                  Specifies a set of .NET types that use this list view
                                                  definition.

 TypeName Element for EntrySelectedBy for         Optional element.
 ListControl
                                                  Specifies a .NET type that uses this list view definition.

Parent Elements

                                                                                          ﾉ   Expand table

 Element                                    Description

 ListEntry Element for ListControl          Defines how the rows of the list are displayed.

Remarks
You must specify at least one type, selection set, or selection condition for a list view definition.
There is no maximum limit to the number of child elements that you can use.

Selection conditions are used to define a condition that must exist for the definition to be
used, such as when an object has a specific property or that a specific property value or script
evaluates to true . For more information about selection conditions, see Defining Conditions
for when Data is displayed.

For more information about the components of a list view, see Creating a List View.

Example
The following example shows how to define the objects for a list view using their .NET type
name.

 XML

<!-- p.2670 -->

  <ListEntry>
    <EntrySelectedBy>
      <TypeName>NameofDotNetType</TypeName>>
    </EntrySelectedBy>
  </ListEntry>

See Also
ListEntry Element for ListControl

SelectionCondition Element for EntrySelectedBy for ListControl

SelectionSetName Element for EntrySelectedBy for ListControl

TypeName Element for EntrySelectedBy for ListControl

Creating a List View

Defining Conditions for when Data is Displayed

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2671 -->

SelectionCondition Element for
EntrySelectedBy for ListControl
Defines the condition that must exist to use this definition of the list view. There is no limit to
the number of selection conditions that can be specified for a list definition.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     EntrySelectedBy Element
     SelectionCondition Element

Syntax
 XML

 <SelectionCondition>
   <TypeName>Nameof.NetType</TypeName>
   <SelectionSetName>NameofSelectionSet</SelectionSetName>
   <PropertyName>.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate</ScriptBlock>
 </SelectionCondition>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionCondition element.

Attributes
None.

Child Elements

<!-- p.2672 -->

                                                                                          ﾉ    Expand table

 Element                                                         Description

 PropertyName Element for SelectionCondition for                 Optional element.
 EntrySelectedBy for ListEntry
                                                                 Specifies the .NET property that triggers
                                                                 the condition.

 ScriptBlock Element for SelectionCondition for                  Optional element.
 EntrySelectedBy for ListEntry
                                                                 Specifies the script that triggers the
                                                                 condition.

 SelectionSetName Element for SelectionCondition for             Optional element.
 EntrySelectedBy for ListEntry
                                                                 Specifies the set of .NET types that
                                                                 trigger the condition.

 TypeName Element for SelectionCondition for                     Optional element.
 EntrySelectedBy for ListEntry
                                                                 Specifies a .NET type that triggers the
                                                                 condition.

Parent Elements

                                                                                          ﾉ    Expand table

 Element                            Description

 EntrySelectedBy Element for        Defines the .NET types that use this table entry or the condition that
 TableRowEntry                      must exist for this entry to be used.

Remarks
lWhen you are defining a selection condition, the following requirements apply:

     The selection condition must specify a least one property name or a script block, but
     cannot specify both.
     The selection condition can specify any number of .NET types or selection sets, but
     cannot specify both.

For more information about how to use selection conditions, see Defining Conditions for when
Data is Displayed.

For more information about other components of a list view, see Creating a List View.

<!-- p.2673 -->

See Also
Creating a List View

Defining Conditions for When Data Is Displayed

ListEntry Element

SelectionSetName Element for EntrySelectedBy for ListEntry

TypeName Element for EntrySelectedBy for ListEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2674 -->

PropertyName Element for
SelectionCondition for EntrySelectedBy for
ListControl
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the list entry is used.

     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

Child Elements
None.

<!-- p.2675 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist for this list
 for ListEntry                                    entry to be used.

Text Value
Specify the .NET property name.

Remarks
The selection condition must specify at least one property name or a script block, but cannot
specify both. For more information about how to use selection conditions, see Defining
Conditions for when a View Entry or Item is Used.

For more information about other components of a list view, see Creating List View.

See Also
Creating a List View

Defining Conditions for When Data is Displayed

ListEntry Element

ScriptBlock Element for SelectionCondition for EntrySelectedBy for ListEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2676 -->

ScriptBlock Element for SelectionCondition
for EntrySelectedBy for ListControl
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the list entry is used.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     ListControl Element
     ListEntries Element
     ListEntry Element
     EntrySelectedBy Element
     SelectionCondition Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

Child Elements
None.

<!-- p.2677 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist for this list
 for ListEntry                                    entry to be used.

Text Value
Specify the script that is evaluated.

Remarks
The selection condition must specify a least one script or property name to evaluate, but
cannot specify both. (For more information about how selection conditions can be used, see
Defining Conditions for when a View Entry or Item is Used.)

For more information about the other components of a list view, see List View.

See Also
ListEntry Element

PropertyName Element for SelectionCondition for EntrySelectedBy for ListEntry

SelectionCondition Element for EntrySelectedBy for ListEntry

List View

Defining Conditions for when a View Entry or Item is Used

Writing a Windows PowerShell Formatting and Types File

 Last updated on 05/20/2025

<!-- p.2678 -->

SelectionSetName Element for
SelectionCondition for EntrySelectedBy for
ListEntry
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met, and the object is displayed by using this definition of the list
view.

Schema
        Configuration Element
        ViewDefinitions Element
        View Element
        ListControl Element
        ListEntries Element
        ListEntry Element
        EntrySelectedBy Element
        SelectionCondition Element
        SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None.

Child Elements

<!-- p.2679 -->

None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist to use this
 for ListEntry                                    definition of the list view.

Text Value
Specify the name of the selection set.

Remarks
The selection condition can specify a selection set or .NET type, but cannot specify both. For
more information about how to use selection conditions, see Defining Conditions for when
Data is Displayed.

Selection sets are common groups of .NET objects that can be used by any view that the
formatting file defines. For more information about creating and referencing selection sets, see
Defining Sets of Objects.

For more information about other components of a list view, see Creating a List View.

See Also
Creating a List View

Defining Conditions for When Data Is Displayed

SelectionCondition Element for EntrySelectedBy for ListEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2680 -->

TypeName Element for SelectionCondition
for EntrySelectedBy for ListControl
Specifies a .NET type that triggers the condition. When this type is present, the list entry is
used.

Schema
        Configuration Element
        ViewDefinitions Element
        View Element
        ListControl Element
        ListEntries Element
        ListEntry Element
        EntrySelectedBy Element
        SelectionCondition Element
        TypeName Element

Syntax
 XML

 <TypeName>Nameof.NetType</TypeName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
TypeName element.

Attributes
None.

Child Elements
None.
