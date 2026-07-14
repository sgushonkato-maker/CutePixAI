import fal_client

from app.texts.prompts import STYLE_PROMPTS


async def generate_image(
    image_url: str,
    style: str,
) -> str | None:

    prompt = STYLE_PROMPTS.get(
        style,
        STYLE_PROMPTS["style_anime"],
    )

    try:

        result = fal_client.subscribe(
            "fal-ai/flux/dev/image-to-image",
            arguments={
                "image_url": image_url,
                "prompt": prompt,
                "strength": 0.85,
                "guidance_scale": 3.5,
                "num_inference_steps": 28,
                "num_images": 1,
                "output_format": "jpeg",
            },
        )

        return result["images"][0]["url"]

    except Exception as e:
        print(f"Fal AI error: {e}")
        return None