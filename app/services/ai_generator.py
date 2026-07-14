import fal_client

from app.config import FAL_API_KEY
from app.texts.prompts import STYLE_PROMPTS


fal_client.api_key = FAL_API_KEY


async def generate_image(
    image_url: str,
    style: str,
) -> str:

    prompt = STYLE_PROMPTS.get(
        style,
        STYLE_PROMPTS["style_anime"]
    )

    try:

        result = fal_client.subscribe(

            "fal-ai/flux-pro/kontext",

            arguments={

                "prompt": prompt,

                "image_url": image_url,

            },

        )

        return result["images"][0]["url"]

    except Exception as e:

        print(e)

        return None