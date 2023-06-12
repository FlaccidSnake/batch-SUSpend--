# Import the main window object (mw) from aqt
from aqt import mw
from anki.hooks import addHook
# Import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# Import all of the Qt GUI library
from aqt.qt import *
import glob
import os

from . import const

# Create Rule window
class CreateRuleDialog(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Create Unsuspend Rule")

		# Dialog layout
		layout = QGridLayout()
		self.setLayout(layout)
		self.rule_saved = pyqtSignal()
		# Create Save button
		self.save_button = QPushButton("Save")
		self.save_button.clicked.connect(self.save_options)

		layout.addWidget(QLabel("Name"), 0, 0, Qt.AlignCenter)
		layout.addWidget(QLabel("Tag"), 0, 1, Qt.AlignCenter)
		layout.addWidget(QLabel("Count"), 0, 2, Qt.AlignCenter)
		layout.addWidget(QLabel("Every day(s)"), 0, 3, Qt.AlignCenter)
		
		# Initialise values
		self.rule_name = QLineEdit()
		self.tag_box = QComboBox()
		tags = mw.col.tags.all()
		self.tag_box.addItems(tags)
		self.count_box = QSpinBox(value=0, minimum=1, maximum=999)
		self.days_box = QSpinBox(value=1, minimum=1, maximum=30)

		# Add widgets to gird
		layout.addWidget(self.rule_name, 1, 0)
		layout.addWidget(self.tag_box, 1, 1)
		layout.addWidget(self.count_box, 1, 2)
		layout.addWidget(self.days_box, 1, 3)

		layout.addWidget(self.save_button, 2, 0, 2, 4, Qt.AlignCenter)# Qt6,  alignment=Qt.AlignmentFlag.AlignRight)

	# Save options
	def save_options(self):
		selected_rule_name = self.rule_name.text()
		selected_tag = self.tag_box.currentText()
		selected_count = self.count_box.value()
		selected_days = self.days_box.value()

		rule_dict = {}
		rule_dict["tag"] = selected_tag
		rule_dict["count"] = selected_count
		rule_dict["days"] = selected_days

		const.CONFIG["Rules"][selected_rule_name] = rule_dict

		mw.addonManager.writeConfig(const.ADDON_NAME, const.CONFIG)
		# Reload Meta and refresh options_dialog screen
		const.META = const.load_meta(const.META_PATH)
		self.close()