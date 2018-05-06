from pywinauto.application import Application
from datetime import datetime
import os

class Voiceroid2:

    TITLE_PATTERN = "VOICEROID2\\*?"
    CLASS_NAME = "Window"
    BACKEND = "uia"

    def __init__(self):
        self.app = Application(backend=self.BACKEND).connect(title_re=self.TITLE_PATTERN, class_name=self.CLASS_NAME)
        self._define_controls()
        self._pre_binding()

    def _define_controls(self):
        dlg = self.app.top_window()
        self.ref_edit     = dlg.child_window(auto_id="TextBox")
        self.ref_play     = dlg.child_window(auto_id="c").Button3
        self.ref_save     = dlg.child_window(auto_id="c").Button7
        self.ref_filename = dlg.child_window(auto_id="1001", control_type="Edit")
        self.ref_done     = dlg.child_window(auto_id="2", control_type="Button")

    def _pre_binding(self):
        # this may reduce talk latency
        self.control_edit = self.ref_edit.wrapper_object()
        self.control_play = self.ref_play.wrapper_object()
        self.control_save = self.ref_save.wrapper_object()

    def _set_text(self, speaker, sentence):
        self.control_edit.set_edit_text("%s＞%s" % (speaker, sentence))

    def _play_text(self):
        self.control_play.click()

    def _generate_filename(self, path, speaker, sentence):
        name = "[%s] [%s] %s (%d)" % (datetime.now().strftime("%y%m%d"), speaker, sentence[:8], len(sentence))
        return os.path.join(path, name)

    def _save_speech(self, filename):
        self.control_save.click()
        control_filename = self.ref_filename.wrapper_object()
        control_filename.set_edit_text(filename)
        control_filename.type_keys("{ENTER}")
        self.ref_done.click()

    def talk(self, speaker, sentence):
        self._set_text(speaker, sentence)
        self._play_text()

    def export(self, speaker, sentence, path):
        filename = self._generate_filename(path, speaker, sentence)
        self._set_text(speaker, sentence)
        self._save_speech(filename)

# voiceroid = Voiceroid2()
# desktop_path = os.path.join(os.environ["HOMEPATH"], "Desktop")
# voiceroid.export("東北きりたん(v1)", "私は今もうこうした保留顔というのの以上で参りですた。もし今朝が矛盾順もどうもその攻撃うんなりへするているませをは忠告しななて、そうにはなるないませますた。貧民を着ますものはもち場合にかつてうですだ。", desktop_path)