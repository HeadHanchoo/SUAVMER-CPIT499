from datetime import datetime, timedelta
import os
import hashlib
import uuid
import csv

# SUAVMER simple mission report + manifest + image metadata + simulated image files + QC report
# This is an early prototype for local mission logging, image metadata, file integrity, and quality control.

def calculate_checksum(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


mission_id = str(uuid.uuid4())[:8]
mission_name = "Mapping Grid Mission Test"
mission_type = "Mapping / Lawnmower Grid"
altitude_m = 20
number_of_waypoints = 8
expected_images = 8
mission_status = "Completed"
notes = "The drone successfully followed a grid-style mapping route in Gazebo using PX4 and QGroundControl."

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

os.makedirs("logs", exist_ok=True)
os.makedirs("metadata", exist_ok=True)
os.makedirs("images", exist_ok=True)

report_filename = f"logs/mission_report_{timestamp}.txt"
manifest_filename = f"logs/manifest_{timestamp}.txt"
metadata_filename = f"metadata/image_metadata_{timestamp}.csv"
qc_report_filename = f"logs/qc_report_{timestamp}.txt"

simulated_image_files = []

# Create mission report
with open(report_filename, "w") as file:
    file.write("SUAVMER Mission Report\n")
    file.write("======================\n\n")
    file.write(f"Mission ID: {mission_id}\n")
    file.write(f"Mission Name: {mission_name}\n")
    file.write(f"Mission Type: {mission_type}\n")
    file.write(f"Date and Time: {now}\n")
    file.write(f"Altitude: {altitude_m} meters\n")
    file.write(f"Number of Waypoints: {number_of_waypoints}\n")
    file.write(f"Mission Status: {mission_status}\n")
    file.write(f"Notes: {notes}\n")

# Create simulated image metadata CSV and simulated image files
with open(metadata_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        "mission_id",
        "image_name",
        "capture_time",
        "waypoint_number",
        "altitude_m",
        "latitude",
        "longitude",
        "camera_angle",
        "capture_status",
        "image_file_path"
    ])

    for i in range(1, number_of_waypoints + 1):
        image_name = f"image_{i:03}.txt"
        image_path = f"images/{image_name}"
        capture_time = now + timedelta(seconds=i * 5)
        waypoint_number = i
        latitude = 21.000000 + (i * 0.000010)
        longitude = 39.000000 + (i * 0.000010)
        camera_angle = "Downward"
        capture_status = "Captured"

        with open(image_path, "w") as image_file:
            image_file.write("SUAVMER Simulated Image File\n")
            image_file.write("============================\n")
            image_file.write(f"Mission ID: {mission_id}\n")
            image_file.write(f"Image Name: {image_name}\n")
            image_file.write(f"Capture Time: {capture_time}\n")
            image_file.write(f"Waypoint Number: {waypoint_number}\n")
            image_file.write(f"Altitude: {altitude_m} meters\n")
            image_file.write(f"Latitude: {latitude}\n")
            image_file.write(f"Longitude: {longitude}\n")
            image_file.write(f"Camera Angle: {camera_angle}\n")
            image_file.write("Note: This is a placeholder file for simulated image capture.\n")

        simulated_image_files.append(image_path)

        writer.writerow([
            mission_id,
            image_name,
            capture_time,
            waypoint_number,
            altitude_m,
            latitude,
            longitude,
            camera_angle,
            capture_status,
            image_path
        ])

# Basic quality-control calculations
captured_images = len(simulated_image_files)
capture_success_rate = (captured_images / expected_images) * 100

if captured_images == expected_images and mission_status == "Completed":
    qc_result = "PASS"
else:
    qc_result = "FAIL"

coverage_estimate = "100%" if qc_result == "PASS" else "Incomplete"
overlap_status = "Simulated overlap check passed"

# Create quality-control report
with open(qc_report_filename, "w") as file:
    file.write("SUAVMER Quality Control Report\n")
    file.write("==============================\n\n")
    file.write(f"Mission ID: {mission_id}\n")
    file.write(f"Mission Type: {mission_type}\n")
    file.write(f"Mission Status: {mission_status}\n")
    file.write(f"Expected Images: {expected_images}\n")
    file.write(f"Captured Images: {captured_images}\n")
    file.write(f"Capture Success Rate: {capture_success_rate:.2f}%\n")
    file.write(f"Coverage Estimate: {coverage_estimate}\n")
    file.write(f"Overlap Status: {overlap_status}\n")
    file.write(f"QC Result: {qc_result}\n\n")
    file.write("Notes:\n")
    file.write("This is a simulated QC report. Later, these values can be calculated from real captured images, telemetry, and mapping coverage.\n")

# Calculate checksums
report_checksum = calculate_checksum(report_filename)
metadata_checksum = calculate_checksum(metadata_filename)
qc_report_checksum = calculate_checksum(qc_report_filename)

image_checksums = []
for image_path in simulated_image_files:
    checksum = calculate_checksum(image_path)
    image_checksums.append((image_path, checksum))

# Create manifest file
with open(manifest_filename, "w") as file:
    file.write("SUAVMER Mission Manifest\n")
    file.write("========================\n\n")
    file.write(f"Mission ID: {mission_id}\n")
    file.write(f"Created At: {now}\n")
    file.write(f"Mission Type: {mission_type}\n")
    file.write(f"Mission Status: {mission_status}\n\n")

    file.write("Output Files:\n")
    file.write("-------------\n\n")

    file.write(f"File Name: {report_filename}\n")
    file.write("File Type: Mission Report\n")
    file.write(f"SHA256 Checksum: {report_checksum}\n\n")

    file.write(f"File Name: {metadata_filename}\n")
    file.write("File Type: Image Metadata CSV\n")
    file.write(f"SHA256 Checksum: {metadata_checksum}\n\n")

    file.write(f"File Name: {qc_report_filename}\n")
    file.write("File Type: Quality Control Report\n")
    file.write(f"SHA256 Checksum: {qc_report_checksum}\n\n")

    file.write("Simulated Image Files:\n")
    file.write("----------------------\n")

    for image_path, checksum in image_checksums:
        file.write(f"File Name: {image_path}\n")
        file.write("File Type: Simulated Image Placeholder\n")
        file.write(f"SHA256 Checksum: {checksum}\n\n")

print(f"Mission report created successfully: {report_filename}")
print(f"Image metadata created successfully: {metadata_filename}")
print("Simulated image files created successfully in: images/")
print(f"Quality control report created successfully: {qc_report_filename}")
print(f"Mission manifest created successfully: {manifest_filename}")
