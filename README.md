# SUAVMER-CPIT499

## Simulation-Based UAV System for Mapping and Emergency Response

SUAVMER is a graduation project prototype focused on simulation-based UAV mapping and emergency response. The system is designed to support a single operator by allowing the UAV to execute mapping-style missions, save local mission outputs, and generate post-flight reports.

## Current Prototype Status

The current prototype includes:

- PX4 SITL simulation
- Gazebo X500 drone simulation
- QGroundControl connection
- Takeoff and landing test
- Basic waypoint mission
- Mapping/lawnmower grid mission
- Local mission report generation
- Image metadata CSV generation
- Simulated image output files
- Mission manifest with SHA256 checksums
- Quality control report generation
- GitHub version control

## Tools Used

- PX4 Autopilot
- Gazebo Sim
- QGroundControl
- Ubuntu WSL2
- Python
- Git and GitHub

## Project Folder Structure

```text
SUAVMER/
├── images/
│   ├── image_001.txt
│   ├── image_002.txt
│   └── ...
├── logs/
│   ├── mission_report_*.txt
│   ├── manifest_*.txt
│   └── qc_report_*.txt
├── metadata/
│   └── image_metadata_*.csv
├── mission_report.py
└── README.md
```
How to Run

From the project folder, run:
cd ~/SUAVMER
python3 mission_report.py

The script generates:

A mission report
A mission manifest
An image metadata CSV file
Simulated image files
A quality control report
Quality Control Output

The current QC report checks:

Expected image count
Captured image count
Capture success rate
Coverage estimate
Simulated overlap status
Final QC result
Current Limitations

This is still an early prototype. The image files are simulated placeholder files, not real Gazebo camera images yet. The mission data is also manually simulated instead of being collected directly from PX4 telemetry.

Next Steps

Planned next steps:

Improve the logging system.
Connect the script to real PX4 telemetry.
Install and configure ROS 2.
Connect ROS 2 with PX4.
Create custom SUAVMER mission nodes.
Capture real simulated camera images.
Store mission data in PostgreSQL.
Generate more advanced quality-control reports.


