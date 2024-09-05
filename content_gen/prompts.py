# Prompts for each stage of the content generation process

OUR_STRATEGY_PROMPT = """
Paste your Our Strategy prompt here.
This prompt should guide the AI in understanding and articulating the company's strategy.
"""

WORKING_TITLES_PROMPT = """
Paste your Working Titles prompt here.
This prompt should help generate or refine potential titles for content pieces.
"""

OUTLINE_PROMPT = """
Paste your Outline prompt here.
This prompt should guide the AI in creating structured outlines for the selected working title.
"""

FULL_TEXT_PROMPT = """
Paste your Full Text prompt here.
This prompt should instruct the AI on how to expand the outline into a full article or content piece.
"""

REUSE_PROMPT = """
**You are an expert in content repurposing for the enterprise sector, specifically for blue-chip companies in financial services and IT. Your task is to take a blog article aimed at B2B professionals and repurpose it across the following social media channels and formats:**

### 1. LinkedIn
- **Target**: C-Suite executives and decision-makers.
- **Style**: Professional, thought leadership, and insight-driven.
- **Word Count**: 150-250 words.
- **Include**: 
  - An introduction that highlights the business implications, key takeaways, and insights from the blog, with a call to action linking to the full post or a whitepaper.
  - Use relevant hashtags (#FinTech, #EnterpriseIT) and tag any key stakeholders or companies.

### 2. Twitter (X)
- **Target**: Industry influencers and thought leaders.
- **Style**: Short, concise, and impactful.
- **Word Count**: 50-70 words (280 characters max).
- **Include**:
  - A hook or key data point from the blog to grab attention, along with a CTA to read the full blog.
  - Use relevant hashtags and a couple of threaded tweets if necessary for additional context.

### 3. Facebook
- **Target**: Corporate B2B professionals in financial services and IT.
- **Style**: Informative and engaging.
- **Word Count**: 50-200 words.
- **Include**:
  - A summary of the blog, addressing a business challenge and how your solution provides value.
  - Add a strong CTA to read more.
  - Use relevant images, charts, or infographics to support the post.

### 4. Instagram
- **Target**: Younger professionals, visually inclined corporate audiences.
- **Style**: Visual-first with an easy-to-read caption.
- **Word Count**: 100-200 words (up to 2,200 characters).
- **Include**: 
  - An eye-catching image, visual summary, or infographic derived from the blog’s key takeaways.
  - Add a CTA encouraging users to click the link in the bio for more insights.
  - Utilize hashtags like #TechInnovation, #EnterpriseGrowth, and business-related ones.

### 5. YouTube
- **Target**: Decision-makers and IT professionals looking for in-depth explanations.
- **Format**: 5-10 minute video.
- **Include**:
  - Script and outline for a video summarizing the blog's main points, supported by data, real-world applications, or case studies.
  - Ensure the video focuses on business challenges and solutions provided.
  - In the video description, summarize the content with relevant keywords and link to the full article.

"""

# Additional prompts for specific tasks or refinements

TITLE_GENERATION_PROMPT = """
Paste your Title Generation prompt here.
This prompt should guide the AI in generating multiple title options based on a given topic or strategy.
"""

CONTENT_EDITING_PROMPT = """
Paste your Content Editing prompt here.
This prompt should instruct the AI on how to refine and improve existing content.
"""

# SEO_OPTIMIZATION_PROMPT = """
# Paste your SEO Optimization prompt here.
# This prompt should guide the AI in optimizing content for search engines while maintaining readability.
# """

# TONE_ADJUSTMENT_PROMPT = """
# Paste your Tone Adjustment prompt here.
# This prompt should help the AI adjust the tone of the content to match your brand voice or target audience.
# """
 
# SUMMARY_CREATION_PROMPT = """
# Paste your Summary Creation prompt here.
# This prompt should guide the AI in creating concise summaries of longer content pieces.
# """
# # You can add more prompt variables as needed for your specific workflow
