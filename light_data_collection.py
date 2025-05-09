from PySide6.QtCore import QObject, Signal, Slot, QTimer
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os

class DataCollector(QObject):
    dataUpdated = Signal(float)  # Signal to emit new sensor readings

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_collecting = False
        self.data = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_sensor)
        self.arduino = None
        self.csv_file = None
        self.csv_writer = None
        self.current_file = None

    def set_arduino(self, arduino):
        self.arduino = arduino

    def start_collection(self, filename=None):
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"sensor_data_{timestamp}.csv"

        self.current_file = filename
        self.csv_file = open(filename, 'w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['Timestamp', 'Sensor Value'])

        # Turn on the sensor
        if self.arduino and self.arduino.isWritable():
            self.arduino.write(b'o')
            self.arduino.flush()

        self.is_collecting = True
        self.timer.start(100)  # Read every 100ms to match Arduino delay
        return filename

    def stop_collection(self):
        # Turn off the sensor
        if self.arduino and self.arduino.isWritable():
            self.arduino.write(b'c')
            self.arduino.flush()

        self.timer.stop()
        self.is_collecting = False
        if self.csv_file:
            self.csv_file.close()
            self.plot_data()

    @Slot()
    def read_sensor(self):
        if not self.arduino or not self.arduino.isReadable():
            return

        if self.arduino.waitForReadyRead(100):  # Shorter timeout since we're reading frequently
            data = self.arduino.readLine().data().decode().strip()
            try:
                # Check if the data is a number and not "ON" or "OFF"
                if data not in ["ON", "OFF"]:
                    value = float(data)
                    timestamp = datetime.now()
                    self.csv_writer.writerow([timestamp.strftime("%Y-%m-%d %H:%M:%S"), value])
                    self.dataUpdated.emit(value)
            except ValueError:
                # Ignore non-numeric values (like "ON" or "OFF" messages)
                pass

    def plot_data(self):
        if not self.current_file or not os.path.exists(self.current_file):
            return

        df = pd.read_csv(self.current_file)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        plt.figure(figsize=(12, 8))

        # Create the main plot
        plt.subplot(2, 1, 1)
        plt.plot(df['Timestamp'], df['Sensor Value'], 'b-', label='Sensor Values')
        plt.title('Light Sensor Data Over Time')
        plt.xlabel('Time')
        plt.ylabel('Sensor Value')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()

        # Add a histogram of values
        plt.subplot(2, 1, 2)
        plt.hist(df['Sensor Value'], bins=50, color='green', alpha=0.7)
        plt.title('Distribution of Sensor Values')
        plt.xlabel('Sensor Value')
        plt.ylabel('Frequency')
        plt.grid(True)

        plt.tight_layout()

        # Save plot with same name as CSV but with .png extension
        plot_file = self.current_file.rsplit('.', 1)[0] + '.png'
        plt.savefig(plot_file)
        plt.close()

        # Generate statistics
        stats_file = self.current_file.rsplit('.', 1)[0] + '_stats.txt'
        with open(stats_file, 'w') as f:
            f.write("Light Sensor Data Statistics\n")
            f.write("==========================\n")
            f.write(f"Total Readings: {len(df)}\n")
            f.write(f"Average Value: {df['Sensor Value'].mean():.2f}\n")
            f.write(f"Maximum Value: {df['Sensor Value'].max():.2f}\n")
            f.write(f"Minimum Value: {df['Sensor Value'].min():.2f}\n")
            f.write(f"Standard Deviation: {df['Sensor Value'].std():.2f}\n")
