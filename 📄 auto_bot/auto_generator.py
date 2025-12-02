# Псевдокод автогенератора


def generate_reel(topic):
ideas = idea_generator(topic)
idea = choose_best(ideas)


script = script_writer(idea)
style = visual_style_ai(script)
captions = caption_generator(script)


return {
"topic": topic,
"idea": idea,
"script": script,
"style": style,
"captions": captions
}
