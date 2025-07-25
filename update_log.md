# [2.5.5]

* Fix colab inpaint issue by moving an import statement

# [2.5.4]

* Fix validation for default_ip_image_* and default_inpaint_mask_sam_model
* Fix enhance mask debugging in combination with image sorting
* Fix loading of checkpoints and LoRAs when using multiple directories in config and then switching presets

# [2.5.3]

* Only load weights from non-safetensors files, preventing harmful code injection
* Add checkbox for applying/resetting styles when describing images, also allowing multiple describe content types

# [2.5.2]

* Fix not adding positive prompt when styles didn't have a {prompt} placeholder in the positive prompt
* Extend config settings for input image

# [2.5.1]

* Update download URL in readme
* Increase speed of metadata loading
* Fix reading of metadata from jpeg, jpg and webp (exif)
* Fix debug preprocessor
* Update attributes and add inline prompt features section to readme
* Add checkbox, config and handling for saving only the final enhanced image. Use config `default_save_only_final_enhanced_image`, default False.
* Add sorting of final images when enhanced is enabled. Use argument `--disable-enhance-output-sorting` to disable.

# [2.5.0]

This version includes various package updates. If the auto-update doesn't work you can do one of the following:
1. Open a terminal in the AI Image Generator folder (location of config.txt) and run `git pull`
2. Update packages
   - Windows (installation through zip file): open a terminal in the AI Image Generator folder (location of config.txt) `..\python_embeded\python.exe -m pip install -r .\requirements_versions.txt` (Windows using embedded python, installation method zip file) or download AI Image Generator again (zip file attached to this release)
   - other: manually update the packages using `python.exe -m pip install -r requirements_versions.txt` or use the docker image

---

* Update python dependencies, add segment_anything
* Add enhance feature, which offers easy image refinement steps (similar to adetailer, but based on dynamic image detection instead of specific mask detection models).
* Rewrite async worker code, make code much more reusable to allow iterations and improve reusability
* Improve GroundingDINO and SAM image masking
* Fix inference tensor version counter tracking issue for GroundingDINO after using Enhance
* Move checkboxes Enable Mask Upload and Invert Mask When Generating from Developer Debug Mode to Inpaint Or Outpaint
* Add persistent model cache for metadata. Use `--rebuild-hash-cache X` (X = int, number of CPU cores, default all) to manually rebuild the cache for all non-cached hashes
* Rename `--enable-describe-uov-image` to `--enable-auto-describe-image`, now also works for enhance image upload
* Rename checkbox `Enable Mask Upload` to `Enable Advanced Masking Features` to better hint to mask auto-generation feature
* Get upscale model filepath by calling downloading_upscale_model() to ensure the model exists
* Rename tab titles and translations from singular to plural
* Rename document to documentation
* Update default models to latest versions
  * animaPencilXL_v400 => animaPencilXL_v500
  * DreamShaperXL_Turbo_dpmppSdeKarras => DreamShaperXL_Turbo_v2_1
  * SDXL_FILM_PHOTOGRAPHY_STYLE_BetaV0.4 => SDXL_FILM_PHOTOGRAPHY_STYLE_V1
* Add preset for pony_v6 (using ponyDiffusionV6XL)
* Add style `AI Image Generator Pony`
* Add restart sampler ([paper](https://arxiv.org/abs/2306.14878))
* Add config option for default_inpaint_engine_version, sets inpaint engine for pony_v6 and playground_v2.5 to None for improved results (incompatible with inpaint engine)
* Add image editor functionality to mask upload (same as for inpaint, now correctly resizes and allows more detailed mask creation)

# [2.4.3]

* Fix alphas_cumprod setter for TCD sampler
* Add parser for env var strings to expected config value types to allow override of all non-path config keys 

# [2.4.2]

* Fix some small bugs (tcd scheduler when gamma is 0, chown in Dockerfile, update cmd args in readme, translation for aspect ratios, vae default after file reload)
* Fix performance LoRA replacement when data is loaded from history log and inline prompt
* Add support and preset for playground v2.5 (only works with performance Quality or Speed, use with scheduler edm_playground_v2)
* Make textboxes (incl. positive prompt) resizable
* Hide intermediate images when performance of Gradio would bottleneck the generation process (Extreme Speed, Lightning, Hyper-SD)

# [2.4.1]

* Fix some small bugs (e.g. adjust clip skip default value from 1 to 2, add type check to aspect ratios js update function)
* Add automated docker build on push to main, tagged with `edge`.

# [2.4.0]

* Change settings tab elements to be more compact
* Add clip skip slider
* Add select for custom VAE
* Add new style "Random Style"
* Update default anime model to animaPencilXL_v310
* Add button to reconnect the UI after AI Image Generator crashed without having to configure everything again (no page reload required)
* Add performance "hyper-sd" (based on [Hyper-SDXL 4 step LoRA](https://huggingface.co/ByteDance/Hyper-SD/blob/main/Hyper-SDXL-4steps-lora.safetensors))
* Add [AlignYourSteps](https://research.nvidia.com/labs/toronto-ai/AlignYourSteps/) scheduler by Nvidia
* Add [TCD](https://github.com/jabir-zheng/TCD) sampler and scheduler (based on sgm_uniform)
* Add NSFW image censoring (disables intermediate image preview while generating). Set config value `default_black_out_nsfw` to True to always enable.
* Add argument `--enable-describe-uov-image` to automatically describe uploaded images for upscaling
* Add inline lora prompt references with subfolder support, example prompt: `colorful bird <lora:toucan:1.2>`
* Add size and aspect ratio recommendation on image describe
* Add inpaint brush color picker, helpful when image and mask brush have the same color
* Add automated Docker image build using Github Actions on each release.
* Add full raw prompts to history logs
* Change code ownership for automated issue / MR notification

# [2.3.1]

* Remove positive prompt from anime prefix to not reset prompt after switching presets
* Fix image number being reset to 1 when switching preset, now doesn't reset anymore
* Fix outpainting dimension calculation when extending left/right
* Fix LoRA compatibility for LoRAs in a1111 metadata scheme

# [2.3.0]

* Add performance "lightning" (based on [SDXL-Lightning 4 step LoRA](https://huggingface.co/ByteDance/SDXL-Lightning/blob/main/sdxl_lightning_4step_lora.safetensors))
* Add preset selection to UI, disable with argument `--disable-preset-selection`. Use `--always-download-new-model` to download missing models on preset switch.
* Improve face swap consistency by switching later in the process to (synthetic) refiner
* Add temp path cleanup on startup
* Add support for wildcard subdirectories
* Add scrollable 2 column layout for styles for better structure
* Improve Colab resource needs for T4 instances (default), positively tested with all image prompt features
* Improve anime preset, now uses style `AI Image Generator Semi Realistic` instead of `AI Image Generator Negative` (less wet look images)

# [2.2.1]

* Fix some small bugs (e.g. image grid, upscale fast 2x, LoRA weight width in Firefox)
* Allow prompt weights in array syntax
* Add steps override and metadata scheme to history log

# [2.2.0]

* Isolate every image generation to truly allow multi-user usage
* Add array support, changes the main prompt when increasing the image number. Syntax: `[[red, green, blue]] flower` 
* Add optional metadata to images, allowing you to regenerate and modify them later with the same parameters 
* Now supports native PNG, JPG and WEBP image generation
* Add Docker support

# [2.1.865]

* Various bugfixes
* Add authentication to --listen

# 2.1.864

* New model list. See also discussions.

# 2.1.861 (requested update)

(2023 Dec 21) Hi all, the feature updating of AI Image Generator will be paused for about two or three weeks because we have some other workloads. See you soon and we will come back in mid or late Jan. However, you may still see updates if other collaborators are fixing bugs or solving problems.

* Show image preview in Style when mouse hover.

# 2.1.860 (requested update)

* Allow upload inpaint mask in developer mode.

# 2.1.857 (requested update)

* Begin to support 8GB AMD GPU on Windows.

# 2.1.854

* Add a button to copy parameters to clipboard in log.
* Allow users to load parameters directly by pasting parameters to prompt.

# 2.1.853

* Add Marc K3nt3L's styles. Thanks [Marc K3nt3L](https://github.com/K3nt3L)!

# 2.1.852

* New Log System: Log system now uses tables. If this is breaking some other browser extension or javascript developments, see also use previous version.

# 2.1.846

* Many users reported that image quality is different from 2.1.824. We reviewed all codes and fixed several precision problems in 2.1.846.

# 2.1.843

* Many improvements to Canvas. Thanks CanvasZoom author!

# 2.1.841

* Backend maintain.
* Fix some potential frozen after model mismatch.
* Fix crash when cfg=1 when using anime preset.
* Added some guidelines for troubleshoot the "CUDA kernel errors asynchronously" problem.
* Fix inpaint device problem in `--always-gpu` mode.

# 2.1.839

* Maintained some computation codes in backend for efficiency.
* Added a note about Seed Breaking Change.

**Seed Breaking Change**: Note that 2.1.825-2.1.839 is seed breaking change. The computation float point is changed and some seeds may give slightly different results. The minor change in 2.1.825-2.1.839 do not influence image quality. See also use previous version.

# 2.1.837

* Fix some precision-related problems.

# 2.1.836

* Avoid blip tokenizer download from torch hub

# 2.1.831

# [2.1.830]

* SegmindVega support.

# [2.1.829]

* Change SDE tree to CPU on AMD/DirectMl to avoid potential problems.

# [2.1.828]

* Allow to disable gradio analytics.
* Use html table in log.
* fix some SSL problems.

# [2.1.826]

* New backend.
* FP8 support (see also the new cmd flag list in Readme, eg, --unet-in-fp8-e4m3fn and --unet-in-fp8-e5m2).
* Fix some MPS problems.
* GLoRA support.
* Turbo scheduler.

# [2.1.823]

(2023 Nov 26) Hi all, the feature updating of AI Image Generator will be paused for about two or three weeks because we have some other workloads. See you soon and we will come back in mid December. However, you may still see updates if other collaborators are fixing bugs or solving problems.

* Fix some potential problem when LoRAs has clip keys and user want to load those LoRAs to refiners.

# [2.1.822]

* New inpaint system (inpaint beta test ends).

# [2.1.821]

* New UI for LoRAs.
* Improved preset system: normalized preset keys and file names.
* Improved session system: now multiple users can use one AI Image Generator at the same time without seeing others' results.
* Improved some computation related to model precision.
* Improved config loading system with user-friendly prints.

# [2.1.820]

* support "--disable-image-log" to prevent writing images and logs to hard drive.

# [2.1.819]

* Allow disabling preview in dev tools.

# [2.1.818]

* Fix preset lora failed to load when the weight is exactly one.

# [2.1.817]

* support "--theme dark" and "--theme light".
* added preset files "default" and "lcm", these presets exist but will not create launcher files (will not be exposed to users) to keep entry clean. The "--preset lcm" is equivalent to select "Extreme Speed" in UI, but will likely to make some online service deploying easier.

# [2.1.815]

* Multiple loras in preset.

# [2.1.814]

* Allow using previous preset of official SAI SDXL by modify the args to '--preset sai'. ~Note that this preset will set inpaint engine back to previous v1 to get same results like before. To change the inpaint engine to v2.6, use the dev tools -> inpaint engine -> v2.6.~ (update: it is not needed now after some tests.)

# [2.1.813]

* Allow preset to set default inpaint engine.

# [2.1.812]

* Allow preset to set default performance.
* heunpp2 sampler.

# [2.1.810]

* Added hints to config_modification_tutorial.txt
* Removed user hacked aspect ratios in I18N english templates, but it will still be read like before.
* fix some style sorting problem again (perhaps should try Gradio 4.0 later).
* Refreshed I18N english templates with more keys.

# [2.1.809]

* fix some sorting problem.

# [2.1.808]

* Aspect ratios now show aspect ratios.
* Added style search.
* Added style sorting/ordering/favorites.

# [2.1.807]

* Click on image to see it in full screen.

# [2.1.806]

* Fix some lora problems related to clip.

# [2.1.805]

* Responsive UI for small screens.
* Added skip preprocessor in dev tools.

# [2.1.802]

* Default inpaint engine changed to v2.6. You can still use inpaint engine v1 in dev tools.
* Fix some VRAM problems.

# [2.1.799]

* Added 'Extreme Speed' performance mode (based on LCM). The previous complicated settings are not needed now.

# [2.1.798]

* added lcm scheduler - LCM may need to set both sampler and scheduler to "lcm". Other than that, see the description in 2.1.782 logs.

# [2.1.797]

* fixed some dependency problems with facexlib and filterpy.

# [2.1.793]

* Added many javascripts to improve user experience. Now users with small screen will always see full canvas without needing to scroll.

# [2.1.790]

* Face swap (in line with Midjourney InsightFace): Input Image -> Image Prompt -> Advanced -> FaceSwap
* The performance is super high. Use it carefully and never use it in any illegal things!
* This implementation will crop faces for you and you do NOT need to crop faces before feeding images into AI Image Generator. (If you previously manually crop faces from images for other software, you do not need to do that now in AI Image Generator.)

# [2.1.788]

* Fixed some math problems in previous versions.
* Inpaint engine v2.6 join the beta test of AI Image Generator inpaint models. Use it in dev tools -> inpaint engine -> v2.6 .

# [2.1.785]

* The `user_path_config.txt` is deprecated since 2.1.785. If you are using it right now, please use the new `config.txt` instead. See also the new documentation in the Readme.
* The paths in `user_path_config.txt` will still be loaded in recent versions, but it will be removed soon.
* We use very user-friendly method to automatically transfer your path settings from `user_path_config.txt` to `config.txt` and usually you do not need to do anything.
* The new `config.txt` will never save default values so the default value changes in scripts will not be prevented by old config files.

# [2.1.782]

2.1.782 is mainly an update for a new LoRA system that supports both SDXL loras and SD1.5 loras.

Now when you load a lora, the following things will happen:

1. try to load the lora to the base model, if failed (model mismatch), then try to load the lora to refiner.
2. try to load the lora to refiner, if failed (model mismatch) then do nothing.

In this way, AI Image Generator 2.1.782 can benefit from all models and loras from CivitAI with both SDXL and SD1.5 ecosystem, using the unique AI Image Generator swap algorithm, to achieve extremely high quality results (although the default setting is already very high quality), especially in some anime use cases, if users really want to play with all these things.

Recently the community also developed LCM loras. Users can use it by setting the sampler as 'LCM', scheduler as 'sgm_uniform' (Update in 2.1.798: scheduler should also be "lcm"), the forced overwrite of sampling step as 4 to 8, and CFG guidance as 1.0, in dev tools. Do not forget to change the LCM lora weight to 1.0 (many people forget this and report failure cases). Also, set refiner to None. If LCM's feedback in the artists community is good (not the feedback in the programmer community of Stable Diffusion), AI Image Generator may add some other shortcuts in the future.

# [2.1.781]

(2023 Oct 26) Hi all, the feature updating of AI Image Generator will (really, really, this time) be paused for about two or three weeks because we really have some other workloads. Thanks for the passion of you all (and we in fact have kept updating even after last pausing announcement a week ago, because of many great feedbacks)  - see you soon and we will come back in mid November. However, you may still see updates if other collaborators are fixing bugs or solving problems.

* Disable refiner to speed up when new users mistakenly set same model to base and refiner.

# [2.1.779]

* Disable image grid by default because many users reports performance issues. For example, https://github.com/YUKII2K3/Image-generator/issues/829 and so on. The image grid will cause problem when user hard drive is not super fast, or when user internet connection is not very good (eg, run in remote). The option is moved to dev tools if users want to use it. We will take a look at it later.

# [2.1.776]

* Support Ctrl+Up/Down Arrow to change prompt emphasizing weights.

# [2.1.750]

* New UI: now you can get each image during generating.

# [2.1.743]

* Improved GPT2 by removing some tokens that may corrupt styles.

# [2.1.741]

Style Updates:

* "Default (Slightly Cinematic)" as renamed to "AI Image Generator Cinematic".
* "Default (Slightly Cinematic)" is canceled from default style selections. 
* Added "AI Image Generator Sharp". This style combines many CivitAI prompts that reduces SDXL blurry and improves sharpness in a relatively natural way.
* Added "AI Image Generator Enhance". This style mainly use the very popular [default negative prompts from JuggernautXL](https://civitai.com/models/133005) and some other enhancing words. JuggernautXL's negative prompt has been proved to be very effective in many recent image posts on CivitAI to improve JuggernautXL and many other models.
* "AI Image Generator Sharp" and "AI Image Generator Enhance" and "AI Image Generator V2" becomes the new default set of styles.
* Removed the default text in the "negative prompt" input area since it is not necessary now.
* You can reproduce previous results by using "AI Image Generator Cinematic".
* "AI Image Generator Sharp" and "AI Image Generator Enhance" may undergo minor revision in future updates.

# [2.1.739]

* Added support for authentication in --share mode (via auth.json).

# [2.1.737]

* Allowed customizing resolutions in config. 

Modifying this will make results worse if you do not understand how Positional Encoding works. 

You have been warned.

If you do not know why numbers must be transformed with many Sin and Cos functions (yes, those Trigonometric functions that you learn in junior high school) before they are fed to SDXL, we do not encourage you to change this - you will become a victim of Positional Encoding. You are likely to suffer from an easy-to-fail tool, rather than getting more control.

Your knowledge gained from SD1.5 (for example, resolution numbers divided by 8 or 64 are good enough for UNet) does not work in SDXL. The SDXL uses Positional Encoding. The SD1.5 does not use Positional Encoding. They are completely different. 

Your knowledge gained from other resources (for example, resolutions around 1024 are good enough for SDXL) is wrong. The SDXL uses Positional Encoding. People who say "all resolutions around 1024 are good" do not understand what is Positional Encoding. They are not intentionally misleading. They are just not aware of the fact that SDXL is using Positional Encoding. 

The number 1152 must be exactly 1152, not 1152-1, not 1152+1, not 1152-8, not 1152+8. The number 1152 must be exactly 1152. Just Google what is a Positional Encoding.

Again, if you do not understand how Positional Encoding works, just do not change the resolution numbers.

# [2.1.735]

* Fixed many problems related to torch autocast.

# [2.1.733]

* Increased allowed random seed range.

# [2.1.728]

* Fixed some potential numerical problems since 2.1.723

# [2.1.723]

* Improve AI Image Generator Anime a bit by using better SD1.5 refining formulation.

# [2.1.722]

* Now it is possible to translate 100% all texts in the UI.

# [2.1.721]

* Added language/en.json to make translation easier.

# [2.1.720]

* Added Canvas Zoom to inpaint canvas
* Fixed the problem that image will be cropped in UI when the uploaded image is too wide.

# [2.1.719]

* I18N

# [2.1.718]

* Corrected handling dash in wildcard names, more wildcards (extended-color).

# [2.1.717]

* Corrected displaying multi-line prompts in Private Log.

# [2.1.716]

* Added support for nested wildcards, more wildcards (flower, color_flower).

# [2.1.714]

* Fixed resolution problems.

# [2.1.712]

* Cleaned up Private Log (most users won't need information about raw prompts).

# [2.1.711]

* Added more information about prompts in Private Log.
* Made wildcards in negative prompt use different seed.

# [2.1.710]

* Added information about wildcards usage in console log.

# [2.1.709]

* Allowed changing default values of advanced checkbox and image number.

# [2.1.707]

* Updated Gradio to v3.41.2.

# [2.1.703]

* Fixed many previous problems related to inpaint.

# [2.1.702]

* Corrected reading empty negative prompt from config (it shouldn't turn into None).

# [2.1.701]

* Updated FreeU node to v2 (gives less overcooked results).

# [2.1.699]

* Disabled smart memory management (solves some memory issues).

# [2.1.698]

* Added support for loading model files from subfolders.

# [2.1.696]

* Improved wildcards implementation (using same wildcard multiple times will now return different values).

**(2023 Oct 18) Again, the feature updating of AI Image Generator will be paused for about two or three weeks because we have some other workloads - we will come back in early or mid November. However, you may still see updates if other collaborators are fixing bugs or solving problems.**

# [2.1.695 (requested emergency bug fix)]

* Reduced 3.4GB RAM use when swapping base model.
* Reduced 372MB VRAM use in VAE decoding after using control model in image prompt.
* Note that Official ComfyUI (d44a2de) will run out of VRAM when using sdxl and control-lora on 2060 6GB that does not support float16 at resolution 1024. AI Image Generator 2.1.695 succeeded in outputting images without OOM using exactly same devices.

(2023 Oct 17) Announcement of update being paused.

# [2.1.693]

* Putting custom styles before pre-defined styles.
* Avoided the consusion between AI Image Generator Anime preset and AI Image Generator style (AI Image Generator style is renamed to AI Image Generator Masterpiece because it does not make images Anime-looking if not using with AI Image Generator Anime preset).
* Fixed some minor bugs in AI Image Generator Anime preset's prompt emphasizing of commas.
* Supported and documented embedding grammar (and wildcards grammar). 
* This release is a relative stable version and many features are determined now.

# [2.1.687]

* Added support for wildcards (using files from wildcards folder - try prompts like `__color__ sports car` with different seeds).

# [2.1.682]

* Added support for custom styles (loaded from JSON files placed in sdxl_styles folder).

# [2.1.681]

* Added support for generate hotkey (CTRL+ENTER).
* Added support for generate forever (RMB on Generate button).
* Added support for playing sound when generation is finished ('notification.ogg' or 'notification.mp3').

# [2.1.62]

* Preset system. Added anime and realistic support.

# [2.1.52]

* removed pygit2 dependency (expect auto update) so that people will never have permission denied problems.

# [2.1.50]

* Begin to support sd1.5 as refiner. This method scale sigmas given SD15/Xl latent scale and is probably the most correct way to do it. I am going to write a discussion soon.

# [2.1.25]

AMD support on Linux and Windows.

# [2.1.0]

* Image Prompt
* Finished the "Moving from Midjourney" Table

# [2.0.85]

* Speed Up Again

# [2.0.80]

* Improved the scheduling of ADM guidance and CFG mimicking for better visual quality in high frequency domain and small objects.

# [2.0.80]

* Rework many patches and some UI details.
* Speed up processing.
* Move Colab to independent branch.
* Implemented CFG Scale and TSNR correction when CFG is bigger than 10.
* Implemented Developer Mode with more options to debug.

### [2.0.72]

(2023 sep 21) The feature updating of AI Image Generator will be paused for about two or three weeks because we have some events and travelling - we will come back in early or mid October. 

### [2.0.72]

* Allow users to choose path of models.

### [2.0.65]

* Inpaint model released.

### [2.0.50]

* Variation/Upscale (Midjourney Toolbar) implemented.

### [2.0.16]

* Virtual memory system implemented. Now Colab can run both base model and refiner model with 7.8GB RAM + 5.3GB VRAM, and it never crashes.
* If you are lucky enough to read this line, keep in mind that ComfyUI cannot do this. This is very reasonable that AI Image Generator is more optimized because it only need to handle a fixed pipeline, but ComfyUI need to consider arbitrary pipelines. 
* But if we just consider the optimization of this fixed workload, after 2.0.16, AI Image Generator has become the most optimized SDXL app, outperforming ComfyUI.

### [2.0.0]

* V2 released.
* completely rewrite text processing pipeline (higher image quality and prompt understanding).
* support multi-style.
* In 100 tests (prompts written by ChatGPT), V2 default results outperform V1 default results in 87 cases, evaluated by two human.
* In 100 tests (prompts written by ChatGPT), V2 prompt understanding outperform V1 prompt understanding in 81 cases, evaluated by two human, in both default setting and multi/single style mode.
* Because the above number is above 80%, we view this as a major update and directly jump to 2.0.0.
* Some other things are renamed.

### [1.0.67]

* Use dynamic weighting and lower weights for prompt expansion.

### [1.0.64]

* Fixed a small OOM problem.

### [1.0.62]

* Change prompt expansion to suffix mode for better balance of semantic and style (and debugging).

### [1.0.60]

* Tune the balance between style and Prompt Expansion.

### [1.0.56]

* Begin to use magic split.

### [1.0.55]

* Minor changes of Prompt Expansion.

### [1.0.52]

* Reduce the semantic corruption of Prompt Expansion.

### [1.0.51]

* Speed up Prompt Expansion a bit.

### [1.0.50]

* Prompt expansion and a "Raw mode" to turn it off (similar to Midjourney's "raw").

### [1.0.45]

* Reworked SAG, removed unnecessary patch
* Reworked anisotropic filters for faster compute.
* Replaced with guided anisotropic filter for less distortion.

### [1.0.41]

(The update of AI Image Generator will be paused for a period of time for AUTOMATIC1111 sd-webui 1.6.X, and some features will also be implemented as webui extensions)

### [1.0.40]

* Behaviors reverted to 1.0.36 again (refiner steps). The 1.0.36 is too perfect and too typical; beating 1.0.36 is just impossible.

### [1.0.39]

* Reverted unstable changes between 1.0.37 and 1.0.38 .
* Increased refiner steps to half of sampling steps.

### [1.0.36]

* Change gaussian kernel to anisotropic kernel.

### [1.0.34]

* Random seed restoring.

### [1.0.33]

* Hide items in log when images are removed.

### [1.0.32]

* AI Image Generator private log

### [1.0.31]

* Fix typo and UI.

### [1.0.29]

* Added "Advanced->Advanced->Advanced" block for future development.

### [1.0.29]

* Fix overcook problem in 1.0.28

### [1.0.28]

* SAG implemented

### [1.0.27]

* Fix small problem in textbox css 

### [1.0.25]

* support sys.argv --listen --share --port

### [1.0.24]

* Taller input textbox.

### [1.0.23]

* Added some hints on linux after UI start so users know the App does not fail.

### [1.0.20]

* Support linux.

### [1.0.20]

* Speed-up text encoder.

### [1.0.20]

* Re-write UI to use async codes: (1) for faster start, and (2) for better live preview.
* Removed opencv dependency
* Plan to support Linux soon

### [1.0.19]

* Unlock to allow changing model.

### [1.0.17]

* Change default model to SDXL-1.0-vae-0.9. (This means the models will be downloaded again, but we should do it as early as possible so that all new users only need to download once. Really sorry for day-0 users. But frankly this is not too late considering that the project is just publicly available in less than 24 hours - if it has been a week then we will prefer more lightweight tricks to update.)

### [1.0.16]

* Implemented "AI-Image-Generator/outputs" folder for saving user results.
* Ignored cv2 errors when preview fails.
* Mentioned future AMD support in Readme.
* Created this log.

### [1.0.15]

Publicly available.

### [1.0.0]

Initial Version.
