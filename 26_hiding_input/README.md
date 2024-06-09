##	I see what I don't see

-	especially by entering account informations it might be better to enter the data without seeing them
-	by default, Python does not comes with a function for that (at this moment)

###	different kind of hiding the input

1.	install getpass package by pip(3/.exe) install getpass

use:
```
import getpass
getpass.getpass(str: promt)
```

2.	install maskpass package by pip(3/.exe) install maskpass

use:
```
import maskpass
maskpass.askpass(str: promt)
```

3.	install getch package by pip(3/.exe) install getch

use:
```
import getch
getch.getch()
```