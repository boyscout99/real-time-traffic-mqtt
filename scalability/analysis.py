# Python libraries
import os
import pandas as pd
# Personal modules
import network_data_util as ndu
import plotter_util as pu

# Names of the files which store the time stamps
sub_file = '500sub1pub1bro_rx_sub.txt'
pub_file = '500sub1pub1bro_tx_pub.txt'

# Constructing absolute path to simulat relative paths
dirname = os.path.dirname(__file__)
f_sub = os.path.join(dirname, f'{sub_file}')
f_pub = os.path.join(dirname, f'{pub_file}')

# Read in both files and create a dataframe with all values
data_sub = ndu.read_in_one_dimensional_dataset(
    f_sub,
    column_name='Timestamp Sub.',
    data_type='ts')
data_pub = ndu.read_in_one_dimensional_dataset(
    f_pub,
    column_name='Timestamp Pub.',
    data_type='ts')
data = pd.concat([data_sub, data_pub], axis=1)
# Calculate delay
data['Index'] = data.index
data['Delay (ns)'] = data['Timestamp Sub.'] - data['Timestamp Pub.']
print('Delay data frame:')
print(data['Delay (ns)'])
print(data['Delay (ns)'].describe())

# Plot graphs
pu.generate_time_plot(
    data=data,
    file_name='TEST',
    column='Delay (ns)',
    title='Delay Over Time',
    ts_column='Timestamp Pub.',
    xlabel='Date and Time',
    ts_format='%d %H:%m:%s',
    xpadding=0.4)
pu.generate_line_graph(
    data=data[['Delay (ns)', 'Index']],
    file_name='500sub1pub1bro-line',
    title='Delay Over Time',
    ylog=True,
    nth_xlabel=1,
    padding_bottom=0.2)
