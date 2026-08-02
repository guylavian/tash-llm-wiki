---
title: "How to use this documentation — pages 2561-2600"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2561-2600
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2561-2600
family: powershell
documentKind: "doc"
abstract: "FirstLineHanging Element for Frame for CustomControl Specifies how many characters the first line of data is shifted to the left. This element is used when defining a custom control view. Schema Configuration Element ViewDefinitions Element View Element CustomControl Element Cus"
---

# How to use this documentation — pages 2561-2600

<!-- p.2561 -->

FirstLineHanging Element for Frame for
CustomControl
Specifies how many characters the first line of data is shifted to the left. This element is used
when defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element
     FirstLineHanging Element

Syntax
 XML

 <FirstLineHanging>NumberOfCharactersToShift</FirstLineHanging>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
FirstLineHanging element.

Attributes
None.

Child Elements
None.

<!-- p.2562 -->

Parent Elements

                                                                                     ﾉ   Expand table

 Element                                     Description

 Frame Element for CustomItem for            Defines how the data is displayed, such as shifting the
 CustomControl for View                      data to the left or right.

Text Value
Specify the number of characters that you want to shift the first line of the data.

Remarks
If this element is specified, you cannot specify the FirstLineIndent element.

See Also
FirstLineIndent Element for Frame for CustomControl for View

Frame Element for CustomItem for CustomControl for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2563 -->

FirstLineIndent Element for Frame for
CustomControl for View
Specifies how many characters the first line of data is shifted to the right. This element is used
when defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element
     FirstLineIndent Element

Syntax
 XML

 <FirstLineIndent>NumberOfCharactersToShift</FirstLineIndent>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
FirstLineIndent element.

Attributes
None.

Child Elements
None.

<!-- p.2564 -->

Parent Elements

                                                                                     ﾉ   Expand table

 Element                                     Description

 Frame Element for CustomItem for            Defines how the data is displayed, such as shifting the
 CustomControl for View                      data to the left or right.

Text Value
Specify the number of characters that you want to shift the first line of the data.

Remarks
If this element is specified, you cannot specify the FirstLineHanging element.

See Also
FirstLineHanging Element for Frame for CustomControl for View

Frame Element for CustomItem for CustomControl for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2565 -->

LeftIndent Element for Frame for
CustomControl for View
Specifies how many characters the data is shifted away from the left margin. This element is
used when defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element
     LeftIndent Element

Syntax
 XML

 <LeftIndent>CharactersToShift</LeftIndent>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
LeftIndent element.

Attributes
None.

Child Elements
None.

<!-- p.2566 -->

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                    Description

 Frame Element for CustomItem for           Defines how the data is displayed, such as shifting the
 CustomControl for View                     data to the left or right.

Text Value
Specify the number of characters that you want to shift the data to the left.

Remarks
See Also
Frame Element for CustomItem for CustomControl for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2567 -->

RightIndent Element for Frame for
CustomControl for View
Specifies how many characters the data is shifted away from the right margin. This element is
used when defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element
     RightIndent Element

Syntax
 XML

 <RightIndent>CharactersToShift</RightIndent>

Attributes and Elements
The following sections describe attributes, child elements, and parent element of the
RightIndent element.

Attributes
None.

Child Elements
None.

<!-- p.2568 -->

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                    Description

 Frame Element for CustomItem for           Defines how the data is displayed, such as shifting the
 CustomControl for View                     data to the left or right.

Text Value
Specify the number of characters that you want to shift the data to the right.

Remarks
See Also
Frame Element for CustomItem for CustomControl for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2569 -->

NewLine Element for CustomItem for
CustomControl for View
Adds a blank line to the display of the control. This element is used when defining a custom
control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     NewLine Element

Syntax
 XML

 <NewLine/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
NewLine element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2570 -->

                                                                                ﾉ   Expand table

 Element                                       Description

 CustomItem Element for CustomEntry for View   Defines a control for the custom control view.

Remarks
See Also
CustomItem Element for CustomEntry for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2571 -->

Text Element for CustomItem for
CustomView for View
Specifies text that is added to the data that is displayed by the control, such as a label, brackets
to enclose the data, and spaces to indent the data. This element is used when defining a
custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Text Element

Syntax
 XML

 <Text>TextToDisplay</Text>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the Text
element.

Attributes
None.

Child Elements
None.

<!-- p.2572 -->

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                           Description

 CustomItem Element for CustomEntry for View       Defines a control for the custom control view.

Text Value
Specify the text of a control for data that you want to display.

Remarks
See Also
CustomItem Element for CustomEntry for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2573 -->

EntrySelectedBy Element for CustomEntry
for CustomControl for View
Defines the .NET types that use this custom entry or the condition that must exist for this entry
to be used.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element

Syntax
 XML

 <EntrySelectedBy>
   <TypeName>Nameof.NetType</TypeName>
   <SelectionSetName>NameofSelectionSet</SelectionSetName>
   <SelectionCondition>...</SelectionCondition>
 </EntrySelectedBy>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
EntrySelectedBy element.

Attributes
None.

Child Elements

<!-- p.2574 -->

                                                                                         ﾉ   Expand table

 Element                                            Description

 SelectionCondition Element for EntrySelectedBy     Optional element.
 for CustomEntry
                                                    Defines the condition that must exist for this
                                                    definition to be used.

 SelectionSetName Element for EntrySelectedBy for   Optional element.
 CustomEntry
                                                    Specifies a set of .NET types that use this definition
                                                    of the control view.

 TypeName Element for EntrySelectedBy for           Optional element.
 CustomEntry
                                                    Specifies a .NET type that uses this definition of the
                                                    control view.

Parent Elements

                                                                                         ﾉ   Expand table

 Element                                            Description

 CustomEntry Element for CustomEntries for View     Defines the controls used by specific .NET objects.

Remarks
You must specify at least one type, selection set, or selection condition for an entry. There is no
maximum limit to the number of child elements that you can use.

Selection conditions are used to define a condition that must exist for the entry to be used,
such as when an object has a specific property or when a specific property value or script
evaluates to true . For more information about selection conditions, see Defining Conditions
for when a View Entry or Item is Used.

For more information about the components of a custom control view, see Custom Control
View.

See Also
SelectionCondition Element for EntrySelectedBy for CustomEntry

<!-- p.2575 -->

SelectionSetName Element for EntrySelectedBy for CustomEntry

TypeName Element for EntrySelectedBy for CustomEntry

CustomEntry Element for CustomEntries for View

Custom Control View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2576 -->

SelectionCondition Element for
EntrySelectedBy for CustomControl
Defines a condition that must exist for a control definition to be used. This element is used
when defining a custom control view.

     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
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

<!-- p.2577 -->

                                                                                           ﾉ   Expand table

 Element                                                        Description

 PropertyName Element for SelectionCondition for                Optional element.
 CustomControl for View
                                                                Specifies a .NET property that triggers the
                                                                condition.

 ScriptBlock Element for SelectionCondition for                 Optional element.
 CustomControl for View
                                                                Specifies the script that triggers the
                                                                condition.

 SelectionSetName Element for SelectionCondition for            Optional element.
 Custom Control for View
                                                                Specifies the set of .NET types that triggers
                                                                the condition.

 TypeName Element for SelectionCondition for                    Optional element.
 CustomControl for View
                                                                Specifies a .NET type that triggers the
                                                                condition.

Parent Elements

                                                                                           ﾉ   Expand table

 Element                                     Description

 EntrySelectedBy Element for CustomEntry     Defines the .NET types that use this control definition or the
 for CustomControl for View                  condition that must exist for this definition to be used.

Remarks
When you are defining a selection condition, the following requirements apply:

     The selection condition must specify a least one property name or a script block, but
     cannot specify both.
     The selection condition can specify any number of .NET types or selection sets, but
     cannot specify both.

For more information about how to use selection conditions, see Defining Conditions for when
Data is Displayed.

<!-- p.2578 -->

See Also
PropertyName Element for SelectionCondition for CustomControl for View

ScriptBlock Element for SelectionCondition for CustomControl for View

SelectionSetName Element for SelectionCondition for Custom Control for View

TypeName Element for SelectionCondition for CustomControl for View

EntrySelectedBy Element for CustomEntry for CustomControl for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2579 -->

PropertyName Element for
SelectionCondition for EntrySelectedBy for
EnumerableExpansion
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the definition is used.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansion Element
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

<!-- p.2580 -->

Parent Elements

                                                                                           ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist to expand the
 for EnumerableExpansion                          collection objects of this definition.

Text Value
Specify the .NET property name.

Remarks
The selection condition must specify at least one property name or a script to evaluate, but
cannot specify both. For more information about how to use selection conditions, see Defining
Conditions for when Data is Displayed.

See Also
Defining Conditions for When Data is Displayed

ScriptBlock Element for SelectionCondition for EntrySelectedBy for EnumerableExpansion

SelectionCondition Element for EntrySelectedBy for EnumerableExpansion

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2581 -->

ScriptBlock Element for SelectionCondition
for EntrySelectedBy for
EnumerableExpansion
Specifies the script that triggers the condition.

Schema
     Configuration Element
     DefaultSettings Element
     EnumerableExpansions Element
     EnumerableExpansion Element
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

Parent Elements

<!-- p.2582 -->

                                                                                     ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist to expand the
 for EnumerableExpansion                          collection objects of this definition.

Text Value
Specify the script that is evaluated.

Remarks
The selection condition must specify at least one script or property name to evaluate, but
cannot specify both. For more information about how to use selection conditions, see Defining
Conditions for when Data is Displayed.

See Also
Defining Conditions for When Data Is Displayed

PropertyName Element for SelectionCondition for EntrySelectedBy for EnumerableExpansion

SelectionCondition Element for EntrySelectedBy for EnumerableExpansion

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2583 -->

SelectionSetName Element for
SelectionCondition for CustomControl for
View
Specifies the set of .NET types that trigger the condition. When any of the types in this set are
present, the condition is met and the object is displayed using this control. This element is used
when defining a custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     EntrySelectedBy Element

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

<!-- p.2584 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the
 CustomControl for View                               control definition to be used.

Text Value
Specify the name of the selection set.

Remarks
Selection sets are common groups of .NET objects that can be used by any view that the
formatting file defines. For more information about creating and referencing selection sets, see
Defining Sets of Objects.

The selection condition can specify a selection set or .NET type, but cannot specify both. For
more information about how to use selection conditions, see Defining Conditions for when
Data is Displayed.

See Also
SelectionCondition Element for EntrySelectedBy for CustomControl for View

Defining Conditions for When Data Is Displayed

Defining Selection Sets

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2585 -->

TypeName Element for SelectionCondition
for CustomControl for View
Specifies a .NET type that triggers the condition. This element is used when defining a custom
control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
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
None.

<!-- p.2586 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                              Description

 SelectionCondition Element for EntrySelectedBy for   Defines a condition that must exist for the
 CustomControl for View                               control definition to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
See Also
SelectionCondition Element for EntrySelectedBy for CustomControl for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2587 -->

SelectionSetName Element for
EntrySelectedBy for CustomControl for
View
Specifies a set of .NET objects for the list entry. There is no limit to the number of selection sets
that can be specified for an entry.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

<!-- p.2588 -->

Parent Elements

                                                                                    ﾉ   Expand table

 Element                           Description

 EntrySelectedBy Element for       Defines the .NET types that use this custom entry or the condition
 CustomEntry for View              that must exist for this entry to be used.

Text Value
Specify the name of the selection set.

Remarks
Each custom control entry must have at least one type name, selection set, or selection
condition defined.

Selection sets are typically used when you want to define a group of objects that are used in
multiple views. For example, you might want to create a table view and a list view for the same
set of objects. For more information about defining selection sets, see Defining Selection Sets.

For more information about the components of a custom control view, see Creating Custom
Controls.

See Also
EntrySelectedBy Element for CustomEntry for View

Custom Control View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2589 -->

TypeName Element for EntrySelectedBy for
CustomEntry for View
Specifies a .NET type that uses this definition of the custom control view. There is no limit to
the number of types that can be specified for a definition.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
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

Parent Elements

<!-- p.2590 -->

                                                                                      ﾉ   Expand table

 Element                         Description

 EntrySelectedBy Element for     Defines the .NET types that use this custom control view definition or
 CustomEntry for View            the condition that must exist for this definition to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
Each custom control view definition must have at least one type name, selection set, or
selection condition defined.

For more information about the components of a custom control view, see Creating Custom
Controls.

See Also
Creating Custom Controls

EntrySelectedBy Element for CustomEntry for View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2591 -->

GroupBy Element for View
Defines how a new group of objects is displayed. This element is used when defining a table,
list, wide, or custom control view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element

Syntax
 XML

 <GroupBy>
   <PropertyName>.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate</ScriptBlock>
   <Label>TextToDisplay</Label>
   <CustomControl>...</CustomControl>
   <CustomControlName>NameOfControl</CustomControlName>
 </GroupBy>

Attributes and Elements
The following sections describe attributes, child elements, and parent elements.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

 Element                              Description

 CustomControl Element for GroupBy    Optional element.

<!-- p.2592 -->

 Element                               Description

                                       Defines the custom control that display new groups.

 CustomControlName Element for         Optional element.
 GroupBy
                                       Specifies the name of a control that is used to display the new
                                       group.

 Label Element for GroupBy             Optional element.

                                       Specifies a label that is displayed when a new group is
                                       encountered.

 PropertyName Element for GroupBy      Optional element.

                                       Specifies the .NET property the starts a new group whenever its
                                       value changes.

 ScriptBlock Element for GroupBy       Optional element.

                                       Specifies the script that starts a new group whenever its value
                                       changes.

Parent Elements

                                                                                       ﾉ   Expand table

 Element               Description

 View Element          Defines a view that displays one or more .NET objects.

Remarks
When defining how a new group of objects is displayed, you must specify the property or
script that will start the new group; however, you cannot specify both.

See Also
CustomControlName Element for GroupBy

Label Element for GroupBy

PropertyName Element for GroupBy

ScriptBlock Element for GroupBy

<!-- p.2593 -->

View Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2594 -->

CustomControl Element for GroupBy
Defines the custom control that displays the new group.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element

Syntax
 XML

 <CustomControl>
   <CustomEntries>...</CustomEntries>
 <CustomControl>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
CustomControl element. You can specify any number of child elements and list them in any

order.

Attributes
None.

Child Elements

                                                                                    ﾉ   Expand table

 Element                                                  Description

 CustomEntries Element for CustomControl for GroupBy      Required element.

                                                          Provides the definitions for the control.

<!-- p.2595 -->

Parent Elements

                                                                                  ﾉ   Expand table

 Element                     Description

 GroupBy Element for View    Defines how Windows PowerShell displays a new group of objects.

Remarks

See Also
CustomEntries Element for CustomControl for GroupBy

GroupBy Element for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2596 -->

CustomEntries Element for CustomControl
for GroupBy
Provides the definitions for the control. This element is used when defining how a new group
of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
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

<!-- p.2597 -->

 Element                                                    Description

 CustomEntry Element for CustomControl for GroupBy          Required element.

                                                            Provides a definition of the control.

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                Description

 CustomControl Element for GroupBy      Defines the custom control that displays the new group.

Remarks
In most cases, a control has only one definition, which is specified in a single CustomEntry
element. However, it is possible to provide multiple definitions if you want to use the same
control to display different groups. In those cases, you can define a CustomEntry element for a
group.

See Also
CustomEntry Element for CustomEntries for Controls for View

CustomControl Element for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2598 -->

CustomEntry Element for CustomControl
for GroupBy
Provides a definition of the control. This element is used when defining how a new group of
objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
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

                                                                               ﾉ   Expand table

<!-- p.2599 -->

 Element                             Description

 EntrySelectedBy Element for         Optional element.
 CustomEntry for GroupBy
                                     Defines the .NET types that use this control definition or the
                                     condition that must exist for this definition to be used.

 CustomItem Element for              Required element.
 CustomEntry for GroupBy
                                     Defines how the control displays the data.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                                     Description

 CustomEntries Element for CustomControl for GroupBy         Provides the definitions for the control.

Remarks

See Also
EntrySelectedBy Element for CustomEntry for GroupBy

CustomItem Element for CustomEntry for GroupBy

CustomEntries Element for CustomControl for GroupBy

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2600 -->

CustomItem Element for CustomEntry for
GroupBy
Defines what data is displayed by the custom control view and how it is displayed. This element
is used when defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomItem Element

Syntax
 XML

 <CustomItem>
   <ExpressionBinding>...</ExpressionBinding>
   <Frame>...</Frame>
   <NewLine/>
   <Text>TextToDisplay</Text>
 </CustomItem>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomItem element.

Attributes
None.

Child Elements
