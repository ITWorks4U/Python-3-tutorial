#	strings are just words, right?

acutally yes, but sometimes it shouldn't, especially when reading from keyboard or from a file a "word" shall be a number => this must be converted into its correct format
strings are immutable => once defined it's not allowed to change it's content on the hardcoded way => there're functions, which can do this, but these can only return a new string with the new content => the old content still exists on runtime

##	A word can easy be read in every situation, right?

No. It depends on the used format. Usually, you're using ASCII (basic alphabet in small and capital letters, numbers between 0-9 and "only" a few of "special characters").
Imagine, you want to use emojis, then you have to use an another unicode format. The same condition exists for other real languages, like chinese, russian, ...