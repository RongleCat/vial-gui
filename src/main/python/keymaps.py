from keycodes import Keycode
from keymap import danish, eurkey, french, german, hungarian, latam, norwegian, russian, slovak, spanish, swedish, swiss

KEYMAPS = [
    ("QWERTY", dict()),
    ("Danish (QWERTY)", danish.keymap),
    ("EurKey (QWERTY)", eurkey.keymap),
    ("French (AZERTY)", french.keymap),
    ("German (QWERTZ)", german.keymap),
    ("Hungarian (QWERTZ)", hungarian.keymap),
    ("Latin American (QWERTY)", latam.keymap),
    ("Norwegian (QWERTY)", norwegian.keymap),
    ("Russian (ЙЦУКЕН)", russian.keymap),
    ("Slovak (QWERTY)", slovak.keymap),
    ("Spanish (QWERTY)", spanish.keymap),
    ("Swedish (QWERTY)", swedish.keymap),
    ("Swiss (QWERTZ)", swiss.keymap)
]

# make sure that qmk IDs we used are all correct
for name, keymap in KEYMAPS:
    for qmk_id in keymap.keys():
        if Keycode.find_by_qmk_id(qmk_id) is None:
            raise RuntimeError("Misconfigured - cannot find QMK keycode {}".format(qmk_id))
