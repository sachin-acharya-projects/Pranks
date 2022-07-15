# BackGround Changer
________________________________
This is a simple application that can change wallpaper of windows devices (v10 or above).
To change the application, we simply need to run the application, it will change wallpaper to the image that is inside
WALLPAPER folder in it's root directory.

#### Additional Informations
We can change some settings, dictate the behaviour of our application. To change the settings, we first need to create a 
`.config` file and open it in any text editor. This `.config` files properties are same as .ini files

This Config file should follow the following pattern
````
[config]
    debugger = [Boolean]
    wallpaper = [String]
    date = [Integer]
    mode = [permanent/temporary]
    count = [0/1]
````
and now we can simply run the application with this config in the base path of our application to implement this settings.

Above setting-pattern consist of some variables which are explained below

*(All the variables and property amust of lowercase and quotation mark, " or ' must be omited)*

* Debugger [Boolean]:
    This variable accept boolean value and if set to true, the application will not change the wallpaper until this config file exists. Can be used to change settings without having any effective change on our machine

* Wallpaper [String]:
    This variable accept string value and it represent the path to wallpaper that will replace the existing wallpaper inside WALLPAPER directory.

* Date:
    This variable accept integer between 0 - 6 representing Monday (0) to Sunday (6) in calender. With this variable, only on the decided date, will the application changes the wallpaper even it is executed.

* Mode:
    This variable accept only one of two value, `permanent` and `temporary`. When set to permanent, wallpaper change persist even when the device is rebooted or re-signed in and setting temporary does opposite.

* Count
    This variable too accept one of two value, 0 and 1. Setting 0, will cause application to change wallpaper only the first time it is executed and setting 0, allows application to change wallpaper, everytime it is executed.