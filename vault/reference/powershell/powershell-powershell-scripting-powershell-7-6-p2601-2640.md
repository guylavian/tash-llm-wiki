---
title: "How to use this documentation — pages 2601-2640"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2601-2640
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2601-2640
family: powershell
documentKind: "doc"
abstract: "ﾉ Expand table Element Description ExpressionBinding Element for CustomItem Optional element. for GroupBy Defines the data that is displayed by the control. Frame Element for CustomItem for Optional element. GroupBy Defines what data is displayed by the custom control view and h"
---

# How to use this documentation — pages 2601-2640

<!-- p.2601 -->

                                                                                       ﾉ   Expand table

 Element                                    Description

 ExpressionBinding Element for CustomItem   Optional element.
 for GroupBy
                                            Defines the data that is displayed by the control.

 Frame Element for CustomItem for           Optional element.
 GroupBy
                                            Defines what data is displayed by the custom control view
                                            and how it is displayed.

 NewLine Element for CustomItem for         Optional element.
 GroupBy
                                            Adds a blank line to the display of the control.

 Text Element for CustomItem for GroupBy    Optional element.

                                            Specifies additional text to the data displayed by the
                                            control.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                              Description

 CustomEntry Element for CustomControl for GroupBy    Provides a definition of the custom control view.

Remarks
See Also
CustomEntry Element for CustomControl for GroupBy

ExpressionBinding Element for CustomItem for GroupBy

Frame Element for CustomItem for GroupBy

NewLine Element for CustomItem for GroupBy

Text Element for CustomItem for GroupBy

Writing a PowerShell Formatting File

<!-- p.2602 -->

Last updated on 05/20/2025

<!-- p.2603 -->

ExpressionBinding Element for CustomItem
for GroupBy
Defines the data that is displayed by the control. This element is used when defining how a
new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
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

<!-- p.2604 -->

None.

Child Elements

                                                                                       ﾉ    Expand table

 Element                                                              Description

 CustomControl Element                                                Optional element.

                                                                      Defines a control that is used by
                                                                      this control.

 CustomControlName Element for ExpressionBinding for GroupBy          Optional element.

                                                                      Specifies the name of a common
                                                                      control or a view control.

 EnumerateCollection Element for ExpressionBinding for                Optional element.
 GroupByEnumerateCollection Element for ExpressionBinding for
 GroupBy                                                              Specified that the elements of
                                                                      collections are displayed.

 ItemSelectionCondition Element for ExpressionBinding for GroupBy     Optional element.

                                                                      Defines the condition that must
                                                                      exist for this control to be used.

 PropertyName Element for ExpressionBinding for GroupBy               Optional element.

                                                                      Specifies the .NET property whose
                                                                      value is displayed by the control.

 ScriptBlock Element for ExpressionBinding for GroupBy                Optional element.

                                                                      Specifies the script whose value is
                                                                      displayed by the control.

Parent Elements

                                                                                       ﾉ    Expand table

 Element                                  Description

 CustomItem Element for CustomEntry       Defines what data is displayed by the custom control view and
 for GroupBy                              how it is displayed.

<!-- p.2605 -->

See Also
CustomControlName Element for ExpressionBinding for GroupBy

EnumerateCollection Element for ExpressionBinding for GroupBy

ItemSelectionCondition Element for ExpressionBinding for GroupBy

PropertyName Element for ExpressionBinding for GroupBy

ScriptBlock Element for ExpressionBinding for GroupBy

CustomItem Element for CustomEntry for GroupBy

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2606 -->

CustomControlName Element for
ExpressionBinding for GroupBy
Specifies the name of a common control or a view control. This element is used when defining
how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     CustomControlName Element

Syntax
 XML

 <CustomControlName>NameofCustomControl</CustomControlName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
CustomControlName element.

Attributes
None.

Child Elements
None.

<!-- p.2607 -->

Parent Elements

                                                                                  ﾉ   Expand table

 Element                                            Description

 ExpressionBinding Element for CustomItem for       Defines the data that is displayed by the
 GroupBy                                            control.

Text Value
Specify the name of the control.

Remarks
You can create common controls that can be used by all the views of a formatting file, and you
can create view controls that can be used by a specific view. The following elements specify the
names of these controls:

      Name Element for Control for Controls for Configuration

      Name Element for Control for Controls for View

See Also
Name Element for Control for Controls for Configuration

Name Element for Control for Controls for View

ExpressionBinding Element for CustomItem for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2608 -->

EnumerateCollection Element for
ExpressionBinding for GroupBy
Specifies that the elements of collections are displayed. This element is used when defining
how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     EnumerateCollection Element

Syntax
 XML

 <EnumerateCollection/>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
EnumerateCollection element.

Attributes
None.

Child Elements
None.

<!-- p.2609 -->

Parent Elements

                                                                              ﾉ   Expand table

 Element                                        Description

 ExpressionBinding Element for CustomItem for   Defines the data that is displayed by the
 GroupBy                                        control.

Remarks

See Also
ExpressionBinding Element for CustomItem for GroupBy

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2610 -->

ItemSelectionCondition Element for
ExpressionBinding for GroupBy
Defines the condition that must exist for this control to be used. There is no limit to the
number of selection conditions that can be specified for a control item. This element is used
when defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     ItemSelectionCondition Element

Syntax
 XML

 <ItemSelectionCondition>
   <PropertyName>.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToEvaluate</ScriptBlock>
 </ItemSelectionCondition>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ItemSelectionCondition element.

Attributes
None.

<!-- p.2611 -->

Child Elements

                                                                                       ﾉ   Expand table

 Element                                                Description

 PropertyName Element for ItemSelectionCondition for    Optional element.
 GroupBy
                                                        Specifies the .NET property that triggers the
                                                        condition.

 ScriptBlock Element for ItemSelectionCondition for     Optional element.
 GroupBy
                                                        Specifies the script that triggers the condition.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                               Description

 ExpressionBinding Element for CustomItem for          Defines the data that is displayed by the
 GroupBy                                               control.

Remarks
You can specify one property name or a script for this condition but cannot specify both.

See Also
Writing a PowerShell Formatting File

ExpressionBinding Element for CustomItem for GroupBy

 Last updated on 05/20/2025

<!-- p.2612 -->

PropertyName Element for
ItemSelectionCondition for GroupBy
Specifies the .NET property that triggers the condition. When this property is present or when it
evaluates to true , the condition is met, and the control is used. This element is used when
defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     ItemSelectionCondition Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
PropertyName element.

Attributes
None.

<!-- p.2613 -->

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                                Description

 ItemSelectionCondition Element for ExpressionBinding   Defines the condition that must exist for this
 for GroupBy                                            control to be used.

Text Value
Specify the name of the .NET property that triggers the condition.

Remarks
If this element is used, you cannot specify the ScriptBlock element when defining the selection
condition.

See Also
ScriptBlock Element for ItemSelectionCondition for GroupBy

ItemSelectionCondition Element for ExpressionBinding for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2614 -->

ScriptBlock Element for
ItemSelectionCondition for GroupBy
Specifies the script that triggers the condition. When this script is evaluated to true , the
condition is met, and the control is used. This element is used when defining how a new group
of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
     ItemSelectionCondition Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToEvaluate</ScriptBlock>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
ScriptBlock element.

Attributes
None.

<!-- p.2615 -->

Child Elements
None.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                                                Description

 ItemSelectionCondition Element for ExpressionBinding   Defines the condition that must exist for this
 for GroupBy                                            control to be used.

Text Value
Specify the script that is evaluated.

Remarks
If this element is used, you cannot specify the PropertyName element when defining the
selection condition.

See Also
ItemSelectionCondition Element for ExpressionBinding for GroupBy

PropertyName Element for ItemSelectionCondition for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2616 -->

PropertyName Element for
ExpressionBinding for GroupBy
Specifies the .NET property whose value is displayed by the control. This element is used when
defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
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

<!-- p.2617 -->

Parent Elements

                                                                                 ﾉ   Expand table

 Element                                           Description

 ExpressionBinding Element for CustomItem for      Defines the data that is displayed by the
 GroupBy                                           control.

Text Value
Specify the name of the .NET property whose value is displayed by the control.

Remarks
See Also
ExpressionBinding Element for CustomItem for GroupBy

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2618 -->

ScriptBlock Element for ExpressionBinding
for GroupBy
Specifies the script whose value is displayed by the control. This element is used when defining
how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     ExpressionBinding Element
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

<!-- p.2619 -->

Parent Elements

                                                                                   ﾉ   Expand table

 Element                                             Description

 ExpressionBinding Element for CustomItem for        Defines the data that is displayed by the
 GroupBy                                             control.

Text Value
Specify the script whose value is displayed by the control.

Remarks
See Also
ExpressionBinding Element for CustomItem for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2620 -->

Frame Element for CustomItem for
GroupBy
Defines how the data is displayed, such as shifting the data to the left or right. This element is
used when defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
     CustomItem Element
     Frame Element

Syntax
 XML

 <Frame>
   <LeftIndent>NumberOfCharactersToShift</LeftIndent>
   <RightIndent>NumberOfCharactersToShift</RightIndent>
   <FirstLineHanging>NumberOfCharactersToShift</FirstLineHanging>
   <FirstLineIndent>NumberOfCharactersToShift</FirstLineIndent>
   <CustomItem>...</CustomItem>
 </Frame>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the Frame
element.

Attributes
None.

<!-- p.2621 -->

Child Elements

                                                                                           ﾉ   Expand table

 Element                                             Description

 CustomItem Element                                  Required Element

 FirstLineHanging Element for Frame for GroupBy      Optional element.

                                                     Specifies how many characters the first line of data is
                                                     shifted to the left.

 FirstLineIndent Element for Frame for GroupBy       Optional element.

                                                     Specifies how many characters the first line of data is
                                                     shifted to the right.

 LeftIndent Element for Frame for GroupBy            Optional element.

                                                     Specifies how many characters the data is shifted away
                                                     from the left margin.

 RightIndent Element for Frame for                   Optional element.
 GroupByRightIndent Element
                                                     Specifies how many characters the data is shifted away
                                                     from the right margin.

Parent Elements

                                                                                           ﾉ   Expand table

 Element                                         Description

 CustomItem Element for CustomEntry for          Defines what data is displayed by the control and how it is
 GroupBy                                         displayed.

Remarks
You cannot specify the FirstLineHanging and the FirstLineIndent elements in the same Frame
element.

See Also
FirstLineHanging Element for Frame for GroupBy

<!-- p.2622 -->

FirstLineIndent Element for Frame for GroupBy

LeftIndent Element for Frame for GroupBy

RightIndent Element for Frame for GroupBy

CustomItem Element for CustomEntry for GroupBy

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2623 -->

FirstLineHanging Element for Frame for
GroupBy
Specifies how many characters the first line of data is shifted to the left. This element is used
when defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
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

<!-- p.2624 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                               Description

 Frame Element for CustomItem for      Defines how the data is displayed, such as shifting the data to
 GroupBy                               the left or right.

Text Value
Specify the number of characters that you want to shift the first line of the data.

Remarks
If this element is specified, you cannot specify the FirstLineIndent element.

See Also
FirstLineIndent Element for Frame for GroupBy

Frame Element for CustomItem for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2625 -->

FirstLineIndent Element for Frame for
GroupBy
Specifies how many characters the first line of data is shifted to the right. This element is used
when defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element for View
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

<!-- p.2626 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                               Description

 Frame Element for CustomItem for      Defines how the data is displayed, such as shifting the data to
 GroupBy                               the left or right.

Text Value
Specify the number of characters that you want to shift the first line of the data.

Remarks
If this element is specified, you cannot specify the FirstLineHanging element.

See Also
FirstLineHanging Element for Frame for GroupBy

Frame Element for CustomItem for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2627 -->

LeftIndent Element for Frame
Specifies how many characters the data is shifted away from the left margin. This element is
used when defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
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

<!-- p.2628 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                               Description

 Frame Element for CustomItem for      Defines how the data is displayed, such as shifting the data to
 GroupBy                               the left or right.

Text Value
Specify the number of characters that you want to shift the data to the left.

Remarks
See Also
Frame Element for CustomItem for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2629 -->

RightIndent Element for Frame for
GroupBy
Specifies how many characters the data is shifted away from the right margin. This element is
used when defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
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

<!-- p.2630 -->

Parent Elements

                                                                                       ﾉ   Expand table

 Element                               Description

 Frame Element for CustomItem for      Defines how the data is displayed, such as shifting the data to
 GroupBy                               the left or right.

Text Value
Specify the number of characters that you want to shift the data to the right.

Remarks
See Also
Frame Element for CustomItem for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2631 -->

NewLine Element for CustomItem for
GroupBy
Adds a blank line to the display of the control. This element is used when defining how a new
group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
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

<!-- p.2632 -->

Parent Elements

                                                                                 ﾉ   Expand table

 Element                                          Description

 CustomItem Element for CustomEntry for GroupBy   Defines a control for the custom control view.

Remarks

See Also
CustomItem Element for CustomEntry for GroupBy

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2633 -->

Text Element for CustomItem for GroupBy
Specifies text that is added to the data that is displayed by the control, such as a label, brackets
to enclose the data, and spaces to indent the data. This element is used when defining how a
new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element
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

<!-- p.2634 -->

Parent Elements

                                                                                    ﾉ   Expand table

 Element                                             Description

 CustomItem Element for CustomEntry for GroupBy      Defines a control for the custom control view.

Text Value
Specify the text of a control for data that you want to display.

Remarks
See Also
CustomItem Element for CustomEntry for GroupBy

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2635 -->

EntrySelectedBy Element for CustomEntry
for GroupBy
Defines the .NET types that use this control definition or the condition that must exist for this
definition to be used. This element is used when defining how a new group of objects is
displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element for View
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
The following sections describe attributes, child elements, and parent element of the
EntrySelectedBy element. You must specify at least one type, selection set, or selection

condition for a definition. There is no maximum limit to the number of child elements that you
can use.

Attributes

<!-- p.2636 -->

None.

Child Elements

                                                                                       ﾉ   Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Optional element.
 for GroupBy
                                                  Defines the condition that must exist for this
                                                  definition to be used.

 SelectionSetName Element for EntrySelectedBy     Optional element.
 for GroupBy
                                                  Specifies a set of .NET types that use this definition
                                                  of the control.

 TypeName Element for EntrySelectedBy for         Optional element.
 GroupBy
                                                  Specifies a .NET type that uses this definition of the
                                                  control.

Parent Elements

                                                                                       ﾉ   Expand table

 Element                                                      Description

 CustomEntry Element for CustomControl for GroupBy            Provides a definition of the control.

Remarks
Selection conditions are used to define a condition that must exist for the definition to be
used, such as when an object has a specific property or when a specific property value or script
evaluates to true . For more information about selection conditions, see Defining Conditions
for when a View Entry or Item is Used.

See Also
SelectionCondition Element for EntrySelectedBy for GroupBy

SelectionSetName Element for EntrySelectedBy for GroupBy

<!-- p.2637 -->

TypeName Element for EntrySelectedBy for GroupBy

CustomEntry Element for CustomEntries for Controls for View

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2638 -->

SelectionCondition Element for
EntrySelectedBy for GroupBy
Defines a condition that must exist for a control definition to be used. This element is used
when defining how a new group of objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     GroupBy Element for View
     CustomControl Element
     CustomEntries Element
     CustomEntry Element
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

<!-- p.2639 -->

Child Elements

                                                                                           ﾉ   Expand table

 Element                                                  Description

 PropertyName Element for SelectionCondition for          Optional element.
 GroupBy
                                                          Specifies a .NET property that triggers the
                                                          condition.

 ScriptBlock Element for SelectionCondition for           Optional element.
 GroupBy
                                                          Specifies the script that triggers the condition.

 SelectionSetName Element for SelectionCondition for      Optional element.
 GroupBy
                                                          Specifies the set of .NET types that triggers the
                                                          condition.

 TypeName Element for SelectionCondition for              Optional element.
 GroupBy
                                                          Specifies a .NET type that triggers the condition.

Parent Elements

                                                                                           ﾉ   Expand table

 Element                               Description

 EntrySelectedBy Element for           Defines the .NET types that use this control definition or the
 CustomEntry for GroupBy               condition that must exist for this definition to be used.

Remarks
When you are defining a selection condition, the following requirements apply:

     The selection condition must specify a least one property name or a script block, but
     cannot specify both.

     The selection condition can specify any number of .NET types or selection sets, but
     cannot specify

     both. For more information about how to use selection conditions, see Defining
     Conditions for when Data is Displayed.

<!-- p.2640 -->

See Also
PropertyName Element for SelectionCondition for CustomControl for View

ScriptBlock Element for SelectionCondition for CustomControl for View

SelectionSetName Element for SelectionCondition for Custom Control for View

TypeName Element for SelectionCondition for GroupBy

EntrySelectedBy Element for CustomEntry for GroupBy

Writing a PowerShell Formatting File

Last updated on 05/20/2025
