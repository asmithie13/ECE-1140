# OJ AND THE COWBOY HATS: Autonmous Train System
A detailed guide on how to install and run our autonomous train system.

# MEMBERS:
| Name | Module |
| ----------- | ----------- | 
| Abigail Magistro | CTC |
| Alexander Smith | SW Track Controller |
| Lillian Jones | HW Track Controller |
| Anh Nguyen |  Track Model |
| Tanvi Verma |  Train Model |
| Lauren Gilfillan | SW Train Controller |
| Chad Collina | HW Train Controller |


## Usage
The following sections discuss the correct usage of our autonomous train system.
Prerequisites: [Python 3.9 or greater](https://www.python.org/downloads/) 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```
1. Retrieve system code from our [ECE 1140](https://github.com/asmithie13/ECE-1140/releases) git repository.
2. Unzip the files in a convenient location


### Starting the simulation

1. Find the file named Start Simulation.bat and run it. 
2. Start Simulation.bat ensures that the user has all python packages installed. The user should ensure that they have the correct version of Python installed as mentioned in 

### Opening and Running a Train

**NOTE*: By convention, the order of initial dispatching of trains from the yard must correspond to the Train ID number, i.e. T1 must be dispatched first, followed by T2, etc. There are sample schedules available in the CTC/Schedules folder that follow this convention, but it is the responsibility of the scheduler to ensure this convention is followed.

**In Manual Mode:** 
1. Open the CTC UI
2. Select Manual Mode
3. By default, a new train will be dispatched, indicated by the * in front of the Train ID. If you are adding a stop to a train that’s already dispatched, select the intended Train ID from the drop down.
4. Select the destination and the arrival time. Destinations should be added to the schedule in the order they are in on the route.
5. Click the “Add Train to Schedule” button. This will calculate the dispatch time and departure station, and add the information to the schedule.


**In Automatic Mode:**
1. Open the CTC UI
2. Select Automatic Mode
3. Click the “Upload Schedule” button  and select the .csv file containing the schedule. (Sample Schedules under CTC/Schedules, see Schedule Formatting below for more details)
4. Click Open. The schedule will automatically populate with all the dispatch information on the schedule


**Schedule Formatting:**

- Schedules must be .csv files
- A schedule file’s header row should be “Line,TrainID,Destination,ArrivalTime”
- Each line after the header will represent one entry on the schedule
    - Line should be either Green or Red
    - TrainID must be in the format “T1”, and follow the convention on order of initial dispatch mentioned above
    - Destination should be a station from the correct line and capitalized
    - ArrivalTime should be in the hh:mm format, on a 24 hour clock



### CTC UI
For information on dispatching a train, refrence the **Opening and Running a Train** Section

**Maintenance Mode:**

Click the Maintenance Mode button to enter Maintenance Mode

- To see block and switch options, make sure a line color is selected
- To close a block, select the block ID and click the "Close Block" button,
- To set a switch position, select the block ID of the switch, then select the block ID indicating the switch positon. Click the "Set Switch Position" button. 
- To reopen a block or release a switch under maintenance, reselect the correct ID of a block or switch that is closed and select the "Reopen Block" button or the "Release Switch" button.

### Wayside Software UI

### Wayside Hardware UI


### Track Model 
1. Selecting a line in the top middle, Green or Red. A map should appear in the UI.
2. Select a block via drop down or by clicking on the block directly. Information about the track should show up on the right, including Block Occupancy.

- If the user wants to upload a different track layout, they can do so by clicking the green upload track layout button and selecting an XML or CSV file.
- Murphy can select a failure by selecting a block and click the button to trigger that failure. 
- The Track Model can toggle the track heaters by changing the environmental temperature.


### Train Model UI
- The left side indicates all the numbers calculated by using Newton's Laws.
- The right side displays live train statistics.
- Murphy’s failures can be sent using the Enable/Disable buttons by simply clicking on them.
- The emergency brake can be toggled on the bottom. 
- As a user, you can view the status of the interior lights, exterior lights, doors and cabin temperature.


### Train Controller Software/Hardware  UI 
#### Moving the Train
    Once the departure time set by the CTC is hit by the global clock, the Train Controller UI will automatically open. 
    
##### Increasing the Speed 

The train will be **stopped** upon deployment. In order to get the train moving you have two options...

**If Authority or Commanded Speed is zero the Train will not move no matter what inputs you provide**

1. Increase the Accelerartion Slider
Click on the Slider and drag upwards. Once desired speed is reached, drag the accerlation slider all the way down to zero. This will allow the Train to coast 

2. Change into Automatic Mode
In the upper right hand corner, click the 'automatic' button, the accerlation slider should automatically toggle and increase the speed of the Train

#### Decreasing the Speed 
1. Increase the brake slider to 1. The slider only has 2 states, 1 or 0.
2. In case of emergency, the EBrake Button will stop the train at a faster rate then the brake slider

#### Entering KI and KP
Type or use the arrows on the text boxes. The default values are optimal for operation but can be changed if so desired. The changes should only be made by the Train Engineer

#### Changing into Automatic/Manual Mode
Use the toggle buttons in the top left, the depressed button is the current mode.

#### Station Announcements 
Type the desired message in the box next to annoucement and press enter. The output should appear next to Current Output. 

#### Temperature

#### Door Control
Press open or close on the desired door. Doors cannot be opened while moving

#### Lighting Control

#### Interior 
In the upper right hand corner, next to Int, use the slider to either select 0 , 1 , 2. Where zero is off, one is dim, and two is full brightness


##### Exterior 
In the upper right hand corner, next to the text Headlights, select either on or off. The depressed button in the current satat


#### Automatic Functionality

#### Why isn't my Train Running?
1. Does the Train Have Authority?
If the train recieves an authority of zero, it will not move. Authority can be viewed on the right hand side labeled "Distance to Stop" 
2. Are either of the brakes enabled?

On the center of the screen there is brake slider, if the value is displaying '1', this means the service break is on.
Simply slide the slider down to turn it off

If either the
    3. Is the Train at a red light?
    4. Your Train is imputed?
        This is usually caused by the weight of your mama on the train

#### 

## License

[MIT](https://choosealicense.com/licenses/mit/)
