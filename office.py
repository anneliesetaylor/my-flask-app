
from flask import Flask, render_template
import csv


def convert_to_dict(filename):
    """
    Convert a CSV file to a list of Python dictionaries
    """
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # create DictReader object
    my_reader = csv.DictReader(datafile)

    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)

    # close original csv file
    datafile.close()

    # return the list
    return list_of_dicts



app = Flask(__name__)
application = app

office_list = convert_to_dict('gsofficedata2.csv')

pairs_list = []

for e in office_list:
    pairs_list.append( (e['id'], e['episode']) )



# first route
@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="The Best of The Office")


# second route
@app.route('/episode/<num>')
def detail(num):
    try:
        office_dict = office_list[int(num) - 1]
    except:
        return f"<h1>Invalid Episode Number: {num}</h1>"

    return render_template('episode.html', epi=office_dict, the_title=('The Best of The Office: ' + office_dict['episode']))



# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
