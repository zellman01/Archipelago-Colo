# Pokemon Colosseum Randomizer Setup Guide

## Dolphin Settings

To remove text flickering set the following settings in Dolphin

- Options -> Graphic Options -> Hacks -> Set "Texture Cache Accuracy" to Safe

## Required Software

- [Archipelago](https://archipelago.gg)
- [Dolphin](https://dolphin-emu.org)
- American ISO file for Colosseum

## Installation Procedures
1. Download and install most recent Archipelago Multiworld Suite from the above link, making sure the most recent version is installed
2. Acquire the most recent APWorld from [Release page](https://github.com/zellman01/Archipelago-Colo/releases/latest) and place it in the custom_world folder of your Archipelago install
3. Download and install Dolphin Gamecude/Wii Emulator from the link above, making sure to install the most recent version (minimum 2503), and open it once to ensure it is able to run
4. Make sure Dolphin's MMU is disabled / un-checked in the following path.
 - Dolphin -> Configuration -> Advanced
5. Make sure Emulated Memory Size Override on the same screen is disabled
6. Ensure "Texture Cache Accuracy" is set to safe in Options -> Graphic Options -> Hacks, especially if you suffer from epilepsy and you are doing this APWorld. Optionally, if you want funny text (and do not suffer from epilepsy), do not do this and have fun understanding the game.
 * Note to Windows users: You may experience some issues patching the ISO file if it is stored on OneDrive

## Create a Config (.yaml) file
### What is a config file and why do I need it?
Your config file contains a set of configuration options which provice the generator with information about how it should generate your game. Each player of a multiworld will provide their own config file. This setup allows each player to enjoy an experience customized for their taste, and different players in the same multiworld can all have different options.

### Where do I get a config file?
Run the ArchipelagoLauncher.exe from your Archipelago install and click `Generate Template Options`. This will produce a `/Players/Templates` folder in your Archipelago install, which contains default config files for every game in your `custom_worlds` and `lib/worlds` folder. You can manually edit the config file using a text editor of your choice.

Alternately, the [Player Settings](../player-settings) page on the website allows you to configure your personal settings and export a config file from them.

### Verifying your config file
If you would like to validate your config file to make sure it works, you may do so on the [YAML Validator](../mysterycheck) page.

1. After modifying your yaml, place it into your Archipelago/player folder
   - Alternately, navigate to the [Player Settings](../player-settings) page, configure your options,
      and click the "Generate Game" button.
2. Open the Archipelago Launcher and click "Generate". This will create a zip file in Archipelago/output
   - You will need to open this .zip to get your .appc patch file if you are not using the Archipelago website
3. Navigate to the Archipelago website and go to the Host Game page (top right menu)
4. Click upload file and pass it the .zip created in your output folder
5. Click the "Create New Room" link. You are now able to download your patch file from here (as of AP 0.6.2).
6. Run the ArchipelagoLauncher.exe and click `Open Patch`. Select your `.appc` patch file.
You will be prompted to locate your Pokemon Colosseum ISO the first time you do this.
   - This action will automatically run the Pokemon Colosseum Client (and connect to the webhost if the patch was downloaded from there).
   - The patch will be placed in the same folder as your patch file by default.
   - You will ***not*** need to patch the game every time, and can simply run the `PCClient` from the list on the right of the Archipelago Launcher
to continue later.
7. Open Dolphin and from Dolphin, open your newly patched Pokemon Colosseum ISO. Do not go any further than the main menu after the splash screen.
   - Ensure that "Enable GPU Overclock" and "Emulated Memory Size Override" are both off in your Dolphin settings, and if you do not want spicy text, that "Texture Cache Accuracy" is set to safe
8. In the server page, there will be a port number. Copy this port number into the top of your PCClient if it did not populate on its own. 
   - The field should read `archipelago.gg:<port number>`
9. Once you have loaded into the game, click the `Connect` button at the top of the PCClient. You are now connected and ready to play!
   - The client takes around 10 seconds to finish connecting, and only connects once you are actually in the mansion
   - Unfortunately, due to the nature of some checks, you must be connected to a server while playing. Please keep a link to the webpage on hand
   - There is a currently known issue where the client sometimes makes you connect twice to successfully connect to the server
10. To rejoin the room later, you need to open the webpage, open the PC Client through the Archipelago Launcher, and open the patched ISO with Dolphin.
Then you can click connect on the PC Client so long as the port matches what is shown on the webpage.

## Joining a MultiWorld Game

### Obtain your patch file and create your ROM

When you join a multiworld game, you will be asked to provide your config file to whoever is hosting. Once that is done,
the host will provide you with either a link to download your patch file, or with an APPC patch file that they have extracted from the zip. 

Put your patch file on your desktop or somewhere convenient. Open the ArchipelagoLauncher.exe and click `Open Patch`. 
This should automatically launch the client, and will also create your ISO in the same place as your patch file. On first time patching, you will be prompted 
to locate your Pokemon Colosseum ISO

### Connect to the client

When the ISO patched, the Pokemon Colosseum client (PCClient) should have also automatically launched in
the background. If it did not, please check the log in your Archipelaog/logs folder. If this is its first time launching, you may be prompted to allow it to communicate through the Windows Firewall. You must reopen the client each time you connect to a different randomized ISO.

1. Open Dolphin and from Dolphin, open your newly patched Pokemon Colosseum ISO
2. In the server page, there will be a port number. Copy this port number into the top of your PCClient. 
   - The field should read `archipelago.gg:<port number>`
3. Once you have loaded into the game, the client should log that Dolphin has been connected. Click the `Connect` button
at the top of the PCClient. If the port number is correct, you are now connected and ready to play!
   - Unfortunately, due to the nature of some checks, you must be connected to a server while playing
   - There is also a known issue where the client will make you hit the `Connect` button twice before actually connecting

### Play the game