# ETRE Data Visualization Webapp
This is a 4-week project on Creating website for traffic flow data visualization.
	* <a href="https://www.linkedin.com/pulse/traffic-data-visualization-web-app-henock-demessie">More on Project's article page</a>
	* <a href="http://twinerhenock.pythonanywhere.com">Project's Website</a>

<table>
<caption><h2>Project's Source Code</h2></caption>
<tr><td><a href="https://github.com/twinnerhenock/alx_portfolio">Go To Files</a></td><td><a href="https://github.com/twinnerhenock/alx_portfolio/tree/master/main.py">Main</a></td>
</tr>
</table>

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
        * Dataset csv files df_joined.csv and daily_tulu_data.csv for visualizing traffic flow of Ethiopian Toll Roads Enterprie is also contained in this module.
        * ml_model is a folder to contain our saved model Long Short Term Memory(LSTM) .

