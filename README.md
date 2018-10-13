# dash-tutorial
Learn how to build web apps using [dash](https://plot.ly/products/dash/) and [plotly](https://plot.ly/)
## Installation
```
pip install dash==0.28.2  # The core dash backend
pip install dash-html-components==0.13.2  # HTML components
pip install dash-core-components==0.33.0  # Supercharged components
pip install plotly==3.3.0
```
## Running the app
Run `python app.py` in your terminal.
## Bootcamp
1. Import the data using pandas. Feel free to use the [NumPy + Pandas bootcamp](https://github.com/HarvardOpenData/data-science-tutorial) as a guide.
2. Display a table with the data. The [Dash user guide](https://dash.plot.ly/getting-started) has an example of how to create a table from a Pandas DataFrame.
2. Create a bar graph showing the number of people who ranked each house first. [Plotly documentation](https://plot.ly/python/bar-charts/) may be helpful.
2. Create an interactive bar chart with a dropdown menu that allows you to select a house and view the distribution of rankings for that house. Dropdown documentation can be found [here](https://dash.plot.ly/getting-started).
2. Change the title of the page to something more appropriate.
3. Link dash and plotly to their respective websites.
3. Make something prettier by changing `assets/style.css`.
