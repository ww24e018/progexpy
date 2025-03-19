"""Angabe:
Write a class EscapeCharacters.Main that produces the following output on the console. (Output contains
some hints!)

escape sequence is started with a backslash: \
to print a tab ( ) use "\t"
to print a backslash (\) use "\\"
to print double quotes (") use "\""
to print a single quote (') use "\'"
to start a new line (
) use "\n"

Using: https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences

Takeaway1: Dieses Bsp koennte das richtige Einstiegslevel sein, vom Prinzip.
    Details vom Escaping sind in python anders genug dass die selbst-erklaerung an qualitaet verliert.
    Note: Die letzte Anweisung hier benutzt zwar den gleichen escape wie java, aber zusaetlich ein python dings
    um den String selber auf 2 Zeilen aufzuteilen :)
Takeaway2: Die python comments (bzw docstring syntax) sind mighty enough dass der output kopierbar war ohne
    was anpassen zu muessen.
"""

print("escape sequence is started with a backslash: \\")
print('to print a tab (\t) use "\\t"')
#print("to print a backslash (\\) use \"\\\\\"")
print('to print a backslash (\) use "\\\\"')
print('to print double quotes (") use "\\""')
print("to print a single quote (') use \"\\'\"")
print('to start a new line (\n\
) use "\\n"')