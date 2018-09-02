#create dictionary for pressure switches.
#each switch key is a string based on name of switch.
#each key is assigned a tuple as its value.
#index 0 = upper target, index 1 = lower target, index 2 = tolerance window &
#index 3 is part number.
pressureSwitch={}

#main reservoir upper and lower target values
pressureSwitch['Main Reservoir']=(8.50, 7.50, 0.15, 'WMV-6230')

#brake pipe upper and lower targetvalues
pressureSwitch['Brake Pipe']=(2.50, 2.00, 0.15, 'WMV-6230')

#parking brake upper and lower target values
pressureSwitch['Parking Brake']=(1.50, 1.00, 0.15, 'WMV-6230')


tuple2  = ('MR', 'PB')
dictdude = {tuple2[0]: 160, tuple2[1]: 17}
