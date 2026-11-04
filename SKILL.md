---
name: xiaohongshu-cover-copy
description: Create a ready-to-post Xiaohongshu package from an existing video, transcript, topic, or brand reference, including a 3:4 cover, title, long-form body, topic tags, character-count verification, and saved deliverables. Use when the user asks for 小红书封面、标题、长文、视频笔记文案，或要把现有内容改造成小红书发布素材；不负责未经明确授权直接发布到账号。
---

# Xiaohongshu cover and copy

Turn the user's real source material into one coherent Xiaohongshu publishing package. Preserve the source's claims and the user's voice; do not manufacture results, customers, numbers, or testimonials.

## Establish the source

- Use the supplied video, transcript, notes, screenshots, logo, and existing visual system before inventing a new angle.
- For a video, inspect representative frames and use its transcript or spoken content when available. Do not claim that a visual or quote exists unless it was verified.
- Treat logos and brand marks as invariants. Use them as supplied; do not redraw, respell, or stretch them.
- Do not edit or re-cut the source video as part of this skill; use a video-editing workflow when that is the requested deliverable.
- Ask at most one question only when the missing answer would materially change the topic, audience, or brand. Otherwise proceed with a reasonable assumption and state it briefly.

## Verify current limits

When the user says “限制内”, “可直接发”, or requests a final publishing package, verify the current title and body limits from official Xiaohongshu documentation. Prefer official product or learning-center pages over third-party summaries.

If live verification is unavailable, use the conservative ordinary-note defaults of 20 Unicode characters for the title and 1000 for the body, count whitespace and topic tags, and label those limits as unverified. Do not confuse ordinary notes with a separate long-form editor unless the user explicitly asks for that mode.

If an official limit is available only for a different or narrower note context, treat it as partially verified: use the stricter applicable value, state the source's scope, and do not present it as a confirmed universal platform limit.

## Build the package

### Cover

- Default to a 3:4 portrait cover unless the user or source requires another supported ratio.
- Make the promise readable at phone-thumbnail size: one small context line, a two- or three-line headline, and at most one compact proof or step badge.
- Match an existing palette and typography when references exist. Otherwise choose a restrained, high-contrast system appropriate to the topic.
- Use the built-in image-generation tool when available. Label each input image by role, quote all required text verbatim, prohibit extra copy and watermarks, and inspect the result for text accuracy, logo fidelity, safe margins, and readability.
- If the generated cover misspells required text or changes the logo, make one targeted correction and recheck it. Do not hand off a visibly incorrect cover.
- Do not ask for an API key for the normal built-in image-generation path. Use an API or CLI fallback only when the user explicitly chooses it.
- If required text or the logo remains wrong after two generation attempts, stop and report the exact defect instead of presenting the image as final.

### Title and body

- Write one primary title comfortably below the verified limit. It should name a concrete pain, result, or contrarian choice that the body actually supports.
- Write in the user's natural first-person voice when the source is a personal case or method. Prefer specific operational details over slogans.
- A useful body shape is: real opening observation, existing problem, practical method, grounded example, suitable boundary, and one low-pressure call to action. Change the structure when the source calls for it.
- For an ordinary 1000-character note, normally target about 600–850 characters including whitespace and tags. Do not fill the limit for its own sake.
- Use a small set of highly relevant topic tags. Keep the full body under the verified limit after tags are added.
- Remove generic AI marketing language such as “颠覆”, “革命”, “赋能”, “全新范式”, and unsupported superlatives. Avoid emoji decoration unless it is part of the user's established style.

## Count and save

Use `scripts/check_xhs_copy.py` for the final count. Pass the current verified limits when they differ from the script defaults.

The script counts Unicode code points. Composite emoji can differ from a client's visible-character accounting, so avoid emoji in tightly limited titles unless the live publishing interface confirms the count.

Save a compact package in the user's chosen location, or a clearly named output folder near the source:

- `xiaohongshu-cover.png`
- `xiaohongshu-copy.md`
- `cover-prompt.txt` when image generation was used

The Markdown file should contain the selected title, body, exact counts, topic tags, and cover filename. Preserve normal Markdown spacing unless the user explicitly asks for a compact file with blank lines removed. Do not overwrite existing deliverables without explicit permission; create a versioned sibling instead.

## Quality gate

Before finishing, confirm all of the following:

- the cover opens, has the intended aspect ratio, and contains no misspelled required text;
- the supplied logo remains recognizable and correctly spelled;
- the title and complete body pass the verified limits;
- the body is grounded in the supplied source and does not promise unsupported outcomes;
- every reported path exists and is directly usable.

Report the saved files, the final title/body counts, the limits used and whether they were live-verified, plus the image-generation mode and final prompt location. Publishing to the user's account or another external destination requires separate explicit authorization.
