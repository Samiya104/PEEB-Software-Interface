import time
import platform
from PySide6.QtCore import QObject, Signal, QProcess

class ArduinoFlasher(QObject):
    progressUpdate = Signal(str)
    flashingComplete = Signal(bool, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.arduino_cli = QProcess(self)
        self.is_compiling = False

        # Connect process signals
        self.arduino_cli.readyReadStandardOutput.connect(self.handle_process_output)
        self.arduino_cli.readyReadStandardError.connect(self.handle_process_error_output)
        self.arduino_cli.finished.connect(self.handle_process_finished)
        self.arduino_cli.errorOccurred.connect(self.handle_process_error)

    def flash_sketch(self, sketch_path: str, port: str, board: str):
        program = self.get_arduino_cli_path()
        compile_args = ["compile", "--fqbn", board, sketch_path]

        self.progressUpdate.emit("Compiling sketch...")
        self.arduino_cli.start(program, compile_args)
        self.arduino_cli.waitForFinished()

        if self.arduino_cli.exitCode() != 0:
            error = self.arduino_cli.readAllStandardError().data().decode()
            self.flashingComplete.emit(False, f"Compilation failed: {error}")
            return

        time.sleep(1)

        upload_args = ["upload", "--fqbn", board, "--port", port, sketch_path]
        self.progressUpdate.emit("Uploading to Arduino...")
        self.arduino_cli.start(program, upload_args)

    def handle_process_output(self):
        output = self.arduino_cli.readAllStandardOutput().data().decode()
        self.progressUpdate.emit(output)

    def handle_process_error_output(self):
        error = self.arduino_cli.readAllStandardError().data().decode()
        self.progressUpdate.emit(f"Error: {error}")

    def handle_process_finished(self, exit_code, exit_status):
        if exit_code != 0:
            error = self.arduino_cli.readAllStandardError().data().decode()
            self.flashingComplete.emit(False, f"Process failed: {error}")
        else:
            self.flashingComplete.emit(True, "Successfully flashed Arduino!")

    def handle_process_error(self, error):
        error_messages = {
            QProcess.ProcessError.FailedToStart: "Failed to start Arduino CLI. Make sure it's installed correctly.",
            QProcess.ProcessError.Crashed: "Arduino CLI process crashed.",
            QProcess.ProcessError.Timedout: "Process timed out.",
            QProcess.ProcessError.WriteError: "Write error occurred.",
            QProcess.ProcessError.ReadError: "Read error occurred.",
            QProcess.ProcessError.UnknownError: "An unknown error occurred with Arduino CLI."
        }
        error_msg = error_messages.get(error, "An error occurred with Arduino CLI")
        self.flashingComplete.emit(False, error_msg)

    def get_arduino_cli_path(self) -> str:
        if platform.system() == 'Windows':
            return "C:/Users/qasmi/arduino-cli_1.1.1_Windows_32bit/arduino-cli.exe"
        return "/usr/local/bin/arduino-cli"
