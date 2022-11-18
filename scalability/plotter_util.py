# Python libraries
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from pandas.core.frame import DataFrame


def generate_line_graph(
        data: DataFrame,
        file_name: str,
        title='default',
        xlabel='default',
        nth_xlabel=-1,
        ylog=True,
        padding_left=-1.0,
        padding_bottom=-1.0):
    """Generates two line graphs out of the first two columns of a data frame.
    The first column will be depicted on the x-axis, the second column will be
    depicted on the y-axis.

    Parameters
    ----------
    data: DataFrame
        Pandas data frame which stores the values to be plotted.
    file_name: str
        Name of the PNG file to save the graph in.
    nth_xlabel : int
        When given, prints only every n-th x-label. If defined as -1, all
        x-labels are printed.
    padding_left : float
        When given, adjust the left side padding of the plot.
    padding_bottom : float
        When given, adjusts the bottom padding of the plot.
    """
    plt.plot(data.iloc[:, 1], data.iloc[:, 0])
    if xlabel == 'default':
        plt.xlabel(list(data)[1])
    else:
        plt.xlabel(xlabel)
    plt.ylabel(list(data)[0])
    # Rotate x-axis labels
    plt.xticks(rotation=90)

    # Adjust design and layout
    # Adjust design and layout
    if title != ' default':
        plt.title(title)
    else:
        plt.title('')
    if nth_xlabel != -1:
        ax = plt.gca()
        ax.set_xticks(ax.get_xticks()[::nth_xlabel])
    if padding_bottom != -1.0:
        plt.gcf().subplots_adjust(bottom=padding_bottom)
    if padding_left != -1.0:
        plt.gcf().subplots_adjust(left=padding_left)

    plt.savefig(f'{file_name}.png')
    if ylog:
        generate_logarithmic_graph(False, ylog, file_name)
    plt.clf()  # Clear the figure


def generate_time_plot(
        data,
        file_name: str,
        column: str,
        title='default',
        ts_column='Timestamp',
        ts_format='%d/%m/%Y',
        xlabel='default',
        xlabel_rotation=90,
        xpadding=0.2,
        ylog=False,
        verbose=False) -> None:
    """Generates a time plot for time series data.

    Sources: https://stackoverflow.com/questions/1574088/
                plotting-time-in-python-with-matplotlib

    Parameters
    ----------
    data : DataFrame
        Data to plot.
    file_name : str
        Name of the file to generate.
    column : str
        Name of the column to plot over time.
    ts_column : str, default='Timestamp'
        Name of the column which stores the time stamps.
    ts_format : str, default='%d.%m.%Y'
        Format to apply to time stamps. Calls the axis' object's function
        set_major_formatter().
    xlabel : str, default='default'
        x-axis label. If not given, uses the name of the plotted column.
    xpadding : float, default=0.2
        Sets the space for xlabels by calling the subplots_adjust() function.
    ylog : bool, default=False
        Whether to generate a second plot with a logarithmic y-axis.
    verbose : bool, default=False
        Whether to print debug messages.
    """
    # Plot data
    fig, ax = plt.subplots()
    plt.plot_date(
        x=data[ts_column],
        y=data[column],
        xdate=True,
        markersize=1)
    # Adjust design and layout
    if title != ' default':
        plt.title(title)
    else:
        plt.title('')
    # Format the x-axis
    plt.xticks(rotation=xlabel_rotation)  # rotate x axis labels
    if xlabel == 'default':
        plt.xlabel('Date')
    else:
        plt.xlabel(xlabel)
    plt.gcf().subplots_adjust(bottom=xpadding)
    # Define date formatter
    formatter = DateFormatter(ts_format)
    ax.xaxis.set_major_formatter(formatter)
    # Format y-axis
    plt.ylabel(column)
    # Save the plot
    plt.savefig(f'{file_name}.png')
    if ylog:
        generate_logarithmic_graph(False, ylog, file_name)
    plt.clf()  # Clear figure


def generate_logarithmic_graph(xlog: bool, ylog: bool, file_name: str):
    """Dynamically plots axes on a logarithmic scale and adapts the axes
    labels accordingly, when one or both arguments are true. Saves the new
    plot in a separate file with a '-log.png' extension.

    Parameters
    ----------
    xlog : bool
        Whether to apply a logarithmic scale on the x-axis.
    ylog : bool
        Same as xlog, but for the y-axis.
    file_name : str
        Name of the file to save the graph into.
    """
    ax = plt.gca()
    if xlog:
        plt.xscale('log')
        plt.xlabel('log(' + ax.get_xlabel() + ')')
    if ylog:
        plt.yscale('log')
        plt.ylabel('log(' + ax.get_ylabel() + ')')
    plt.savefig(f'{file_name}-log.png')
