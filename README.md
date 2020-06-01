# ctf-timer
<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Description</a></li>
<li><a href="#sec-2">2. Setup</a></li>
<li><a href="#sec-3">3. Using the script</a></li>
</ul>
</div>
</div>

# Description<a id="sec-1" name="sec-1"></a>

Tiny utility for CTF players that serves as a timer, displays the remaining hours of a certain initiated CTF session.
CTFTimer feeds the remaining hours data to i3status in order to be displayed by i3wm.
Cronic calls are done by linux cronjob every hour.

# Setup<a id="sec-2" name="sec-2"></a>

Required modules:
-   python3
-   i3wm
-   cron

The setup is simply editing i3status configuration file in order to let it read the file created by ctftimer.

Run this command in bash in order to setup a convenient i3status configuration environment.
```
bash$ [ -f ~/.config/i3status/config ] || { mkdir ~/.config/i3status; cp /etc/i3status.conf ~/.config/i3status/config }
```

Edit i3status configuration file:
```
bash$ vim ~/.config/i3status/config
```

Add a new directive to point to ctftimer file as follow (change PATH/TO/HOME accordingly):
```
order += "read_file CTF"
read_file CTF {
        path = "*PATH/TO/HOME/.ctftimer"
        format = "CTF Timer ~%contenth remaining"
}
```

Add 'start' as a convenient alias (change PATH/TO/CTFTIMER accordingly):
```
bash$ echo "alias start='python3 /PATH/TO/CTFTIMER/ctfer.py'" >> ~/.bashrc
bash$ source ~/.bashrc
```

Add an hourly cron job as follow:
```
bash$ crontab -e
```

Add the following job which calls ctftimer script once hourly.
```
0 * * * * python3 /PATH/TO/CTFTIMER/ctfer.py
```

You are all set.

# Using the script<a id="sec-3" name="sec-3"></a>

Initiate a session giving the total hours with start:
```
bash$ start 24
```

The script when called with an argument (24 in this case), would create 2 files:
  -> '.ctftimer' holds the remaining hours
  -> '.ctftimer-temp' holds the timestamp of the finish time (current timestamp + number of hours given)

The use of 2 files is actually a work around default i3status limitations, please suggest a better universal approach.

The hourly cronjob will handle the rest of the job, each consequent call to the script without an argument would
serve in decrementing the timer by comparing the current timestamp calculated on the fly to the future timestamp read from the temp file '.ctftimer-temp' and writes the difference in hours
to the '.ctftimer' file in order to be read and displayed by i3status.

When future timstamp is reached '.ctftimer' would hold 0 as value.
