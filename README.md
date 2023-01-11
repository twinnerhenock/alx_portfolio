# ETRE Data Visualization Webapp
This is a 4-week project on Creating website for traffic flow data visualization.
	* <a href="https://www.linkedin.com/pulse/traffic-data-visualization-web-app-henock-demessie">More on Project's article page</a>
	* <a href="http://twinerhenock.pythonanywhere.com">Project's Website</a>

<table>
<caption><h2>Project's Source Code</h2></caption>
<tr><td><a href="https://github.com/twinnerhenock/alx_portfolio">Go To Files</a></td><td><a href="https://github.com/twinnerhenock/alx_portfolio/tree/master/main.py">Main</a></td>
</tr>
</table>

![alt text](https://github.com/twinnerhenock/alx_portfolio/blob/master/website/static/logo_blog.png)

# Installation

This web application can be run with python2 installed on any operating system. All the required dependencies are found in <a href="https://github.com/twinnerhenock/alx_portfolio/blob/master/requirements.txt">requiremetns.txt </a>.

## Setup
* Upgrade your pip before proceeding to pip installation of the requirements. You dont need anaconda enviroment to be installed. Only tensor flow with pip installation is opt.
* Git is required for obtaining the code and keeping your codebase up to date. Obtain git for your distribution from <a href="https://github.com/topics/signup-page">here </a>
## Manual installation on ubuntu operating system
	* pip2 install --upgrade pip
	* sudo apt update
	* sudo apt install python2(for installing python version two)
	* sudo apt install python3(for installing python version three)
	* pip install -r ./requirements.txt

# Usage

* main.py

    * <a href="https://github.com/twinnerhenock/alx_portfolio/tree/master/main.py">main.py </a> Its the entry point to our flask application
    * Creates an instance of flask app by calling create_app() from website module.

* website module

    * <a href="https://github.com/twinnerhenock/alx_portfolio/tree/master/website">webiste </a> Contains bule prints of our web page models, views and auth files; and aslo templates, static folders;and an init file to start our dash and flask app.
    * Dataset csv files dfjoined.csv and dailytuludata.csv for visualizing traffic flow of Ethiopian Toll Roads Enterprie is also contained in this module.
    * machine learning model is a folder to contain our saved model Long Short Term Memory(LSTM) .
## Features

    * Upon clicking to the website's domain, user will be routed the landing page or login page. New users are required to signup before going to the home page. Then the home page has two features; either go to the dash board page or use the dropdown menus to observe plotly charts of ETRE's traffic flow. Below the home page default chart, there is an input field for the users to enter number of days or horizon period so that new prediction model result plotly chart is generated based on the horizon period entered from the user.

## About Long Short Term Memory Model 

For anyone interested in understanding the deep learning models, please visit the links <a href="https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21">here</a> for further explanation.

# Deployment

This code is deployed on and hosted by <a href="https://www.pythonanywhere.com/">pythonanywhere</a>. Anyone interested to deploy a simple showcase webpp can create free account and get access to one time 500mb size application deployment.


