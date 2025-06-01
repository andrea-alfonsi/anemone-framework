from signatureflow.datatypes.image import Image
import pytest


def black_png():
    return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdjYGBg+A8AAQQBAHAgZQsAAAAASUVORK5CYII="


def transparent_png():
    return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAAtJREFUGFdjYAACAAAFAAGq1chRAAAAAElFTkSuQmCC"


@pytest.mark.parametrize("data", [black_png(), transparent_png()])
def test_png(data: str):
    image = Image(shape=(1, 1, 4))
    assert image.validate(data) == None


# TODO: add tests with other formats too
