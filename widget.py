import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader
from arduino_flasher import ArduinoFlasher
from light_data_collection import DataCollector

class ArduinoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load the UI file
        loader = QUiLoader()
        self.ui = loader.load('form.ui', self)

        self.arduino_uno_vendor_id = 9025
        self.arduino_uno_product_id = 67
        self.arduino_is_available = False
        self.arduino_port_name = ""
        self.arduino = QSerialPort()

        self.flasher = ArduinoFlasher(self)
        self.flasher.progressUpdate.connect(self.on_progress_update)
        self.flasher.flashingComplete.connect(self.on_flashing_complete)

        self.data_collector = DataCollector(self)
        self.data_collector.dataUpdated.connect(self.update_sensor_display)

        # Connect all signals
        self.ui.Led_On.clicked.connect(self.on_LED_On_clicked)
        self.ui.Led_Off.clicked.connect(self.on_LED_Off_clicked)
        self.ui.Button_On.clicked.connect(self.on_Button_On_clicked)
        self.ui.Button_Off.clicked.connect(self.on_Button_Off_clicked)

        self.ui.set_0.clicked.connect(self.set_to_0)
        self.ui.set_90.clicked.connect(self.set_to_90)
        self.ui.set_180.clicked.connect(self.set_to_180)

        self.ui.servo_control_slide.valueChanged.connect(self.on_servo_slide_changed)
        self.ui.servo_control_rotate.valueChanged.connect(self.on_servo_rotate_changed)

        self.ui.Light_sensor_On.clicked.connect(self.on_Light_sensor_On_clicked)
        self.ui.Light_sensor_Off.clicked.connect(self.on_Light_sensor_Off_clicked)

        self.ui.startDataButton.clicked.connect(self.start_data_collection)
        self.ui.stopDataButton.clicked.connect(self.stop_data_collection)
        self.ui.stopDataButton.setEnabled(False)

        self.ui.browseButton.clicked.connect(self.browse_clicked)
        self.ui.flashButton.clicked.connect(self.flash_clicked)

        self.detect_arduino()
        self.setup_arduino()

    def detect_arduino(self):
        for port_info in QSerialPortInfo.availablePorts():
            if (port_info.hasVendorIdentifier() and
                port_info.hasProductIdentifier() and
                port_info.vendorIdentifier() == self.arduino_uno_vendor_id and
                port_info.productIdentifier() == self.arduino_uno_product_id):
                self.arduino_port_name = port_info.portName()
                self.arduino_is_available = True
                self.ui.status_label.setText(f"Arduino Status: Found on {self.arduino_port_name}")
                break

    def setup_arduino(self):
        if self.arduino_is_available:
            self.arduino.setPortName(self.arduino_port_name)
            if self.arduino.open(QSerialPort.OpenModeFlag.ReadWrite):
                self.arduino.setBaudRate(QSerialPort.BaudRate.Baud9600)
                self.arduino.setDataBits(QSerialPort.DataBits.Data8)
                self.arduino.setParity(QSerialPort.Parity.NoParity)
                self.arduino.setStopBits(QSerialPort.StopBits.OneStop)
                self.arduino.setFlowControl(QSerialPort.FlowControl.NoFlowControl)
            else:
                QMessageBox.warning(self, "Port Error", "Couldn't open the Arduino port")
        else:
            QMessageBox.warning(self, "Port Error", "Couldn't find the Arduino")

    def on_LED_On_clicked(self):
        if self.arduino and self.arduino.isWritable():
            if self.ui.checkRed.isChecked():
                self.arduino.write(b'R')
            if self.ui.checkYellow.isChecked():
                self.arduino.write(b'Y')
            if self.ui.checkBlue.isChecked():
                self.arduino.write(b'B')

    def on_LED_Off_clicked(self):
        if self.arduino and self.arduino.isWritable():
            if self.ui.checkRed.isChecked():
                self.arduino.write(b'r')
            if self.ui.checkYellow.isChecked():
                self.arduino.write(b'y')
            if self.ui.checkBlue.isChecked():
                self.arduino.write(b'b')

    def on_Button_On_clicked(self):
        if self.arduino and self.arduino.isWritable():
            self.arduino.write(b'o')
            self.arduino.flush()

    def on_Button_Off_clicked(self):
        if self.arduino and self.arduino.isWritable():
            self.arduino.write(b'c')
            self.arduino.flush()

    def set_to_0(self):
        if self.arduino and self.arduino.isWritable():
            command = "0\n"
            self.arduino.write(command.encode())
            self.arduino.flush()

    def set_to_90(self):
        if self.arduino and self.arduino.isWritable():
            command = "90\n"
            self.arduino.write(command.encode())
            self.arduino.flush()

    def set_to_180(self):
        if self.arduino and self.arduino.isWritable():
            command = "180\n"
            self.arduino.write(command.encode())
            self.arduino.flush()

    def set_servo_position(self, position):
        if self.arduino and self.arduino.isWritable():
            command = f"{position}\n"
            self.arduino.write(command.encode())
            self.arduino.flush()

    def on_servo_slide_changed(self, value):
        self.set_servo_position(value)

    def on_servo_rotate_changed(self, value):
        self.set_servo_position(value)

    def on_Light_sensor_On_clicked(self):
        if self.arduino and self.arduino.isWritable():
            self.arduino.write(b'o')  # 'o' for open/turn on
            self.arduino.flush()
            self.ui.status_label.setText("Light Sensor: Turned ON")

    def on_Light_sensor_Off_clicked(self):
        if self.arduino and self.arduino.isWritable():
            self.arduino.write(b'c')  # 'c' for close/turn off
            self.arduino.flush()
            self.ui.status_label.setText("Light Sensor: Turned OFF")

    def start_data_collection(self):
        self.data_collector.set_arduino(self.arduino)
        filename = self.data_collector.start_collection()
        self.ui.startDataButton.setEnabled(False)
        self.ui.stopDataButton.setEnabled(True)
        self.ui.status_label.setText(f"Data collection started: {filename}")

    def stop_data_collection(self):
        self.data_collector.stop_collection()
        self.ui.startDataButton.setEnabled(True)
        self.ui.stopDataButton.setEnabled(False)
        self.ui.status_label.setText("Data collection stopped. Plot and statistics saved.")

    def update_sensor_display(self, value):
        self.ui.sensorValueLabel.setText(f"Sensor Value: {value:.2f}")

    def browse_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Arduino Sketch",
            "",
            "Arduino Sketches (*.ino)"
        )
        if file_name:
            self.ui.sketchPathEdit.setText(file_name)

    def flash_clicked(self):
        if not self.ui.sketchPathEdit.text():
            self.ui.flashStatusLabel.setText("Please select a sketch file")
            return

        if not self.arduino_is_available:
            self.ui.flashStatusLabel.setText("Arduino not detected. Please connect the device.")
            return

        was_open = False
        if self.arduino and self.arduino.isOpen():
            was_open = True
            self.arduino.close()

        self.ui.flashButton.setEnabled(False)
        self.ui.flashStatusLabel.setText("Starting flash process...")

        self.flasher.flash_sketch(
            self.ui.sketchPathEdit.text(),
            self.arduino_port_name,
            "arduino:avr:uno"
        )

        QTimer.singleShot(3000, lambda: self.restore_connection(was_open))

    def restore_connection(self, was_open):
        if was_open:
            self.setup_arduino()
            self.ui.flashStatusLabel.setText("Flash completed - Ready to use!")
        self.ui.flashButton.setEnabled(True)

    def on_progress_update(self, status):
        self.ui.flashStatusLabel.setText(status)

    def on_flashing_complete(self, success, message):
        if success:
            self.ui.flashStatusLabel.setText("Flashing successful - Restoring connection...")
        else:
            self.ui.flashStatusLabel.setText(message)
            self.ui.flashButton.setEnabled(True)

            if self.arduino and not self.arduino.isOpen():
                self.setup_arduino()

    def closeEvent(self, event):
        if hasattr(self, 'data_collector') and self.data_collector.is_collecting:
            self.data_collector.stop_collection()
        if self.arduino and self.arduino.isOpen():
            self.arduino.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ArduinoWidget()
    widget.show()
    sys.exit(app.exec())
