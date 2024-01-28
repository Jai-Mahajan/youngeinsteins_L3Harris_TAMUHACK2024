import vertexai
from vertexai.preview.language_models import TextGenerationModel

vertexai.init(project="tamuhack24", location="us-central1")
parameters = {
    "max_output_tokens": 477,
    "temperature": 0.6,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("gemini-pro")
response = model.predict(
    """Define the categories for the text below?
Options:
- visual
- audio
- handson

Text: Watching a video explaining the concept with visual animations and demonstrations.
Categories: visual

Text: Listening to an audio lecture or podcast discussing the concept in detail.
Categories: audio

Text: Engaging in hands-on experiments or activities to explore the concept firsthand.
Categories: handson

Text: By visualizing the problem and using diagrams or drawings to understand the concepts.
Categories: visual

Text: By listening to explanations and working through problems step-by-step with verbal guidance.
Categories: audio

Text: By using manipulatives, such as blocks or counters, to represent numbers and solve problems through tactile exploration.
Categories: handson

Text: Designing and creating visual presentations or digital artwork related to the topic.
Categories: visual

Text: Participating in discussions or listening to podcasts exploring different aspects of technology.
Categories: audio

Text: Building and programming robots or working with interactive simulations to explore technology concepts.
Categories: handson

Text: Watching videos or virtual tours of engineering marvels and architectural structures.
Categories: visual

Text: Listening to interviews or lectures from engineers discussing their projects and innovations.
Categories: audio

Text: Building structures, designing prototypes, and solving engineering challenges through hands-on projects.
Categories: handson

Text: Observing images, diagrams, or videos that illustrate the phenomena in detail.
Categories: visual

Text: Listening to narrated explanations or stories that describe the phenomena\'s causes and effects.
Categories: audio

Text: Conducting experiments, collecting data, and making observations to investigate the phenomena firsthand.
Categories: handson

Text: Based on the picture, can you identify the number of objects?
Categories: visual

Text: How high is the ladder based on the image?
Categories: visual

Text: After trying the right hand rule, which way does the magnetic field point?
Categories: handson

Text: What is your estimate for the height of the building in the image?
Categories: visual

Text: After counting the number apples with the blocks, what answer did you come up with?
Categories: handson

Text: What is the pattern used to determine the number of objects in the image?
Categories: visual

Text: Based on the video where she explained the topic, what is the definition of speed?
Categories: audio

Text: Identify and count the number of specific objects labeled A, B, C, and D.
Categories: visual

Text: Use the coins on your to determine the change left over.
Categories: handson

Text: According to the interviewee, why is understanding frequency crucial in their field of study?
Categories: audio

Text: How many objects are there in the image?
Categories: visual

Text: After removing all the red skittles, how many are left?
Categories: handson

Text: Based on the audio in the video, what does the frequency sound like?
Categories: audio

Text: Identify two key factors mentioned in the audio that can influence an object\'s acceleration.
Categories: audio

Text: Once you count the number of sticks on the table, enter your answer.
Categories: handson

Text: After flipping the dice, what probability did you determine?
Categories: handson

Text: After listening to the speech, what is the order of PEMDAS?
Categories: audio

Text: Can you summarize the key concepts explained by the speaker?
Categories: audio

Text: What key information did you gather from the oral presentation?
Categories: audio

Text: After listening to the audio clip, what is the main message or takeaway?
Categories: audio

Text: How did the tone of the conversation change during specific segments?
Categories: audio

Text: In language learning, how did practicing pronunciation through listening help you grasp the nuances of the language?
Categories: audio

Text: Were there any specific sounds or words that were challenging to pronounce correctly?
Categories: audio

Text: After hearing a story or narrative, what were the key events that stood out to you?
Categories: audio

Text: How did the narrator\'s voice contribute to the atmosphere of the story?
Categories: audio

Text: Can you retell the story in your own words?
Categories: audio

Text: How did physically manipulating objects enhance your understanding of geometric shapes?
Categories: handson

Text: Provide an example of a real-world scenario where these geometric concepts could be applied?
Categories: handson

Text: What variables were manipulated in the experiment, and how did they affect the outcomes?
Categories: handson

Text: Describe the transformation that occurs in the pupa stage based on the diagram shown.
Categories: visual

Text: Based on the graph, determine the combined percentage of housing and transportation expenses.
Categories: visual

Text: Describe the scene depicted in the artwork.
Categories: visual

Text: Identify any symbols or details that convey the historical context.
Categories: visual

Text: Locate the mountain range marked on the map.
Categories: visual

Text: Where is Australia located on the map?
Categories: visual

Text: How high is the ladder based on the image?
Categories:
""",
    **parameters
)
print(f"Response from Model: {response.text}")
