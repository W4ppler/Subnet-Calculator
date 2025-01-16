from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from netaddr import IPNetwork

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.label_ip_mask = QLabel("IP and Mask (XXX.XXX.XXX.XXX/XX):")
        self.input_ip_mask = QLineEdit()
        self.button_process = QPushButton("Process")
        self.label_output = QLabel("")

        # Layout widgets
        layout = QWidget()
        grid = QGridLayout(layout)
        grid.addWidget(self.label_ip_mask, 0, 0)
        grid.addWidget(self.input_ip_mask, 0, 1)
        grid.addWidget(self.button_process, 1, 0, 1, 2)
        grid.addWidget(self.label_output, 2, 0, 1, 2)
        self.setCentralWidget(layout)

        # Connect button click to process function
        self.button_process.clicked.connect(self.process_network)

    def process_network(self):
        try:
            network = self.input_ip_mask.text()
            net = IPNetwork(network)
            output = f"""
IP in binary:
{net.ip.bits()}

Mask in binary:
{net.netmask.bits()}

Mask:
{net.netmask}

Netaddress:
{net.network}

First Host:
{net.network + 1}

Last Host:
{net.broadcast - 1}

Broadcast address:
{net.broadcast}
"""
            self.label_output.setText(output)
        except:
            self.label_output.setText(f"Error: Invalid input format.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
