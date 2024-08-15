Motion Detection with Visualization
This project consists of two main components:

Motion Detection Script: Detects motion from a video feed and records the start and end times of detected motion.
Bokeh Visualization: Visualizes the recorded motion events as a graph.
Components
1. Motion Detection Script
File: motion_detector.py

This script uses OpenCV to detect motion in a video feed from the webcam. It captures the start and end times of detected motion and saves this data to a CSV file.

Features
Motion Detection: Detects motion by comparing frames and analyzing changes.
Time Recording: Records the start and end times of motion events.
CSV Output: Saves motion times to Times.csv.
Installation and Usage
Dependencies:

Install OpenCV and pandas using pip:

pip install opencv-python pandas

Run the Script:

Execute the motion_detector.py script to start the motion detection:

python motion_detector.py

Press 'q' to stop the script and save the recorded times to Times.csv.
2. Bokeh Visualization
File: plot_motion.py

This script reads the motion times from Times.csv, processes the data, and creates a visualization using Bokeh. The resulting HTML file shows a graph of detected motion events.

Features
Data Processing: Reads and formats motion times from the CSV file.
Graph Visualization: Displays a candlestick chart representing motion events.
Interactive Plot: Hover over the plot to see the start and end times of motion events.
Installation and Usage
Dependencies:

Install Bokeh and pandas-datareader using pip:

pip install bokeh pandas-datareader

Run the Script:

Execute the plot_motion.py script to generate the visualization:

python plot_motion.py

Open Graph.html in a web browser to view the plot.
Example
Motion Detection:

Run motion_detector.py to capture motion times.
Visualization:

After running motion_detector.py, execute plot_motion.py to visualize the captured motion times.

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

Contact
For any inquiries or feedback, please reach out to [pramodkumar23la@gmail.com].
