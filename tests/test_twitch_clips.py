import pytest
import sys
import twitch_clips
from selenium.common.exceptions import *


def test_load_category_with_error():
    twitch = twitch_clips.TwitchClips()
    with pytest.raises(NoSuchElementException):
        twitch.load_category("drfh")


def test_load_category():
    twitch = twitch_clips.TwitchClips()
    try:
        twitch.load_category("chess")
    except NoSuchElementException:
        pytest.fail("This category provoke an error for load_category...")

