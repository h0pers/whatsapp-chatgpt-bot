from time import sleep

from bot.config import OPEN_AI_CLIENT, OPEN_AI_ASSISTANCE_ID


def assistance_answer(message_text: str) -> str:
    thread = OPEN_AI_CLIENT.beta.threads.create()
    message = OPEN_AI_CLIENT.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message_text
    )
    run = OPEN_AI_CLIENT.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=OPEN_AI_ASSISTANCE_ID,
    )
    while run.status != 'completed':
        sleep(1)
        run = OPEN_AI_CLIENT.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

    messages = OPEN_AI_CLIENT.beta.threads.messages.list(
        thread_id=thread.id,
    )
    return messages.data[0].content[0].text.value
