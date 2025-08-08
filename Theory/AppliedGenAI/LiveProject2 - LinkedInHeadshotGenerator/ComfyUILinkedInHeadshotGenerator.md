# LinkedIn Headshot Generator App using ComfyUI

## Steps:

1. Get the Text to image template available in ComfyUI on the canvas.

2. Change to dev mode in ComfyUI:
	- Go to Settings
	- Switch Dev mode ON 
	- Select Menu to "Bottom"

3. Add `InstantID` nodes 
	- Right click on the canvas -> Add Node -> InstantID -> Load InstantID Model
	- Right click on the canvas -> Add Node -> InstantID -> InstantID Face Analysis
	- Right click on the canvas -> Add Node -> InstantID -> Apply InstantID Advanced

        ---
        ### ComfyUI - InstantID Nodes Explained

        These three nodes in ComfyUI are used together to perform face detection and identity preservation during image generation (e.g., using Stable Diffusion + ControlNet).

        #### 1. `InstantID -> Load InstantID Model`

        **📦 Purpose**: Loads the pretrained InstantID model components needed for face analysis and identity feature extraction.

        - **What it does**:
        - Loads the backbone model (e.g., face encoder, landmark detector).
        - Makes the model available to other nodes like `Face Analysis` and `Apply Advanced`.

        - **Inputs**: None  
        - **Outputs**: Loaded InstantID model reference

        **🔧 Must be used before the other two nodes.**

        #### 2. `InstantID -> InstantID Face Analysis`

        **🧠 Purpose**: Analyzes a reference face image to extract identity and pose features.

        - **What it does**:
        - Detects face in the input image.
        - Extracts:
            - Identity embedding (vector)
            - Facial landmarks
            - Face parsing (segmentation)

        - **Inputs**:
        - InstantID model (from Node 1)
        - Reference image (usually a photo)

        - **Outputs**:
        - Face identity embedding
        - Landmark map
        - Optional segmentation map

        #### 3. `InstantID -> Apply InstantID Advanced`

        **🎨 Purpose**: Applies the extracted identity features into the image generation process.

        - **What it does**:
        - Feeds identity and pose features into a diffusion pipeline (e.g., via ControlNet or LoRA).
        - Enables advanced controls:
            - Pose preservation
            - Expression control
            - Identity strength

        - **Inputs**:
        - Face analysis output (from Node 2)
        - Stable Diffusion model input or conditioning

        - **Outputs**:
        - Enhanced conditioning for image generation

        #### 🔁 Typical Workflow in ComfyUI

        ```text
        [Load InstantID Model]
                ↓
        [InstantID Face Analysis]
                ↓
        [Apply InstantID Advanced]
                ↓
        [Stable Diffusion / ControlNet Pipeline]
        ```
        ---

4. Add `ControlNet` node
    - Right click on the canvas -> Add Node -> loaders -> Load ControlNet Model

        ---
        #### 🔗 Purpose
        The Load ControlNet Model node loads a specific ControlNet checkpoint that enhances guided image generation by conditioning the Stable Diffusion model on structural inputs like pose, depth, edges, or face landmarks.

        This is essential for applying spatial control over the output image — such as preserving facial pose or body structure from a reference image.

        #### 🔍 Example: Identity-Preserving Face Generation with InstantID

        Goal: Generate a new image of a person, preserving facial identity and pose.

        🧩 Nodes:
        1. Load InstantID Model
        2. InstantID Face Analysis (on a real photo)
        3. Apply InstantID Advanced (injects face identity)
        4. Load ControlNet Model (InstantID landmarks)
        5. Stable Diffusion

        🔄 Flow:

        ```plaintext
        [Photo] → [Face Analysis] → (Identity + Landmarks)
            ↓                      ↓
        [Load InstantID Model]   [Load ControlNet Model (InstantID)]  
                                    ↓
                        [Apply InstantID Advanced]
                                    ↓
                            [Stable Diffusion]
        ```
        ---

5. Add two nodes for loading images
    - Right click on the canvas -> Add Node -> image -> Load Image
    - Right click on the canvas -> Add Node -> image -> Load Image

6. Download models
    - Click `Manager` on right bottom, it will open a modal box
    - Click on `Model Manager`, it will open a modal box
    - Type `InstantID` in the search box and now you need to install following models from the filtered list:
        - `diffusion_pytorch_model.safetensors`. It will say: "To apply the installed model, please click the 'Refresh' button." Hold on, we will do refresh once we have installed all the needed models. Install one-by-one
        - `InstantID\ip-adapter`
        - `1k3d68.onnx`
        - `2d106det.onnx`
        - `genderage.onnx`
        - `glintr100.onnx`
        - `scrfd_10g_bnkps.onnx`
    - Restart the ComfyUI Server
        - Back -> Restart
    - Refresh the browser
        - `Manager` -> `Model Manager` -> Search "InstantID" -> You will see Green tick infront of installed models

7. Select the relevant options on the newly added nodes in Step 3 and 4:
    - In the `Load InstantID Model` node, select the `SDXL\ip-adapter.bin`
    - In the `InstantID Face Analysis` node, select `CUDA`
    - In the `Load ControlNet Model` node, select `instantid\diffusion_pytorch_model.safetensors`

8. Add your two selfies on the two newly added image nodes