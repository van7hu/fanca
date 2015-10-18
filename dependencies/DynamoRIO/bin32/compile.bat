set dy_home=C:\fanca\dependencies\DynamoRIO
set include=C:\fanca\dependencies\DynamoRIO\include
set libpath=C:\fanca\dependencies\DynamoRIO\lib32\release

cl myclient10.c  /I%include% /GS- /DWINDOWS /DX86_32 /link /libpath:%libpath% dynamorio.lib  /dll   /out:myclient10.dll

