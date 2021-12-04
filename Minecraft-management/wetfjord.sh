#!/bin/bash

if [[ "$1" == -* ]]
then
	echo "please specify servername as the first argument!"
	exit 1
fi

source $1.config

option="${2}"
case ${option} in
	-start) MEM="${3:-1024}"
			screen -d -m -S "$1"
			sleep 2
			screen -R "$1" -X stuff "cd "$serverlocation"\n"
			screen -R "$1" -X stuff ""$javapath" -Xms"$MEM"M -Xmx"$MEM"M -jar "$serverlocation""$serverjar" nogui\n"
		;;
	-restart) MEM="${3:-1024}"
			screen -R "$1" -X stuff "say server will reboot in 30 seconds. Back in 1 minute $(printf '\r')"
			sleep 10
			screen -R "$1" -X stuff "say server will reboot in 20 seconds. Back in 1 minute $(printf '\r')"
			sleep 10
			screen -R "$1" -X stuff "say server will reboot in 10 seconds. Back in 1 minute $(printf '\r')"
			sleep 5
			screen -R "$1" -X stuff "say server will reboot in 5 seconds. Back in 1 minute $(printf '\r')"
                        #Post meme to Discord channel
                        curl -H "Content-Type: application/json" -X POST -d '{"username": "wetfjordserver", "content": "Server will fart in 5 seconds."}' "$discordwebhook"
                        curl -H "Content-Type: application/json" -X POST -d '{"username": "wetfjordserver", "content": "https://wetfjord.eu/server_will_fart.png"}' "$discordwebhook"
			sleep 1
			screen -R "$1" -X stuff "say server will reboot in 4 seconds. Back in 1 minute $(printf '\r')"
			sleep 1
			screen -R "$1" -X stuff "say server will reboot in 3 seconds. Back in 1 minute $(printf '\r')"
			sleep 1
			screen -R "$1" -X stuff "say server will reboot in 2 seconds. Back in 1 minute $(printf '\r')"
			sleep 1
			screen -R "$1" -X stuff "say server will reboot in 1 second. Back in 1 minute $(printf '\r')"
			sleep 1
			screen -R "$1" -X stuff "stop $(printf '\r')"
			sleep 30
			cp "$buildtoolslocation""$serverjar" "$serverlocation""$serverjar"
			screen -R "$1" -X stuff ""$javapath" -Xms"$MEM"M -Xmx"$MEM"M -jar "$serverlocation""$serverjar" nogui\n"
                        curl -H "Content-Type: application/json" -X POST -d '{"username": "wetfjordserver", "content": "Server restart completed."}' "discordwebhook"
		;;
	-backup)
                        screen -R "$1" -X stuff "say Backup starting. You may experience a little lag$(printf '\r')"
                        screen -R "$1" -X stuff "save-off $(printf '\r')"
                        screen -R "$1" -X stuff "save-all $(printf '\r')"
                        sleep 3
                        date=$(date +%y%m%d-%H%M%S)
                        tar -cpvzf "$backuplocation""$1-""$date".tar.gz "$serverlocation"
                        screen -R "$1" -X stuff "save-on $(printf '\r')"
                        screen -R "$1" -X stuff "say Backup completed. $(printf '\r')"
		;;
	-stop)
			screen -R "$1" -X stuff "say The server will shut down in 30 seconds. For more information check facebook/twitter/discord/our website $(printf '\r')"
			sleep 10
			screen -R "$1" -X stuff "say The server will shut down in 20 seconds. For more information check facebook/twitter/discord/our website $(printf '\r')"
			sleep 10
			screen -R "$1" -X stuff "say The server will shut down in 10 seconds. For more information check facebook/twitter/discord/our website $(printf '\r')"
			sleep 10
			screen -R "$1" -X stuff "say The server will shut down in 5 seconds. For more information check facebook/twitter/discord/our website $(printf '\r')"
			sleep 5
			screen -R "$1" -X stuff "say The server will shut down in 4 seconds. For more information check facebook/twitter/discord/our website $(printf '\r')"
			sleep 1
			screen -R "$1" -X stuff "say The server will shut down in 3 seconds. For more information check facebook/twitter/discord/our website $(printf '\r')"
			sleep 1
			screen -R "$1" -X stuff "say The server will shut down in 2 seconds. For more information check facebook/twitter/discord/our website $(printf '\r')"
			sleep 1
			screen -R "$1" -X stuff "say The server will shut down in 1 second. For more information check facebook/twitter/discord/our website $(printf '\r')"
			sleep 1
			screen -R "$1" -X stuff "stop $(printf '\r')"
			sleep 10
			screen -R "$1" -x stuff 'exit\n'
		;;
	-delete)
			find "$backuplocation"* -mindepth 1 -mtime +"$keepdays" -delete
		;;
	-reload)
			screen -R "$1" -X stuff "whitelist reload $(printf '\r')"
		;;
	-update) REVISION="${3}"
			cd "$buildtoolslocation"
			curl "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar" -o BuildTools.jar
			"$javapath" -jar BuildTools.jar --rev "$REVISION"
			mv "$buildtoolslocation"spigot-"$REVISION".jar "$buildtoolslocation""$serverjar"
		;;
	-announcement)
			screen -R "$1" -X stuff "say §2Announcement: ${announcements[$RANDOM % ${#announcements[@]} ]} $(printf '\r')"
		;;
   *)
      echo "`basename ${0}`: usage: [servername] | [-start memory in mb] | [-restart memory in mb] | [-backup] | [-stop] | [-delete] |  [-reload] | [-update] | [-announcement]"
      exit 1 # Command to come out of the program with status 1
		;;
esac
