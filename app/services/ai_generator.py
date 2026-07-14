import fal_client
from app.config import FAL_API_KEY

fal_client.api_key = FAL_API_KEY


STYLE_PROMPTS = {
    "style_anime": (
        "Transform this photo into high-quality anime art. "
        "Keep the person's face recognizable, preserve pose and composition."
    ),

    "style_shoujo": (
        "Transform this photo into beautiful shoujo manga art. "
        "Soft pastel colors, expressive eyes, romantic atmosphere."
    ),

    "style_darkcute": (
        "Transform this photo into dark cute anime style. "
        "Cute but gothic, purple and black palette."
    ),

    "style_ghibli": (
        "Transform this photo into a hand-painted fantasy animation style "
        "with warm colors and cozy atmosphere."
    ),

    "style_fantasy": (
        "Transform this photo into an epic fantasy illustration. "
        "Magical lighting, cinematic look."
    ),
}


async def generate_image(image_url: str, style: str):

    prompt = STYLE_PROMPTS.get(
        style,
        STYLE_PROMPTS["style_anime"]
    )

    result = fal_client.subscribe(
        "fal-ai/flux-pro/kontext",
        arguments={
            "prompt": prompt,
            "image_url": image_url,
        },
    )

    return result["images"][0]["url"]