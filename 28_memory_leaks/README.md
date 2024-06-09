#	Wait? There are memory leaks?

-	Have you ever thought, that Python with it's automatically clean up features does not comes with memory leaks? Well, now you know that.

##	What is a memory leak?

-	a requested resource, like file operation, network access, ..., which has not (successfully) been released
-	often accoured by using a resouce without **with**, if available and in combination with an exception or a signal or "the normal way"
-	without caring about your application or also your **whole machine** can be affected

examples:
```
fc = open("file.dat", mode="w")
#.......

#	What about fc.close()?
```
>	This resource has not been released.

```
fc = open("file.dat", mode="w")
#......
raise Exception("Oops!")
fc.close()
```
>	A resource release exists, but in case of an exception this resource is now orphan.