# ![](http://i.imgur.com/RcRWvzE.jpg) FLITrap: Fly Line Information Trap

> FLITrap is a GUI application written in Python that allows a researcher to access pieces of data from the the GAL4 lines of a particular Bloomington Drosophila Stock Center stock number without having to visit numerous websites.

### Table of contents
1. [What is FLITrap?](https://github.com/raford/flitrap#what-is-flitrap)
2. [How do I run FLITrap on my machine?](https://github.com/raford/flitrap#how-do-i-run-flytrap-on-my-machine)
3. [Screenshots of FLITrap in action](https://github.com/raford/flitrap#screenshots-of-flitrap-in-action)
4. [Acknowledgments](https://github.com/raford/flitrap#acknowledgements)
5. [References](https://github.com/raford/flitrap#references)


## What is FLITrap?
FLITrap is a GUI application that makes use of several pieces of data obtained via webscraping from the Howard Hughes Medical Institute Janelia Farm's (HHMIJF) FlyLight[1], the Bloomington Drosophila Stock Center (BDSC)[2], and FlyBase[3] to allow a researcher to access data related to _D. melanogaster_ BDSC GAL4 lines without having to visit numerous websites. This in turn allows a researcher to work more efficiently and not waste his or her time searching for these data points. This GUI application is unique in several ways: the researcher is able to copy a BDSC stock number's FASTA sequence to his or her machine's clipboard with the press of a button, find FBsf and other data points for a particular BDSC stock number, and the researcher is able to press a button to view the expression data video for a searched line (provided he or she is connected to the Internet) on the HHMIJF. Moreover, this application was developed in Python 2.7.X and requires only the scientific Python stack to run. This application _should_ run on Microsoft's Windows, Apple's OSX, and various GNU/Linux distributions with little problems — assuming the necessary modules are installed.


## How do I run FLITrap on my machine?
There are two ways to run FLITrap on your machine: use a standalone version of FLITrap, or download all of the files needed to run FLITrap. We will show you how to run FLITrap for both of these ways.

### Standalone versions
Standalone versions of FLITrap do not require you to have the scientific Python stack installed on your machine. We have made standalone versions of FLITrap available for the following:
* OSX 10.10 (Yosemite)
* Windows 7 (win32)

Standalone versions can be downloaded from [here.](https://www.dropbox.com/sh/zkm6gbizss5pf1u/AAC5nJ-rn-YrjmJE0s3dLsyca?dl=0)

##### Installing a standalone version of FLITrap on OSX
Following these instructions will allow you to have a standalone version of FLITrap on an OSX machine.

* Download the correct standalone version for your machine.
![](http://i.imgur.com/vYnZd0z.png)

* Uncompress the `.zip` file to view its contents, and then open the `dist` folder.
![](http://i.imgur.com/VDHaNpx.png)

* Click-on and drag `FLITrap` to your `Applications` folder.
![](http://i.imgur.com/K0zVvZu.png)

* You can now delete the `.zip` file and its expanded version from your machine.

* The first time that you run FLITrap you might be presented with the following window.
![](http://i.imgur.com/Y6HSXiQ.png)

* To fix this issue, you will need to open your `System Preferences` and select the `Security & Privacy` option.
![](http://i.imgur.com/Feg9tFl.png)

* Select the `Open Anyway` option to launch FLITrap.
![](http://i.imgur.com/q9HyeCA.png)

* Congratulations! You can now use FLITrap to find information about different BDSC stock numbers.

### Downloading all of the files
In order to run FLITrap without downloading a standalone version of FLITrap, you will need to download the `master-flitrap.zip.` This can be accomplished by following the steps below. Note: You will need to have the scientific Python stack installed on your machine to run a nonstandalone version of FLITrap.

* Download the `flitrap-master.zip` as seen below (by clicking the button in the red box).
![](http://i.imgur.com/gyrclLg.png)

* After the file has completed downloading, move the `.zip` to a desired location and uncompress it (for this example we have placed it on our `Desktop`). You should see something similar to the following.
![](http://i.imgur.com/RhGR02H.png)

* Open your machine's terminal and navigate to the location that you placed the uncompressed `.zip` file.

![](http://i.imgur.com/Dabhj7M.png)

* Type `python flitrap.py` into your terminal and press enter/return to start FLITrap. You should see something similar to the image below.

![](http://i.imgur.com/iDhFAcx.png)

* Congratulations! You can now use FLITrap to find information about different BDSC stock numbers.

##### WAIT!!! I am using Python 3.X NOT Python 2.7!
No problem! Just change line 62 in `flitrap.py` from
```python
from Tkinter import *
```
to 
```python
from tkinter import *
```
and everything should _just work._

## Screenshots of FLITrap in action
Below is a screenshot of FLITrap being used to search for information about BDSC stock number 47708.

![](http://i.imgur.com/GOoeEBx.png "Screenshot of FLITrap")

If you should happen to enter an invalid BDSC stock number, then you will see the following.

![](http://i.imgur.com/ihN6pNd.png "Screenshot of FLITrap with an invalid BDSC stock number")

## Acknowledgements
This work is supported in part by the NSF grant DUE-0926721 and NIH-NIMHD grant 5G12MD007592. I would like to thank the University of Texas at El Paso's [Undergraduate Participation in Bioinformatics Training (UPBiT)](http://www.bioinformatics.utep.edu/UPBiT/index.php) for giving me the opportunity to participate in bioinformatics research as an undergraduate majoring in statistics. Under the mentorship of Professors Ming-Ying Leung and Kyung-An Han, I was given what I feel is a once-in-a-lifetime opportunity to learn more about statistics, computer science, and biology — beyond what was offered in the courses required for my degree.

## References
1. Pfeiffer BD, Jenett A, Hammonds AS, Ngo TT, Misra S. GAL4 driver collection of Rubin Laboratory at Janelia Farm. ([url](http://flweb.janelia.org/cgi-bin/flew.cgi))
2. Bloomington Drosophila Stock Center. (2014). Janelia GAL4 stocks. ([url](http://flystocks.bio.indiana.edu/bloomhome.htm))
3. St. Pierre SE, Ponting L, Stefancsik R, McQuilton P, the FlyBase Consortium. (2014). FlyBase 102 — advanced approaches to interrogating FlyBase. _Nucleic Acids Research_ 42(D1):D780-88. ([url](http://flybase.org/))