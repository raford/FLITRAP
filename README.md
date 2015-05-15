# ![](http://i.imgur.com/RcRWvzE.jpg) FLITrap: Fly Line Information Trap

> FLITrap is a GUI application written in Python, using the Tkinter module, that allows a researcher to access pieces of data from the the GAL4 lines of a particular Bloomington Drosophila Stock Center stock number without having to visit numerous websites.

### Table of contents
1. [What is FLITrap?](https://github.com/raford/flitrap#what-is-flitrap)
2. [How do I run FLITrap on my machine?](https://github.com/raford/flitrap#how-do-i-run-flytrap-on-my-machine)
3. [Screenshots of FLITrap in action](https://github.com/raford/flitrap#screenshots-of-flitrap-in-action)
4. [Acknowledgements](https://github.com/raford/flitrap#acknowledgements)
5. [References](https://github.com/raford/flitrap#references)


## What is FLITrap?
FLITrap makes use of several pieces of data obtained from the HHMI Janelia Farm[1], Bloomington Drosophila Stock Center (BDSC)[2], and FlyBase[3] --- obtained via webscraping --- to allow a researcher to access data related to _D.melanogaster_ BDSC GAL4 lines without having to visit numerous sites. This in turn allows a researcher to work more efficiently and not waste his or her precious time looking for these data points. This GUI application is unique in several ways: the researcher is able to copy a BDSC stock number's FASTA sequence to his or her machine's clipboard with the press of a button, find FBsf (etc.) for a particular stock number, and the researcher is able to press a button to view the expression data video for a searched line (provided he or she is connected to the Internet). Moreover, this application was developed in Python 2.7.X and requires only the scientific Python stack to run. This application _should_ run on Windows, OSX, and various GNU/Linux distributions with little problems --- assuming the necessary modules are installed.


## How do I run FLITrap on my machine?
There are two ways to run FLITrap on your machine: use a standalone version of FLITrap, or download all of the files needed to run FLITrap. We will show you how to run FLITrap for both of these ways.

### Standalone versions
We have made standalone versions of FLITrap available for the following:
* OSX 10.10 (Yosemite)

Standalone versions can be downloaded from [here.](https://www.dropbox.com/sh/zkm6gbizss5pf1u/AAC5nJ-rn-YrjmJE0s3dLsyca?dl=0)


### Downloading all of the files
In order to run FLITrap without downloading a standalone version of FLITrap, you will need to download the "master-flitrap" zip. This can be accomplished by following the steps below. 

1. Download the `flitrap-master.zip` as seen below.
![](http://i.imgur.com/gyrclLg.png)

2. After the file has completed downloading, move the `.zip` to the desired location and uncompress it (for this example we have placed it on our `Desktop`). You should see something similar to the following.
![](http://i.imgur.com/RhGR02H.png)

3. Open your machine's terminal and navigate to the location that you placed the uncompressed `.zip` file.

![](http://i.imgur.com/Dabhj7M.png)

4. Type the following into your terminal and press enter/return to start FLITrap. You should see something similar to the following.

![](http://i.imgur.com/iDhFAcx.png)


## Screenshots of FLITrap in action
Below is a screenshot of FLITrap being used to search for information about BDSC stock number 47708.

![](http://i.imgur.com/GOoeEBx.png "Screenshot of FLITrap")

If you should happen to enter an invalid BDSC stock number, then you will see the following.

![](http://i.imgur.com/ihN6pNd.png "Screenshot of FLITrap with an invalid BDSC stock number")

## Acknowledgements
This work is supported in part by the NSF grant DUE-0926721 and NIH-NIMHD grant 5G12MD007592. I would like to thank the University of Texas at El Paso's [Undergraduate Participation in Bioinformatics Training (UPBiT)](http://www.bioinformatics.utep.edu/UPBiT/index.php) for giving me the opportunity to participate in bioinformatics research as an undergraduate majoring in statistics. Under the mentorship of Professors Ming-Ying Leung and Kyung-An Han, I was given what I feel is a once-in-a-lifetime opportunity to learn more about statistics, computer science, and biology---beyond what was offered in the courses required for my degree.

## References
1. HHMI Janelia Farm reference here
2. BDSC reference here
3. FlyBase reference here