# vision_check.py
# Purpose: confirm image+text (multimodal) works on Groq, no Gemini needed.
# Model may change — check console.groq.com/docs/vision if this 404s.

import argparse
import base64
import mimetypes
import os
import sys

from dotenv import load_dotenv
from groq import Groq

VISION_MODEL = "qwen/qwen3.6-27b"  # <- one variable to change if this deprecates


def encode_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Smoke-test Groq vision (image + text) with a local image."
    )
    parser.add_argument(
        "image",
        nargs="?",
        default="image3.jpg",
        help="Path to a local jpg/png/webp image (default: image3.jpg)",
    )
    args = parser.parse_args()

    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        sys.exit("Missing GROQ_API_KEY. Add it to .env and retry.")

    image_path = args.image
    if not os.path.isfile(image_path):
        sys.exit(
            f"Image not found: {image_path}. "
            "Pass a path: python vision_check.py path/to/image.jpg"
        )

    mime_type, _ = mimetypes.guess_type(image_path)
    if mime_type not in ("image/jpeg", "image/png", "image/webp"):
        sys.exit(f"Unsupported image type for {image_path}. Use jpg, png, or webp.")

    client = Groq(api_key=api_key)
    image_b64 = encode_image(image_path)

    response = client.chat.completions.create(
        model=VISION_MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image in one sentence."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{mime_type};base64,{image_b64}"},
                    },
                ],
            }
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
