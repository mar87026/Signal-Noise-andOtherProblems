# Defog - Dark_Channel_Prior_1 : Thought and Reality

DCG is a the most famous dehaze method, everyone knows its concept:

*No matter how vibrant the image, shadows are structurally necessary to give it depth.*

Someime, people think the usage is easy to realize: Remove the smallest RGB values.

#### Let’s show it.

![Primary objects of interest: Road markings, license plates, traffic signs, and signals.](/operational_is_su-fficient/isp_fundamentals/defog_-_dark_channel_prior_1_thought_and_reality/image.png)

Primary objects of interest: Road markings, license plates, traffic signs, and signals.

#### Here are some results without any smooth process:

![Reduce 25% minimum](/operational_is_su-fficient/isp_fundamentals/defog_-_dark_channel_prior_1_thought_and_reality/image_1.png)

Reduce 25% minimum

![Reduce 50% grid’ minumum value](/operational_is_su-fficient/isp_fundamentals/defog_-_dark_channel_prior_1_thought_and_reality/image_2.png)

Reduce 50% grid’ minumum value

Weired. It become darker and objects don’t clear. Let lighten the result.

![Reduce 25% minimum and bright up with the mean of minimum.](/operational_is_su-fficient/isp_fundamentals/defog_-_dark_channel_prior_1_thought_and_reality/dehazed5_normalize_25.jpg)

Reduce 25% minimum and bright up with the mean of minimum.

Object of Interests are not more accurate, however the bush look vivid. What’s differenet between them?

[Defog - Dark_Channel_Prior_2:Basic model and Cover by Object Distance](/operational_is_su-fficient/isp_fundamentals/defog_-_dark_channel_prior_2_basic_model_and_cover.md)