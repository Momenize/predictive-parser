## Hey!
There's this simple method in context-free grammars (as in regular grammars for regular languages), in which, if there's a rule where `A => aA | aB`, then you replace it with `A => aC`, hitting your grammar with a new non-terminal called `C` (Or whatever else you want, the symbol won't matter) with the rule of `C => A | B`.<br/>
This method is called <b>Left Factoring</b> and it's used for removing common prefixes in a rule, so that this grammar could be implemented more easily in compilers.

## When will the comedy start?
This method makes implementing grammars much much more simple. No argue in that. what I couldn't accept when my professor was teaching this section (using the same grammar that I've used in the code as an example) in the class, was that she stated that using this is a <b>must</b> when implementing a grammar that suffers from common prefixes. I disagreed and she dared me to implement the same grammar without left factoring, and I hard-coded it in 30 minutes or so, and I'm going to declare war against her in the next section. 

## To explain it better
Let's take a look at this grammar:<br/>
```
A => aA | aB   
B => bB | c
```
<br/>
Using left factoring, we create another non-terminal (I called it R, you can call it whatever you desire) and the grammar would change as following:<br/>

```
A => aR
R => A | B
B => bB | c
```
<br/>

--
-To Be Completed-
