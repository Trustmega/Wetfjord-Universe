# Wetfjord-Universe

This is where all custom scripts for the Wetfjord-universe (WFU) will be placed.

Feel free to use them for your own servers, but please link to the source.

## Minecraft-management

wetfjord.config.default: 
Copy wetfjord.config.default to yourservername.config and change the options to your usecase.

wetfjord.sh: 
Usage: [servername] | [-start memory in mb] | [-restart memory in mb] | [-backup] | [-stop] | [-delete] |  [-reload] | [-update] | [-announcement]

To start a server named "wetfjordsurvival" with 8GB memory the usage is as follows:
`./wetfjord.sh wetfjordsurvival -start 8192`

Announcements are picked randomly from the options file.

The same script can be used to manage several servers, just create more .config files with the name of the server and use the same way as stated above.

Tasks can easily be automated by using crontab, example:

```
# m h  dom mon dow   command
0 4 * * * /path/to/wetfjord.sh wetfjordsurvival -restart 8192
45 20 * * * /path/to/wetfjord.sh wetfjordsurvival -delete
0 */6 * * * /path/to/wetfjord.sh wetfjordsurvival -backup
*/15 * * * * /path/to/wetfjord.sh wetfjordsurvival -announcement
```

## Hansibot

Install the discord.py dependency by doing the following:

python3 -m pip install --user discord.py==1.3.3


## Distributed World Backup
download-World-Backup.sh is a script to download the latest Wetfjord Encrypted backup for Minecraft.

[Read More](Distributed-World-Backup/README.md)
