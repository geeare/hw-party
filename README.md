# hw-party
Software running the visualizations for the Hello World release party

This is the basis for the program which runs the visualization for my Hello 
World album release party on January 6th, 2024. It's similar to the other 
visualization programs in other repos, but a bit more involved because it has to 
handle playback of multiple different audio files. 


## Requirements

You can install all of the Python requirements for the visualization using the 
supplied `requirements.txt` file:

```bash
$ pip3 install -r requirements.txt
```

In addition to the Python requirements, you will need an audio player 
application which supports the MPRIS protocol. Finally, you can optionall 
install the  the [cli-visualizer](dpayne/cli-visualizer) program to let it 
display the audio visual, however, this is not a hard requirement.


## mpris.py

This is a lightweight MPRIS client used to play and pause the audio, get the 
currently playing track, and detect when the album has finished so that the
visualizer can switch over to the closing section. It is not set up for general 
purpose (but could be easily expanded to do so if desired). It uses pympris and 
DBus to talk to MPRIS players

### Setup

You will need to create a playlist with the songs you want the script to play 
using your audio player. Make sure it has a unique name.

Once you have a playlist created, enter it in the `mpris.py` file, for the 
`PLAYLIST_NAME` variable. You'll also want to enter the name of your audio 
player in the `AUDIO_PLAYER` variable.


## init.txt

This file contains the text which wil be displayed at the begining of the 
program, during the "loading" phase. This text will be "typed" into the terminal 
one character at a time with a 10ms delay between each character. This can 
contain any text you want except for `!` characters, as these are not printed 
and instead serve as a delay character.

The copyright of the `init.txt` file is hearby dedicated to the public domain.


## halt.txt

This file contains the text which is printed at the end of the program. It 
functions the same as the `init.txt` file. 

The copyright of the `halt.txt` file is hearby dedicated to the public domain.


## ascii-cover-release.c

This is a functional C program which is displayed as the main "album art" in the 
visualization. There is space provided at the top of the file to add an 
ascii-art comment with the full art you want. This file is not compiled/run in 
the course of the visualization, but it is printed to the screen.


## hello_world

This is the main control program. There are a few configuration variables at the 
top of the file:

* `ARTIST` = `str` The name of the artist to display in the "Now Playing" tag
* `ALBUM` = `str` The name of the album to display in the "Now Playing" tag
* `PROMPT` = `str` The text to display in the initial/end command prompt
* `SHOW_VIS` = `bool` Whether or not to use `vis` to display the Vis visualization.
* `VIS_TTY` = `int` The TTY number of the terminal to display Vis on.


### Usage

To run the visualization program, open your audio player and then run the 
`hello_world` program. The screen will clear and the `PROMPT` variable will be 
displayed on the screen. You can type at this prompt, but the input will not 
matter. When you press the enter key on your keyboard, the "Loading" phase will 
begin and the `init.txt` file will be printed to your console. Following this, 
the `ascii-cover-release.c` file will be printed to the screen, with the audio 
playback starting simultaneously. After the C program is printed, the Metadata 
tag will be printed, with the Artist and Album configured and the title ID3 tag 
from the currently playing track. When the next song starts, the song title will 
be automatically be replaced with the new title.

At the end of the playlist, following a short delay, the screen will clear and 
the `halt.txt` file will be displayed. At the end of this, the prompt will 
be displayed again. The only valid command is `exit`, which ends the program. 
You can also press Ctrl + C to end. 

You can trigger the end sequence at any time by pausing music playback. If you 
skip tracks forward or backward, the title will be updated to match. 


### Matching the look of the release party video

If you want to match the overall look of the release party video, you'll want to 
install [cool-retro-term](Swordfish90/cool-retro-term). Open a second terminal 
window in the background and set it to full screen. Then, execute this command 
to turn off the prompt (The prompt will be reset when you close the terminal):

```
PS1=''
```

Next, open Cool Retro Term and in the settings set the Opacity to 0%. Also set 
this to full-screen and set position it above the other terminal window. 
Navigate to the `hello_world` program and run it. The program should then take 
care of all of the remaining details.

## Troubleshooting

The most common problem would likely be a lack of Vis running to display the 
background visualization. This is caused by having the wrong TTY number. To get 
the correct number, in your background terminal run `tty`. The correct number is 
the one at the end of that output. Set the `TTY` variable to this value. 
