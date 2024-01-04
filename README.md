> Guide for pose estimation for NYU Abhu Dhabi 2024 with Dr. Moore

# Live webcam pose estimation

>This will use your webcam to perform single person pose estimation at real time. Follow the steps given below for your operating system:

## Windows 10/11
1. Click [here](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe) to download `Docker Desktop` into your ***Downloads*** folder
1. Press <kbd>Win</kbd>+<kbd>R</kbd>
1. Type `powershell` and press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Enter</kbd>
1. Execute the following commands by pasting them into powershell and pressing enter:

    a. `wsl --install -n -d Ubuntu`

    b. ```Invoke-WebRequest -Uri "https://raw.githubusercontent.com/aarav2you/nyu-abu-dhabi-pose-estimation/main/fixWSL.reg" -OutFile "$env:TEMP\fixWSL.reg"; Start-Process -filepath "$env:windir\regedit.exe" -Argumentlist @("/s", "`"$env:TEMP\fixWSL.reg`"")```

1. Open the newly installed `Ubuntu` app, wait for it to install and then close it

1. Execute the following commands in powershell:

    a. `cd Downloads`

    b. `& '.\Docker Desktop Installer.exe' install --accept-license`
1. Proceed through the installation
1. Open the newly installed app called `Docker Desktop`
1. Click ***'Continue without signing in'*** and then click ***'Skip'***
1. Press <kbd>Win</kbd>+<kbd>R</kbd>
1. Type `powershell` and press enter
1. Wait for docker engine to start, then execute the following commands:

    a. `docker pull archav2you/track` (this downloads the pose estimation software)

    b. `docker run -p 1234:1234 archav2you/track` (this runs the pose estimation software, so execute this command when you need to run the pose estimation software again, and make sure docker desktop is running beforehand)

1. When you see `Built in <whatever> seconds`, go to [localhost:1234/?model=movenet](localhost:1234/?model=movenet) in your web browser.

1. Allow camera and wait for it to load

1. (Optional): Change the `type` to `thunder` for more accurate pose estimation

1. Close the `powershell` window to stop the software
### Removing the software
1. Press <kbd>Win</kbd>+<kbd>R</kbd>
1. Type `powershell` and press enter
1. Execute the following commands:

    a. ```docker rm -f $(docker ps -a -q --filter ancestor=archav2you/track)```

    b. ```docker rm -f $(docker ps -a -q --filter ancestor=archav2you/track)```
1. Uninstall `Docker Desktop`
## MacOS
1. Open the `terminal` app. For the following steps, enter password when prompted.
1. Execute the following commands by pasting them into terminal and pressing enter:

    a. ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"``` (this will install Homebrew)

    b. ```(echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> /Users/$USER/.zprofile```

    c. ```eval "$(/usr/local/bin/brew shellenv)"```
1. Wait for the command to finish, then execute the following command:

    ```brew install --cask docker```

1. Wait for the command to finish, bring up the MacOS spotlight and open the newly installed app called `Docker`
1. Click ***'Continue without signing in'*** and then click ***'Skip'***
1. Wait for docker engine to start, then execute the following commands:

    a. `docker pull archav2you/track` (this downloads the pose estimation software)

    b. `docker run -p 1234:1234 archav2you/track` (this runs the pose estimation software, so execute when you need to run again)

1. When you see `Built in <whatever> seconds`, go to [localhost:1234/?model=movenet](localhost:1234/?model=movenet) in your web browser.

1. Allow camera and wait for it to load

1. (Optional): Change the `type` to `thunder` for more accurate pose estimation

1. Close the `terminal` window to stop the software

### Removing the software
> It is reccomended to not remove the software yet so you can run pose estimation in video files (scroll down below)
1. Execute the following commands in `terminal`:

    a. ```docker rm -f $(docker ps -a -q --filter ancestor=archav2you/track)```

    b. ```docker image rm archav2you/track```
1. Uninstall the `Docker` app
1. Uninstall `homebrew` by executing the following command:

    ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"```
1. Unintsall Xcode by executing the following command:

    ```sudo rm -r /Library/Developer/CommandLineTools```

# Video upload pose estimation

>This will use a video you specify to perform multi person pose estimation. Follow the steps given below for your operating system:

## Windows 10/11
1. Press <kbd>Win</kbd>+<kbd>R</kbd>
1. Type `powershell` and press enter
1. Make sure `Docker` is installed from the steps above
1. Make sure `Docker Desktop` is running by opening the `Docker` app
1. Execute the following commands in the `terminal`:

    a. ```cd Downloads```

    b. ```git pull archav2you/video-track```

    c. ```docker run -p 7070:7070 archav2you/video-track```

1. Go to [localhost:7070](localhost:7070) in your web browser.

1. Upload the video, when done the video will be played on the webpage and can be downloaded


### Removing the software
1. Execute the following commands in `powershell`:

    a. ```docker rm -f $(docker ps -a -q --filter ancestor=archav2you/video-track)```

    b. ```docker image rm archav2you/video-track```

## MacOS
1. Open `terminal`
1. Make sure `Docker` is installed from the steps above
1. Make sure `Docker` is running by opening the `Docker` app
1. Execute the following commands:

    a. ```cd Downloads```

    b. ```git pull archav2you/video-track```

    c. ```docker run -p 7070:7070 archav2you/video-track```

1. Go to [localhost:7070](localhost:7070) in your web browser.

1. Upload the video, when done the video will be played on the webpage and can be downloaded

### Removing the software
1. Execute the following commands in `terminal`:

    a. ```docker rm -f $(docker ps -a -q --filter ancestor=archav2you/video-track)```

    b. ```docker image rm archav2you/video-track```