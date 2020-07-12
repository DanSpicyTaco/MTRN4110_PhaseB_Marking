# MTRN4110 Phase B Marking Script

This is the marking script for Phase B.

## Setup

Please note, this installation process is OS-independent, meaning it should work for Windows, OSX and Linux.

1. **Download Python** from the [Python website](https://www.python.org/downloads/) (yellow button that says “_Download Python X_").
   Doing this will also install an application called IDLE. 

   Mac users are recommended to download python through the HomeBrew package manager
2. **Clone repository**. Go to GitHub and download this repository.
   Do this by clicking the green button labelled _“Code”_, then “_Download ZIP_”.
   Extract the download to wherever you want.
3. **Open file**. Open IDLE, then go to “_File -> Open_”. Navigate to the extracted ZIP file and open “_main.py_”.
4. **Run file with demo answer**. Once the file is opened, you can run it with “_Run -> Run Module_”.
   The script runs our solution with "_Map.txt_" and compares the answer to what is given in “_answer.txt_”.
   Furthermore, “_PathPlanFound.txt_” should contain your path plan (see Section 3.4).
5. **Run with your answer**. To make the script check your solution, copy and paste, your controller executable in `f1/f2/`. 
   Rename the executable from `z1234567_MTRN4110_PhaseB` to `ans` so it's path is `./f1/f2/ans`.

### Using Git to keep up-to-date

I predict that more issues will be found over the next week.
To avoid having to re-download this repository every time a bug is fixed, you can use Git.

1. Download [Git](https://git-scm.com/downloads) and [GitHub Desktop](https://desktop.github.com/).
2. On this repository, go to "_Code_", then "_Open in GitHub Desktop_".
3. Follow the instructions on GitHub Desktop to set up the folder for you.
4. Now, you can update the copy of your script on your computer by clicking "_Fetch Origin_" and "_Pull Origin"_.

## Known Bugs

| Bug                                                                                                  | Status |
| :--------------------------------------------------------------------------------------------------- | :----: |
| Final path wasn't added to the `get_paths` function, taking off marks for a correct answer.          | Fixed  |
| Student's `PathPlanFound.txt` was in a different location to the automarker's repo, giving an error. | Fixed  |
| Linux is not supported - the `./sln` is outdated.                                                    | Fixed  |

## Contribution

If you have found a bug, please message me on Teams.
Come back for status updates on known bugs (see above).
If you're familiar with GitHub, make a PR - it's a lot easier for me as well!
