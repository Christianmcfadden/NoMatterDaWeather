# NoMatterDaWeather
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden

Date Started: 12/7/24

This should be a Basic Weather app using python and an weather api so that real time weather predictions are possible.

API Website Links:

Table Of Contents
    1. `Create Virtual Environment/Install Requirements`
    2. `How To refreeze the requirements`
    3. `Clone the GitHub Repository`
    4. `How To Stage The File To Commit To Repository`
    5. `How To Commit Files To The Main Branch In The Repository`
    6. `How To Commit Files To A New Branch In The Repository`

1. `Create Virtual Environment And Install Requirements`
   * You must install the requirements.txt *(IF NEEDED NMDW was mine)
        * Create Virtual Environment:
            (`python -m venv "myvenv"`)

    * Activate Environment:
        On windows -->   name of environment -->(`"myvenv"\Scripts\activate`) 
        On mac --> (`source "myvenv"/bin/activate`) (Name is in "")

    * Install Requirements:
        (`pip install -r requirements.txt`) 

2. `How To refreeze the requirements`

    * Freeze Any New Requirements:
        (`pip freeze > requirements.txt`)

    * Mention in request to submit that you need the requirements updated Note the packages added

3. `Clone the GitHub Repository`
    * Install git
          Official git site:
              `https://git-scm.com/downloads/mac`
          Check Git Version:
              `git --version`
          Install Homebrew:
              `$ brew install git`
          Install MacPorts (If needed):
              `$ sudo port install git`
      
    * Clone the Repositiory:
        (`git clone https://github.com/Christianmcfadden/NoMatterDaWeather.git`)

    * Navigate to Repositiory:
        (`cd my-repo`)

4. `How To Stage The File`
    (`git add .`)   <-- Adds modified files to the staging area
    (`git add file1.txt file2.txt`) <-- If you manually want to stage specific files

5. `How To Commit Files To The Main Branch In The Repository`
    * Stage The Files:
        
    * Commit The Files:
        Commit Files With Message:
            (`git commit -m "Your commit message"`)
        Push To Main:
            (`git push origin main`)

6. `How To Commit Files To A New Branch In The Repository`
    * Stage The Files:

    * Commit The Files:
        Create a New Branch:
            (`git checkout -b your-branch-name`)
        
        Push the New Branch:
            (`git push origin your-branch-name`)

        Submit a Pull Request (PR):
            Go to the original repository on GitHub.
            You’ll see a prompt to create a pull request for the new branch.
            Click Compare & pull request.
            Add a description of your changes and submit the PR for review.
