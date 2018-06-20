This simple webscraper takes table data from NFLCombineResults.com and puts it into an Excel spreadsheet. 
A GUI was made and it was turned into an executable with the intention of giving this program to a colleague who has little to no 
programming experience and they would be able to benefit from it without issues.

Currently I am experiencing an issue in the conversion to an executable.

When executing the file, a command window is opened for a brief second before it goes away, then nothing happens.
After making a batch file to keep the window open I see the error:

"import _tkinter ImportError: DLL load failed: %1 is not a valid Win32 application."

I am reading this could be caused by variations between 32-bit python I'm using and 64-bit libraries that could have been installed.

Any experience or help is appreciated. Otherwise, scripts run just fine by themselves.
