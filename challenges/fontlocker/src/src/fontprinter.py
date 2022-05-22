# This module keeps track of the fonts that are requested from

from flask import Blueprint, Response, request, send_file, send_from_directory, session


app = Blueprint('fontprinter', __name__)

# Available fonts
CHECKS = [{'class': 'char_0', 'local': 'Exo 2', 'online': 'ComicNeue', 'weight': 'normal', 'italic': True, 'expect_online': False, 'online_filename': 'ComicNeue-Italic.ttf'},
          {'class': 'char_1', 'local': 'ComicNeue', 'online': 'Anton', 'weight': 'normal',
              'italic': False, 'expect_online': False, 'online_filename': 'Anton-Regular.ttf'},
          {'class': 'char_2', 'local': 'Mukta', 'online': 'Rubik', 'weight': 'lighter',
              'italic': False, 'expect_online': False, 'online_filename': 'Rubik-Light.ttf'},
          {'class': 'char_3', 'local': 'Poppins', 'online': 'Anybody', 'weight': 'normal',
              'italic': True, 'expect_online': False, 'online_filename': 'Anybody-Italic.ttf'},
          {'class': 'char_4', 'local': 'Tourney', 'online': 'Teko', 'weight': 'normal',
           'italic': False, 'expect_online': False, 'online_filename': 'Teko-Regular.ttf'},
          {'class': 'char_5', 'local': 'Radio Canada', 'online': 'Righteous', 'weight': 'normal',
           'italic': False, 'expect_online': True, 'online_filename': 'Righteous-Regular.ttf'},
          {'class': 'char_6', 'local': 'Radio Canada Condensed', 'online': 'ComicNeue', 'weight': 'bold',
           'italic': False, 'expect_online': True, 'online_filename': 'ComicNeue-Bold.ttf'},
          {'class': 'char_7', 'local': 'Mukta', 'online': 'Poppins', 'weight': 'lighter',
           'italic': False, 'expect_online': True, 'online_filename': 'Poppins-ExtraLight.ttf'},
          {'class': 'char_8', 'local': 'Barlow Semi Condensed', 'online': 'NanumGothic', 'weight': 'lighter',
              'italic': True, 'expect_online': False, 'online_filename': 'Poppins-ThinItalic.ttf'},
          {'class': 'char_9', 'local': 'Radio Canada Condensed', 'online': 'Questrial', 'weight': 'normal',
              'italic': False, 'expect_online': True, 'online_filename': 'Questrial-Regular.ttf'}]
_DB = [x['local'] for x in CHECKS]
EXPECTED_FINGERPRINT = [x['expect_online'] for x in CHECKS]


class FontSession:
    def __init__(self, data=[False for x in range(len(CHECKS))]):
        self.data = data

    def add_font_request(self, font: str):
        font_entry_opt = next(filter(
            lambda item: item[1]["online_filename"] == font, enumerate(CHECKS)), None)
        if font_entry_opt is None:
            return None

        idx, entry = font_entry_opt

        italics = entry["italic"]
        weight = entry["weight"]
        self.data[idx] = True

    def debug_print(self):
        print("FP :\t\t", self.data)

    def get_data(self) -> list:
        return self.data

    def data_reset(self):
        self.data = [None for x in range(len(CHECKS))]

    def is_good_for_safe(self) -> bool:
        return self.data == EXPECTED_FINGERPRINT


def generate_stylesheet():
    """Generates the stylesheet to create a fingerprint of the installed fonts at runtime (lazy, aka only once)"""
    output = ""
    output_fonts = ""

    # Verify that the weight of pairs of fonts is the same

    # Add the selectors
    for check in CHECKS:
        class_name = check["class"]
        local = check["local"]
        online = check["online"]
        weight = check["weight"]
        italic = check["italic"]
        online_filename = check["online_filename"]
        italic_str = " font-style: italic;" if italic else ""

        output += "#%s { font-family: '%s', '%s'; font-weight: %s;%s }\n" % (
            class_name, local, online, weight, italic_str)

        # Add fontface declarations
        output_fonts += "@font-face { font-family: '%s'; font-weight: %s;%s src: url(fonts/%s); }\n" % (
            online, weight, italic_str, online_filename)

    return output + output_fonts


_GENERATED_STYLESHEET = generate_stylesheet()


@app.route("/fonts.css", methods=["GET"])
def stylesheet():
    """Returns the stylesheet, generated from the list of available fonts above."""
    return Response(_GENERATED_STYLESHEET, 200, mimetype="text/css")


@app.route("/fonts/<font>")
def download_font(font: str):
    """Route to track fonts."""
    fsession = None
    if session.get("fingerprint") is None:
        fsession = FontSession()
    else:
        fsession = FontSession(session["fingerprint"])
    fsession.add_font_request(font)

    session["fingerprint"] = fsession.get_data()
    response = send_from_directory("fonts", font)

    # Make the challenge a little doable
    response.headers["Cache-Control"] = "no-store, must-revalidate"
    #response.headers["Cache-Control"] = "max-age=1"
    response.headers["Expires"] = "0"
    return response
