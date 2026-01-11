#!/usr/bin/env python3
"""
Claude Code Stop Hook - Task Completion Announcer
Plays pre-generated audio clips and sends Google Chat notifications
"""

import json
import os
import sys
import subprocess
import urllib.request
from pathlib import Path


def play_audio(audio_file):
    """Play audio file using system audio player"""
    try:
        # Use afplay on macOS
        subprocess.run(["afplay", str(audio_file)], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to play audio: {audio_file}")
    except FileNotFoundError:
        print(
            "Audio player not found. Install afplay or modify script for your system."
        )


def send_google_chat_notification(message):
    """Send notification to Google Chat space via webhook"""
    webhook_url = os.environ.get("GOOGLE_CHAT_WEBHOOK_URL")

    if not webhook_url:
        print("GOOGLE_CHAT_WEBHOOK_URL not set, skipping chat notification")
        return

    try:
        data = json.dumps({"text": message}).encode("utf-8")
        req = urllib.request.Request(
            webhook_url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        urllib.request.urlopen(req, timeout=5)
        print("Google Chat notification sent")
    except Exception as e:
        print(f"Failed to send Google Chat notification: {e}")


def main():
    """Main function for Claude Code stop hook"""
    print("Stop hook triggered!")

    # Default message
    notification_message = "Claude needs your attention!"

    # Override with specific message if provided as argument
    if len(sys.argv) > 1:
        notification_message = sys.argv[1]

    # Send Google Chat notification
    send_google_chat_notification(notification_message)

    # Get audio directory
    audio_dir = Path(__file__).parent.parent / "audio"

    # Default to task_complete sound
    audio_file = "task_complete.mp3"

    # Full path to audio file
    audio_path = audio_dir / audio_file

    # Play audio if it exists
    if audio_path.exists():
        play_audio(audio_path)
    else:
        print(f"Audio file not found: {audio_path}")


main()
