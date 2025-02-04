# DeGirum PySDK 

DeGirum PySDK is a software development kit, focused on edge AI development, that supports multiple hardware options, enabling AI solution providers to add AI to their applications using simple APIs.
![Degirum pysdk](/images/pysdk_hw_support.png)

**[ORCA1 Performance Benchmarks](ORCABenchmarks.md)**

## Quick Start

1. Sign up for an account on [DeGirum Cloud Portal](https://cs.degirum.com/login?screen_hint=signup).

1. Log in to [DeGirum Cloud Portal](https://cs.degirum.com).

1. Create cloud API access token on [**Tokens** page of DeGirum Cloud Portal](https://hub.degirum.com/tokens/).

1. Install DeGirum PySDK. Read the instructions [here](https://docs.degirum.com/content/pysdk/basic-install/).

1. The following script will perform ML inference of a test image with two cats using a model from
DeGirum public mode zoo. The inference result will be displayed in both text and graphical form.

    ```python
    import degirum as dg         # import DeGirum PySDK package
    
    # load mobilenet model from deGirum's public model zoo to run in the cloud
    model = dg.load_model(
        model_name = "mobilenet_v2_ssd_coco--300x300_quant_n2x_cpu_1",
        inference_host_address = dg.CLOUD,
        zoo_url = "degirum/public",
        token = "<your cloud access token>",
        image_backend='pil'
    )
    
    # perform AI inference of an image specified by URL
    result = model("https://raw.githubusercontent.com/DeGirum/PySDKExamples/main/images/TwoCats.jpg")

    print(result)                # print numeric results
    result.image_overlay.show()  # show graphical results
    ```

## Running PySDK Examples

This repository provides PySDK example scripts that can perform ML inferences on the following hosting options:

1. Using [DeGirum Cloud Platform](https://hub.degirum.com),
1. On DeGirum AI Server deployed on a localhost or on some computer in your LAN or VPN,
1. On DeGirum ORCA accelerator directly installed on your local computer.

To try different options, you need to assign the appropriate value to `hw_location` variable, typically 
located in the first code cell of each example notebook:

1. `hw_location = "@cloud"` for cloud hosting;
1. `hw_location = "<hostname>"` for AI server hosting, where <hostname> is the hostname or IP address of yuor AI server in your LAN;
1. `hw_location = "@local"` for local hosting.
   
You have two ways to run examples:
1. running them in the cloud in **Google Colab**,
2. or running them locally **on your computer**.

To run examples in Google Colab, first register your Google Colab account, then scroll down to the 
[Examples Directory](#examples-directory) section, select the example you want to run, and click the link: it will be opened in Google Colab. 

To run examples locally, please perform the following steps:

1. Make sure you have installed Python version 3.9, 3.10, or 3.11. For convenience of future maintenance we recommend 
you to work in the virtual environment, such as [Miniconda](https://docs.conda.io/en/latest/miniconda.html). 
Make sure you activated your Python virtual environment.

1. Clone DeGirum PySDKExamples repo by executing the following command in the terminal / command prompt:

    ```
    git clone https://github.com/DeGirum/PySDKExamples.git
    ```

1. In the terminal / command prompt, change the current directory to the repo directory, and install necessary Python
dependencies by executing the following command:

    ``` Python
    pip install -r requirements.txt
    ```

1. Inside the repo directory, open `env.ini` file and fill the required authentication details by assigning the
following variables:

    |Variable Name|Description|
    |-------------|-----------|
    |`DEGIRUM_CLOUD_TOKEN`|DeGirum cloud platform API access token. To obtain a token, visit [**Tokens** page on DeGirum Cloud Portal](https://hub.degirum.com/tokens/).|


    This will allow loading the token from the `env.ini` file instead of hard-coding the value in the script. Please make sure not to commit the `env.ini` file with the token value.

1. Start Jupyter server by executing the following command in the terminal / command prompt,
making sure your current directory is still PySDKExample repo root directory:

    ```
    jupyter lab
    ```

    Jupyter Lab GUI will open in your default browser.  In Jupyter Lab GUI navigate to `examples` subdirectory, then select desired example and run it.

1. Alternatively, if you have [Visual Studio Code](https://code.visualstudio.com/) IDE installed, just open Visual Studio Code in PySDKExample repo root directory.
Make sure Jupyter plugin is installed in your Visual Studio Code. Then you can open any Jupyter notebook example directly in Visual Studio Code
and execute it from there.

## Examples Directory

* [Basic Examples](#basic-examples)
* [Single Model Examples](#single-model-examples)
* [Combining Multiple Models](#combining-multiple-models)
* [Advanced Algorithms](#advanced-algorithms)
* [Benchmarks](#benchmarks)
* [Examples of `degirum_tools.streams` Toolkit Usage](#examples-of-degirum_toolsstreams-toolkit-usage)
* [Applications](#applications)

### Basic Examples
| Example | Description |
|---------|-------------|
|[object detection image](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/basic/basic_pysdk_demo_image.ipynb)|One of the simplest examples how to do AI inference on a graphical file using object detection model. This example does not depend on any other packages such as `degirum_tools`|
|[object detection video stream file](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/basic/basic_pysdk_demo_video_stream.ipynb)|How to do AI inference on a video stream, and show annotated video in real-time. |

### Single Model Examples

| Example | Description |
|---------|-------------|
|[object detection image](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/singlemodel/object_detection_image.ipynb)|One of the simplest examples how to do AI inference on a graphical file using object detection model.|
|[object detection annotate video file](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/singlemodel/object_detection_annotate_video_file.ipynb)|How to do AI inference on a video file, show annotated video, and save it to another video file. |
|[object detection video stream](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/singlemodel/object_detection_video_stream.ipynb)|How to do AI inference on a video stream, and show annotated video in real-time.|
|[object detection class filtering](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/singlemodel/object_detection_class_filtering.ipynb)|How to do object detection AI inference on an image file filtering only desired set of classes.|
|[sound classification audio stream](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/singlemodel/sound_classification_audio_stream.ipynb)|How to do sound classification AI inference on an audio stream from a local microphone in real time. The result label with highest probability is displayed for each inference while keeping history few steps back.|


### Combining Multiple Models

| Example | Description |
|---------|-------------|
|[hand face person detection parallel video stream](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/multimodel/hand_face_person_detection_parallel_video_stream.ipynb)|How to run three models side-by-side and combine results of the three models. A video stream is processed simultaneously by the hand, face, and person detection models. Combined result is then displayed.|
|[license plate recognition pipelined image](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/multimodel/license_plate_recognition_pipelined_image.ipynb)|How to do AI inference of a graphical file using two AI models: license plate detection and license plate text recognition. The license plate detection model is run on the image and the results are then processed by the license plate text recognition model, one bounding box at a time. Combined result is then displayed.|
|[face gender recognition pipelined image](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/multimodel/face_gender_recognition_pipelined_image.ipynb)|How to do AI inference of a graphical file using two AI models: face detection and gender classification. The face detection model is run on the image and the results are then processed by the gender classification model, one face at a time. Combined result is then displayed.|
|[face combined age gender pipelined image](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/multimodel/face_combined_age_gender_pipelined_image.ipynb)|How to do AI inference of a graphical file using three AI models: face detection, age regression, and gender classification. The face detection model is run on the image and the results are then processed by the age regression and gender classification models, one face at a time. Combined result is then displayed.|
|[license plate recognition pipelined video stream](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/multimodel/license_plate_recognition_pipelined_video_stream.ipynb)|A video stream from a video camera is processed by the license plate detection model. The face detection results are then processed by the license plate text recognition model, one bounding box at a time. Combined results are then displayed as an annotated video in real-time.|
|[sound classification and object detection asynchronous](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/multimodel/sound_classification_and_object_detection_asynchronous.ipynb)|How to perform parallel inferences on two **asynchronous** data streams with different frame rates. To achieve maximum performance this example uses **non-blocking** batch prediction mode.|

### Advanced Algorithms

| Example | Description |
|---------|-------------|
|[hand tracking and control](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/specialized/hand_tracking_and_control.ipynb)|How to perform hand detection with tracking and following detection of palm keypoints. The combined result of hand detection and palm keypoints detection is used to imitate mouse operation.|
|[multi object tracking video file](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/specialized/multi_object_tracking_video_file.ipynb)|How to perform object detection with multi-object tracking (MOT) from a video file to count vehicle traffic.|
|[object detection dataset](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/specialized/object_detection_dataset.ipynb)|How to do AI inference on an image dataset and calculate performance metrics. An image dataset is retrieved from the cloud using `fiftyone` API.|
|[object in zone counting video file](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/specialized/object_in_zone_counting_video_file.ipynb)|Object detection and object counting in polygon zone: video file annotation|
|[object in zone counting video stream](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/specialized/object_in_zone_counting_video_stream.ipynb)|Object detection and object counting in polygon zone: streaming video processing|
|[tiled object detection](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/specialized/tiled_object_detection.ipynb)|How to do tiled object detection of a video stream from a video file. Each video frame is divided by tiles with some overlap, each tile of the AI model input size (to avoid resizing). Object detection is performed for each tile, then results from different tiles are combined.|
|[advanced tiling for object detection](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/specialized/advanced_tiling_strategies.ipynb)|Demonstrates how to perform image tiling with various strategies that mitigates partial/duplicate detections introduced by tiling.|

### Benchmarks

| Example | Description |
|---------|-------------|
|[single model performance test](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/benchmarks/single_model_performance_test.ipynb)|Performance measurements for all Orca-based image detection AI models from DeGirum public model zoo.|
|[multi model performance test](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/benchmarks/multi_model_performance_test.ipynb)|Performance measurements for simultaneous inference of multiple AI models.|
|[object detection multiplexing multiple streams](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/benchmarks/object_detection_multiplexing_multiple_streams.ipynb)|How to perform object detection from multiple video files, multiplexing frames. This example demonstrates lowest possible and stable AI inference latency while maintaining decent throughput. This is achieved by using synchronous prediction mode and video decoding offloaded into separate thread.|

### Examples of `degirum_tools.streams` Toolkit Usage

| Example | Description |
|---------|-------------|
|[dgstreams demo](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/dgstreams/dgstreams_demo.ipynb)|Extensive demo notebook of `degirum_tools.streams` toolkit: lightweight multi-threaded pipelining framework|
|[multi camera multi model detection](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/dgstreams/multi_camera_multi_model_detection.ipynb)|How to perform AI inferences of multiple models processing multiple video streams. Each video stream is fed to every model. Each model processes frames from every video stream in multiplexing manner.|
|[person pose detection pipelined video stream](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/dgstreams/person_pose_detection_pipelined_video_stream.ipynb)|A video stream from a video camera is processed by the person detection model. The person detection results are then processed by the pose detection model, one person bounding box at a time. Combined results are then displayed as an annotated video in real-time.|

### Applications
| Example | Description |
|---------|-------------|
|[person count video](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/applications/person_count_video.ipynb)|Counting people in a video frame-by-frame using multiple detection models in parallel and annotating the video with the results.|
|[stop sign violation detection](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/applications/stop_sign_violation_detection.ipynb)|Stop sign violation detection using object detection, object tracking, zone counting, line cross counting, and event detection.|
|[person age gender detection](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/applications/person_age_gender_detection.ipynb)|Person detection followed by object tracking, zone presence detection, age detection, and gender classification with result averaging among all occurrences of detected person in the zone.|
|[car wrong direction detection](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/applications/car_wrong_direction_detection.ipynb)|Detect a car going in the wrong direction using object detection, object tracking, line cross counting, and event detection. When an event is detected, the notification is sent to the notification service of your choice and a video clip around that event is uploaded to S3-compatible storage of your choice.|
|[parking management](https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/applications/parking_management.ipynb)|Monitor a parking lot's occupancy using object detection and zone intrusion detection in a video. Zones defined for parking spaces are checked for occupancy and counted, and the video is annotated with occupancy/vacancy counts.|


## Full List of Variables in `env.ini` Configuration File

|Variable Name|Description|Default Value|
|-------------|-----------|-------------|
|`DEGIRUM_CLOUD_TOKEN`| DeGirum cloud platform API access token. To obtain a token, visit *Management > My Tokens* page on [DeGirum Cloud Portal](https://cs.degirum.com). | `None` |
|`DEGIRUM_CLOUD_PLATFORM_URL`|URL of DeGirum cloud platform server used by `degirum_tools.connect_model_zoo()` | `"https://cs.degirum.com"` |
|`CLOUD_ZOO_URL`| Cloud zoo URL used by `degirum_tools.connect_model_zoo()` | `""` |
|`AISERVER_HOSTNAME_OR_IP`| AI server host name/IP address used by `degirum_tools.connect_model_zoo()` | `None` |
|`CAMERA_ID`| Video source for inference: 0-based index of local camera, URL of RTSP stream, URL of YouTube Video, local video file path | `0` |
|`AUDIO_ID`| Audio source for inference: 0-based index for local microphones or local WAV file path | `0` |
|`TEST_MODE`| Test node flag (for unit testing) | `None` |
