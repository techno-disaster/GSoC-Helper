projects_starter = (
    "Please, figure out what you want to work on, see what's needed (for example, by looking at open issues, "
    "or just by playing with the software yourself and finding out how it could be improved), then reach "
    "out to however is in charge of that specific thing. Also checkout the FAQs of common projects using the following commands in the channel: \n\n/rutorrent\n\nFor previous GSoC ideas use: /2020-ideas\n"
)
rutorrent = "I guess you wish to contribute in our rutorrent-flutter project. I would suggest you to go through the README once so that you have an idea of what the application does.Now for using the app you need to have either a seedbox account or rutorrent installed on your system, of which installation is though quite easy but there are chances you will get stuck somewhere as it also requires you to install rtorrent which further needs LAMP stack to run, therefore for simplicity we have provided a docker image(find link in the README) which runs rtorrent and rutorrent inside the container.After you have successfully downloaded the docker image, the next step is to run this command, sudo docker run -p 5000:8080 crazymax/rtorrent-rutorrentthrough which you port map the container port 8080 (on which rutorrent is running) to your system port 5000Now finally, open browser on localhost:5000 and you will see the rutorrent web interface.Finally, to connect the app with rutorrent running on your system, you need to have your phone and system on the same network, after which you will enter the url(location) in the app which is the ip adress of your system and port (5000) on whichrutorrent is running (ofcouse including the schema, http) and leave the username and password as blank and voila, you are logged in :slightly_smiling_face:All the best,"
ideas_block = [
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "2020 Project ideas"},
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "View",
            },
            "value": "2020-ideas",
            "url": "https://www.ccextractor.org/public:gsoc:ideas_page_for_summer_of_code_2020",
            "action_id": "button-action",
        },
    }
]
