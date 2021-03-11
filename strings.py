projects_starter = (
    "Please, figure out what you want to work on, see what's needed (for example, by looking at open issues, "
    "or just by playing with the software yourself and finding out how it could be improved), then reach "
    "out to however is in charge of that specific thing. Also checkout the FAQs of common projects using the following commands in the channel (not supported in threads): \n\n/rutorrent\n/sample-platform\nFor previous GSoC ideas use: /2020-ideas\n"
)

rutorrent = "Thank you for showing interest in our rutorrent-flutter project. If you haven't looked at the README on the GitHub page of the project yet, I would suggest you to do that first, so that you have an idea of what the application does. Using the app means you either need a seedbox account, or a local installation of rutorrent. If you get stuck installing rtorrent locally, you can try out the Docker file we provide instead (this command should work for you: sudo docker run -p 5000:8080 crazymax/rtorrent-rutorrent). It'll run both rtorrent and rutorrent inside the container. Once it's running (refer to the README on how to do that), you should be able to access the rutorrent web interface on http://localhost:5000. To connect the app with rutorrent running on your system, make sure you connected to the same network and enter a combination of the IP of your local PC (i.e. 192.168.0.101) and the port number as URL (i.e. http://192.168.0.101:5000), with a blank username/password. If you still have trouble at this point, feel free to ask us :slightly_smiling_face:"

sample_platform = "Thank you for showing interest in our project for regression testing on CCExtractor (a.k.a. the Sample Platform). If you haven't looked at the README on the GitHub page of the project yet, I would suggest you to do that first, so that you have an idea of what the application does. Installing the sample platform might be a bit tricky, but the installation guide should be of some help. Alternatively, you can look at our Ansible installation script (WIP): https://github.com/canihavesomecoffee/sample-platform-ansible. For the upcoming GSoC edition it is also recommended to get familiar with the Google Cloud Platform and it's python API."

ideas_block = [
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "2021 Project ideas"},
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "View",
            },
            "value": "2020-ideas",
            "url": "https://www.ccextractor.org/public:gsoc:ideas_page_for_summer_of_code_2021",
            "action_id": "button-action",
        },
    }
]



