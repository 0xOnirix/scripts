import sys
from Evtx.Evtx import Evtx
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox, QTreeWidget, QTreeWidgetItem,
    QTextEdit, QVBoxLayout, QWidget, QHeaderView, QLabel, QHBoxLayout
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QByteArray

###################### ASSETS #######################

svg_error = '''
<svg viewBox="-2.4 -2.4 28.80 28.80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd"
        d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2
           2 6.477 2 12s4.477 10 10 10zm-1.5-5.009c0-.867.659-1.491
           1.491-1.491.85 0 1.509.624 1.509 1.491 0 .867-.659
           1.509-1.509 1.509-.832 0-1.491-.642-1.491-1.509zM11.172
           6a.5.5 0 0 0-.499.522l.306 7a.5.5 0 0 0 .5.478h1.043a.5.5
           0 0 0 .5-.478l.305-7a.5.5 0 0 0-.5-.522h-1.655z"
        fill="#e01b24"></path>
</svg>
'''

svg_warning = '''
<svg viewBox="-51.2 -51.2 614.40 614.40" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round" stroke="#CCCCCC" stroke-width="8.192"></g><g id="SVGRepo_iconCarrier"> <title>warning-filled</title> <g id="Page-1" stroke-width="0.00512" fill="none" fill-rule="evenodd"> <g id="add" fill="#f6d32d" transform="translate(32.000000, 42.666667)"> <path d="M246.312928,5.62892705 C252.927596,9.40873724 258.409564,14.8907053 262.189374,21.5053731 L444.667042,340.84129 C456.358134,361.300701 449.250007,387.363834 428.790595,399.054926 C422.34376,402.738832 415.04715,404.676552 407.622001,404.676552 L42.6666667,404.676552 C19.1025173,404.676552 7.10542736e-15,385.574034 7.10542736e-15,362.009885 C7.10542736e-15,354.584736 1.93772021,347.288125 5.62162594,340.84129 L188.099293,21.5053731 C199.790385,1.04596203 225.853517,-6.06216498 246.312928,5.62892705 Z M224,272 C208.761905,272 197.333333,283.264 197.333333,298.282667 C197.333333,313.984 208.415584,325.248 224,325.248 C239.238095,325.248 250.666667,313.984 250.666667,298.624 C250.666667,283.264 239.238095,272 224,272 Z M245.333333,106.666667 L202.666667,106.666667 L202.666667,234.666667 L245.333333,234.666667 L245.333333,106.666667 Z" id="Combined-Shape"> </path> </g> </g> </g></svg>
'''

svg_informations = '''
<svg fill="#7ed0ec" viewBox="-1 0 19 19" xmlns="http://www.w3.org/2000/svg" class="cf-icon-svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M16.417 9.583A7.917 7.917 0 1 1 8.5 1.666a7.917 7.917 0 0 1 7.917 7.917zM9.64 5.78a1.136 1.136 0 1 0-1.136 1.135A1.136 1.136 0 0 0 9.64 5.781zm-.344 2.884a.792.792 0 1 0-1.583 0v5.203a.792.792 0 0 0 1.583 0z"></path></g></svg>
'''
##################### DICTIONARIES ###################

suid_labels = {
    'S-1-5-18': 'System',
    'S-1-5-19': 'Local Service',
    'S-1-5-20': 'Network Service',
}

event_id_labels = {
    # Add labels for Event IDs if needed
}

level_labels = {
    '0': 'Success Audit',
    '1': 'Failure Audit',
    '2': 'Error',
    '3': 'Warning',
    '4': 'Information'
}

#######################################################

# Define XML namespaces
ns = {'ns': 'http://schemas.microsoft.com/win/2004/08/events/event'}

def parse_evtx(evtx_file):
    """
    Parses an EVTX file and extracts event information.

    Args:
        evtx_file (str): Path to the EVTX file.

    Returns:
        list: A list of dictionaries containing event information.
    """
    events = []
    with Evtx(evtx_file) as evtx:
        for record in evtx.records():
            xml_content = record.xml()
            root = ET.fromstring(xml_content)

            # Extract elements from the XML tree
            provider = root.find('.//ns:System/ns:Provider', ns)
            event_id = root.find('.//ns:System/ns:EventID', ns)
            version = root.find('.//ns:System/ns:Version', ns)
            level = root.find('.//ns:System/ns:Level', ns)
            opcode = root.find('.//ns:System/ns:Opcode', ns)
            keywords = root.find('.//ns:System/ns:Keywords', ns)
            time_created = root.find('.//ns:System/ns:TimeCreated', ns)
            event_record_id = root.find('.//ns:System/ns:EventRecordID', ns)
            execution = root.find('.//ns:System/ns:Execution', ns)
            channel = root.find('.//ns:System/ns:Channel', ns)
            computer = root.find('.//ns:System/ns:Computer', ns)
            security = root.find('.//ns:System/ns:Security', ns)
            event_data = root.findall('.//ns:EventData/ns:Data', ns)

            # Build a dictionary with the extracted information
            event_info = {
                'Provider Name': provider.attrib.get('Name', '') if provider is not None else '',
                'Event Source Name': provider.attrib.get('EventSourceName', '') if provider is not None else '',
                'Event ID': event_id.text if event_id is not None else '',
                'Version': version.text if version is not None else '',
                'Level': level.text if level is not None else '',
                'Opcode': opcode.text if opcode is not None else '',
                'Keywords': keywords.text if keywords is not None else '',
                'Time Created': time_created.attrib.get('SystemTime', '') if time_created is not None else '',
                'Event Record ID': event_record_id.text if event_record_id is not None else '',
                'Process ID': execution.attrib.get('ProcessID', '') if execution is not None else '',
                'Thread ID': execution.attrib.get('ThreadID', '') if execution is not None else '',
                'Channel': channel.text if channel is not None else '',
                'Computer': computer.text if computer is not None else '',
                'Security User ID (SUID)': security.attrib.get('UserID', '') if security is not None else '',
                'Event Data': {}
            }

            # Extract event data if available
            if event_data:
                for data in event_data:
                    name = data.attrib.get('Name', '')
                    value = data.text if data.text is not None else ''
                    event_info['Event Data'][name] = value

            events.append(event_info)
    return events


class EvtxViewer(QMainWindow):
    """Main window class for the EVTX Viewer application."""

    def __init__(self, events):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("EVTX Viewer")
        self.resize(800, 600)
        self.events = events

        # Maximize the window
        self.showMaximized()

        # Create the main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        # Create the QTreeWidget
        self.tree = QTreeWidget()
        self.tree.setColumnCount(4)
        self.tree.setHeaderLabels(['Level', 'Time Created', 'Provider Name', 'Event ID'])
        self.tree.header().setSectionResizeMode(QHeaderView.Stretch)
        self.tree.itemDoubleClicked.connect(self.show_event_details)
        layout.addWidget(self.tree)

        # Load icons
        self.load_icons()

        # Populate the QTreeWidget with events
        self.populate_tree()

    def load_icons(self):
        """Load SVG icons for different event levels."""
        self.level_icons = {}

        # Load error icon (Level 2)
        pixmap_error = QPixmap()
        pixmap_error.loadFromData(QByteArray(svg_error.encode('utf-8')), 'SVG')
        icon_error = QIcon(pixmap_error)
        self.level_icons['2'] = icon_error  # Level 2 corresponds to an error

        # Load warning icon (Level 3)
        pixmap_warning = QPixmap()
        pixmap_warning.loadFromData(QByteArray(svg_warning.encode('utf-8')), 'SVG')
        icon_warning = QIcon(pixmap_warning)
        self.level_icons['3'] = icon_warning  # Level 3 corresponds to a warning

        # Load informaitons icon (Level 4)
        pixmap_informations = QPixmap()
        pixmap_informations.loadFromData(QByteArray(svg_informations.encode('utf-8')), 'SVG')
        icon_informations = QIcon(pixmap_informations)
        self.level_icons['4'] = icon_informations  # Level 4 corresponds to an informations

        # You can load other icons for different levels here

    def populate_tree(self):
        """Populate the tree widget with event data."""
        for idx, event_info in enumerate(self.events):
            level = event_info.get('Level', '')
            level_label = level_labels.get(level, level)
            display_level = f"{level_label} ({level})" if level_label != level else level

            # Create a QTreeWidgetItem
            item = QTreeWidgetItem([
                display_level,
                event_info['Time Created'],
                event_info['Provider Name'],
                event_info['Event ID']
            ])

            # Add the icon if available
            icon = self.level_icons.get(level)
            if icon:
                item.setIcon(0, icon)

            # Store the event index for later access
            item.setData(0, Qt.UserRole, idx)

            self.tree.addTopLevelItem(item)

    def show_event_details(self, item, column):
        """Display the details of the selected event in a new window."""
        idx = item.data(0, Qt.UserRole)
        event_info = self.events[idx]

        level = event_info.get('Level', '')
        level_label = level_labels.get(level, level)
        display_level = f"{level_label} ({level})" if level_label != level else level

        # Prepare the event details
        details = (
            f"Provider Name             : {event_info['Provider Name']}\n"
            f"Event Source Name         : {event_info['Event Source Name']}\n"
            f"Event ID                  : {event_info['Event ID']}\n"
            f"Version                   : {event_info['Version']}\n"
            f"Level                     : {display_level}\n"
            f"Opcode                    : {event_info['Opcode']}\n"
            f"Keywords                  : {event_info['Keywords']}\n"
            f"Time Created              : {event_info['Time Created']}\n"
            f"Event Record ID           : {event_info['Event Record ID']}\n"
            f"Process ID                : {event_info['Process ID']}\n"
            f"Thread ID                 : {event_info['Thread ID']}\n"
            f"Channel                   : {event_info['Channel']}\n"
            f"Computer                  : {event_info['Computer']}\n"
            f"Security User ID (SUID)   : {event_info['Security User ID (SUID)']}\n"
        )

        # Add event data if available
        if event_info['Event Data']:
            details += "Event Data:\n"
            for name, value in event_info['Event Data'].items():
                details += f"  {name}: {value}\n"

        # Create a new window to display the details
        detail_window = QMainWindow(self)
        detail_window.setWindowTitle("Event Details")
        detail_window.resize(500, 400)

        # Create a central widget and layout
        central_widget = QWidget()
        detail_layout = QVBoxLayout(central_widget)

        # Create a horizontal layout for the level icon and label
        level_layout = QHBoxLayout()
        icon = self.level_icons.get(level)
        if icon:
            icon_label = QLabel()
            icon_label.setPixmap(icon.pixmap(32, 32))
            level_layout.addWidget(icon_label)

        # Create a label for the level text
        level_text_label = QLabel(f"Level: {display_level}")
        level_layout.addWidget(level_text_label)
        level_layout.addStretch()
        detail_layout.addLayout(level_layout)

        # Add the details text
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setText(details)
        detail_layout.addWidget(text_edit)

        detail_window.setCentralWidget(central_widget)
        detail_window.show()


def main():
    """
    Main function that prompts the user to select an EVTX file and displays the GUI.
    """
    app = QApplication(sys.argv)

    # Prompt the user to select an EVTX file
    options = QFileDialog.Options()
    evtx_file, _ = QFileDialog.getOpenFileName(
        None,
        "Select an EVTX file",
        "",
        "EVTX files (*.evtx)",
        options=options
    )
    if not evtx_file:
        QMessageBox.information(None, "Information", "No file selected. Exiting the program.")
        sys.exit()

    # Parse the EVTX file
    events = parse_evtx(evtx_file)

    # Sort events by 'Time Created' by default
    events.sort(key=lambda x: x['Time Created'])

    # Create and display the main window
    viewer = EvtxViewer(events)
    viewer.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
